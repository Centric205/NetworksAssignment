# NetworksAssignment
CSC3002F Networks Assignment 1 2022

Just for reference the current work flow is as follows:

The serverApp is started and waits for clients to join. 


When the clientApp is started, the user selects a unique name.

The clientApp's receiver thread will then send a "/knock knock" command with the name attached. This identifies the client and it's reciever address.
After that, the clientApp's sender thread will send a "/come in" command. This identifies the client's sender address. The server stores those 2 addresses and the clients name as attributes in a clientObj.

After that, the clients can chat to each other in the waiting room. I still need to add create and join chatroom functionality 