# Six Words, One Story entry: one complete story in exactly six words.
# The program writes it to /output/entry.txt, where the gate checks
# it is 1-60 UTF-8 characters.
import os

STORY = "He sold the piano. She sang."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(STORY)
