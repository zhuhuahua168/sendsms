import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def job_func():
     print("当前时间：", datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f"))

scheduler = BlockingScheduler()

# 每2小时触发
# scheduler.add_job(job_func, 'interval', hours=2)

# 在 2019-04-15 17:00:00 ~ 2019-12-31 24:00:00 之间, 每隔两分钟执行一次 job_func 方法
scheduler .add_job(job_func, 'interval', minutes=1, start_date='2021-05-26 17:00:00' , end_date='2021-05-26 18:00:00')

scheduler.start()