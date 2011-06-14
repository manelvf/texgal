import Image
import os
import redis
import logging
import settings

from flask import Flask, url_for
from flaskext.uploads import UploadSet, IMAGES

from settings import r, UPLOADS_DEFAULT_DEST



textures = UploadSet('textures', IMAGES)


app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
      s = ""

      members = r.smembers("image-list")
      member_list = []
      for e in members:
          member_list.append(e)
          
      cur_member = 0 #members[0]

      s = """
      <html>
        <script src="/static/microajax.minified.js"></script>
        <body>
          <center>
            <img src="#" width="800" height="800" id="img-frame" />
            <br />
            <a href="#" id="backward" onclick="javascript:loadImage(-1);" > << </a>
            <a href="#" id="forward" onclick="javascript:loadImage(1);" > >> </a>
          </center>

          

          <script>

          var img = document.getElementById("img-frame");
          var forward = document.getElementById("forward");
          var backward= document.getElementById("backward");

          var member_list=%s;
          cur_image = 0;

          function loadImage(val) {
              cur_image += val;
              cur_image %%= member_list.length;
              if (cur_image < 0) {
                  cur_image = member_list.length + cur_image;
              }

              /*
              microAjax("/img/" + member_list[window.cur_image], function(res) {
                  console.log(res);
              });
              */
              imgurl="/img/" + member_list[window.cur_image];
              img.src = imgurl;
          }

          loadImage(0);
          </script>
        </body>
      </html>
      """

      return s % (str(member_list),)

@app.route('/img/<int:img_id>')
def get_image(img_id):
  i = r.get("image:"+str(img_id)+":content")
  mimetype = "image/jpeg"
  return app.response_class(i,mimetype=mimetype)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'texture' in request.files:
        filename = textures.save(request.files['texture'])
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


configure_uploads(app, (textures, ))
patch_request_class(app) # 16MB limit



if __name__ == '__main__':
      app.run()
