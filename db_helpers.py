import sqlite3

class DBHelper():
    
    def __init__(self):
        self.__dbconn = sqlite3.connect("transactions.db")


    def create_table(self):
        #create db if not exists
        c = self.__dbconn.cursor()
        # Create table
        c.execute("DROP TABLE IF EXISTS TRANSACTIONS")
        c.execute('''CREATE TABLE if not exists `transactions`
                (date text, balance real, sender text, amount real, minus BOOLEAN)''')
        c.close()


    def add_to_db(self,transaction):
        c = self.__dbconn.cursor()
        c.execute("INSERT INTO transactions VALUES(?,?,?,?,?)",transaction)
        c.close()
        self.__dbconn.commit()

    def check_if_exists(self,transaction):
        date = transaction["narrative2"]
        transaction_from = transaction["narrative3"]
        amount = transaction["amount"]
        minus = transaction["minus"]

        c = self.__dbconn.cursor()
        c.execute("SELECT * from `transactions` where (date=? AND sender =? AND amount=? AND minus=?)",(date,transaction_from,amount,minus))
        result = c.fetchall()

        if len(result) > 0:
            return True
        
        return False

