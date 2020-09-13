from flask import Flask, render_template ,request
from flask_sqlalchemy import SQLAlchemy
import json
from flask_mail import Mail


with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True

app = Flask(__name__)
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD=  params['gmail-password']
)
mail = Mail(app)
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    print("Server not found")
db = SQLAlchemy(app)


class Contacts(db.Model):
    SNO = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    Query = db.Column(db.String(120), nullable=False)


@app.route("/")
def home():
    return render_template("index.html" , params=params)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('msg')

        entry = Contacts(name=name, email=email, Query=message)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients=[params['gmail-user']],
                          body=message
                          )
    return render_template('contact.html', params=params)







app.run(debug=True)