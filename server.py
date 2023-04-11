import socket 
import threading

HEADER = 64
PORT = 5050
SERVER = "localhost"#socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "/quit"

Help_Contents = "\nHelp command. Syntax: /help\n \
                This command prints out a list of all supported commands and their behaviors\n \
                Users command. Syntax /users\n \
                This command will display a list of currently active users.\n\
                Direct Message command. Syntax: /dm username \"message\" \n\
                This command sends the message between quotes to the specified username\n\
                Broadcast command. Syntax: /bc \"message\"\n\
                This command should send the message between quotes to all other connected users.\n\
                Quit command. Syntax: /quit\n\
                Disconnect from the server.\n"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []
addresses = []
aliases = []



def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    #here we append addr instead of client because 
    #we are implementing/testing on a single machine
    #when implementing on a network, the same 
    #code can be modified to use client
    
    
    
    
    #Code to assign alias to client
    
    latest_alias_name="User"+str(len(aliases)+1)
    aliases.append(latest_alias_name)
    
    print("\nThis is list of currently active clients along with their aliases: \n",addresses,"\n", aliases)
    
    alias_msg="Your assigned alias is: "+latest_alias_name+"\nYou will be addressed in the chat server using this alias"
    
    conn.send(alias_msg.encode(FORMAT))
    #Code to append alias to alias list
    #Henceforth refer to client as alias in chat server
    
    connected = True
    while connected:
        
        msg_length = conn.recv(HEADER).decode(FORMAT)
        
        if msg_length:
            
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            msg_input_list = msg.split()
            
            print(msg_input_list)
            
            if msg == DISCONNECT_MESSAGE:
                
                
                removing_idx= clients.index(conn)
                
                discon_broadcast = str(addr)+" has left the chat !"
                
                for a in clients:
                    if a != conn:
                        a.send(discon_broadcast.encode(FORMAT))
                
                del aliases[removing_idx]
                del clients[removing_idx]
                del addresses[removing_idx]
                
                #removing disconnected client
                
                print("\nThis is list of currently active clients along with their aliases: \n",addresses,"\n", aliases)
                connected = False
                
            if msg_input_list[0] == "/dm":
                if msg_input_list[1] in aliases:
                    
                
                    #Send msg_input_list[2] to client referred in
                    #msg_input_list[1]
                     
                    #iterate through clients array
                    #send dm to client for which raddr value matches
                    #the addresses index   
                    sending_idx=aliases.index(msg_input_list[1])
                    clients[sending_idx].send(msg_input_list[2].encode(FORMAT))
                
                else:
                    err = "Wrong number/style of inputs please try again.\n check help using /help command if needed !"
                    conn.send(err.encode(FORMAT))
                    
                    
                
            if msg_input_list[0] == "/bc":
                #Send msg_input_list[1] to all clients in clients list
                #msg_input_list[1]
                for a in clients:
                    if a != conn:
                        a.send(msg_input_list[1].encode(FORMAT))
                
                
            
            if msg_input_list[0] == "/help":
                #Send help contents to client requesting help
                #Help_Contents
                conn.send(Help_Contents.encode(FORMAT))
                pass
            
            if msg_input_list[0] == "/users":
                #Send list of aliases of active users to requesting client
                #for alias in aliases:
                
                a_str=''
                for alias in aliases:
                    a_str += alias+' '
                    
                conn.send(a_str.encode(FORMAT))
                pass
            

            print(f"[{addr}] {msg}")
            #client.send("Msg received".encode(FORMAT))

    conn.close()
        

def start():
    server.listen()
    
    print(f"Our Server process is now active on the {SERVER} address")
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        addresses.append(addr)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"\nAdministrator, you have these many active connections: {threading.activeCount() - 7}")
        #Since our system has created 7 other threads
        #for our program before the server,
        #We subtract by 7 to get the number of active connections
        #This number "7" needs to be changed based on the Computer 
        #thread configuration where the server.py file resides


print("This is Bhavana's chat server program !!\nServer process is starting...")
start()