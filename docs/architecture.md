# My App Architecture

This document shows how I used AWS services to build NoteCloud.

## How the services talk to each other
I connected many AWS parts together to make my app work.

1. **EC2 (The Server)**: This is where my Flask code is running. It is the center of the app.
2. **Cognito (The Lock)**: When you try to login, my app asks Cognito if your password is right. I don't store passwords myself because Cognito is safer.
3. **RDS (The Brain)**: All the text data like student names and class lists are in my MySQL database here. 
4. **S3 (The Storage)**: When you upload a file, I send it to my S3 bucket. My database only saves the link to the file.
5. **CloudWatch (The Watchman)**: I send my app logs here so I can see what is happening in the AWS console.

## Links to AWS Services
* S3: https://aws.amazon.com/s3/
* EC2: https://aws.amazon.com/ec2/
* RDS: https://aws.amazon.com/rds/
* Cognito: https://aws.amazon.com/cognito/
* CloudWatch: https://aws.amazon.com/cloudwatch/

I used these services because they make my app very professional and secure.
