import pandas as pd
import requests
import re
from bs4 import BeautifulSoup as bs

url = 'https://www.toutiao.com/article/v2/tab_comments/?aid=24&app_name=toutiao_web&offset=0&count=20&group_id=7044094970898153998&item_id=7044094970898153998&_signature=_02B4Z6wo00f01eoGLDwAAIDCWvfA9nkYV7XqIyiAABtFt1aXq1V8bTLHMF.7RNlU9cLwvEibaQMgA00arME.w72alMsveWXabcUXPETTSH5lcl7HDhU3rgh5.ymxccs8omLlyoKTreZ7m4CKd6'

res = requests.get(url).text
print(res)