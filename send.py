# CS 361
# Name: Honggwan Shin
# Email: shinhong@oregonstate.edu
# Description: CS361: Assignment 6: Microservices Case Study & Pipe Spike

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

currency = input("Select the currency (EUR, JPY, KRW, INR, CAD): ")

channel.basic_publish(exchange='', routing_key='hello', body=currency)
print(" [x] Sent 'My partner's string to me ")
connection.close()