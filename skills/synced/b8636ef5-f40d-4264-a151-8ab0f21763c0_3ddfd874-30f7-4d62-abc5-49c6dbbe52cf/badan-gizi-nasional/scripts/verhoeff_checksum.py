#!/usr/bin/env python3
"""Verhoeff checksum — generate/validasi check digit ID numerik (mis. UIN PM 10 digit).
Pakai: python3 verhoeff_checksum.py validate 1234567896
       python3 verhoeff_checksum.py generate 123456789   (menambahkan 1 digit cek)
"""
import sys

_d = [[0,1,2,3,4,5,6,7,8,9],[1,2,3,4,0,6,7,8,9,5],[2,3,4,0,1,7,8,9,5,6],[3,4,0,1,2,8,9,5,6,7],
      [4,0,1,2,3,9,5,6,7,8],[5,9,8,7,6,0,4,3,2,1],[6,5,9,8,7,1,0,4,3,2],[7,6,5,9,8,2,1,0,4,3],
      [8,7,6,5,9,3,2,1,0,4],[9,8,7,6,5,4,3,2,1,0]]
_p = [[0,1,2,3,4,5,6,7,8,9],[1,5,7,6,2,8,3,0,9,4],[5,8,0,3,7,9,6,1,4,2],[8,9,1,6,0,4,3,5,2,7],
      [9,4,5,3,1,2,6,8,7,0],[4,2,8,6,5,7,3,9,0,1],[2,7,9,3,8,0,6,4,1,5],[7,0,4,6,9,1,3,2,5,8]]
_inv = [0,4,3,2,1,5,6,7,8,9]

def checksum(num: str) -> int:
    c = 0
    for i, ch in enumerate(reversed(num)):
        c = _d[c][_p[(i + 1) % 8][int(ch)]]
    return _inv[c]

def validate(num: str) -> bool:
    c = 0
    for i, ch in enumerate(reversed(num)):
        c = _d[c][_p[i % 8][int(ch)]]
    return c == 0

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("validate", "generate") or not sys.argv[2].isdigit():
        print(__doc__); sys.exit(1)
    mode, num = sys.argv[1], sys.argv[2]
    if mode == "generate":
        print(f"{num}{checksum(num)}")
    else:
        ok = validate(num)
        print("VALID" if ok else "TIDAK VALID")
        sys.exit(0 if ok else 2)
