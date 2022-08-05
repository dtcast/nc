import random
from datetime import datetime
from app_store_scraper import AppStore
from pprint import pprint
import pandas as pd

lineage = AppStore(country="kr", app_name="리니지2M")
lineage.review(how_many=10000)
reviews = lineage.reviews
df = pd.DataFrame(reviews)
df.to_csv("app_store_test.csv")

