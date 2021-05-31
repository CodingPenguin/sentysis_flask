import re
from textblob import TextBlob

def spellcheck(value):
    replace_dict = {"\xa0": " ", "&#39;": "'", "&quot;": '"', "\u003cbr /\u003e": " ", "\r": "" }
    rep = dict((re.escape(k), v) for k, v in replace_dict.items())
    pattern = re.compile("|".join(rep.keys()))
    value = str(TextBlob(pattern.sub(lambda m: rep[re.escape(m.group(0))], value)))
    return value
