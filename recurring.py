import os
import redis
import requests

redis_db = redis.Redis(
	host=os.environ.get("REDIS_HOSTNAME"),
	port=os.environ.get("REDIS_PORT"), 
	password=os.environ.get("REDIS_PASSWORD")
)

for key in redis_db.keys():
	value = redis_db.get(key)
	try:
		r = requests.get(key)

		if r.status_code == value:
			print("{} -- match".format(key))
		else:
			print("{} -- no match".format(key))
	except Exception as e:
		print(str(e))