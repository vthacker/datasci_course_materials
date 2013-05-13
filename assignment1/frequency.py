import sys
import json
from sets import Set

tweets = [] #initialize an empty dictionary

def hw(tweet_file):
    loadTweetFile(tweet_file)
    allTweetsCombined = ' '.join(tweets)
    uniqueTerms = generateUniqueTerms(allTweetsCombined)
    calculateFrequencies(uniqueTerms, allTweetsCombined)
    
def loadTweetFile(tweet_file):
    for line in tweet_file:
        entireTweet = json.loads(line)
        tweetText = entireTweet.get('text', None)
        if(tweetText != None):
            tweets.append(tweetText)

def generateUniqueTerms(allTweets):
    words = allTweets.split()
    uniqueTerms = Set()
    for word in words:
        uniqueTerms.add(word)
    return uniqueTerms

def calculateFrequencies(terms, allTweetsCombined):
    
    terms_total = len(allTweetsCombined.split())

    # Count all the occurrences.
    for term in terms:
        count = allTweetsCombined.count(term)
        frequency = float(count)/float(terms_total)
        print term + " " + str(frequency)
            

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()
