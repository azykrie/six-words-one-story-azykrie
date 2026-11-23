import os
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write("He sold the piano. She sang.")
