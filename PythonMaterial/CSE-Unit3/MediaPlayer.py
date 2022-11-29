#name, artist, duration, lyrics, album, explicit, genre, producer
#string, string, int, string, boolean, string, string

#4:38 -> 4*60+38 int - 8 bits or 1 byte
#4:38 -> 4+38/60 float - 32 bits
#"4:38" -> "4:38" string - takes up the most data, each character is a byte
from song import song

# while stop != "Y":
#     a=input("Name")
#     b=input("Aritst")
#     c=input("Lyrics")
#     d=input("Album Name")
#     e=input("Genere")
#     f=input("Producer")
#     stop=input("Stop?""(Y/N)")
# InputStorage=[a,b,c,d,e,f]
# print(InputStorage)
library=[]
ui=""
while ui!="n":
    newSong = song(input("name:"),
        input("artist::"),
        input("lyrics::"),
        input("album name:"),
        input("genre:"),
        input("producer:"),
        int(input("duration:")),
        bool(input("explicit:")),
    )
    
    library.append(song)
    ui=input("keep going?""(y/n)")
    
for sont in library:
    print(song)
    
    songToFind=input("Which media?)")
    for song in library:
        if song.getName()==songToFind:
            print(song.getDuration())
    
'''
while ui!="n":
    song=[]
    song.append(input("name:"))
    song.append(input("artist::"))
    song.append(input("lyrics::"))
    song.append(input("album name:"))
    song.append(input("genre:"))
    song.append(input("producer:"))
    song.append(int(input("name:")))
    song.append(bool(input("name:")))
    library.append(song)
    ui=input("keep going?""(y/n)")
'''