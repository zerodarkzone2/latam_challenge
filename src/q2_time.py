from typing import List, Tuple
import polars as pl
import emoji


def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Read the json file as a polars DataFrame
    data: pl.LazyFrame = pl.scan_ndjson(file_path)

    # Parse emoji data using the emoji library
    emoji_data = data.select(
        pl.col("content").map_elements(lambda x: [em.chars for em in emoji.analyze(x)]).explode()
    ).filter(pl.col("content").is_not_null())

    # Get the top 10 emojis
    top_emojis = emoji_data.group_by("content").count().sort("count", descending=True).head(10)

    # Return a tuple with the answer
    return top_emojis.collect().rows()
