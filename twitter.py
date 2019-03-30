from TwitterSearch import *

def search(keyword):
    try:
        tso = TwitterSearchOrder() 
        tso.set_keywords([i for i in keyword.split()])
        tso.set_language('en') 
        tso.set_include_entities(False) 

        
        ts = TwitterSearch(
            consumer_key = '8xwfAotIMlpjBidB6LN2oBaVb',
            consumer_secret = 'JHZU1hhfsQZON1L6zZM4NlomA9gKWDTwasPF3b7mkzzY0i9WRN',
            access_token = '1040904429333929986-rJveV2YAwYJnTyhG9fIY436jCSJm9F',
            access_token_secret = 'tJMiqZMBOQJFre39kcDM0GW3aEEDhikSWq3q1y8IBYiHe'
        )
        tweets = []
        
        for tweet in ts.search_tweets_iterable(tso):
            #tweets.append('@%s tweeted: %s (end)' % ( tweet['user']['screen_name'], tweet['text'] ) )
            tweets.append(tweet['text'])

        return tweets
    except TwitterSearchException as e: 
        return []

def tweep(keyword):
    a = search(keyword)
    return a

if __name__ == "__main__":
    print((tweep(input("Enter keyword: "))))
