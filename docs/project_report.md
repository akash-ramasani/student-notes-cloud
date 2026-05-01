# Detailed Project Report - NoteCloud Platform

## Introduction and Goal
My project is called NoteCloud. The main goal is to give students a safe place to keep their study materials. Many students only save things on their laptops. If the laptop crashes then all notes are gone. NoteCloud solves this by using AWS cloud services to store everything safely.

## Features and Functionality
I built many features to make this a real system for school.

### 1. User Accounts and Security
Users can make an account as a Student or a Professor. I used AWS Cognito for this because it is very secure. It handles the login and registration. If a user forgets their password they can reset it with a code sent to their email. The login page has a special 40/60 split design which looks very professional and modern.

### 2. Personal Library
Every student has their own private space. They can upload PDFs or images here. They can see all their files in a list and download them whenever they want. This means they can access notes from any computer.

### 3. Smart Classrooms
This is a big part of the app. Professors can create a class and get a join code. Students use this code to enter the class. Inside the class the professor can organize the curriculum.
* **Modules and Exams**: Professors can add learning modules or midterms and finals.
* **Inline Editing**: I made it so professors can edit the names of modules directly in the table without opening new pages.
* **Automatic Sorting**: The system is smart. It always puts the Final Exam at the bottom and Modules at the top so it stays organized.

## Technical Implementation

### Frontend
I used HTML and CSS for the design. I did not use templates from internet. I built a custom design system with nice colors and smooth animations. I used some Javascript to make the toasts and the inline editing work smoothly.

### Backend
The backend is written in Python using the Flask framework. It handles all the logic like checking who is logged in and talking to the database.

### AWS Services Used
* **Amazon S3**: This is the heart of the storage. Every file a student uploads goes here. It is very reliable.
* **Amazon EC2**: This is where the website is running. I have a server in the cloud that stays on all the time.
* **Amazon RDS**: I use a MySQL database here. It stores the names of users and which students are in which class.
* **AWS Cognito**: This is for the authentication. It makes sure only the right people can see the notes.
* **Amazon CloudWatch**: I added this to monitor the app. Every time someone logs in or uploads a file it sends a message to CloudWatch. This is good for seeing if there are errors.

## Project Performance
The app works very well. Because I use S3 the files are delivered very fast. The RDS database is also optimized so the classroom lists load quickly. The design is responsive so it works on mobile phones too.

## What Worked Well
The integration between Flask and AWS was very good. Using the Boto3 library made it easy to talk to S3 and CloudWatch. Also the 40/60 split design on the login page came out looking very nice.

## Issues Faced
I had some trouble with the database schema. First I only had one file per module but then I wanted many files. I had to make a new table and link them. It was a bit hard to fix the data but I learned a lot about SQL. Also setting up the CloudWatch logs took some time to get the permissions right in AWS.

## Conclusion
NoteCloud is a complete cloud application. It uses storage and compute and database services from AWS. It solves a real problem for students and shows how cloud computing can make life easier.
