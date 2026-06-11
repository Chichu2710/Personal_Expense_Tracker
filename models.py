from database import db
import pandas as pd

class ExpenseModel:

    def get_all_expenses(self):
        query = """

        SELECT * FROM expenses
        ORDER BY date DESC

        """
        return db.execute_query(query, fetch=True)


    def get_expense_by_id(self,id):

        query = """

        SELECT * FROM expenses
        WHERE id=%s

        """
        return db.execute_query(
            query,
            (id,),
            fetch=True
        )


    def add_expense(self,data):

        query = """
        
        INSERT INTO expenses
        (title,amount,category,date)
        VALUES(%s,%s,%s,%s)

        """

        return db.execute_query(

            query,
            data

        )


    def update_expense(self,data):

        query = """

        UPDATE expenses
        SET title=%s,
        amount=%s,
        category=%s,
        date=%s
        WHERE id=%s

        """

        return db.execute_query(

            query,
            data

        )


    def delete_expense(self,id):

        query="DELETE FROM expenses WHERE id=%s"

        return db.execute_query(

            query,
            (id,)

        )


    def get_statistics(self,expenses):


        if not expenses:

            return {

            "total":0,
            "category_data":{}

            }


        df=pd.DataFrame(expenses)

        df["amount"]=df["amount"].astype(float)

        total=df["amount"].sum()


        category_data=(

            df.groupby("category")
            ["amount"]
            .sum()
            .to_dict()

        )


        return {

            "total":total,
            "category_data":category_data

        }