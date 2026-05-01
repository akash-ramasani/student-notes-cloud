# NoteCloud - My Cloud Based Student Notes Storage System

## What is my project?
I built NoteCloud to give students a safe and easy way to store their school notes in the cloud. Many students lose their files when their computer breaks or they delete something by mistake. My app solves this by using AWS cloud services to keep everything safe and accessible from anywhere.

## Key Features
* **Modern Login Page**: I built a custom authentication page with a 40/60 split design. It uses AWS Cognito to make logins very secure.
* **Personal Library**: Students can upload their own PDFs and images to my S3 bucket. They can see, download, or delete them anytime.
* **Smart Classrooms**: I built a system where professors can make classes. Students join with a code. 
* **Inline Table Editing**: Professors can change the names of modules directly in the table. I also made it so the Final Exam always stays at the bottom of the list.
* **Cloud Monitoring**: I connected my app to AWS CloudWatch so I can see logs and track activity in the AWS console.

## The Tech Stack I used
* **Backend**: Python (Flask)
* **Frontend**: HTML, CSS, Javascript
* **Database**: MySQL on Amazon RDS
* **Storage**: Amazon S3
* **Auth**: AWS Cognito
* **Monitoring**: Amazon CloudWatch
* **Server**: Amazon EC2

## How to see more details
I wrote detailed reports for my project which you can find in the **docs/** folder:
* **project_report.md**: Full details on how my app works.
* **architecture.md**: How I connected all the AWS services.
* **setup_guide.md**: How to install and run my code.
* **technical_details.md**: Deep dive into my code and logic.

I hope you like my project!
