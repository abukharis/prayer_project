# import render_template function from the flask module
from flask import render_template
# import the app object from the ./application/__init__.py
from application import app
# define routes for / & /home, this function will be called when these are accessed
#from application.models import Posts, Users
#from application.forms import PostForm, RegistrationForm, LoginForm, UpdateAccountForm
#from flask_login import login_required, current_user, login_user, logout_user


prayerTime = [
    {  
        "prayer": {"prayer_type":"zoher", "city":"manchester"},
        "prayer":"zoher",
        "content":"time 13:30"
    },
    {   
        "prayer": {"prayer_type":"aser", "city":"manchester"},
        "prayer":"aser",
        "content":"time 15:30"
    }
]
@app.route('/')
@app.route('/home')
def home():
    #postData = Posts.query.all()
    return render_template('home.html', title='home', prayers=prayerTime)
