import os

ENTRY = "I ran the migration twice because the first run looked lonely, so now production has two of everything \u2014 including the outage."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
