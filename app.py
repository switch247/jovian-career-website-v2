from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS =[{
  'id':1,
  'title': 'Data Analyst',
  'Location': 'Delhi, India',
  'salary': 'br. 12,000'
},
{
 'id':2,
  'title': 'Data scientist',
  'Location': 'Delhi, India',
  'salary': 'br. 12,000'
}
,
{
 'id':3,
  'title': 'Front End Developer',
  'Location': 'Delhi, India',
}
]

@app.route("/")
def hello_world():
  return render_template("home.html",jobs=JOBS,comp_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
