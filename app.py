from flask import Flask, request,render_template, jsonify,Request
from datetime import datetime
import json
import pytz
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/generated', methods=['GET'])
def generated():
  file = json.load(open('metaData.json'))
    
  return render_template("generated.html", title = file["title"],description = file['description'],
                                         keywords = file['keywords'], url = file['urls'],
                                         ind3x = file['ind3x'], twAcc = file['twAcc'],
                                         siteName = file['siteName'], ma1l = file['mail'],
                                         img7 = file['img7'], type = file['webType'], time0 = file['time0'],
                                         classification=file['classification'], keyList=json.dumps(file['keyList']))
  

@app.route('/generator', methods=['GET'])
def formofGenerator():
  return render_template("generator.html")

@app.route('/generator', methods=['POST'])
def generate():
  title = request.form.get('title')
  description = request.form.get('description')
  keywords = request.form.get('keywords')
  #makeit array each key will be 1 item in array
  #key = [str(key) for key in keywords] 
  urls = request.form.get('urls')
  ind3x = request.form.get('ind3x')
  twAcc = request.form.get('twAcc')
  siteName = request.form.get('siteName')
  ma1l = request.form.get('ma1l')
  img7 = request.form.get('img7')
  webType = request.form.get('type') #website or article
  classification = request.form.get('classification') #webType or industry of the website or article 
  #7img7 is 1200x630 image
  #7img8alt is the alt of that image
  datetimeRaw = f'{datetime.now(pytz.timezone("Europe/Istanbul"))}'
  time0 = datetimeRaw.replace(' ', 'T')
  theMeta = {
    'title':f'{title}',
    'description':f'{description}',
    'keywords':f'{keywords}',
    'urls':f'{urls}',
    'ind3x': f'{ind3x}',
    'twAcc':f'{twAcc}',
    'siteName':f'{siteName}',
    'mail':f'{ma1l}',
    'img7':f'{img7}',
    'webType':f'{webType}',
    'classification':f'{classification}',
    'time0':f'{time0}',
    'keyList':f'{keyList}'
  }
  json_object = json.dumps(theMeta)
  with open("metaData.json", "w") as outfile:
    outfile.write(json_object)
  return render_template("generated.html")
 
#run the server
if __name__ == '__main__':
  app.run(debug=True)  