from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from datetime import date,datetime,timedelta

def start(arg1,arg2,uid):
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(
      auto_hello,
      'date',
      run_date=datetime.now() + timedelta(seconds=10),
      args=[arg1,arg2],
      id=uid,
      max_instances=1,
      replace_existing=True,
      misfire_grace_time=1000,
      coalesce=True
    )
    

    try:
      print('Job Schedule')
      
      scheduler.start()
    except KeyboardInterrupt:
      print("Stopping scheduler...")
      
    



def auto_hello(arg1,arg2):
    print("arg1: ",arg1)
    print("arg2: ",arg2)
    print("Msg sent")