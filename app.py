from flask import Flask, render_template, request
import BjApi as bj 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form['data']  # 获取表单数据
    url=bj.browser(data)[0]
    #print(url)
    # 在这里处理数据，例如保存到数据库等
    return render_template('index.html',URL=url)

if __name__ == '__main__':
    app.run(debug=True)