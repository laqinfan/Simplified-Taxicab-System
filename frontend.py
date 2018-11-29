from flask import Flask, render_template, jsonify
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

    def list_employees(self):
        self.cur.execute("SELECT fname, lname FROM employee")
        result = self.cur.fetchall()

        return result

app = Flask(__name__)
db = Database()

@app.route("/")
def hello():
     emps = db.list_employees()
     print(emps)

     #build_direction = "LEFT_TO_RIGHT"
     #table_attributes = {"style" : "width:100%"}
     #html = convert(jsonify(json.dumps(emps)), build_direction=build_direction, table_attributes=table_attributes)

     df = pandas.DataFrame(emps)

     return df.to_html()

if __name__ == "__main__":
    app.run()
