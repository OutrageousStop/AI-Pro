from TwitterSearch import *
import fetch

def search(keyword):
    try:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords([i for i in keyword.split()]) # let's define all words we would like to have a look for
        tso.set_language('en') # we want to see German tweets only
        tso.set_include_entities(False) # and don't give us all those entity information

        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(
            consumer_key = 'ENauUyNYryjA1hGWjmWuzLfyF',
            consumer_secret = 'LzDYf14Ey5nEFt3YpNuFtLl0yE3gIYbv6omyGJgvoilbcukL9z',
            access_token = '1040904429333929986-IyGhvu579GFEqZjlDeSyLTaHdQSJ5a',
            access_token_secret = 'bI4gto3QC0gk3SPJDZKl0iJNSJ92ErQDD4feolKHXEKV4'
        )

        # this is where the fun actually starts :)
        for tweet in ts.search_tweets_iterable(tso):
            print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)


if __name__ == "__main__":
    search('india')