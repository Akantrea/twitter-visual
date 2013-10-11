#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter

#import classifier as cl
#import tweet

def fetchTweet(brand):

    data={}

    twitter_api = twitter.Api()

    tweet_data = twitter_api.GetSearch(term = brand, count=2000)

    for tweet in tweet_data:

        data[ tweet.id ] = {
                        "tweet_created_at" :                                  tweet.created_at,
                        "tweet_text" :                                        tweet.text,
                        "tweet_lang" :                                        tweet.lang,
                        "tweet_hashtags":                                     tweet.hashtags,

                        "user_id" :                                           tweet.user.id,
                        "user_username" :                                     tweet.user.screen_name,
                        "user_tweet_count" :                                  tweet.user.listed_count,
                        "user_friends_count" :                                tweet.user.friends_count,
                        "user_followers_count" :                              tweet.user.followers_count,
                        "user_favourites_count" :                             tweet.user.favourites_count,
                        "user_created_at" :                                   tweet.user.created_at
                    }

    return data