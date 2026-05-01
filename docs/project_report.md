MY PROJECT REPORT NOTECLOUD

WHAT IS NOTECLOUD
I made notecloud to help students keep notes safe in cloud: many students lose files when laptop breaks: my app use aws so students can upload notes and never lose them

FEATURES I BUILT
I built these features to make app useful for school:

1 SECURE LOGIN WITH COGNITO
I used aws cognito for login: it is very safe: i made custom login page with 40 60 split design: form is on left and nice background is on right: if you forget password you can reset with email code

2 PERSONAL NOTE STORAGE
Every student has dashboard: i made it so you can upload own pdf or images: these files go to s3 bucket: you can download or delete anytime

3 CLASSROOM AND CURRICULUM
I built classroom system where professor and student can talk:
JOIN CODES: every class has code: i made it so students enter code to join
MODULE TABLE: i built clean table to show study modules
INLINE EDITING: if you are professor you can click edit icon and change module name in table: i made this so you dont have to open new pages
FINAL EXAM AT BOTTOM: i wrote code to make sure final exam always stays at bottom of list so it stays organized

HOW I BUILT IT TECH STACK
FRONTEND: i used html and css for all designs: i made it look modern
BACKEND: i used python flask for logic
DATABASE: i used mysql on amazon rds to store user names and class info
FILE STORAGE: i used amazon s3 for all pdfs
MONITORING: i used amazon cloudwatch to see app logs in aws console

WHAT I LEARNED
I had some trouble with database tables at first but i fixed it: i learned lot about how to connect python to aws services like s3 and cognito: my app is fast and it works good on mobile too
