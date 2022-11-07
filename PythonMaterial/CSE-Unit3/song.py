class song: 
    
    
    #what makes a song
    def __init__(self, name, artist, lyrics, albumName, genre, producer, duration, explicit): 
        self.name=name
        self.artist=artist
        self.lyrics=lyrics
        self.albumName=albumName
        self.genre=genre
        self.producer=producer
        self.duration=duration
        self.explicit=explicit
        
        
    #what does a song look like when you print it
    # toString method
    def __str__(self):
        out = self.name + "\n\t" + self.artist
        out2=f'''
        {self.name}
            {self.artist}
        '''
        
        return out
    
    
    #getters and setters
    def getName():
        return self.name
    
    def getDuration(self):
        return self.duration
    
    def setName(self,newTitle):
        self.title=newTitle 
    
    
    
    #other methods 
    
    