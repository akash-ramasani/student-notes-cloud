MY APP ARCHITECTURE

This document shows how i used aws services to build notecloud and how everything stays safe and fast:

HOW SERVICES TALK TO EACH OTHER
I connected many aws parts together to make my app work:

1 EC2 THE SERVER: this is where my flask code is running: it is center of app
2 COGNITO THE LOCK: when you try to login my app asks cognito if password is right: i dont store passwords myself because cognito is safer
3 RDS THE BRAIN: all text data like student names and class lists are in my mysql database here
4 S3 THE STORAGE: when you upload file i send it to s3 bucket: my database only saves link to file
5 CLOUDWATCH THE WATCHMAN: i send my app logs here so i can see what is happening in aws console

HOW DATA FLOWS
I designed system so data moves in safe path:
UPLOAD: student ec2 server amazon s3
DOWNLOAD: s3 secure pre signed link student browser
METADATA: ec2 server rds mysql database

SECURITY MEASURES
I made sure my app is secure for students:
PRIVATE STORAGE: my s3 bucket is private: you can only get files if app gives you special pre signed url that expires after few minutes
NETWORK FIREWALL: i use ec2 security groups to only allow traffic on certain ports: this stops hackers from entering server
ENCRYPTED AUTH: cognito handles all encryption for user passwords and emails

WHY THIS IS BETTER ON CLOUD
SCALABILITY: if i have 1000 more students tomorrow amazon s3 and rds can grow automatically to store all their notes
RELIABILITY: if my ec2 server restarts all notes and user accounts are still safe in s3 and rds
GLOBAL ACCESS: because it is on aws students can access notes from anywhere in world

LINKS TO AWS SERVICES
s3 storage: https:aws amazon com s3
ec2 servers: https:aws amazon com ec2
rds database: https:aws amazon com rds
cognito auth: https:aws amazon com cognito
cloudwatch monitoring: https:aws amazon com cloudwatch

I used these services because they make my app very professional and secure
