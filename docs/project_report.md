# My Project Report - NoteCloud

## What is NoteCloud?
I made NoteCloud to help students keep their notes safe in the cloud. Many students lose files when their laptop breaks. My app uses AWS so students can upload their notes and never lose them. 

## Features I built
I built these features to make the app useful for school:

### 1. Secure Login with Cognito
I used AWS Cognito for the login. It is very safe. I made a custom login page with a 40/60 split design. The form is on the left and a nice background is on the right. If you forget your password you can reset it with an email code.

### 2. Personal Note Storage
Every student has a dashboard. I made it so you can upload your own PDFs or images. These files go to my S3 bucket. You can download or delete them anytime.

### 3. Classroom and Curriculum
I built a classroom system where professors and students can talk.
* **Join Codes**: Every class has a code. I made it so students just enter the code to join.
* **Module Table**: I built a clean table to show all the study modules. 
* **Inline Editing**: If you are a professor you can click the edit icon and change the module name right in the table. I made this so you don't have to open new pages.
* **Final Exam at Bottom**: I wrote code to make sure the Final Exam always stays at the bottom of the list so it stays organized.

## How I built it (Tech Stack)
* **Frontend**: I used HTML and CSS for all the designs. I made it look very modern.
* **Backend**: I used Python Flask for all the logic.
* **Database**: I used MySQL on Amazon RDS to store user names and class info.
* **File Storage**: I used Amazon S3 for all the PDFs.
* **Monitoring**: I used Amazon CloudWatch to see my app logs in the AWS console.

## What I learned
I had some trouble with the database tables at first but I fixed it. I learned a lot about how to connect Python to AWS services like S3 and Cognito. My app is fast and it works good on mobile too.
