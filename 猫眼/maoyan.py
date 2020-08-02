'''
Function:
	猫眼电影评论爬取
作者:
	Charles
公众号:
	Charles的皮卡丘
'''
import re
import time
import json
import pickle
import random
import datetime
import requests


'''
Function:
	爬虫类
'''
class Spider():
	def __init__(self):
		self.info = '猫眼电影评论爬虫'
		self.json_url = "http://m.maoyan.com/mmdb/comments/movie/{}.json?v=yes&offset={}&startTime="
		self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

	'''开始爬取'''
	def start(self, url, num_retries=3):
		film_id = url.split('/')[-1]
		start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())).replace(' ', '%20')
		res = requests.get(url, headers=self.headers)
		end_time = re.findall(r'"ellipsis">(\d+-\d+-\d+).*?<', res.text)[0]
		all_data_dict = {}
		while start_time.split(' ')[0] > end_time:
			print('[INFO]: start time is %s...' % start_time.replace('%20', ' '))
			for page in range(100):
				print('<Page>: %s, <Data size>: %s' % (page, len(all_data_dict.keys())))
				json_url = self.json_url.format(film_id, 15*page) + start_time
				res = requests.get(json_url, headers=self.headers)
				try:
					res = requests.get(json_url, headers=self.headers)
				except:
					num_retries -= 1
					if num_retries < 0:
						break
				if res.status_code == 200:
					content = res.content
				else:
					content = None
				if content:
					data = self.__parse_data(content)
					if data:
						all_data_dict = dict(all_data_dict, **data)
				time.sleep(1 + random.random())
			start_time = start_time.replace('%20', ' ')
			start_time = datetime.datetime.fromtimestamp(time.mktime(time.strptime(start_time, '%Y-%m-%d %H:%M:%S'))) + datetime.timedelta(seconds=-24*3600)
			start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.mktime(start_time.timetuple()))).replace(' ', '%20')
		f = open('comments_data.pkl', 'wb')
		pickle.dump(all_data_dict, f)
	'''数据解析'''
	def __parse_data(self, data):
		data_temp = json.loads(data, encoding='utf-8').get('cmts')
		data = {}
		if data_temp:
			for dt in data_temp:
				# 昵称
				nickName = dt.get('nickName')
				# 性别
				gender = dt.get('gender')
				# 评论内容
				content = dt.get('content')
				# 时间
				start_time = dt.get('startTime')
				# 城市
				city_name = dt.get('cityName')
				# 评分
				score = dt.get('score')
				data[nickName] = [gender, city_name, score, content, start_time]
		return data


if __name__ == '__main__':
	url = 'https://maoyan.com/films/78480'
	Spider().start(url)