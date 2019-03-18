import re

string = "[<Element 'meta' content='Want to secure your WordPress site with SSL? Learn how to add an SSL certificate and move your WordPress from HTTP to HTTPS to ensure site security.' property='og:description'>]"

result = re.search(r"(?<==)'(\w+).*\.'", string)

print(result.group(0))