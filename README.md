# 💰 Personal Expense Tracker

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow)
![Status](https://img.shields.io/badge/Project-Active-success)

---

## 📌 Overview

**Personal Expense Tracker** is a full-stack web application designed to help users efficiently manage and analyze personal expenses.

It provides features like expense tracking, CSV import/export, and category-wise financial analysis using **Pandas**, all presented through a clean dashboard interface.

---

## 🚀 Key Features

✔ Add, edit, and delete expenses  
✔ Search expenses by title or category  
✔ CSV file import for bulk data upload  
✔ Drag & drop CSV upload interface  
✔ Export expenses as CSV  
✔ Automatic total expense calculation  
✔ Category-wise analysis using Pandas  
✔ MySQL database integration  
✔ Responsive and clean dashboard UI  

---

## 🧠 Core Functionalities

### 📊 Data Analysis (Pandas)
- Category-wise expense grouping  
- Total spending calculation  
- Structured data processing for insights  

### 📁 CSV System
- Bulk import of expenses  
- Export filtered or full dataset  
- Standard format support for easy data entry  

---

## 🛠️ Tech Stack

- Python  
- Flask  
- MySQL (XAMPP)  
- Pandas  
- HTML, CSS, JavaScript  
- Flask-WTF  
- WTForms  

---

## 📁 Project Structure

```

Personal_Expense_Tracker/
│
├── app.py                # Main Flask application
├── database.py           # Database connection
├── models.py             # Database operations
├── forms.py              # WTForms structure
├── config.py             # Configuration settings
├── requirements.txt      # Dependencies
├── database.sql         # SQL schema
├── README.md            # Documentation
│
├── templates/
│   ├── index.html
│   ├── edit.html
│   └── import.html
│
└── static/
└── style.css

````id="p9k3lm"

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash id="k1d9qp"
git clone https://github.com/Chichu2710/Personal_Expense_Tracker.git
cd Personal_Expense_Tracker
````

---

### 2️⃣ Install Dependencies

```bash id="w7x2aa"
pip install -r requirements.txt
```

---

### 3️⃣ Setup Database (XAMPP / MySQL)

1. Start **Apache & MySQL** from XAMPP
2. Open **phpMyAdmin**
3. Import and run:

```sql id="q2v8zz"
-- database.sql file
```

---

### 4️⃣ Run Application

```bash id="z9x1cc"
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 📊 CSV Import Format

Your CSV file must follow this structure:

```csv id="csv123"
title,amount,category,date

Groceries,450,Food,2026-01-02  
Fuel,2000,Transport,2026-01-10  
Rent,12000,Rent,2026-01-01  
```

---

## 📈 Future Improvements

* 🔐 User authentication system
* 📊 Graph-based expense visualization
* 📅 Monthly / yearly financial reports
* 📄 PDF export feature
* ☁️ Cloud deployment (Render / Railway)
* 📱 Mobile-friendly UI improvements

---

## 👨‍💻 Author

**Meet Changani**
Full-Stack Developer | Python & Flask Enthusiast
