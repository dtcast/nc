import json
import requests
import pandas as pd
from app_store_scraper import AppStore

# https://apps.apple.com/kr/app/watcha/id1096493180
# my_app = AppStore(country='kr', app_name='%EB%A6%AC%EB%8B%88%EC%A7%802m', app_id='1478227443')  # app_id는 optional
# print(my_app)
# review = my_app.review(20)
# print(review)  # 객체 검증

data_list = []
for i in range(1, 20):
    page = 1
    url = f"https://itunes.apple.com/kr/rss/customerreviews/page={page}/id=1478227443/sortBy=mostRecent/json"
    response = requests.get(url=url)
    json_data = json.loads(response.text)
    for i in range(len(json_data['feed']['entry'])):
        data_list.append({
            'created_at': json_data['feed']['entry'][i]['updated']["label"],
            'rate': json_data['feed']['entry'][i]['im:rating']["label"],
            'like': json_data['feed']['entry'][i]['im:voteSum']["label"],
            'dislike': int(json_data['feed']['entry'][i]['im:voteCount']["label"]) - int(
                json_data['feed']['entry'][i]['im:voteSum']["label"]),
            'title': json_data['feed']['entry'][i]['title']["label"],
            'content': json_data['feed']['entry'][i]['content']['label']
        })

df = pd.DataFrame(data_list)
df.to_csv("app_store_test.csv")