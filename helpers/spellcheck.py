import html
from textblob import TextBlob

def spellcheck(value):
    result = TextBlob(html.unescape(value))
    return result
