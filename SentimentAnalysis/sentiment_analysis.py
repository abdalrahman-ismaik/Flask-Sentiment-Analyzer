from textblob import TextBlob

def sentiment_analyzer(text):
    """Analyze sentiment of text using TextBlob"""
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        return "SENTIMENT_POSITIVE", polarity
    elif polarity < 0:
        return "SENTIMENT_NEGATIVE", abs(polarity)
    return "SENTIMENT_NEUTRAL", 0.0