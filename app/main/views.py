from flask import render_template
from flask import render_template,request,redirect,url_for


from . import main



@main.route('/')
def index():
    '''
    my index page
    :return:
    '''
    message= "huhu"
    return render_template('index.html', message=message)
