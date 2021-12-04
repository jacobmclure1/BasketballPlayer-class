The Basketball player class is based on real life NBA players.
It will contain a players name, team, age, total points, games played, and years in the NBA.
It is meant to model a real life NBA player so you can create programs revovling around player stats.
It has methods to return certain player stats and info to make it simpler to make programs with it.
It also has methods to tell if a player is rookie or veteran and has a function which takes a player off their team.

league(class variable): Each Basketball player plays in the league the NBA
name: The players name
age: How old the player is 
team: What team a player plays for , if they don't play for a team they are a free agent
totalpoints: How many points a player has scored in their career
gamesplayed: How many games a player has played in their career
yearsplayed: How many years a player has been in the NBA

GetPlayerAge: returns a players age and can be useful when making programs
GetPlayerTeam: returns a players team and can be useful when making programs
GetPlayerName: returns a players name 
GetPlayerAveragePoints: Takes a player totalpoints and divides it by their games played to calculate their points average per game. Returns the points average per game
IsNBAveteran: In this case an NBA veteran will be someone whos played 5 or more years in the NBA. Takes a player years played and checks if they are a veteran and returns a sentence saying if a player is a veteran or not
IsRookie: A rookie is someone in the nba who is new to the nba and has no experience. This will check yearsplayed and see if its 0 and return a string saying if they are a rookie or not.
ReleaseFromTeam: Changes player from their team to a free agent and returns a string sayin they have been released
__str__: Returns a brief sentence on what a basketball player is

The demo program I created will go through and test a couple of the methods on created player objects.
It is meant to showcase the functionality of the program.
It goes over multiple player objects to show how each methods acts depending on the player.
It shows how to create a player object.
It also will create a list of players who scored over 20 ppg using the GetPlayerAveragePoints, this is to showcase how you can use the program