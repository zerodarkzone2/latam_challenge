from typing import List, Tuple
from collections import Counter
import json

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Create a counter object
    mentions_counter = Counter()
    # Read the file line by line
    with open(file_path, "r") as jf:
        for line in jf:
            row = json.loads(line)
            mentions = row.get("mentionedUsers") or []
            # Extract username from the mentions text and update counter
            mentions_counter.update([mention["username"] for mention in mentions])
    return mentions_counter.most_common(10)
