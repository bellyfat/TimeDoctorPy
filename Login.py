import requests as req


class TimeDoctor:

    def __init__(self,token,data_lenght):
        self.token = token
        self.date_lenght = data_lenght



    def get_user_id(self):
        dict = req.get("https://webapi.timedoctor.com/v1.1/companies?access_token="+self.token)
        if dict.status_code == 200:
            j = dict.json()
            return j["user"]["user_id"]

    def get_company_id(self):
        dict = req.get("https://webapi.timedoctor.com/v1.1/companies?access_token="+self.token)
        if dict.status_code == 200:
            j = dict.json()
            return j["user"]["company_id"]

    def get_tasks(self):
        dict =req.get("https://webapi.timedoctor.com/v1.1/companies/"+str(self.get_company_id())+"/users/"+str(self.get_user_id())+"/tasks?access_token="+self.token)
        if dict.status_code == 200:
            j = dict.json()
            return

    def get_projects(self):
        dict = req.get("https://webapi.timedoctor.com/v1.1/companies/"+str(self.get_company_id())+"/users/"+str(self.get_user_id())+"/projects?access_token="+self.token)
        if dict.status_code == 200:
            j = dict.json()
            return j

    def get_worklog(self,start_date, end_date):
        dict = req.get("https://webapi.timedoctor.com/v1.1/companies/"+str(self.get_company_id())+"/worklogs?access_token="+self.token+"&&start_date="+start_date+"&end_date="+end_date)
        if dict.status_code == 200:
            j= dict.json()
            return j #value total worked in company

    def get_explain_worklog(self,start_date,end_date):
        dict = req.get("https://webapi.timedoctor.com/v1.1/companies/"+str(self.get_company_id())+"/worklogs?access_token="+self.token+"&&start_date="+start_date+"&end_date="+end_date)
        if dict.status_code == 200:
            j = dict.json()
            return j["worklogs"]["items"]


