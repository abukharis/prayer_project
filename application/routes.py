
from flask import render_template, redirect, url_for
from application import app, db
from application.models import Posts
from application.forms import PostForm

prayerTime = [
    {  
        "prayer": {"prayer_type":"zoher", "city":"manchester"},
        "content":"time 13:30"
    },
    {   
        "prayer": {"prayer_type":"aser", "city":"manchester"},
        "content":"time 15:30"
    }
]
@app.route('/')
@app.route('/home')
def home():
    #postData = Posts.query.all()
    return render_template('home.html', title='home', prayers=prayerTime)
@app.route('/about')
def about():
    #postData = Posts.query.all()
    return render_template('about.html', title='about')


