import redis
from flask import Flask
import config

# Initialize the app
app = Flask(__name__, instance_relative_config=True)
redis_db = redis.Redis(
	host=config.REDIS_HOSTNAME,
	port=config.REDIS_PORT, 
	password=config.REDIS_PASSWORD
)

from app import views
app.config.from_object('config')
