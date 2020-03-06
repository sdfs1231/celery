import re

pattern = re.compile(r'(\w+) (\w+)')
print(pattern.match('hello world'))