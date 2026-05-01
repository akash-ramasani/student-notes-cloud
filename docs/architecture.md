# My App Architecture

This document shows how I used AWS services to build NoteCloud and how everything stays safe and fast.

## How the services talk to each other
I connected many AWS parts together to make my app work.

1. **EC2 (The Server)**: This is where my Flask code is running. It is the center of the app.
2. **Cognito (The Lock)**: When you try to login, my app asks Cognito if your password is right. I don't store passwords myself because Cognito is safer.
3. **RDS (The Brain)**: All the text data like student names and class lists are in my MySQL database here. 
4. **S3 (The Storage)**: When you upload a file, I send it to my S3 bucket. My database only saves the link to the file.
5. **CloudWatch (The Watchman)**: I send my app logs here so I can see what is happening in the AWS console.

## How the Data flows
I designed the system so data moves in a safe path:
* **Upload**: Student ➡️ EC2 Server ➡️ Amazon S3.
* **Download**: S3 ➡️ Secure Pre-signed Link ➡️ Student Browser.
* **Metadata**: EC2 Server ➡️ RDS MySQL Database.

## Security Measures
I made sure my app is secure for students:
* **Private Storage**: My S3 bucket is private. You can only get files if the app gives you a special "Pre-signed URL" that expires after a few minutes.
* **Network Firewall**: I use EC2 Security Groups to only allow traffic on certain ports. This stops hackers from entering the server.
* **Encrypted Auth**: Cognito handles all the encryption for user passwords and emails.

## Why this is better on the Cloud
* **Scalability**: If I have 1,000 more students tomorrow, Amazon S3 and RDS can grow automatically to store all their notes.
* **Reliability**: If my EC2 server restarts, all the notes and user accounts are still safe in S3 and RDS.
* **Global Access**: Because it is on AWS, students can access their notes from anywhere in the world.

## Links to AWS Services
* S3 Storage: https://aws.amazon.com/s3/
* EC2 Servers: https://aws.amazon.com/ec2/
* RDS Database: https://aws.amazon.com/rds/
* Cognito Auth: https://aws.amazon.com/cognito/
* CloudWatch Monitoring: https://aws.amazon.com/cloudwatch/

I used these services because they make my app very professional and secure.
