import re

code = "K1KA5CB7"

digit = [s for s in re.findall(r'\d+', code)]
alphabet = [s for s in re.findall(r'[A-Z]', code)]

result = ''.join((sorted(alphabet) + sorted(digit)))
print(result)
