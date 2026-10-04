import re

emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""

pattern = r'(\w+)@(\w+)\.(\w+)'

matches = re.findall(pattern, emails)

for match in matches:
    print("User ID:", match[0])
    print("Domain:", match[1])
    print("Suffix:", match[2])
    print()