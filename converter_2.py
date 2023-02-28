# date: january 31, 2023
# name: honggwan shin
# email: shinhong@oregonstate.edu
# class: cs 361
# description: Assignment 5 Individual Project Milestone number 1
# version 1

import requests
import datetime
import pika
import threading

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the response queue
channel.queue_declare(queue='date_response_queue')

# Define a callback function to handle incoming response messages
def response_callback(ch, method, properties, body):
    print(f"Current date: {body.decode()}")

# Start a new thread for consuming messages
def consume_messages():
    # Start consuming messages on the response queue
    channel.basic_consume(queue='date_response_queue', on_message_callback=response_callback, auto_ack=True)

    # Wait for messages
    print("Waiting for date response...")
    channel.start_consuming()


message_thread = threading.Thread(target=consume_messages)
message_thread.start()

########
# requesting

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Publish a message to the request queue
channel.basic_publish(exchange='',
                      routing_key='date_request_queue',
                      body='Please send me the date!')

# Close the connection
connection.close()

while True:

    print("\n")
    print("The Foreign Exchange Converter")
    print("Welcome!")
    print("If you want to contact the developer, please type CONTACT.")
    print("If you want to restart the program, please type RESTART.")
    print("If you want to exit the program, please type EXIT.")

    #e = datetime.datetime.now()

    # print("Today's date: %s/%s/%s" % (e.month, e.day, e.year))
    # print("Current Time: %s:%s:%s" % (e.hour, e.minute, e.second))

    # print("Today's date: %s/%s/%s" % (body.month, body.day, body.year))
    # print("Current Time: %s:%s:%s" % (body.hour, body.minute, body.second))

    print("\n")
    initial_currency = input("Please type the CURRENCY you want to convert. (e.g. USD, EUR, JPY, GBP, CNY, AUD, KRW): ")


    if initial_currency.upper() == "CONTACT":
        print("\n")
        print("Contact Information")
        print("\n")
        print("Name: Honggwan Shin")
        print("Email: shinhong@oregonstate.edu")
        continue

    if initial_currency.upper() == "RESTART":
        continue

    if initial_currency.upper() == "EXIT":
        quit()

    target_currency = input("Please type the CURRENCY you want it convert to (e.g. USD, EUR, JPY, GBP, CNY, AUD, KRW): ")

    if target_currency.upper() == "CONTACT":
        print("\n")
        print("Contact Information")
        print("\n")
        print("Name: Honggwan Shin")
        print("Email: shinhong@oregonstate.edu")
        continue

    if target_currency.upper() == "RESTART":
        continue

    if target_currency.upper() == "EXIT":
        quit()

    while True:
	    try:
		    amount = float(input("Enter the AMOUNT of currency you want to convert: "))
	    except:
		    print("The amount must be a numeric value!")
		    continue

	    if not amount > 0:
		    print("The amount must be greater than 0")
		    continue

	    else:
		    break

    url = "https://api.apilayer.com/fixer/convert?to=" + target_currency + "&from=" + initial_currency + "&amount=" + str(amount)

    payload = {}
    headers= {
    "apikey": "pqv4s0QigTqTCr1J0BLQfrVrJgNDQ5m7"
    }

    response = requests.request("GET", url, headers = headers, data = payload)

    status_code = response.status_code

    if status_code != 200:
	    print("Uh oh, there was a problem. Please try again later")
	    quit()

    result = response.json()

    print("Conversion result: " + str(round(result["result"],
                                            2)) + " " + target_currency.upper())