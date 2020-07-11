import os 


BML_USERNAME =  os.getenv("BML_USERNAME")
BML_PASSWORD = os.getenv("BML_PASSWORD")


login_params = {
    "username":BML_USERNAME,
    "password": BML_PASSWORD
}

