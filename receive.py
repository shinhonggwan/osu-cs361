# CS 361
# Name: Honggwan Shin
# Email: shinhong@oregonstate.edu
# Description: CS361: Assignment 6: Microservices Case Study & Pipe Spike

#!/usr/bin/env python
import pika, sys, os
import requests

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        new_body1 = body.decode("utf-8")   # the data from the body comes in the byte format, not the utf-8 format. therefore, changing it.
        print("Received Currency: ", new_body1)
        initial_currency = str("USD")
        target_currency = new_body1
        #print(body)
        amount = 1
        url = "https://api.apilayer.com/fixer/convert?to=" + target_currency + "&from=" + initial_currency + "&amount=" + str(
            amount)

        payload = {}
        headers = {
            "apikey": "pqv4s0QigTqTCr1J0BLQfrVrJgNDQ5m7"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        status_code = response.status_code

        if status_code != 200:
            print("Uh oh, there was a problem. Please try again later")
            quit()

        result = response.json()

        print("Conversion result: " + str(round(result["result"],
                                                2)) + " " + target_currency.upper())

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)