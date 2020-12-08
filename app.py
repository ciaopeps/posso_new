from flask import Flask, render_template,request
from Classes.GenerateStory import *
from apscheduler.schedulers.background import BackgroundScheduler
import os
print('it works!')
app = Flask(__name__)

scheduler = BackgroundScheduler()
scheduler.add_job(func=to_app, trigger='interval', hours=12, start_date='2020-12-08 16:05:00', end_date='2100-06-15 09:05:00')



scheduler.start()


@app.route('/')
def home():
    PUBLISHED = list(zip(IMAGE_TO_SLANDER,DATE,TITLE,ARTICLE))

    return render_template('home-page_demo.html',type=type,published = PUBLISHED )

@app.route('/article', methods=["POST"])
def article():
    a = request.form['list']
    print(a)
    ls = list((IMAGE_TO_SLANDER[-int(a)],DATE[-int(a)],TITLE[-int(a)],ARTICLE[-int(a)]))
    # ls = PUBLISHED[int(a)]
    print(ls)
    return render_template('popup.html',article=ls)






@app.template_global(name='zip')
def _zip(*args, **kwargs): #to not overwrite builtin zip in globals
    return __builtins__.zip(*args, **kwargs)


# if __name__ == '__main__':
#     to_app()
#
#
#     app.run(debug=True)



