import os
from discord.ext import commands
from keep_alive import keep_alive
from datetime import datetime
import pytz

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('bot is ready')

#list of active players
player = {
    "ace": 10,
    "spirit": 20,
    "howl": 30,
    "sirius": 40,
    "liq": 30,
    "rich": 25,
    "luna": 35,
    "cody": 40,
    "shuppy": 10,
    "jon": 5,
    "gun": 15,
    "null": 0,
}

#class for 4 v 4
class team4:
    def __init__(self, player1, player2, player3, player4):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4

#class for 5 v 5
class team5:
    def __init__(self, player1, player2, player3, player4, player5):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        self.player5 = player5

#class for 6 v 6
class team6:
    def __init__(self, player1, player2, player3, player4, player5, player6):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        self.player5 = player5
        self.player6 = player6

#class for 7 v 7
class team7:
    def __init__(self, player1, player2, player3, player4, player5, player6,
                 player7):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        self.player5 = player5
        self.player6 = player6
        self.player7 = player7

#displays all players
@client.command(help="Displays a list of players")
async def players(ctx):
  for k, v in player.items():
    result = (k, v)
    await ctx.send(result)
    await ctx.send("Null is reserved for players not listed")



#compares two teams
@client.command(help="Compares two teams with pre-defined values")
async def team_compare(ctx, pc, p1, p2, p3, p4, p5, p6, p7, p8, *arg: str):
    pc = int(pc)
    if pc == 4:
        team1 = team4(p1, p2, p3, p4)
        team2 = team4(p5, p6, p7, p8)
        #score totalling
        team1_score = player[team1.player1] + player[team1.player2] + player[
            team1.player3] + player[team1.player4]
        team2_score = player[team2.player1] + player[team2.player2] + player[
            team2.player3] + player[team2.player4]
    if pc == 5:
        for p in arg:
            p9 = p
            p10 = p
        team1 = team5(p1, p2, p3, p4, p5)
        team2 = team5(p6, p7, p8, p9, p10)
        #score totalling
        team1_score = player[team1.player1] + player[team1.player2] + player[
            team1.player3] + player[team1.player4] + player[team1.player5]
        team2_score = player[team2.player1] + player[team2.player2] + player[
            team2.player3] + player[team2.player4] + player[team2.player5]
    if pc == 6:
        for p in arg:
            p9 = p
            p10 = p
            p11 = p
            p12 = p
        team1 = team6(p1, p2, p3, p4, p5, p6)
        team2 = team6(p7, p8, p9, p10, p11, p12)
        #score totalling
        team1_score = player[team1.player1] + player[team1.player2] + player[
            team1.player3] + player[team1.player4] + player[
                team1.player5] + player[team1.player6]
        team2_score = player[team2.player1] + player[team2.player2] + player[
            team2.player3] + player[team2.player4] + player[
                team2.player5] + player[team2.player6]
    if pc == 7:
        for p in arg:
            p9 = p
            p10 = p
            p11 = p
            p12 = p
            p13 = p
            p14 = p
        team1 = team7(p1, p2, p3, p4, p5, p6, p7)
        team2 = team7(p8, p9, p10, p11, p12, p13, p14)
        #score totaling
        team1_score = player[team1.player1] + player[team1.player2] + player[
            team1.player3] + player[team1.player4] + player[
                team1.player5] + player[team1.player6] + player[team1.player7]
        team2_score = player[team2.player1] + player[team2.player2] + player[
            team2.player3] + player[team2.player4] + player[
                team2.player5] + player[team2.player6] + player[team1.player7]
    if team1_score > team2_score:
        result = (team1_score - team2_score)
        print("Team 1 is better by ", result)
        await ctx.send("Team1: {} vs Team2: {}".format(team1_score,
                                                       team2_score))
        await ctx.send(
            "Team 2 is better by: {} \nPlease add {}0 points for adjustment".
            format(result, result))
    elif team2_score > team1_score:
        result = (team2_score - team1_score)
        print("Team 2 is better by ", result)
        await ctx.send("Team1: {} vs Team2: {}".format(team1_score,
                                                       team2_score))
        await ctx.send(
            "Team 2 is better by: {} \nPlease add {}0 points for adjustment".
            format(result, result))
    else:
        print("Push - Team 1: {} vs Team2: {}".format(team1_score,
                                                      team2_score))
        await ctx.send("Push")

#displays time and game time
@client.command(help="Displays current time and game time")
async def time(ctx):
    
    tz_NY = pytz.timezone('America/New_York') 
    datetime_NY = datetime.now(tz_NY)
    cur_time = ("The Current time is:", datetime_NY.strftime("%H:%M:%S"))
    await ctx.send(cur_time)
    await ctx.send("Game time is at 21:30:00 EASTERN TIMEZONE")


keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
