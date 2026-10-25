#!/usr/bin/env python3
"""Writes index.json from banks/*/info.json (run by the GitHub action - don't edit index.json by hand)."""
import json, os

RAW = "https://raw.githubusercontent.com/KiruTheProot-Creative/EmulonX-Banks/main/"
banks = []
for name in sorted(os.listdir("banks")):
    folder = os.path.join("banks", name)
    try:
        info = json.load(open(os.path.join(folder, "info.json"), encoding="utf-8"))
    except Exception:
        continue
    entry = {"id": name}
    for key, default in (("name", name), ("author", ""), ("official", False), ("soon", False), ("description", ""),
                         ("presets", 0), ("version", "1.0"), ("download", ""), ("size", 0), ("colour", 0)):
        entry[key] = info.get(key, default)
    if os.path.exists(os.path.join(folder, "cover.png")):
        entry["cover"] = RAW + f"banks/{name}/cover.png"
    banks.append(entry)
banks.sort(key=lambda b: (not b["official"], b["name"].lower()))
with open("index.json", "w", encoding="utf-8") as f:
    json.dump({"format": "emulonx-banks", "version": 1, "banks": banks}, f, indent=2, ensure_ascii=False)
    f.write("\n")
print(f"{len(banks)} banks")
