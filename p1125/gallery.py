import json
import oracledb
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
json_path = BASE_DIR / "gallerylist.json"

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["response"]["body"]["items"]["item"]
df = pd.DataFrame(items)

# PK인 gno 생성 (1부터 시작)
df.insert(0, "gno", range(1, len(df) + 1))

cols = [
    "gno",
    "galContentId",
    "galContentTypeId",
    "galTitle",
    "galWebImageUrl",
    "galCreatedtime",
    "galModifiedtime",
    "galPhotographyMonth",
    "galPhotographyLocation",
    "galPhotographer",
    "galSearchKeyword",
]
rows = [tuple(x) for x in df[cols].itertuples(index=False, name=None)]

conn = oracledb.connect(
    user="ora_user", password="1111", dsn="localhost:1521/xe"
)
cur = conn.cursor()

sql = """
INSERT INTO gallerylist2 (
    gno, galContentId, galContentTypeId, galTitle, galWebImageUrl,
    galCreatedtime, galModifiedtime, galPhotographyMonth,
    galPhotographyLocation, galPhotographer, galSearchKeyword
) VALUES (
    :1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11
)
"""

cur.executemany(sql, rows)
conn.commit()
cur.close()
conn.close()
