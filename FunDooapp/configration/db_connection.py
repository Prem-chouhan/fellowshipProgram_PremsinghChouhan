import mysql.connector


class db_connection:

    def connection(self):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="admin@123",
            database="fundoo"
        )
        return self.mydb