CREATE DATABASE expense_tracker;

USE expense_tracker;

CREATE TABLE expenses(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    amount FLOAT,
    category VARCHAR(50),
    date DATE
);
