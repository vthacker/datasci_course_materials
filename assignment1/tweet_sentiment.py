import sys
import json

scores = {} # initialize an empty dictionary
tweets = [] # initialize an empty list


def hw(sent_file, tweet_file):
    loadAffinityFile(sent_file)
    loadTweetFile(tweet_file)
    computeSentiment()
    
def computeSentiment():
    for tweet in tweets:
        words = tweet.lower().split(' ')
        sentiment = 0
        for word in words:
            sentiment = sentiment + scores.get(word, 0)
        print float(sentiment)
    
def loadAffinityFile(sent_file):
    for line in sent_file:
         term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
         scores[term] = int(score)  # Convert the score to an integer.
         
def loadTweetFile(tweet_file):
    for line in tweet_file:
        entireTweet = json.loads(line)
        tweetText = entireTweet.get('text', None)
        if(tweetText != None):
            tweets.append(tweetText)

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
