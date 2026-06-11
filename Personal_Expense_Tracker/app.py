from flask import Flask,render_template,request,redirect,url_for,flash,Response
import pandas as pd
from config import Config
from forms import ExpenseForm
from models import ExpenseModel

app=Flask(__name__)

app.config.from_object(Config)

model=ExpenseModel()

@app.route("/")
def index():

    search=request.args.get("query")

    expenses=model.get_all_expenses()

    if search:
        expenses=[
        e for e in expenses
        if search.lower() in e["title"].lower()
        or search.lower() in e["category"].lower()
        ]


    stats=model.get_statistics(expenses)

    return render_template(

        "index.html",
        expenses=expenses,
        total=stats["total"],
        category_data=stats["category_data"]

    )



@app.route("/add",methods=["GET","POST"])

def add():

    form=ExpenseForm()

    if form.validate_on_submit():

        data=(
        form.title.data,
        form.amount.data,
        form.category.data,
        form.date.data
        )

        model.add_expense(data)
        flash("Expense Added")
        return redirect("/")



    return render_template(

        "edit.html",
        form=form,
        title="Add Expense"

    )



@app.route("/edit/<int:id>",methods=["GET","POST"])

def edit(id):

    expense=model.get_expense_by_id(id)[0]
    form=ExpenseForm()

    if form.validate_on_submit():


        data=(
        form.title.data,
        form.amount.data,
        form.category.data,
        form.date.data,
        id
        )

        model.update_expense(data)

        return redirect("/")



    form.title.data=expense["title"]
    form.amount.data=expense["amount"]
    form.category.data=expense["category"]
    form.date.data=expense["date"]


    return render_template(

        "edit.html",
        form=form,
        title="Edit Expense"
    )



@app.route("/delete/<int:id>")

def delete(id):

    model.delete_expense(id)
    return redirect("/")



@app.route("/export")

def export_csv():

    expenses=model.get_all_expenses()
    df=pd.DataFrame(expenses)
    csv=df.to_csv(index=False)

    return Response(

        csv,
        mimetype="text/csv",
        headers={
        "Content-Disposition":
        "attachment; filename=expenses.csv"
        }

    )



@app.route("/import", methods=["GET","POST"])
def import_csv():

    if request.method == "POST":
        file = request.files["file"]
        if file:
            df = pd.read_csv(file)
            for index,row in df.iterrows():
                data = (

                    row["title"],
                    row["amount"],
                    row["category"],
                    row["date"]

                )

                model.add_expense(data)

            flash("CSV Imported Successfully!")
            return redirect("/")

    return render_template("import.html")

if __name__=="__main__":

    app.run(debug=False, port=5000)