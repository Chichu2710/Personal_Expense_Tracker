import mysql.connector

class Database:


    def execute_query(self, query, params=None, fetch=False):

        try:

            conn = mysql.connector.connect(

                host="localhost",
                user="root",
                password="",
                database="expense_tracker"

            )


            print("MYSQL CONNECTED")

            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, params)


            if fetch:
                result = cursor.fetchall()

            else:
                conn.commit()
                result = cursor.lastrowid

            cursor.close()
            conn.close()
            return result


        except Exception as e:
            print("DATABASE ERROR:",e)
            return []

db = Database()