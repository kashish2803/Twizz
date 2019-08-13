import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis
    '''
    def __init__(self):
        '''
        Class constructor or initializer
        '''
        # Keys and Tokens
        consumer_key = "YOUR_CONSUMER_KEY" 
        consumer_secret = "YOUR_CONSUMER_SECRET"
        access_token = "YOUR_ACCESS_TOKEN"
        access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

        # Attempt authentication
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Authentication failed")
    
    def get_tweets(self, query, count = 10):
        '''
        Main Function to get tweets and parse them
        '''
        tweets = []

        try:
            # Call twitter API to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # Parsing the tweets
            for tweet in fetched_tweets:
                parsed_tweet = {}
                parsed_tweet['text'] = tweet.text
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # Appending tweets to the tweets list
                if tweet.retweet_count > 0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            return tweets

        except tweepy.TweepError as e:
            # Print error if any
            print("Error: " + str(e))

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet by removing links, special characters using RegEx
        '''
        pattern = r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"
        tweet = re.sub(pattern, " ", str(tweet))
        tweet = ' '.join(tweet.split())
        return tweet
    
    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of parsed tweet
        '''
        analysis = TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'


def main():
    # Create an object of twitter class
    api = TwitterClient()

    # Calling the function to get tweets
    tweets = api.get_tweets(query = "EidAdhaMubarak", count = 200)

    # Calculating percentages of positive and negative tweets
    # positive_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # negative_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']

    return tweets

    # print("Positive tweets percentage: {:.2f} %".format(len(positive_tweets)/len(tweets)*100))
    # print("Negative tweets percentage: {:.2f} %".format(len(negative_tweets)/len(tweets)*100))
    # print("Neutral tweets: {:.2f} %".format((len(tweets) - len(positive_tweets) - len(negative_tweets))/len(tweets)*100))

    # Printing first 5 positive tweets
    # print("\n\nPositive Tweets:")
    # for tweet in positive_tweets[:5]:
        # print(tweet['text'])

    # Printing first 5 negative tweets
    # print("\n\nNegative Tweets:")
    # for tweet in negative_tweets[:5]:
        # print(tweet['text'])

if __name__ == "__main__":
    main()