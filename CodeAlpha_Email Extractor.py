import re

text = """
Contact us:
abc@gmail.com
test@yahoo.com
hello123@gmail.com
"""

emails = re.findall(r'\S+@\S+', text)

for email in emails:
    print(email)import re

text = """
Contact us:
abc@gmail.com
test@yahoo.com
hello123@gmail.com
"""

emails = re.findall(r'\S+@\S+', text)

for email in emails:
    print(ema