import os 

DEBUG = True
REDIS_HOSTNAME = os.environ.get("REDIS_HOSTNAME")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
REDIS_PORT = os.environ.get("REDIS_PORT")
API_KEY = os.environ.get("API_KEY")