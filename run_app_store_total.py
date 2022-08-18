import random
from datetime import datetime
from app_store_scraper import AppStore
from pprint import pprint
import pandas as pd

keyword_list = ["원신", "세븐나이츠 레볼루션"]
keyword = "원신"

lineage = AppStore(country="kr", app_name=f"{keyword}", app_id="1517783697")
lineage.review(how_many=10000)
reviews = lineage.reviews
df = pd.DataFrame(reviews)
df.to_csv(f"{keyword}_app_store.csv")