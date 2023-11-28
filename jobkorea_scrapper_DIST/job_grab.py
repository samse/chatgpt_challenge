from flask import Flask, render_template, request
from extractor.jobkorea import extract_job

app = Flask(__name__)

@app.route('/') # 접속하는 url
def index():
    if request.method == "POST":
        print(request.form.get('keyword')) # 안전하게 가져오려면 get
        keyword = request.form.get('keyword')
        print(request.form.get('keyword'))
        extract_job('nto0102', keyword)
        return render_template('index.html', keyword=keyword)
    elif request.method == "GET":
        keyword = request.args.get('keyword')
        print(f"keyword = {request.args.get('keyword')}")
        result = extract_job('nto0102', keyword)
        return result 
    #return render_template('index.html', keyword=keyword)

if __name__=="__main__":
    app.run(host="0.0.0.0", port="5001", debug=True)
