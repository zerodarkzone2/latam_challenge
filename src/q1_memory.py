from typing import List, Tuple
from datetime import datetime
from collections import Counter
import json


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Get the top 10 dates using a counter object
    days_counter = Counter()
    with open(file_path, "r") as jf:
        for line in jf:
            row = json.loads(line)
            date = datetime.fromisoformat(row["date"]).date()
            days_counter.update([date])

    top_10_dates = [date[0] for date in days_counter.most_common(10)]

    # Get the top user for every date
    date_user_counter = {key: Counter() for key in top_10_dates}
    with open(file_path, "r") as jf:
        for line in jf:
            row = json.loads(line)
            date = datetime.fromisoformat(row["date"]).date()
            user = row["user"]["username"]
            if date in top_10_dates:
                date_user_counter[date].update([user])

    return [(k, v.most_common(1)[0][0]) for k, v in date_user_counter.items()]
