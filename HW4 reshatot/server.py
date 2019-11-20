import socket
import data

def connection():
    '''
    the function creating connection with the client and giving them information about pink floyd
    :return: none.
    '''
    data1 = []
    data2 = []
    data3 = []

    data1, data2, data3 = data.a()

    LISTEN_PORT = 1111 #creating connection

    # Create a TCP/IP socket
    listening_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binding to local port 80
    server_address = ('', LISTEN_PORT)
    listening_sock.bind(server_address)

    # Listen for incoming connections
    listening_sock.listen(1)

    # Create a new conversation socket
    client_soc, client_address = listening_sock.accept()
    while True: #while the loop isn't breaking
        try:
            client_msg = client_soc.recv(1024) #getting msg
            client_msg = client_msg.decode()


            if client_msg != "Quit": #if the client didnt sent 'quit'
                print("\n")
                msg = "Welcome!"

                client_soc.sendall(msg.encode())
                client_msg = client_soc.recv(1024)
                client_msg = client_msg.decode()
                print(client_msg)
                if client_msg == '1':  # if the choice is 1
                    albums = data.get_album(data1)  # getting the albums
                    msg = albums
                    print(msg)
                    client_soc.sendall(msg.encode())  # sending the albums

                elif '2' in client_msg:
                    song = client_msg.find('&')  # getting the index of the & to get just the song
                    client_msg = client_msg[song + 1: ]
                    client_msg = client_msg[0].upper() + client_msg[1: ]
                    songs = data.get_songs(data1, client_msg)  # calling the function
                    print(songs)
                    songs = songs.replace("\n\n", "")
                    client_soc.sendall(songs.encode())  # sending

                elif '3' in client_msg:
                    song = client_msg.find('&')  # getting the index of the & to get just the song
                    client_msg = client_msg[song + 1: ]
                    client_msg = client_msg[0].upper() + client_msg[1: ]
                    print(client_msg)
                    time = data.get_time(data3, client_msg)  # calling the function
                    print(time)
                    client_soc.sendall(time.encode())  # sending the time

                elif '4' in client_msg:
                    lyrics = client_msg.find('&')  # getting the index of the & to get just the song
                    client_msg = client_msg[lyrics + 1: ]
                    client_msg = client_msg[0].upper() + client_msg[1: ]
                    print(client_msg)
                    lyrics = data.get_lyrics(data3, client_msg)
                    print(lyrics)
                    client_soc.sendall(lyrics.encode())


                elif '5' in client_msg:
                    sia = client_msg.find('&')  # getting the index of the & to get just the song
                    client_msg = client_msg[sia + 1: ]
                    client_msg = client_msg[0].upper() + client_msg[1: ]
                    client_msg = '*' + client_msg
                    print(client_msg)
                    sia = data.get_sia(data1, client_msg)
                    client_soc.sendall(sia.encode())


                elif '6' in client_msg:
                    sia = client_msg.find('&')  # getting the index of the & to get just the song
                    client_msg = client_msg[sia + 1: ]
                    client_msg = client_msg[0].upper() + client_msg[1: ]
                    print(client_msg)
                    songs = data.get_song_word(data2, client_msg)
                    client_soc.sendall(songs.encode())

                elif '7' in client_msg:
                    sia = client_msg.find('&')  # getting the index of the & to get just the song
                    client_msg = client_msg[sia + 1: ]
                    print(client_msg)
                    songs = data.get_word(data2, client_msg)
                    client_soc.sendall(songs.encode())
                else: #  if the msg isnt correct
                    de = "wrong number, try again please"
                    client_soc.sendall(de.encode())
            else:  # if the client sent quit
                LISTEN_PORT.close()
                listening_sock.close()
                break

        except Exception: #if there is any problem
            listening_sock.close()
            client_soc.close()
            break


def main(): #main that calling the connection function
    connection()

if __name__ == "__main__":
    main()


