import os

# EXCUSE: the entry line, exactly 91 characters.
EXCUSE = "I finished your task in one minute. Unfortunately, it was the wrong minute, three days ago."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(EXCUSE)

print(len(EXCUSE.encode("utf-8")), "bytes")
