#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading

import twitter

#import classifier as cl
#import tweet_model

class AsyncFetchSave(threading.Thread):
    def __init__(self, query, max_output = 90):
        threading.Thread.__init__(self)
        self.query = query
        self.max_output = max_output
        self.output_count = 0
        self.data = {}

    def fetchTweet(brand):
        data = {}

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

        self.output_count = len(data)
        self.data =  data

    def run(self):

    	#set data from twiteer
    	self.fetchTweet(self.query)

    	#add sentiment to the data


    	#add newData to database
    	tweet_model.addTweetFromDict(self.data, self.query)

    	#predict next data size
    	if self.output_count < self.max_output:
    		self.time_to_wait += 10





if __name__ == "__main__":
    brands = ["apple", "siemens", "samsung", "nvidia", "coca-cola"]

    for brand in brands:
        AsyncFetchSave(brand).start()

