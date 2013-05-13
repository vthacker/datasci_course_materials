import sys
import json

scores = {} # initialize an empty dictionary
tweets = [] # initialize an empty list

def hw(sent_file, tweet_file):
    loadAffinityFile(sent_file)
    loadTweetFile(tweet_file)
    findHappiest()

def lines(fp):
    print str(len(fp.readlines()))

def loadAffinityFile(sent_file):
    for line in sent_file:
         term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
         scores[term] = int(score)  # Convert the score to an integer.
         
def loadTweetFile(tweet_file):
    for line in tweet_file:
        entireTweet = json.loads(line)
        if entireTweet.get('text', None) != None and entireTweet.get('place', None) != None and entireTweet['place']['country'] == 'United States'  and entireTweet['place']['country_code'] == 'US':
            tweetText = entireTweet['text']
            state= str((entireTweet["place"]["full_name"]).split(",")[1]).strip()
            tweets.append((tweetText,state))

def findHappiest():
    states={}
    for (tweet, state) in tweets:
        tweet_score = 0.0
        tweet_words = tweet.lower().split()
        for word in tweet_words:
            tweet_score += scores.get(word, 0.0)
        
        if state in states:
            states[state] += tweet_score
        else:
            states[state] = tweet_score
            
    x = 0.0
    finalState = ""
    for key, value in states.iteritems():
        if value > x:
            finalState = key
            x= value
    print finalState
            

def main():
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    #lines(sent_file)
    #lines(tweet_file)
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
