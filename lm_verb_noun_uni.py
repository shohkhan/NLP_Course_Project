#!/usr/bin/env python

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

Total lines: 4861729
Train: 2900000
Validation: 500000
Test: 1461729
'''

import collections, math
import re
from nltk import word_tokenize
import nltk.data
import time
from datetime import datetime
start_time = time.time()

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

puni = collections.defaultdict(int)
nuni = collections.defaultdict(int)

commentthreshold = 8

subreds = collections.defaultdict(int)
subreds['"AskReddit"']= 1
subreds['"leagueoflegends"']= 2
subreds['"Fireteams"']= 3
subreds['"trees"']= 4
subreds['"Dota2Trade"']= 5
subreds['"friendsafari"']= 6
subreds['"reddit.com"']= 7
subreds['"tf2trade"']= 8
subreds['"circlejerk"']= 9
subreds['"GlobalOffensiveTrade"']= 10
subreds['"gaming"']= 11

def smooth_tri():
    vocp = len(puni)
    vocn = len(nuni)
    for k1,v1 in puni.viewitems():
        puni[k1] = math.log(v1 + 1.0) - math.log(vocp * 1.0)
    for k1,v1 in nuni.viewitems():
        nuni[k1] = math.log(v1 + 1.0) - math.log(vocn * 1.0)

def preprocess(line):
    pattern = re.compile(r"[a-z0-9]+")
    line = ' '.join(pattern.findall(line))
    t = word_tokenize(line)
    tags = nltk.pos_tag(t)
    tokens = []
    for tok, pos in tags:
        if pos.startswith("NN") or pos.startswith("VB"):
            tokens.append(tok)
    #tokens.insert(0, "<s>")
    #tokens.append("</s>")
    return tokens

def getlines(l):
    i = l.split(",")
    if len(i) == 9 and i[3].isdigit():
        text = '%s\n%s' % (i[7], i[5])
        text = text.lower()
        pattern = re.compile(r"[a-z0-9!\$&\*\|\?_\./\\]+")
        text = ' '.join(pattern.findall(text))
        text = text.replace("\n\n", "").replace("\\r", "").replace("\\n", "").replace("_", " ").replace("\n", "")
        lines = tokenizer.tokenize(text)
        time = datetime.fromtimestamp(float(i[1]))
        return lines, int(i[3]), len(i[7]), len(i[5]), i[2], i[6], time.year, time.month, time.day, time.hour, time.minute, time.weekday()
    return 0

def calc_probability_tri(l):
    vocp = len(puni)
    vocn = len(nuni)
    pos = 0
    neg = 0
    tag = 0
    lines = getlines(l)
    if lines!= 0:
        if int(lines[1]) > commentthreshold:
            tag = 1
        for line in lines[0]:
            t = preprocess(line)
            for i in range(len(t)):
                if puni[t[i]] == 0:
                    pos += math.log(1.0) - math.log(vocp*1.0)
                else:
                    pos += puni[t[i]]
                if nuni[t[i]] == 0:
                    neg += math.log(1.0) - math.log(vocn*1.0)
                else:
                    neg += nuni[t[i]]
        if pos > neg: out = 1
        else: out = 0
        print lines[2], lines[3], subreds[lines[5]], lines[6], lines[7], lines[8], lines[9], lines[10], lines[11], \
            pos, neg, pos-neg, tag, out#, lines[4]
    return pos, neg, tag

def create_model_tri(path):
    f = open(path, 'r')
    for l in f.readlines():
        lines = getlines(l)
        if lines != 0:
            if int(lines[1]) > commentthreshold:
                for line in lines[0]:
                    tokens = preprocess(line)
                    for i in range(len(tokens)):
                        puni[tokens[i]] += 1
            else:
                for line in lines[0]:
                    tokens = preprocess(line)
                    for i in range(len(tokens)):
                        nuni[tokens[i]] += 1

def predict_tri(file):
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    f = open(file, 'r')
    for l in f.readlines():
        pos, neg, tag = calc_probability_tri(l)
        if pos > neg and tag == 1: TP += 1
        elif pos < neg and tag == 0: TN += 1
        elif pos > neg and tag == 0: FP += 1
        elif pos < neg and tag == 1: FN += 1
    print("TP: %s, TN: %s, FP: %s, FN: %s" % (TP, TN, FP, FN))

if __name__ == "__main__":
    trainset="nlp_train"
    validationset = ""
    testset = "nlp_test"

    create_model_tri(trainset)
    smooth_tri()

    predict_tri(testset)


    print("--- %s seconds ---" % (time.time() - start_time))