START = '*'
END = '::'
def a():
    '''
    getting the data from the file
    :return: 3 lists sorting by diffrent parameters
    '''
    data2 = []
    data3 = []
    file = open("Pink_Floyd_DB.txt", "r")
    data = file.read()

    data = data.split("#")

    for place in data:  # spliting the text
        data2 = data2 + place.split("*")


    for place in data2:
        data3 = data3 + place.split("::")


    file.close()  # closing the file
    return data, data2, data3


def get_album(data):
    '''
    the function returning all the albums in the file
    :param data: list, all the file sorted by album
    :return: albums, string with all the albums
    '''
    album = ""
    albums = ""
    for place in data:
        album = place[ : place.find("::")]
        albums = albums + "\n" + album
    return albums


def get_songs(data, album_name):
    '''
    the function getting all the song in one album
    :param data: the file sorted by albums
    :param album_name: the album that the user requested
    :return: string with the songs
    '''
    songs = ""
    start = 0;
    ending = 0;
    i = 0

    for place in data:  # starting the loop
        if album_name in place:
            while not start == -1:  # while theres songs to add
                start = place.find(START)
                ending = place.find(END)
                if not start == -1:
                    songs = songs +  "\n" + place[start + 1 : ending]  # getting the song in the songs list
                    place = place[ending + 2 : ]
        else:
            i = i + 1

        if i is 9:  # if the album wasnt found
            songs = "sorry. album not found. please try again"

    return songs

def get_time(data3, song_name):
    '''
    the function getting the time of a song
    :param data3: the list of the songs
    :param song_name: string of the song name
    :return: the time of the song
    '''
    i = 0
    j = len(data3)
    for place in data3:  # starting the loop
        if song_name in place:  # if the song is found
            if ':' in data3[i + 2]:  # if its the time of a song and not something else
                time = data3[i + 2]  # getting the time
                break
            else:
                time = "sorry. song not found"
        else:
            i = i + 1
        if i == j:  # if the song is not found
           time = "sorry. song not found"
    return time


def get_lyrics(data3, song_name):
    '''
    the function getting the time of a song
    :param data3: the list of the songs
    :param song_name: string of the lyrics
    :return: the lyrics of the song
    '''
    i = 0
    j = len(data3)
    lyrics = ""
    for place in data3:  # starting the loop
        if song_name == place:  # if the song is found
            if ':' not in data3[i + 4]:  # if its the lyrics of a song and not something else
                lyrics = data3[i + 3]  # getting the lyrics
                break
            else:
                lyrics = "sorry. song not found"
        else:
            i = i + 1
        if i == j:  # if the song is not found
           lyrics = "sorry. song not found"

    return lyrics


def get_sia(data, song_name):
    '''
    the function gets a song and returning its album
    :param data: list that sort by the albums
    :param song_name: the song the user wants to search
    :return: the album
    '''
    album = ""
    i = 0
    for place in data:
        if song_name in place:
            for i in place:
                if i != ':': #  getting the album
                    album = album + i
                else:
                    break
        else:
            i = i + 1

        if i == len(data):
            album = "sorry. wrong song"

    return album


def get_song_word(data2, song_name):
    '''
    the function getting all the song with the search word
    :param data2: list of the songs
    :param song_name: the search word
    :return: string with the songs
    '''
    i = 0
    songs = ""
    g = ""
    data = ""
    songs = ""

    for place in data2:
        data = place.lower() #  making it lower
        song_name = song_name.lower()

        g = data[: place.find('::')]

        if song_name in g and len(place) > 50:
            songs = songs + place[: place.find('::')] + "\n" #  adding it to the string

        else:
            i = i + 1

        if i == len(data2): #  error massege
            songs = "song wasnt found"

    return songs


def get_word(data2, song_name):
    '''
    the function getting all the songs with the search word in the lyrics
    :param data2: list of the songs
    :param song_name: the search word
    :return: string with the songs
    '''
    i = 0
    songs = ""
    for place in data2: #  starting loop
        if song_name in place:
            if len(place) >= 50:  # if its lyrics
                songs = songs + "\n"
                for j in place:
                    if not j == ':':
                        songs = songs + j  # adding the song
                    else:
                        break
            else:
                i = i + 1
        else:
            i = i + 1

    if i == len(data2):
        songs = "songs wasnt found"
    return songs
