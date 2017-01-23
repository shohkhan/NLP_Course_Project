'''
0. author
1. created_utc
2. id
3. num_comments
4. over_18
5. selftext
6. subreddit
7. title
8. url


Mean: 9.66308805824
Median: 3.0
'''

import time
import numpy as np

start_time = time.time()

def getthreshold():
    comment_count = []
    with open("posts_with_selftexts") as f:
        line = f.readline()
        while line:
            i = line.split(",")
            if len(i) == 9 and i[3].isdigit():
                comment_count.append(int(i[3]))
            line = f.readline()
    print ("Mean: %s" % str(np.mean(comment_count)))
    print ("Median: %s" % str(np.median(comment_count)))

def getdataforNLPonly():
    subreddits = ['"AskReddit"',
    '"leagueoflegends"',
    '"Fireteams"',
    '"trees"',
    '"Dota2Trade"',
    '"friendsafari"',
    '"reddit.com"',
    '"tf2trade"',
    '"circlejerk"',
    '"GlobalOffensiveTrade"',
    '"gaming"']

    with open("posts_with_selftexts") as f:
        line = f.readline()
        while line:
            i = line.split(",")
            if len(i) == 9 and subreddits.__contains__(i[6]):
                print line
            line = f.readline()

def getPosNeg():
    posdata1 = 0
    negdata1 = 0
    posdata2 = 0
    negdata2 = 0
    with open("nlp_dataset_2") as f:
        line = f.readline()
        while line:
            i = line.split(",")
            if len(i) == 9 and i[3].isdigit():
                if (int(i[3]) > 8): posdata1 += 1
                else: negdata1 += 1
                #if (int(i[3]) > 3): posdata2 += 1
                #else: negdata2 += 1
            line = f.readline()
    print ("Pos: %s" % str(posdata1))
    print ("Neg: %s" % str(negdata1))
    #print ("Pos: %s" % str(posdata2))
    #print ("Neg: %s" % str(negdata2))

def getenglish():
    with open("nlp_train") as f:
        line = f.readline()
        while line:
            i = line.split(",")
            if len(i) == 9 and i[3].isdigit():
                pass
            line = f.readline()



getPosNeg()