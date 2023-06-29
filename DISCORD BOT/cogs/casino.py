from string import ascii_uppercase
import discord
import random
from discord.ext import commands
#line what charecter is needed to activate commands

class Example(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener
    async def online(self):
        print('Online')
    @commands.command()
    async def why(self,ctx):
        await ctx.send('why not')
    
def setup(client):
    client.add_cog(Example(client))

client = commands.Bot(command_prefix='.')




@client.command(aliases=['BJ'])
async def blackjack(ctx):

    from random import randint
    cardOne = random.randint(1,11)
    cardTwo = random.randint(1,11)
                                    #ace check
    if cardOne ==1 or cardOne==11:
        await ctx.send('You have drawn an ace.!')
        await ctx.send(f'Would you like to change it to 1 or a 11')
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and \
            msg.content.lower() in ["1", "11"]
        msg = await client.wait_for("message", check=check)
        if msg.content.lower() == "1":
            cardOne=1
        else:
            cardOne=11
                                    #second ace check
    if cardTwo==1 or cardTwo==11:
        await ctx.send('You have drawn an ace.!')
        await ctx.send(f'Would you like to change it to 1 or a 11')
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and \
            msg.content.lower() in ["1", "11"]
        msg = await client.wait_for("message", check=check)
        if msg.content.lower() == "1":
            cardTwo=1
        else:
            cardTwo=11

    user=cardOne+cardTwo

    dealer=random.randint(1,11)

    await ctx.send(f'Your hand is:{user}\nThe dealer hand is: {dealer}')
    await ctx.send(f'Would you like to hit to draw another card?\n'
                   'Please type H to draw or S to keep your hand.')
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and \
        msg.content.lower() in ["h", "s"]
    while user<=21:
        msg = await client.wait_for("message", check=check)
        if msg.content.lower() == "h":      #Player hit

            user=user+random.randint(1,11)
            await ctx.send(f"You decided to hit\nYour hand is:{user}\nThe dealer hand is: {dealer}")
            if user<21:
                await ctx.send('Would you like to hit again?')
            elif user>21:
               await ctx.send(f'Your hand is:{user}\nYou have bust!')
               return 0
            elif user==21:
                await ctx.send(f'Your hand is:{user}\nBLACKJACK!')
                return 0

            else:
                await ctx.send('Error in user drawing method')
                return 0
        else:                           #Player stay
            await ctx.send(f"You decided to stay\nYour hand is:{user}\nThe dealer hand is: {dealer}")
            while dealer<=21:
                if dealer<=16:
                    dealer=dealer+random.randint(1,11)
                    await ctx.send(f'Dealer hand is less than 16.\nThe dealer hand is: {dealer}')
                    if dealer>21:
                        await ctx.send('Dealer went bust!')
                        return 0
                    elif dealer==user:
                        await ctx.send('You have tied with the dealer.')
                        return 0
                while dealer>=17:
                    if user<dealer<=21:
                        await ctx.send(f'Dealer hand: {dealer}\nUser hand is:{user}\nYou have lost.')
                        return 0
                    elif dealer<user<=21:
                        await ctx.send('You have beaten the dealer')
                        return 0
                    elif dealer==user:
                        await ctx.send('You have tied with the dealer.')
                        return 0
                    else:
                        await ctx.send('Error in dealer drawing method')
                        return 0

@client.command()
async def roulette(ctx):

    from random import randint
    ball = random.randint(0,36)

    table_data = { 
        0: {'color':'green','row':'null','column':'null'},
        1: {'color':'black','row':3, 'column':1},
        2: {'color':'red','row':2, 'column':1},
        3: {'color':'black','row':1, 'column':1},
        4: {'color':'red','row':3, 'column':1},
        5: {'color':'black','row':2, 'column':1},
        6: {'color':'red','row':1, 'column':1},
        7: {'color':'black','row':3, 'column':1},
        8: {'color':'red','row':2, 'column':1},
        9: {'color':'black','row':1, 'column':1},
        10: {'color':'red','row':3, 'column':1},
        11: {'color':'black','row':2, 'column':1},
        12: {'color':'red','row':1, 'column':1},

        13: {'color':'black','row':3, 'column':2},
        14: {'color':'red','row':2, 'column':2},
        15: {'color':'black','row':1, 'column':2},
        16: {'color':'red','row':3, 'column':2},
        17: {'color':'black','row':2, 'column':2},
        18: {'color':'red','row':1, 'column':2},
        19: {'color':'black','row':3, 'column':2},
        20: {'color':'red','row':2, 'column':2},
        21: {'color':'black','row':1, 'column':2},
        22: {'color':'red','row':3, 'column':2},
        23: {'color':'black','row':2, 'column':2},
        24: {'color':'red','row':1, 'column':2},

        25: {'color':'black','row':3, 'column':3},
        26: {'color':'red','row':2, 'column':3},
        27: {'color':'black','row':1, 'column':3},
        28: {'color':'red','row':3, 'column':3},
        29: {'color':'black','row':2, 'column':3},
        30: {'color':'red','row':1, 'column':3},
        31: {'color':'black','row':3, 'column':3},
        32: {'color':'red','row':2, 'column':3},
        33: {'color':'black','row':1, 'column':3},
        34: {'color':'red','row':3, 'column':3},
        35: {'color':'black','row':2, 'column':3},
        36: {'color':'red','row':1, 'column':3}




    }
    table = '''
    ___________________________________________________________________
  / |_3_|_6_|_9_|_12_|_15_|_18_|_21_|_24_|_27_|_30_|_33_|_36_|_R1_|_2:1_|
| 0 |_2_|_5_|_8_|_11_|_14_|_17_|_20_|_23_|_26_|_29_|_32_|_35_|_R2_|_2:1_|
  \ |_1_|_4_|_7_|_10_|_13_|_16_|_19_|_22_|_25_|_28_|_31_|_34_|_R3_|_2:1_|
    |_______C1_______|_________C2________|_________C3________|
    |_1-18__|__EVEN__|___RED___|__BLACK__|___ODD___|__19-36__|
 
    '''
    await ctx.send(table)

client.run('Token')
