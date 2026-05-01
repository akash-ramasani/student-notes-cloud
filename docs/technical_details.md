TECHNICAL DETAILS OF MY PROJECT

Here i explain how my code works:

1 HOW I HANDLE LOGIN
I use auth service py to talk to aws cognito: when you register i send your email to cognito and it sends you code: my code checks that code to make sure it is really you

2 HOW I STORE FILES
In s3 service py i wrote code to upload files to amazon s3: when you want to see file i generate secret pre signed link: this link only works for short time so it is very secure

3 HOW MY DATABASE IS ORGANIZED
In db service py i made several tables:
USERS: for student and professor info
CLASSES: for class names and codes
MATERIALS: this table lets me link many files to just one module

4 HOW MY PAGES WORK
I wrote logic in app py:
i made sorting system so final exam always comes last in classroom list
i built inline editing so professors can change module names right in table without reloading page

5 WEB SERVER AND SSL
I configured nginx as reverse proxy to handle requests for notecloud akashramasani com: i also setup certbot for automatic ssl renewal

6 HOW I MONITOR APP
I use watchtower to send my python logs to aws cloudwatch: i can see every login and upload in aws console

I built everything to be clean and simple to use
