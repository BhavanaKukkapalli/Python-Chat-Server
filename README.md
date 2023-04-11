# Python-Chat-Server

This is a chat server application developed in Python, which allows multiple clients to connect to a single server and communicate with each other through a socket connection.

## Functionality
The main commands used in this project to chat with other clients are:

- /dm : to send a direct message to a specific client
- /bc : to broadcast a message to all clients connected to the server
- /help : to display all available commands to the clients
- /users : to display all active clients in the chat room
- /quit : to exit the chat room

When a client joins the chat room, they are assigned a unique name. The server uses a TCP Server Socket and the client uses a TCP Client Socket for communication. If a client sends a direct message to another client using the /dm command, the message is only sent to the specific client. If a client leaves the chat room, either by using the /quit command or losing their connection, a message is displayed to all active clients notifying them of the departure.

## Installation
To install and run the chat server application, follow these steps:

- Clone the repository to your local machine using git clone <repository_url>
- Navigate to the project directory: cd chat-server
- Install the required dependencies using pip install -r requirements.txt
- Start the server by running python server.py
- Start the client by running python client.py

## Usage
Once the client is connected to the server, you can use the commands mentioned above to chat with other clients in the chat room. To exit the chat room, use the /quit command.

## Limitations
This chat server application requires a stable internet connection to function properly. Additionally, the server should be run on a machine with sufficient resources to handle multiple clients simultaneously.

## Conclusion
This chat server application is a simple implementation of socket programming in Python, allowing multiple clients to communicate with each other in a chat room. It can be used for educational purposes, personal projects, or even in small organizations.
 
