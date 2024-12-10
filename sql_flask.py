from flask import Flask, render_template, request
import pymysql
# 导入数据库操作类
from sql_init import Mysql

app = Flask(__name__)


@app.route("/info", methods=['GET', 'POST'])
def info():
    # 调用
    db = Mysql()
    results = db.getdata()
    return render_template("sql_select.html", results=results)


if __name__ == "__main__":
    app.run(app.run(debug=True, port=5000, host='127.0.0.1'))
