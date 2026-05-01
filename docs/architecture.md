# Architecture and Service Relationships

This document explains the technical side of how NoteCloud is built using AWS.

## System Architecture
The app is built using a "Three-Tier Architecture" style but on the cloud.

1. **User Interface (Frontend)**:
The users see the website made with HTML and CSS. They interact with the app by clicking buttons or uploading files. These requests go over the internet to our server.

2. **Application Logic (Backend)**:
The Flask app is running on an **Amazon EC2** instance. This is a virtual server in the AWS cloud. This server is the "brain" of the app. It checks if you are a student or professor and decides what you can see.

3. **Data and Storage (Backend Services)**:
The app uses three different services to keep your data safe.
* **AWS Cognito**: When you type your password the EC2 server asks Cognito "is this person real?". Cognito handles all the security so we don't have to worry about hackers.
* **Amazon RDS (MySQL)**: All the "text" data is here. Like your name, your display name, the names of your classes, and which module belongs to which week.
* **Amazon S3**: This is for the "big" data. When you upload a PDF it is sent to an S3 bucket. The database only stores a "link" to the file in S3.

## Monitoring and Logs
We use **Amazon CloudWatch** to keep an eye on everything.
* The EC2 server sends "heartbeats" and "logs" to CloudWatch.
* If a student uploads a file we log it.
* If there is a crash we can see the error in the CloudWatch console.

## External Resource Links
You can learn more about these services here:
* Cloud Storage (S3): https://aws.amazon.com/s3/
* Virtual Servers (EC2): https://aws.amazon.com/ec2/
* Relational Databases (RDS): https://aws.amazon.com/rds/
* Identity Management (Cognito): https://aws.amazon.com/cognito/
* Monitoring (CloudWatch): https://aws.amazon.com/cloudwatch/

## Summary
By using these services together the app is very strong. If one part has a problem the other parts still work. This is the power of cloud computing for students.
