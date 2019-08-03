import tweepy
import time

print("this is a twitter bot")
CONSUMER_KEY='ANeiGT8xMOsE5ikqWqyd0UQ9J'
CONSUMER_SECRET='exBXz9S4ENorma74dsvPSs27tkC3mtgTBu1Y8r3cYj0Zoutoo6'
ACCESS_KEY='875580819078651905-heNcHXKDORBRUtUdBESMq0wCx6yaPXs'
ACCESS_SECRET='hWFH31qfIoACiALU7NfghfXcx5LH0W9xChFnLSuvUp82e'

auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api=tweepy.API(auth)
FILE_NAME = './last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('replying to tweets...')
    last_seen_id=retrieve_last_seen_id(FILE_NAME)
    #print("Last id is:",last_seen_id)
    mentions=api.mentions_timeline()
    for mention in reversed(mentions):
        print(str(mention.id) + ' - '  +mention.text)
        #t0=mention[0]
        last_seen_id=mention.id
        store_last_seen_id(last_seen_id,FILE_NAME)
        if 'hello' in mention.text.lower():
            print('found')
            print('responding...')
            try:
                api.update_status('@'+mention.user.screen_name+' '+'hello back to you!',mention.id)
            except tweepy.TweepError as error:
                if error.api_code == 187:
                # Do something special
                    print('duplicate message')
                else:
                    raise error
            
        else:
            print('not found')

while True:
    reply_to_tweets()
    time.sleep(15)

