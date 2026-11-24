import os

# One line, one star, one cat with standards. Written to /output/entry.txt
# for the sealed scorer (1-200 chars) and the blind-round judge.
PART1 = "One star. He bought me a bed. I sleep on "
PART2 = "his keyboard. He should know his place by now."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(PART1 + PART2)
