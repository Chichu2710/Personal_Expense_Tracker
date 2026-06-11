```md
# 💰 Personal Expense Tracker

A full-stack web application built to manage and analyze personal expenses efficiently. The application allows users to add, edit, delete, search, import CSV files, and export expense records with data stored in a MySQL database.

The project uses Flask as the backend framework and Pandas for data processing to generate expense summaries and category-wise insights. A modern dashboard interface helps users track spending habits and manage financial records easily.


## 🚀 Features

- Add new expense records
- Edit and delete expenses
- Search expenses by title and category
- Import multiple expenses using CSV upload
- Drag and drop CSV file upload interface
- Export expense data as CSV
- Automatic total expense calculation
- Category-wise expense analysis using Pandas
- MySQL database integration
- Clean and responsive dashboard UI


## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- MySQL (XAMPP)
- Pandas
- Flask-WTF
- WTForms



```
## 📂 Project Structure

```text
Personal_Expense_Tracker/
│
├── app.py                 # Main Flask application
├── database.py            # MySQL database connection
├── models.py              # Database operations and Pandas analysis
├── forms.py               # Form validation
├── config.py              # Application configuration
├── requirements.txt       # Required Python packages
├── database.sql            # Database setup script
│
├── templates/             # HTML files
│   ├── index.html
│   ├── edit.html
│   └── import.html
│
└── static/                # CSS and frontend files
    └── style.css
```

````


## ⚙️ Installation & Setup


### Clone Repository

```bash
git clone https://github.com/Chichu2710/Personal_Expense_Tracker.git
````

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Database Setup

1. Start Apache and MySQL from XAMPP
2. Open phpMyAdmin
3. Run the `database.sql` file

### Run Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

## 📊 CSV Import Format

CSV file should contain:

```
title,amount,category,date

Groceries,450,Food,2026-01-02
Fuel,2000,Transport,2026-01-10
```

## 🔮 Future Improvements

* User authentication
* Expense charts and visual analytics
* Monthly reports
* PDF export
* Cloud deployment

## 👨‍💻 Author

**Meet Changani**

B.Tech Artificial Intelligence and Data Science
A.D. Patel Institute of Technology
