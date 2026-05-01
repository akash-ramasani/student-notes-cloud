# Technical details of my project

Here I explain how my code works.

## 1. How I handle Login
I use `auth_service.py` to talk to AWS Cognito. When you register, I send your email to Cognito and it sends you a code. My code checks that code to make sure it is really you.

## 2. How I store Files
In `s3_service.py`, I wrote code to upload files to Amazon S3. When you want to see a file, I generate a secret "Pre-signed" link. This link only works for a short time so it is very secure.

## 3. How my Database is organized
In `db_service.py`, I made several tables:
* **Users**: For student and professor info.
* **Classes**: For the class names and codes.
* **Materials**: This table lets me link many files to just one module.

## 4. How my Pages work
I wrote the logic in `app.py`. 
* I made a sorting system so the **Final Exam** always comes last in the classroom list.
* I built **Inline Editing** so professors can change module names right in the table without reloading the page.

## 5. How I monitor the app
I use `watchtower` to send my Python logs to AWS CloudWatch. I can see every login and upload in the AWS console.

I built everything to be clean and simple to use.
