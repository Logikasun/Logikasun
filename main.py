import json

with open("input.txt", "r", encoding="utf-8") as f:
    raw = f.read().strip()

# Якщо JSON прийшов як string з escape-символами
if raw.startswith('"') or '\\"' in raw:
    raw = raw.encode("utf-8").decode("unicode_escape")

parsed = json.loads(raw)

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(parsed, f, indent=2, ensure_ascii=False)

print("✅ JSON очищено і відформатовано")
