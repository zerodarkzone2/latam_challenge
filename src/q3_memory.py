from typing import List, Tuple
from collections import Counter
import json

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    mentions_counter = Counter()
    with open(file_path, "r") as jf:
        for line in jf:
            row = json.loads(line)
            mentions = row.get("mentionedUsers") or []
            # Extract emojis from text and update counter
            mentions_counter.update([mention["username"] for mention in mentions])
    return mentions_counter.most_common(10)
