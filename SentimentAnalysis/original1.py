# -*- coding: utf-8 -*-
"""
@author: Harsh
"""
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))

sentiment_analyzer_scores("I did not like the movie.")


#Punctuations
print(sentiment_analyzer_scores("The food here is good"))

print(sentiment_analyzer_scores("The food here is good!"))
print(sentiment_analyzer_scores("The food here is good!!"))
print(sentiment_analyzer_scores("The food here is good!!!"))


#Captialization
print(sentiment_analyzer_scores("The food here is great!"))

print(sentiment_analyzer_scores("The food here is GREAT!"))

#Degree modifiers
print(sentiment_analyzer_scores("The service here is good"))

print(sentiment_analyzer_scores("The service here is Tremendously good"))

print(sentiment_analyzer_scores("The service here is marginally good"))

#Conjunction
print(sentiment_analyzer_scores("The food here is great, but the service is horrible"))

#Handeling emojis
print(sentiment_analyzer_scores('I am 😄 today'))
print(sentiment_analyzer_scores('😊'))
print(sentiment_analyzer_scores('😥'))
print(sentiment_analyzer_scores('☹️'))

#Slang
print(sentiment_analyzer_scores("Today SUX!"))
print(sentiment_analyzer_scores("Today only kinda sux! But I'll get by, lol"))

#Emoticons
print(sentiment_analyzer_scores("Make sure you :( or :D today!"))




