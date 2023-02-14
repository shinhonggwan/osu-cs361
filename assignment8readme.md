{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\froman\fcharset0 Times-Roman;\f2\froman\fcharset0 Times-Bold;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Read me for the CS 361 Assignment 8 \
\
A. 
\f1 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Clear instructions for 
\f2\b how to REQUEST
\f1\b0  
\f2\b data
\f1\b0  from the microservice you implemented. Include an example call.\
\
The purpose of the microservice that I plan to implement is to allow users on my partner\'92s pet sharing app to see the foreign exchange conversation rate. For example, 1 USD = 1270 Korean Won (KRW)\
\
The user on my partner\'92s pet sharing app can type the currency he/she would like to see on the app.\
\
For example, \'93KRW\'94 or \'93EUR\'94 or \'93CAD\'94 or \'93JPY\'94 or \'93INR\'94\
\
This would allow users from countries other than the United States on my partner\'92s pet sharing app to have an idea how much it will cost in their preferred currency.\
\
If a user needs help with my foreign currency display app, the user can contact the developer at shinhong@oregonstate.edu who plans to maintain the micro service during the term.\
\
\
B. Clear instructions for 
\f2\b how to RECEIVE data 
\f1\b0 from the microservice you implemented\
\
The file that will request the data (in this case, the foreign currency conversion rate data) will request the data via RabbitMQ in the format of byte as it was explained in Part A above.\
\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 \outl0\strokewidth0 For example, \'93KRW\'94 or \'93EUR\'94 or \'93CAD\'94 or \'93JPY\'94 or \'93INR\'94\
\
Once one of the currencies has been received via RabbitMQ, (for example \'93KRW\'94), then it will produce the real time conversion rate information.\
\
\
C. 
\f2\b \outl0\strokewidth0 \strokec2 UML sequence diagram
\f1\b0 \strokec2  showing how requesting and receiving data work. Make it detailed enough that your partner (and your grader) will understand\
\
Please see the umlsequence.jpg on GitHub\
}