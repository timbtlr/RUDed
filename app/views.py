import redis
import config
import json
from flask import request, make_response

from app import app, redis_db
from authentication import requires_auth

@app.route('/add', methods=['POST'])
@requires_auth
def index():
	response = None
	data = json.loads(request.data)

	# Ensure the correct data is sent in
	if not data.get("url"):
		return make_response(("'url' data field is required", 400))
	if not data.get("expected_status"):
		return make_response(("'expected_status' data field is required", 400))

	redis_db.set(data.get("url"), data.get("expected_status"))

	return make_response(("Added key/value pair", 201))
