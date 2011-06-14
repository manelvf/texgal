import redis

"""
Upload
"""

UPLOADS_DEFAULT_DEST = "/Users/manel/Sites/virtualenvs/texgal/texgal/uploads"
#UPLOADS_DEFAULT_URL = ""


"""
DB
"""

r = redis.Redis(host="localhost",port=6379,db=0)



