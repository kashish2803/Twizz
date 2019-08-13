from flask import Flask, request
from flask import render_template
from twitter import TwitterClient

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    keyword = request.form['keyword']
    count = request.form['count']

    # Get the tweets
    try:
        api = TwitterClient()
        tweets = api.get_tweets(query = keyword, count = count)

        positive_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
        positive_tweets_percentage = round(len(positive_tweets)/len(tweets)*100, 2)

        negative_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
        negative_tweets_percentage = round(len(negative_tweets)/len(tweets)*100, 2)

        neutral_percentage = round((len(tweets) - len(positive_tweets) - len(negative_tweets))/len(tweets)*100, 2)

        context = {
            'ptweets': positive_tweets[:5], 
            'ntweets': negative_tweets[:5], 
            'ppercent': positive_tweets_percentage, 
            'npercent': negative_tweets_percentage,
            'neutral': neutral_percentage
        }
    
        return render_template("results.html", context = context)
    except Exception as e:
        return str(e)
    

if __name__ == "__main__":
    app.run(debug=True)

