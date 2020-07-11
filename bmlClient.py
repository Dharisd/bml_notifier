import requests
import json
import os
import time
import headers
import db_helpers

class BMLClient():
    
    def __init__(self):
        self.BML_ACCOUNT = os.getenv("BML_ACC")
        self.db = db_helpers.DBHelper()
        self.session = requests.Session()



    def login(self):
        login_attempt = self.session.post("https://www.bankofmaldives.com.mv/internetbanking/api/login",data=headers.login_params)
        dash = self.session.get("https://www.bankofmaldives.com.mv/internetbanking/api/profile")
        if dash.status_code == 200:
            return True
        return False

    def get_todays_history(self):
        response = self.session.get(f'https://www.bankofmaldives.com.mv/internetbanking/api/account/{self.BML_ACCOUNT}/history/today')
        
        return json.loads(response.text)


#this a bit confusing should fix later
    def get_transactions(self):
        transactions = {
            "message": "failed",
            "payload":[],
        }
        data = self.get_todays_history()
        if data["message"] == "Success":
            transactions["message"] = "Success"
            transactions["payload"] = data["payload"]
            return data

        if data["message"] == "Please login":
            login_attempt = self.login()
            #relogin and check again
            if login_attempt:
                data = self.get_todays_history()
                transactions["message"] = "Success"
                transactions["payload"] = data["payload"]
                return data
            
            return transactions
            



