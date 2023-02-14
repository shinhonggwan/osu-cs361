Read me for the CS 361 Assignment 8 

A. Clear instructions for how to REQUEST data from the microservice you implemented. Include an example call.

The purpose of the microservice that I plan to implement is to allow users on my partner’s pet sharing app to see the foreign exchange conversation rate. For example, 1 USD = 1270 Korean Won (KRW)

The user on my partner’s pet sharing app can type the currency he/she would like to see on the app.

For example, “KRW” or “EUR” or “CAD” or “JPY” or “INR”

This would allow users from countries other than the United States on my partner’s pet sharing app to have an idea how much it will cost in their preferred currency.

If a user needs help with my foreign currency display app, the user can contact the developer at shinhong@oregonstate.edu who plans to maintain the micro service during the term.


B. Clear instructions for how to RECEIVE data from the microservice you implemented

The file that will request the data (in this case, the foreign currency conversion rate data) will request the data via RabbitMQ in the format of byte as it was explained in Part A above.

For example, “KRW” or “EUR” or “CAD” or “JPY” or “INR”

Once one of the currencies has been received via RabbitMQ, (for example “KRW”), then it will produce the real time conversion rate information.


C. UML sequence diagram showing how requesting and receiving data work. Make it detailed enough that your partner (and your grader) will understand

Please see the umlsequence.jpg on GitHub
