from flask import Flask, request, render_template, jsonify
import pymysql.cursors
#from json2table import convert
import json
import pandas

class Database:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='dbproject',
                                          password='password',
                                          db='pdb1',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.connection.cursor()

    def execute_query(self, query):
        try:
            self.cur.execute(query)
            result = self.cur.fetchall()
        except Exception as e:
            result = e
            print(e)

        return result

app = Flask(__name__)
db = Database()

@app.route("/")
def query_form():
    return render_template('form.html')

@app.route("/", methods=['POST'])
def form_post():
    emps = db.execute_query(request.form['text'])
    print(emps)

    try:
      df = pandas.DataFrame(emps)
      return df.to_html()
    except:
      return str(emps)

if __name__ == "__main__":
    app.run()
