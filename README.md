# AWS Grade Management System

This project is a full-stack web application built using Flask and MySQL, deployed on AWS. It allows users to input, store, and view student grades, with automatic calculation of averages.

## Features

* Add and store student grades
* View all student records
* Automatically calculate overall averages
* Persistent data storage using a relational database
* Cloud deployment using AWS EC2 and RDS

## Technologies Used

* Python (Flask)
* MySQL (AWS RDS)
* AWS EC2
* HTML/CSS
* PyMySQL
* python-dotenv

## How to Run

1. Clone the repository:
   git clone https://github.com/tatequentin/aws-grade-management-system.git
   cd aws-grade-management-system

2. Install dependencies:
   pip install -r requirements.txt

3. Create a `.env` file using `.env.example`:
   DB_HOST=your_host
   DB_USER=your_user
   DB_PASS=your_password
   DB_NAME=your_db
   FLASK_SECRET=your_secret

4. Run the app:
   python app.py

5. Open in browser:
   http://127.0.0.1:5000

## Notes

This project was deployed using AWS EC2 and connected to an AWS RDS MySQL database. It was built to gain experience with cloud infrastructure, backend development, and database integration.

## Future Improvements

* Add authentication system
* Improve UI design
* Add analytics/dashboard features
