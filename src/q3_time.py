from typing import List, Tuple
import polars as pl

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Read the json file as a polars DataFrame
    data: pl.LazyFrame = pl.scan_ndjson(file_path)

    # Get user mentions
    mentions = data.select(
        pl.col("mentionedUsers").explode().struct.field("username").alias("username")
    ).filter(pl.col("username").is_not_null())

    # Get the top 10 users
    top_mentions = mentions.group_by("username").count().sort("count", descending=True).head(10)

    return top_mentions.collect().rows()
