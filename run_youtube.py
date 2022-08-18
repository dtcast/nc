from googleapiclient.discovery import build
import pandas as pd
api_key = 'AIzaSyDiynKGG_h2V8917ZvodqTwwvvKj9OKep8'


def video_comments(video_id):
    # empty list for storing reply
    replies = []

    # creating youtube resource object
    youtube = build('youtube', 'v3',
                    developerKey=api_key)

    # retrieve youtube video results
    video_response = youtube.commentThreads().list(
        part='snippet,replies',
        videoId=video_id
    ).execute()

    # iterate video response

    df = pd.DataFrame()
    comment_info_list = []
    while video_response:

        # extracting required info
        # from each result object
        for item in video_response['items']:


            # Extracting comments
            print(item)
            try:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                user = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
                post_date = item['snippet']['topLevelComment']['snippet']['publishedAt']
            except:
                continue
            # counting number of reply of comment
            # replycount = item['snippet']['totalReplyCount']

            # if reply is there
            # if replycount > 0:
            #
            #     # iterate through all reply
            #     for reply in item['replies']['comments']:
            #         # Extract reply
            #         reply = reply['snippet']['textDisplay']
            #
            #         # Store reply is list
            #         replies.append(reply)

            # print comment with list of reply
            print(user, comment, post_date, end='\n\n')
            comment_info_list.append({"user": user, "comment": comment, "post_date": post_date})

            # empty reply list
            replies = []

        # Again repeat
        if 'nextPageToken' in video_response:
            video_response = youtube.commentThreads().list(
                part='snippet,replies',
                videoId=video_id,
                pageToken=video_response["nextPageToken"]
            ).execute()
        else:
            df = pd.DataFrame(comment_info_list)
            df.to_csv(f"{video_id}_{len(comment_info_list)}.csv")
            break


# Enter video id
video_id = "tkDO3cx7EoU"

# Call function
video_comments(video_id)