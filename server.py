from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_data_to_csv(data):
    with open('database.csv', 'a+', newline='', encoding='utf-8') as db:
        fieldnames = ['email', 'subject', 'message']
        csv_writer = csv.DictWriter(db, fieldnames=fieldnames)
        csv_writer.writerow(data)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_data_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to db'
    else:
        return 'something went wrong, try again'