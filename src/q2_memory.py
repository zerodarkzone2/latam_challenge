from typing import List, Tuple
from collections import Counter
import emoji
import json

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # Create a counter object
    emoji_counter = Counter()
    # Read the file line by line
    with open(file_path, "r") as jf:
        for line in jf:
            row = json.loads(line)
            content = row["content"]
            # Extract emojis from text and update counter
            emoji_counter.update([em.chars for em in emoji.analyze(content)])

    # Get the top 10 emojis
    top_10_emoji = emoji_counter.most_common(10)
    return top_10_emoji
