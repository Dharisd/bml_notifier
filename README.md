Although BML has a great app, it lacks in certain aspects. Not receiving notifications for incoming transactions is particularly annoying.

# How it works

Its simple it just checks the transaction history from the bml web api
and adds any transactions thats not currently saved to the  db to the db
then sends texts to telegram channel using telegram bot api.

# setup
You must have python 3 installed

### Clone the repositry

```git clone https://github.com/Dharisd/bml_notifier```

### Install the requirements

```pip install -r requiremnts.txt```

### Set ENV variables

```BML_USERNAME```
your BML account username

```BML_PASSWORD```
Your BML account password

```BML_ACC``` 
your BML account number as in "https://www.bankofmaldives.com.mv/internetbanking/api/account/{BML_ACCOUNT}/history/today"

```TELEGRAM_TOKEN```
Token for the telegram bot

```TELEGRAM_CHANNEL```
Chatid of the telegram channel you want the bot to post to


### Initialise the Database
```python init_db.py```

### Run the the updater
```python update_history.py```

update_history.py can take --delay in seconds as a paramter. This controls the delay befor subsequent queries 











