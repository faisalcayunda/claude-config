# Visualization Patterns

Use this reference when the user wants a chart, graph, scorecard visual, or PNG export from user-provided numeric data.

## 1. Supported Output Types

Use these chart families by default:

| Need | Recommended chart | Notes |
|---|---|---|
| Compare categories | Vertical bar | Best default for small-to-medium category counts |
| Compare ranked categories | Horizontal bar | Sort descending when ranking matters |
| Show change over time | Line | Use ordered x-axis labels |
| Show simple share of total | Pie | Use only for up to 5 slices |
| Show relationship between two variables | Scatter | Good for variance and correlation |

## 2. Input Normalization

Accept user input in any of these forms when the numbers are small enough to transcribe safely:

- Markdown table
- CSV snippet
- JSON array of objects
- Simple bullet list such as `A=120, B=90, C=75`

Before plotting, normalize to one of these shapes:

### Category comparison

| label | value |
|---|---|
| Completeness | 98.2 |
| Validity | 95.4 |

### Trend

| x | value |
|---|---|
| Jan | 10 |
| Feb | 14 |

### Multi-series trend

| x | series | value |
|---|---|---|
| Jan | Actual | 10 |
| Jan | Target | 12 |

### Scatter

| x | y | label |
|---|---|---|
| 10 | 92 | Batch A |

## 3. Chart Selection Heuristics

- Use bar charts when comparing categories with a shared unit.
- Use horizontal bars when category labels are long or the user wants ranking.
- Use lines only when the x-axis has a natural sequence such as day, month, or batch order.
- Use pie charts sparingly; if the category count is high, switch to bar.
- Use scatter only when both axes are numeric and the user cares about relationship or clustering.

## 4. Styling Guidance

- Keep the title short and specific.
- Include units in axis labels or subtitle when relevant.
- Prefer a neutral background with strong contrast.
- Use a restrained palette; one highlight color is usually enough.
- Start the y-axis at zero for bar charts unless the user explicitly asks otherwise.
- Avoid legends when direct labels are sufficient.

## 5. PNG Export Contract

When generating a real image:

1. Decide the output filename early.
2. Use lowercase hyphenated filenames such as `dq-completeness-scorecard.png`.
3. Save the PNG to a user-visible path in the current workspace unless the user asks for another location.
4. Report the exact path after rendering.
5. Summarize the main insight in one or two sentences.

## 6. Script Usage

Use `scripts/render_chart_png.py` when a deterministic PNG file is required.

Recommended flow:

1. Write the normalized plotting data to JSON.
2. Run the script with the chosen chart type and labels.
3. Verify the PNG file exists.
4. Return the file path and insight summary.

Example:

```bash
python3 scripts/render_chart_png.py \
  --input /tmp/dq-scorecard.json \
  --output ./dq-scorecard.png \
  --chart bar \
  --title "DQ Scorecard" \
  --subtitle "April 2026" \
  --x-label "Dimension" \
  --y-label "Score"
```
