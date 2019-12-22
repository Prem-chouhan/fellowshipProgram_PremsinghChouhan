import mysql.connector
import sys
import os

# sys.path.insert(0, '/home/admin-1/PycharmProjects/Fun/dotenv/')
from dotenv import load_dotenv

load_dotenv()


class db_connection:

    def connection(self):
        self.mydb = mysql.connector.connect(
            host=os.getenv("HOST"),
            port=os.getenv("PORT"),
            user=os.getenv("USER_db"),
            passwd=os.getenv("PASSWD"),
            database=os.getenv("DATABASE"),

        )
        return self.mydb


