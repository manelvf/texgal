import Image
import os
import redis

FOLDER = 'images'

r = redis.Redis(host="localhost",port=6379,db=0)

def populate():
    files = os.listdir(FOLDER)

    for f in files:
        f = open(FOLDER + "/" +f, "rb")
        f.seek(0)
        i = f.read()
        f.close()
        id_image = r.incr("ids:image")
        r.sadd("image-list",id_image)
        r.set("image:"+str(id_image)+":content", i)



if __name__ == '__main__':
    populate()

