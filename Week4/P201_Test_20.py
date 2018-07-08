import re

numberRegex = re.compile(r'\d{3}')
numberRegex.sub(r'\3', '42 4333 1567 6542 789 12344')
