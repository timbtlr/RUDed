# R U Ded?

Ping URLs and verify expected status codes.

### Overview

Send POST requests to a simple Flask application with the following data:

```
{
	"url": "http://hello.com",
	"expected_status": 400
}
```

The key/value pair is added to the redis DB of your choice.  

`recurring.py` can be used to call the URLs saved in the Redis store.  If the status
returned by accessing the URL is not the expected status saved with the URL, then
a bad response metric will be sent to DataDog.

### Required Variables

- REDIS_HOSTNAME - Hostname of the Redis database
- REDIS_PASSWORD - Password to the Redis database
- REDIS_PORT - Port to the Redis database
- API_KEY - API key used to interact with this application