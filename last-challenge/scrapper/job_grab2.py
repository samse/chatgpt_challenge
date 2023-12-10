from flask import Flask, render_template, request
from flask_cors import CORS
from extractor.wwr import extract_wwr_jobs 
from extractor.remoteok import extract_remoteok_jobs
import json

app = Flask(__name__)
CORS(app)


@app.route('/wwr/') # 접속하는 url
def index():
    if request.method == "POST": 
        keyword = request.form.get('keyword')
    elif request.method == "GET":
        keyword = request.args.get('keyword')
    return extract_wwr_jobs(keyword)

@app.route('/rok/') # 접속하는 url
def remoteok():
    if request.method == "POST": 
        keyword = request.form.get('keyword')
    elif request.method == "GET":
        keyword = request.args.get('keyword')
    return extract_remoteok_jobs(keyword)

if __name__=="__main__":
    app.run(host="0.0.0.0", port="5001", debug=True)
