import socket
import playsound
import threading
import hashlib

PASSWORD = "rotem"
PASSWORD = hashlib.sha256(PASSWORD.encode())

def sound():
    '''
    the function plays my favorite song from the dark side of the moon album.
    :return: none.
    '''
    playsound.playsound('h.mp3', True)

print("--music - breath in the air - dark side of the moon, my favorite :)")
t = threading.Thread(target=sound)
t.start()

def server_talk():
    '''
    the function connect to the server and giving you the menu and the answers from data
    :return: none.
    '''
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 1111

    try: #if thers any problem, the client and the server will be closed.
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connecting to remote computer 80
        server_address = (SERVER_IP, SERVER_PORT)
        sock.connect(server_address)

    except Exception: #if there is no connection with the server
        print("Problem with the server")
    msg = ""
    while msg != 'Quit':
        try:
            msg = "hi"
            sock.sendall(msg.encode())
            server_msg = sock.recv(1024)
            server_msg = server_msg.decode()
            print(server_msg)
            msg = input("please select one of the options:\n 1 - get album\n 2 - get songs in specific album\n3 - get time of a song\n4 - get lyrics of a song\n5 - get album of a song\n6 - get song name by part of it\n7 - get song by word search\nor Quit to quit.")

            if msg == '1':
                sock.sendall(msg.encode())
                server_msg = sock.recv(1024)
                server_msg = server_msg.decode()
                print(server_msg)  # albums

            elif msg == '2':  # if the choice is 2
                msg = msg + '&' + input("please select an album\n")
                sock.sendall(msg.encode())  # sending
                server_msg = sock.recv(1024)  # getting answer
                server_msg = server_msg.decode()
                print(server_msg)

            elif msg == '3':
                msg = msg + '&' + input("please select a song\n")
                sock.sendall(msg.encode())  # sending
                server_msg = sock.recv(1024)  # getting answer
                server_msg = server_msg.decode()
                print(server_msg)

            elif msg == '4':
                msg = msg + '&' + input("please select a song\n")
                sock.sendall(msg.encode())  # sending
                server_msg = sock.recv(2000)  # getting answer
                server_msg = server_msg.decode()
                print(server_msg)

            elif msg == '5':
                msg = msg + '&' + input("please select a song\n")
                sock.sendall(msg.encode())  # sending
                server_msg = sock.recv(1024)  # getting answer
                server_msg = server_msg.decode()
                print(server_msg)


            elif msg == '6':
                msg = msg + '&' + input("please select a song or a part of it\n")
                sock.sendall(msg.encode())  # sending
                server_msg = sock.recv(1024)  # getting answer
                server_msg = server_msg.decode()
                print(server_msg)


            elif msg == '7':
                msg = msg + '&' + input("please select a song or a part of it\n")
                sock.sendall(msg.encode())  # sending
                server_msg = sock.recv(1024)  # getting answer
                server_msg = server_msg.decode()
                print(server_msg)

        except Exception: #make the server not crush
            break
def main():
    password = ""
    password = hashlib.sha256(password.encode())
    while password.hexdigest() != PASSWORD.hexdigest():
        password = input("please enter a password")
        password = hashlib.sha256(password.encode())#  while theres no mach

    server_talk() #the main function of the program
    print("goodbye!")

if __name__ == '__main__':
    main()
