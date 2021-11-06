from flask import Flask,render_template,url_for,redirect,request
import csv
from werkzeug import datastructures
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/<string:page_name>')
def page_name(page_name):
    return render_template(page_name) 
def get_the_data(data)   :
    with open('database.csv','a',newline='') as database:

        email=data["email"]
        subject=data['subject']
        message=data['message']
        csv_writter=csv.writer(database,delimiter=",",quotechar=',',quoting=csv.QUOTE_MINIMAL)
        csv_writter.writerow([email,subject,message])
      
    

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=="POST":
        data=request.form.to_dict()
        get_the_data(data)
        

    
    return redirect("thankyou.html")     
