from crontab import CronTab

cron = CronTab(user='sreyan')

train_job = cron.new(
    command='conda activate /mnt/d/ml_files/envs/py_web && python /mnt/d/VITMAS_projects/covid_project/train.py',
    comment='Trained Model'
)

train_job.every(1).days()

for item in cron:
    print(item)

cron.write()