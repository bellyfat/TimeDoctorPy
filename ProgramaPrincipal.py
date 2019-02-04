from Login import TimeDoctor as td
import datetime

token = ''
season = '2019-02-04'


client = td(token,season)

worklog = client.get_explain_worklog(str(season),str(season))


for s in worklog:
    print(season+ ' '+s['project_name']+' '+s["task_name"]+' '+s["user_name"]+': '+str(int(s["length"])/3600))
