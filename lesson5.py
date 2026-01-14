# from datetime import datetime

# from projects.utils import sum_numbers

# import os

# print(os.getcwd())


# now = datetime.now()
# print(now)



import requests

r = requests.get("https://online.geeks.kg")
print(r.status_code)







