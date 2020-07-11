import requests
import bmlClient
import db_helpers
import os
import time 
import pprint
import tg_client
import argparse

bml_client = bmlClient.BMLClient()
db = db_helpers.DBHelper()
BML_ACCOUNT = os.getenv("BML_ACC")


parser = argparse.ArgumentParser(description='Get transaction details from BML api and send texst via telegram for new transaction')
parser.add_argument('--delay',default=30,type=int ,help='delay between requests to API')
args = parser.parse_args()

def update_transactions(bml_client=bml_client,db=db):
    data = bml_client.get_transactions()
    output = {
        "new":[],
        "added":[]
    }

    if data["message"] == "Success":
        transactions = data["payload"]["history"]
        for tx in transactions:
            #check if exists
            check = db.check_if_exists(tx)
            if not check:
                db.add_to_db((tx["narrative2"],tx["balance"],tx["narrative3"],tx["amount"],tx["minus"]))
                output["new"].append([tx['amount'],tx['narrative3']])
            else:
                output["added"].append([tx['amount'],tx['narrative3']])

        return output
    



while 1==1:
    check = update_transactions()
    pprint.pprint(check)
    #update all new transactions to telegram channel
    for tx in check["new"]:
        tg_client.send_text(tx)
    
    time.sleep(args.delay)