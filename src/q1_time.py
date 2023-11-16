from typing import List, Tuple
from datetime import datetime
import polars as pl

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Read the json file as a polars DataFrame
    data: pl.LazyFrame = pl.scan_ndjson(file_path)

    # Select the desired columns
    df = data.select(pl.col("id"), pl.col('date').str.to_datetime().cast(pl.Date).alias("date"),
                     pl.col("user").struct.field("username"))

    # Get the top 10 dates with most tweets
    dates_df = df.group_by("date").count().sort(by="count", descending=True).select("date").head(10)

    # Select only the rows within the respective dates
    df = df.join(dates_df, on="date", how="inner").collect()

    # For every date, select the user with the most tweets
    rows = df.group_by(["date", "username"]).count().with_columns(
        pl.col("count").rank(descending=True).over(["date"]).alias("rn")
    ).filter(pl.col("rn") == 1).select(["date", "username"]).rows()

    return rows
