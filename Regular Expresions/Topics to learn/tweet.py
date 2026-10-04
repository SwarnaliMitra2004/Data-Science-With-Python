import re

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today [http://t.co/lbwej0pxOd](http://t.co/lbwej0pxOd) cc: @garybernhardt #rstats'''

# Remove URLs
tweet = re.sub(r'https?://\S+|\[https?://[^\]]+\]\(https?://[^)]+\)', '', tweet)

# Remove RT and CC
tweet = re.sub(r'\bRT\b|\bcc:', '', tweet)

# Remove mentions
tweet = re.sub(r'@\w+', '', tweet)

# Remove hashtags
tweet = re.sub(r'#\w+', '', tweet)

# Remove punctuation
tweet = re.sub(r'[^\w\s]', '', tweet)

# Remove extra spaces
tweet = re.sub(r'\s+', ' ', tweet).strip()

print(tweet)