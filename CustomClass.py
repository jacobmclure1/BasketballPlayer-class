

class BasketballPlayer:
    __league = "NBA" ##class variable for all basketball players
    def __init__(self, name, team, age, totalpoints, gamesplayed, yearsplayed):
        self.__name = name##player name
        self.__team = team##team they play for
        self.__age = age##age
        self.__totalpoints = totalpoints##points scored throughout their career
        self.__gamesplayed = gamesplayed##games played in their career
        self.__yearsplayed = yearsplayed##years played in their career
    def GetPlayerAge(self):
        return self.__age##returns player age
    def GetPlayerTeam(self):
        return self.__team##returns player team
    def GetPlayerName(self):
        return self.__name##returns player name
    def GetAveragePoints(self):
        averagepoints = self.__totalpoints / self.__gamesplayed ##divide points by game played for points per game
        return averagepoints
    def isNBAveteran(self):
        isVeteran = ""##string we will return
        if self.__yearsplayed > 4:##if they have played 5 or more years they are an NBA veteran
            isVeteran = (f"{self.__name} has played {self.__yearsplayed} years in the {self.__league}, making him an {self.__league} veteran")
        if self.__yearsplayed < 4:
            isVeteran = (f"{self.__name} has played {self.__yearsplayed} years in the {self.__league}, which is not enough years to be considered an {self.__league} Veteran")
        return isVeteran
    def isRookie(self):
        isRookie = ""##string we will return
        if self.__yearsplayed == 0:##if they have not played an nba season they are a rookie
            isRookie = (f"{self.__name} is a {self.__league} rookie since he has played {self.__yearsplayed} years in the {self.__league}")
        else:
            isRookie = (f"{self.__name} is not a {self.__league} rookie since he has played {self.__yearsplayed} years in the {self.__league}")
        return isRookie
    def ReleaseFromTeam(self):
        released = ""
        originalTeam = self.__team
        self.__team = "Free Agent"##change team to free agent since they have been released and aren't on a team
        released = (f"{self.__name} has been released from the {originalTeam} and is currently a {self.__team}")
        return released
    def __str__(self):
        finalstring = (f"A BasketballPlayer plays in the {self.__league}")
        return finalstring

def main():
    HighScorers = [] ##list we will return at the end of our demo program which contains all players who scored over 20 points
    player1 = BasketballPlayer("Lebron James","Lakers",36,35651,1321,19)##player object
    print(player1.__str__())##run all methods
    print(player1.GetPlayerName())
    print(player1.GetPlayerAge())
    print(player1.GetPlayerTeam())
    print(player1.GetAveragePoints())
    print(player1.isNBAveteran())
    print(player1.isRookie())
    print(player1.ReleaseFromTeam())
    print(player1.GetPlayerTeam())
    if player1.GetAveragePoints() > 20:##check if player is high scorer and add to list if they are
        HighScorers.append(player1.GetPlayerName())
    player2 = BasketballPlayer("Alex Caruso","Bulls",27,1271,206,5)##player object 2
    print(player2.__str__())
    print(player2.GetPlayerName())##run methods
    print(player2.GetPlayerAge())
    print(player2.GetPlayerTeam())
    print(player2.GetAveragePoints())
    print(player2.isNBAveteran())
    print(player2.isRookie())
    print(player2.ReleaseFromTeam())
    print(player2.GetPlayerTeam())
    if player2.GetAveragePoints() > 20:
        HighScorers.append(player2.GetPlayerName())
    player3 = BasketballPlayer("Stephen Curry","Warriors",33,18990,782,13)##player object 3
    print(player3.__str__())
    print(player3.GetPlayerName())##run all methods
    print(player3.GetPlayerAge())
    print(player3.GetPlayerTeam())
    print(player3.GetAveragePoints())
    print(player3.isNBAveteran())
    print(player3.isRookie())
    print(player3.ReleaseFromTeam())
    print(player3.GetPlayerTeam())
    if player3.GetAveragePoints() > 20:
        HighScorers.append(player3.GetPlayerName())
    player4 = BasketballPlayer("Jalen Green","Rockets",19,252,18,0)##player object 4
    print(player4.__str__())
    print(player4.GetPlayerName())##run all methods
    print(player4.GetPlayerAge())
    print(player4.GetPlayerTeam())
    print(player4.GetAveragePoints())
    print(player4.isNBAveteran())
    print(player4.isRookie())
    print(player4.ReleaseFromTeam())
    print(player4.GetPlayerTeam())
    if player4.GetAveragePoints() > 20:
        HighScorers.append(player4.GetPlayerName())
    print(f"Of the players we used, this is the list of players who averaged over 20 points per game {HighScorers}")
    ##printing the list of high scorers we created throughout our program




if __name__ == "__main__":
    main()