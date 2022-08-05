from google_play_scraper import Sort, reviews_all
import pandas as pd


rate = 1
result = reviews_all(
    'com.ncsoft.lineage2m19',
    sleep_milliseconds=0, # defaults to 0
    lang='ko', # defaults to 'en'
    country='kr', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    filter_score_with=rate # defaults to None(means all score)
)

df = pd.DataFrame(result)
df.to_csv(f"lineage_google_play_{rate}.csv")