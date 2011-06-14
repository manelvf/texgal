import Image
import os
import redis

FOLDER = 'images'

r = redis.Redis(host="localhost",port=6379,db=0)

def list():
    members = r.smembers("image-list")
    print str(members)
    for e in members:
        print str(e)



if __name__ == '__main__':
    list()

