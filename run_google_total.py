from google_play_scraper import Sort, reviews_all
import pandas as pd

keyword_list = ["com.netmarble.skrv"]

for keyword in keyword_list:
    rate = None
    result = reviews_all(
        f'{keyword}',
        sleep_milliseconds=0, # defaults to 0
        lang='ko', # defaults to 'en'
        country='kr', # defaults to 'us'
        sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
        filter_score_with=rate # defaults to None(means all score)
    )
    df = pd.DataFrame(result)
    df.to_csv(f"{keyword}.csv")
    print(f"{keyword} 에 대한 크롤링 끝")