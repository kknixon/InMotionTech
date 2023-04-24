from flask import Flask, render_template
import os
from operator import truediv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/cabling')
def cabling():
    return render_template('cabling.html')

@app.route('/consolidation')
def consolidation():
    return render_template('consolidation.html')

@app.route('/electrical')
def electrical():
    return render_template('electrical.html')

@app.route('/engineering')
def engineering():
    return render_template('engineering.html')

@app.route('/equipmentinstall')
def equipmentinstall():
    return render_template('equipmentinstall.html')

@app.route('/helpdesk')
def helpdesk():
    return render_template('helpdesk.html')

@app.route('/managedservices')
def managedservices():
    return render_template('managedservices.html')

@app.route('/projectmanagement')
def projectmanagement():
    return render_template('projectmanagement.html')

@app.route('/wlan')
def wlan():
    return render_template('wlan.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(error):
    return render_template('500.html'), 500


if __name__ =='__main__':
    app.run(host='0.0.0.0', port=os.environ.get("PORT"), debug=True)