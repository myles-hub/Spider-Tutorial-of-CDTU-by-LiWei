from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# 路由解析
@app.route('/')
def index():
    # 模板渲染
    return render_template('index.html')

# /movie
@app.route('/movie')
def movie():
    data_lst = []
    conn = sqlite3.connect('top250.db')
    cursor = conn.cursor()
    select_sql = "select * from movie"
    data = cursor.execute(select_sql)
    for item in data:
        data_lst.append(item)
    conn.commit()
    conn.close()
    # 传入电影数据，并进行模板渲染
    return render_template('movie.html', movies=data_lst)

# /score
@app.route('/score')
def score():
    return render_template('index.html')

@app.route('/words')
def words():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)