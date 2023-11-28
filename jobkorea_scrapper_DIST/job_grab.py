from flask import Flask, render_template, request
from extractor.jobkorea import extract_job

app = Flask(__name__)

@app.route('/') # 접속하는 url
def index():
    if request.method == "POST":
        keyword = request.form.get('keyword')
        password = request.form.get('password')
        print(f"{keyword}, {password}")
        result = extract_job('nto0102' if password==None else password, keyword)
        return result
    elif request.method == "GET":
        keyword = request.args.get('keyword')
        password = request.args.get('password')
        print(f"{keyword}, {password}")
        result = extract_job('nto0102' if password==None else password, keyword)
        return result 

if __name__=="__main__":
    app.run(host="0.0.0.0", port="5001", debug=True)
