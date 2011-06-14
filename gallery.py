import Image
import os
import logging
import settings

from flask import (Flask, url_for, render_template, request, redirect, flash,
                   session, g)
from flaskext.uploads import (UploadSet, IMAGES, configure_uploads,
                              patch_request_class)
from settings import r, UPLOADS_DEFAULT_DEST, UPLOADED_DEFAULT_DEST

UPLOADED_IMAGES_DEST = "/Users/manel/Sites/virtualenvs/texgal/texgal/uploads"


app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True

textures_set = UploadSet('textures', IMAGES)
configure_uploads(app, textures_set)


@app.route('/')
def hello_world():
      s = ""

      members = r.smembers("image-list")
      member_list = []
      for e in members:
          member_list.append(e)
          
      cur_member = 0 #members[0]
      print member_list

      return render_template('gallery.html', member_list=member_list)


@app.route('/img/<int:img_id>')
def get_image(img_id):
  i = r.get("image:"+str(img_id)+":content")
  mimetype = "image/jpeg"
  return app.response_class(i,mimetype=mimetype)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'texture' in request.files:
        filename = textures_set.save(request.files['texture'])
        ###rec = Photo(filename=filename, user=g.user.id)
        ###rec.store()
        ###flash("Texture saved.")
        ###return redirect(url_for('show', id=rec.id))
        return redirect(url_for('show', id=1))
    #return render_template('upload.html')
    return "aaa"

@app.route('/texture/<id>')
def show(id):
    """
    texture = Photo.load(id)
    if texture is None:
        abort(404)
    url = textures.url(texture.filename)
    """
    return "bbb"





with app.test_request_context():
    url_for('static', filename="microajax.minified.js")


patch_request_class(app) # 16MB limit


if __name__ == '__main__':
      app.run()
