class Team:
    
    def __init__(self,name,wins,points,injuries):
        self.name=name
        self.wins=wins
        self.points=points
        self.injuries=injuries
        
        
    def __str__(self):
        return self.name

        
    def addPoints(self,newPoints):
        self.points+=newPoints
        
    def addWins(self):
        self.wins+1
        
    def overAllStats(self):
        out=f"""
        {self.name}:
            wins: {self.wins}
            points: {self.points}
            ouchies: {self.injuries}
        
        """
        
        return out
    def record(self):
        out=f'({self.wins},d,l'
        return out
        