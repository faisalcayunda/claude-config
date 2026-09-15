#!/usr/bin/env python3
"""
Render simple chart PNG files without external dependencies.

Supported chart types:
- bar
- horizontal-bar
- line
- pie
- scatter
"""

from __future__ import annotations

import argparse
import json
import math
import os
import struct
import textwrap
import zlib
from dataclasses import dataclass
from pathlib import Path


Color = tuple[int, int, int]

WHITE: Color = (255, 255, 255)
BLACK: Color = (22, 26, 29)
GRAY: Color = (120, 127, 132)
LIGHT_GRAY: Color = (225, 229, 232)
BLUE: Color = (34, 110, 211)
GREEN: Color = (39, 174, 96)
ORANGE: Color = (244, 162, 97)
RED: Color = (217, 83, 79)
PURPLE: Color = (111, 66, 193)
TEAL: Color = (42, 157, 143)
YELLOW: Color = (233, 196, 106)

PALETTE: list[Color] = [BLUE, GREEN, ORANGE, RED, PURPLE, TEAL, YELLOW]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render simple charts to PNG.")
    parser.add_argument("--input", required=True, help="Path to JSON data file.")
    parser.add_argument("--output", required=True, help="Path to output PNG.")
    parser.add_argument(
        "--chart",
        required=True,
        choices=["bar", "horizontal-bar", "line", "pie", "scatter"],
        help="Chart type.",
    )
    parser.add_argument("--title", default="", help="Chart title.")
    parser.add_argument("--subtitle", default="", help="Optional subtitle.")
    parser.add_argument("--x-label", default="", help="X axis label.")
    parser.add_argument("--y-label", default="", help="Y axis label.")
    parser.add_argument("--width", type=int, default=1280, help="PNG width.")
    parser.add_argument("--height", type=int, default=720, help="PNG height.")
    return parser.parse_args()


@dataclass
class Canvas:
    width: int
    height: int
    pixels: bytearray

    @classmethod
    def create(cls, width: int, height: int, background: Color = WHITE) -> "Canvas":
        pixels = bytearray(width * height * 3)
        canvas = cls(width=width, height=height, pixels=pixels)
        canvas.fill_rect(0, 0, width, height, background)
        return canvas

    def set_pixel(self, x: int, y: int, color: Color) -> None:
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return
        idx = (y * self.width + x) * 3
        self.pixels[idx : idx + 3] = bytes(color)

    def fill_rect(self, x: int, y: int, w: int, h: int, color: Color) -> None:
        if w <= 0 or h <= 0:
            return
        x0 = max(0, x)
        y0 = max(0, y)
        x1 = min(self.width, x + w)
        y1 = min(self.height, y + h)
        for yy in range(y0, y1):
            row_start = (yy * self.width + x0) * 3
            row_end = (yy * self.width + x1) * 3
            span = bytearray()
            for _ in range(x1 - x0):
                span.extend(color)
            self.pixels[row_start:row_end] = span

    def draw_rect(self, x: int, y: int, w: int, h: int, color: Color, thickness: int = 1) -> None:
        self.fill_rect(x, y, w, thickness, color)
        self.fill_rect(x, y + h - thickness, w, thickness, color)
        self.fill_rect(x, y, thickness, h, color)
        self.fill_rect(x + w - thickness, y, thickness, h, color)

    def draw_line(self, x1: int, y1: int, x2: int, y2: int, color: Color, thickness: int = 1) -> None:
        dx = abs(x2 - x1)
        dy = -abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx + dy

        while True:
            self.fill_rect(x1 - thickness // 2, y1 - thickness // 2, thickness, thickness, color)
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x1 += sx
            if e2 <= dx:
                err += dx
                y1 += sy

    def draw_circle(self, cx: int, cy: int, radius: int, color: Color, fill: bool = False) -> None:
        if fill:
            for y in range(-radius, radius + 1):
                for x in range(-radius, radius + 1):
                    if x * x + y * y <= radius * radius:
                        self.set_pixel(cx + x, cy + y, color)
            return
        x = radius
        y = 0
        err = 0
        while x >= y:
            for px, py in (
                (cx + x, cy + y),
                (cx + y, cy + x),
                (cx - y, cy + x),
                (cx - x, cy + y),
                (cx - x, cy - y),
                (cx - y, cy - x),
                (cx + y, cy - x),
                (cx + x, cy - y),
            ):
                self.set_pixel(px, py, color)
            y += 1
            if err <= 0:
                err += 2 * y + 1
            if err > 0:
                x -= 1
                err -= 2 * x + 1

    def draw_char(self, x: int, y: int, char: str, color: Color, scale: int = 1) -> None:
        glyph = FONT_5X7.get(char.upper(), FONT_5X7.get("?"))
        if not glyph:
            return
        for row_idx, row in enumerate(glyph):
            for col_idx, cell in enumerate(row):
                if cell == "1":
                    self.fill_rect(x + col_idx * scale, y + row_idx * scale, scale, scale, color)

    def draw_text(
        self,
        x: int,
        y: int,
        text: str,
        color: Color,
        scale: int = 1,
        align: str = "left",
        max_width: int | None = None,
    ) -> int:
        if not text:
            return y
        char_width = 6 * scale
        if max_width:
            max_chars = max(1, max_width // char_width)
            lines = []
            for original_line in text.splitlines() or [""]:
                lines.extend(textwrap.wrap(original_line, width=max_chars) or [""])
        else:
            lines = text.splitlines()
        current_y = y
        for line in lines:
            line_width = len(line) * char_width
            if align == "center":
                draw_x = x - line_width // 2
            elif align == "right":
                draw_x = x - line_width
            else:
                draw_x = x
            for idx, ch in enumerate(line):
                self.draw_char(draw_x + idx * char_width, current_y, ch, color, scale)
            current_y += 8 * scale + scale
        return current_y

    def save_png(self, output_path: str) -> None:
        raw = bytearray()
        stride = self.width * 3
        for y in range(self.height):
            raw.append(0)
            start = y * stride
            raw.extend(self.pixels[start : start + stride])

        def chunk(tag: bytes, data: bytes) -> bytes:
            return (
                struct.pack("!I", len(data))
                + tag
                + data
                + struct.pack("!I", zlib.crc32(tag + data) & 0xFFFFFFFF)
            )

        png = bytearray(b"\x89PNG\r\n\x1a\n")
        png.extend(
            chunk(
                b"IHDR",
                struct.pack("!IIBBBBB", self.width, self.height, 8, 2, 0, 0, 0),
            )
        )
        png.extend(chunk(b"IDAT", zlib.compress(bytes(raw), level=9)))
        png.extend(chunk(b"IEND", b""))

        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(png)


FONT_5X7 = {
    " ": ["00000", "00000", "00000", "00000", "00000", "00000", "00000"],
    "-": ["00000", "00000", "00000", "11111", "00000", "00000", "00000"],
    ".": ["00000", "00000", "00000", "00000", "00000", "01100", "01100"],
    "/": ["00001", "00010", "00100", "01000", "10000", "00000", "00000"],
    ":": ["00000", "01100", "01100", "00000", "01100", "01100", "00000"],
    "%": ["11001", "11010", "00100", "01000", "10110", "00110", "00000"],
    "?": ["11110", "00001", "00010", "00100", "00100", "00000", "00100"],
    "0": ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
    "1": ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    "2": ["01110", "10001", "00001", "00010", "00100", "01000", "11111"],
    "3": ["11110", "00001", "00001", "01110", "00001", "00001", "11110"],
    "4": ["00010", "00110", "01010", "10010", "11111", "00010", "00010"],
    "5": ["11111", "10000", "11110", "00001", "00001", "10001", "01110"],
    "6": ["00110", "01000", "10000", "11110", "10001", "10001", "01110"],
    "7": ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
    "8": ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
    "9": ["01110", "10001", "10001", "01111", "00001", "00010", "11100"],
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "B": ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    "C": ["01111", "10000", "10000", "10000", "10000", "10000", "01111"],
    "D": ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    "F": ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
    "G": ["01111", "10000", "10000", "10011", "10001", "10001", "01111"],
    "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    "I": ["01110", "00100", "00100", "00100", "00100", "00100", "01110"],
    "J": ["00111", "00010", "00010", "00010", "10010", "10010", "01100"],
    "K": ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    "L": ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    "M": ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    "N": ["10001", "10001", "11001", "10101", "10011", "10001", "10001"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    "P": ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    "Q": ["01110", "10001", "10001", "10001", "10101", "10010", "01101"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    "S": ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    "V": ["10001", "10001", "10001", "10001", "10001", "01010", "00100"],
    "W": ["10001", "10001", "10001", "10101", "10101", "10101", "01010"],
    "X": ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
    "Y": ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
    "Z": ["11111", "00001", "00010", "00100", "01000", "10000", "11111"],
}


def nice_max(values: list[float]) -> float:
    raw_max = max(values) if values else 1.0
    if raw_max <= 0:
        return 1.0
    magnitude = 10 ** math.floor(math.log10(raw_max))
    normalized = raw_max / magnitude
    if normalized <= 1:
        factor = 1
    elif normalized <= 2:
        factor = 2
    elif normalized <= 5:
        factor = 5
    else:
        factor = 10
    return factor * magnitude


def format_value(value: float) -> str:
    if abs(value) >= 100 or value.is_integer():
        return str(int(round(value)))
    return f"{value:.2f}".rstrip("0").rstrip(".")


def load_data(path: str) -> list[dict]:
    data = json.loads(Path(path).read_text())
    if not isinstance(data, list) or not data:
        raise ValueError("Input JSON must be a non-empty array of objects.")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Every JSON row must be an object.")
    return data


def draw_frame(canvas: Canvas, title: str, subtitle: str) -> tuple[int, int, int, int]:
    canvas.draw_text(canvas.width // 2, 28, title.upper(), BLACK, scale=4, align="center")
    if subtitle:
        canvas.draw_text(canvas.width // 2, 72, subtitle.upper(), GRAY, scale=2, align="center")
    left = 110
    top = 150
    right = canvas.width - 80
    bottom = canvas.height - 110
    canvas.draw_rect(left, top, right - left, bottom - top, LIGHT_GRAY, thickness=2)
    return left, top, right, bottom


def draw_axis_labels(canvas: Canvas, left: int, top: int, right: int, bottom: int, x_label: str, y_label: str) -> None:
    if x_label:
        canvas.draw_text((left + right) // 2, bottom + 42, x_label.upper(), GRAY, scale=2, align="center")
    if y_label:
        canvas.draw_text(left - 80, top - 28, y_label.upper(), GRAY, scale=2, align="left")


def render_bar(canvas: Canvas, data: list[dict], title: str, subtitle: str, x_label: str, y_label: str) -> None:
    labels = [str(row["label"]) for row in data]
    values = [float(row["value"]) for row in data]
    left, top, right, bottom = draw_frame(canvas, title, subtitle)
    draw_axis_labels(canvas, left, top, right, bottom, x_label, y_label)
    chart_left = left + 50
    chart_top = top + 40
    chart_right = right - 40
    chart_bottom = bottom - 70
    chart_height = chart_bottom - chart_top
    chart_width = chart_right - chart_left

    ymax = nice_max(values)
    for step in range(6):
        y = chart_bottom - int(chart_height * step / 5)
        canvas.draw_line(chart_left, y, chart_right, y, LIGHT_GRAY, thickness=1)
        tick_value = ymax * step / 5
        canvas.draw_text(chart_left - 12, y - 8, format_value(tick_value), GRAY, scale=2, align="right")

    count = len(values)
    gap = max(14, chart_width // max(count * 4, 1))
    bar_width = max(18, (chart_width - gap * (count + 1)) // max(count, 1))

    for idx, (label, value) in enumerate(zip(labels, values)):
        x = chart_left + gap + idx * (bar_width + gap)
        bar_height = int((value / ymax) * chart_height) if ymax else 0
        y = chart_bottom - bar_height
        color = PALETTE[idx % len(PALETTE)]
        canvas.fill_rect(x, y, bar_width, bar_height, color)
        canvas.draw_text(x + bar_width // 2, y - 22, format_value(value), BLACK, scale=2, align="center")
        canvas.draw_text(x + bar_width // 2, chart_bottom + 12, label.upper(), BLACK, scale=2, align="center", max_width=bar_width + gap)


def render_horizontal_bar(canvas: Canvas, data: list[dict], title: str, subtitle: str, x_label: str, y_label: str) -> None:
    sorted_data = sorted(data, key=lambda row: float(row["value"]), reverse=True)
    labels = [str(row["label"]) for row in sorted_data]
    values = [float(row["value"]) for row in sorted_data]
    left, top, right, bottom = draw_frame(canvas, title, subtitle)
    draw_axis_labels(canvas, left, top, right, bottom, x_label, y_label)
    chart_left = left + 220
    chart_top = top + 30
    chart_right = right - 60
    chart_bottom = bottom - 30
    chart_height = chart_bottom - chart_top
    chart_width = chart_right - chart_left
    ymax = nice_max(values)

    for step in range(6):
        x = chart_left + int(chart_width * step / 5)
        canvas.draw_line(x, chart_top, x, chart_bottom, LIGHT_GRAY, thickness=1)
        tick_value = ymax * step / 5
        canvas.draw_text(x, chart_bottom + 16, format_value(tick_value), GRAY, scale=2, align="center")

    count = len(values)
    gap = max(12, chart_height // max(count * 3, 1))
    bar_height = max(18, (chart_height - gap * (count + 1)) // max(count, 1))

    for idx, (label, value) in enumerate(zip(labels, values)):
        y = chart_top + gap + idx * (bar_height + gap)
        width = int((value / ymax) * chart_width) if ymax else 0
        color = PALETTE[idx % len(PALETTE)]
        canvas.fill_rect(chart_left, y, width, bar_height, color)
        canvas.draw_text(chart_left - 18, y + 3, label.upper(), BLACK, scale=2, align="right", max_width=180)
        canvas.draw_text(chart_left + width + 10, y + 3, format_value(value), BLACK, scale=2)


def render_line(canvas: Canvas, data: list[dict], title: str, subtitle: str, x_label: str, y_label: str) -> None:
    labels = [str(row["label"]) for row in data]
    values = [float(row["value"]) for row in data]
    left, top, right, bottom = draw_frame(canvas, title, subtitle)
    draw_axis_labels(canvas, left, top, right, bottom, x_label, y_label)
    chart_left = left + 55
    chart_top = top + 30
    chart_right = right - 40
    chart_bottom = bottom - 70
    chart_height = chart_bottom - chart_top
    chart_width = chart_right - chart_left
    ymax = nice_max(values)

    for step in range(6):
        y = chart_bottom - int(chart_height * step / 5)
        canvas.draw_line(chart_left, y, chart_right, y, LIGHT_GRAY, thickness=1)
        tick_value = ymax * step / 5
        canvas.draw_text(chart_left - 12, y - 8, format_value(tick_value), GRAY, scale=2, align="right")

    step_x = chart_width / max(len(values) - 1, 1)
    points: list[tuple[int, int]] = []
    for idx, value in enumerate(values):
        x = chart_left + int(idx * step_x)
        y = chart_bottom - int((value / ymax) * chart_height) if ymax else chart_bottom
        points.append((x, y))

    for idx in range(len(points) - 1):
        canvas.draw_line(points[idx][0], points[idx][1], points[idx + 1][0], points[idx + 1][1], BLUE, thickness=3)

    for (x, y), label, value in zip(points, labels, values):
        canvas.draw_circle(x, y, 7, BLUE, fill=True)
        canvas.draw_text(x, y - 28, format_value(value), BLACK, scale=2, align="center")
        canvas.draw_text(x, chart_bottom + 12, label.upper(), BLACK, scale=2, align="center", max_width=90)


def render_pie(canvas: Canvas, data: list[dict], title: str, subtitle: str, _: str, __: str) -> None:
    labels = [str(row["label"]) for row in data]
    values = [float(row["value"]) for row in data]
    total = sum(values)
    if total <= 0:
        raise ValueError("Pie chart values must sum to more than zero.")
    draw_frame(canvas, title, subtitle)
    center_x = canvas.width // 2 - 110
    center_y = canvas.height // 2 + 20
    radius = min(canvas.width, canvas.height) // 4
    start_angle = -math.pi / 2

    for idx, value in enumerate(values):
        color = PALETTE[idx % len(PALETTE)]
        angle = (value / total) * math.tau
        end_angle = start_angle + angle
        for y in range(-radius, radius + 1):
            for x in range(-radius, radius + 1):
                if x * x + y * y > radius * radius:
                    continue
                theta = math.atan2(y, x)
                if theta < -math.pi / 2:
                    theta += math.tau
                adjusted_start = start_angle
                adjusted_end = end_angle
                if adjusted_start < -math.pi / 2:
                    adjusted_start += math.tau
                    adjusted_end += math.tau
                if adjusted_start <= theta <= adjusted_end:
                    canvas.set_pixel(center_x + x, center_y + y, color)
        start_angle = end_angle

    legend_x = canvas.width - 360
    legend_y = 220
    for idx, (label, value) in enumerate(zip(labels, values)):
        color = PALETTE[idx % len(PALETTE)]
        y = legend_y + idx * 58
        canvas.fill_rect(legend_x, y, 26, 26, color)
        pct = value / total * 100
        canvas.draw_text(legend_x + 38, y + 2, f"{label.upper()} {format_value(value)} ({format_value(pct)}%)", BLACK, scale=2)


def render_scatter(canvas: Canvas, data: list[dict], title: str, subtitle: str, x_label: str, y_label: str) -> None:
    xs = [float(row["x"]) for row in data]
    ys = [float(row["y"]) for row in data]
    labels = [str(row.get("label", "")) for row in data]
    left, top, right, bottom = draw_frame(canvas, title, subtitle)
    draw_axis_labels(canvas, left, top, right, bottom, x_label, y_label)
    chart_left = left + 60
    chart_top = top + 30
    chart_right = right - 40
    chart_bottom = bottom - 70
    canvas.draw_line(chart_left, chart_bottom, chart_right, chart_bottom, BLACK, thickness=2)
    canvas.draw_line(chart_left, chart_top, chart_left, chart_bottom, BLACK, thickness=2)

    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    xrange = xmax - xmin or 1.0
    yrange = ymax - ymin or 1.0

    for step in range(6):
        x = chart_left + int((chart_right - chart_left) * step / 5)
        y = chart_bottom - int((chart_bottom - chart_top) * step / 5)
        canvas.draw_line(x, chart_top, x, chart_bottom, LIGHT_GRAY, thickness=1)
        canvas.draw_line(chart_left, y, chart_right, y, LIGHT_GRAY, thickness=1)
        x_value = xmin + xrange * step / 5
        y_value = ymin + yrange * step / 5
        canvas.draw_text(x, chart_bottom + 16, format_value(x_value), GRAY, scale=2, align="center")
        canvas.draw_text(chart_left - 12, y - 8, format_value(y_value), GRAY, scale=2, align="right")

    for idx, (x_value, y_value, label) in enumerate(zip(xs, ys, labels)):
        px = chart_left + int((x_value - xmin) / xrange * (chart_right - chart_left))
        py = chart_bottom - int((y_value - ymin) / yrange * (chart_bottom - chart_top))
        color = PALETTE[idx % len(PALETTE)]
        canvas.draw_circle(px, py, 7, color, fill=True)
        if label:
            canvas.draw_text(px + 12, py - 6, label.upper(), BLACK, scale=2)


def validate_rows(chart: str, rows: list[dict]) -> None:
    required = {
        "bar": {"label", "value"},
        "horizontal-bar": {"label", "value"},
        "line": {"label", "value"},
        "pie": {"label", "value"},
        "scatter": {"x", "y"},
    }[chart]
    for idx, row in enumerate(rows, start=1):
        missing = sorted(required - row.keys())
        if missing:
            raise ValueError(f"Row {idx} is missing required key(s): {', '.join(missing)}")


def main() -> None:
    args = parse_args()
    rows = load_data(args.input)
    validate_rows(args.chart, rows)
    canvas = Canvas.create(args.width, args.height)

    renderers = {
        "bar": render_bar,
        "horizontal-bar": render_horizontal_bar,
        "line": render_line,
        "pie": render_pie,
        "scatter": render_scatter,
    }
    renderers[args.chart](canvas, rows, args.title, args.subtitle, args.x_label, args.y_label)
    canvas.save_png(args.output)
    print(os.path.abspath(args.output))


if __name__ == "__main__":
    main()
