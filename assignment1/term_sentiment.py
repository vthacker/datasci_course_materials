import sys
import json

scores = {} # initialize an empty dictionary
tweets = [] # initialize an empty list

def hw(sent_file, tweet_file):
    loadAffinityFile(sent_file)
    loadTweetFile(tweet_file)
    computeTermSentiments()

def lines(fp):
    print str(len(fp.readlines()))

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

def computeTermSentiments():

    # Iterate over tweets.
    for tweet in tweets:
        tweet_score = 0
        tweet_words = tweet.lower().split()

        # Get the score of a tweet.
        for word in tweet_words:
            tweet_score += scores.get(word, 0)

        # Print the score of all words.
        for word in tweet_words:
            word_score = scores.get(word, float(tweet_score)/len(tweet_words))
            print  word + " " + str(float(word_score))
            

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
