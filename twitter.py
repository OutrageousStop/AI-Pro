from TwitterSearch import *

def search(keyword):
    try:
        tso = TwitterSearchOrder() 
        tso.set_keywords([i for i in keyword.split()])
        tso.set_language('en') 
        tso.set_include_entities(False) 

        
        ts = TwitterSearch(
            consumer_key = 'ENauUyNYryjA1hGWjmWuzLfyF',
            consumer_secret = 'LzDYf14Ey5nEFt3YpNuFtLl0yE3gIYbv6omyGJgvoilbcukL9z',
            access_token = '1040904429333929986-IyGhvu579GFEqZjlDeSyLTaHdQSJ5a',
            access_token_secret = 'bI4gto3QC0gk3SPJDZKl0iJNSJ92ErQDD4feolKHXEKV4'
        )
        tweets = []
        
        for tweet in ts.search_tweets_iterable(tso):
            tweets.append('@%s tweeted: %s (end)' % ( tweet['user']['screen_name'], tweet['text'] ) )

        return tweets
    except TwitterSearchException as e: 
        return e


if __name__ == "__main__":
    print(search(input("Enter keyword: ")))