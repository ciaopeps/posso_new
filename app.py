from flask import Flask, render_template
from Classes.GenerateStory import *
from apscheduler.schedulers.background import BackgroundScheduler
import os
print('it works!')
app = Flask(__name__)

scheduler = BackgroundScheduler()
scheduler.add_job(func=to_app, trigger='interval', hours=24, start_date='2020-12-06 06:40:01', end_date='2100-06-15 09:05:00')
scheduler.add_job(func=to_app, trigger='interval', hours=24, start_date='2020-12-06 06:40:02', end_date='2100-06-15 09:05:00')
scheduler.add_job(func=to_app, trigger='interval', hours=24, start_date='2020-12-06 07:00:03', end_date='2100-06-15 11:00:00')
scheduler.add_job(func=to_app, trigger='interval', hours=24, start_date='2020-12-06 07:00:04', end_date='2100-06-15 09:05:00')
scheduler.add_job(func=to_app, trigger='interval', hours=24, start_date='2020-12-06 07:20:05', end_date='2100-06-15 09:05:00')
scheduler.add_job(func=to_app, trigger='interval', hours=24, start_date='2020-12-06 07:20:06', end_date='2100-06-15 09:05:00')
scheduler.add_job(func=to_app, trigger='interval', hours=24, start_date='2020-12-06 07:40:07', end_date='2100-06-15 11:00:00')
scheduler.add_job(func=to_app, trigger='interval', hours=24, start_date='2020-12-06 07:40:08', end_date='2100-06-15 09:05:00')

scheduler.start()


@app.route('/')
def home():
    published = list(zip(IMAGE_TO_SLANDER,DATE,TITLE,ARTICLE))
    if len(published) >= 8:
        return render_template('home-page_demo.html',type=type,published = published )
    else:
        return render_template('popup.html')

@app.template_global(name='zip')
def _zip(*args, **kwargs): #to not overwrite builtin zip in globals
    return __builtins__.zip(*args, **kwargs)


# if __name__ == '__main__':
#     to_app()
#     to_app()
#     to_app()
#     to_app()
#     to_app()
#     to_app()
#     to_app()
#     to_app()
#     to_app()
#     to_app()
#     app.run(debug=True)



