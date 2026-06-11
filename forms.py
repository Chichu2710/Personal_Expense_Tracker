from flask_wtf import FlaskForm

from wtforms import StringField,FloatField,DateField,SubmitField

from wtforms.validators import DataRequired



class ExpenseForm(FlaskForm):


    title=StringField(

        "Title",

        validators=[DataRequired()]

    )


    amount=FloatField(

        "Amount",

        validators=[DataRequired()]

    )


    category=StringField(

        "Category",

        validators=[DataRequired()]

    )


    date=DateField(

        "Date",

        validators=[DataRequired()]

    )


    submit=SubmitField("Save")