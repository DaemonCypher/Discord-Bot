import discord
import random
import os, sys
from discord.ext import commands
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is ready.\nBot is online to wreck havoc!')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command()
async def who(ctx):
    await ctx.send('Your part of the CYPHER ARMY!')

@client.command(aliases=['8ball','eightball'])
async def _8ball(ctx,*,question):
    responses=['As I see it, yes.',
              'Ask again later.',
              'Better not tell you now.',
              'Cannot predict now.',
              'Concentrate and ask again.',
              'Don’t count on it.',
              'It is certain.',
              'It is decidedly so.',
               'Most likely.',
              'My reply is no.',
              'My sources say no.',
              'Outlook not so good.',
              'Outlook good.',
              'Reply hazy, try again.',
              'Signs point to yes.',
              'Very doubtful.',
              'Without a doubt.',
              'Yes.',
              'Yes – definitely.',
              'You may rely on it.']
    await ctx.send(f'Question:{question}\nAnswer:{random.choice(responses)}')


@client.command()
async def clear(ctx,amount=1):
    await ctx.channel.purge(limit=amount+1)

@client.command(aliases=['CF'])
async def coinflip(ctx):
    from random import randint
    coin= (random.randint(0,99))
    if coin<49:
        await ctx.send(f'heads')
    else:
        await ctx.send(f'tails')

@client.command()
async def helper(ctx):
    await ctx.send(f'possible commands are:\n.helper, .penis, .clear [enter a number], .dice, .who, .8ball')

@client.command()
async def kick(ctx,member : discord.Member,*,reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx,member : discord.Member,*,reason=None):
    await member.ban(reason=reason)
    
@client.command()
async def unban(ctx,*,memeber):
    banned_users= await ctx.guild.bans()
    member_name,member_discriminator= member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name,user.discriminator)==(member_name,member_dsicriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
        

@client.command(aliases=['BJ'])
async def blackjack(ctx):

    from random import randint
    cardOne=random.randint(1,11)
    cardTwo=random.randint(1,11)
                                    #ace check
    if cardOne==1 or cardOne==11:
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

@client.command(aliases=['RPS'] )
async def RockPaperScissors(ctx,*,value):
    choice=['Rock','Paper','Scissors']
    if value==choice:
        await ctx.send('You have tied with the Game Master')
    elif (value == Scissors and choice == Paper) or (value == Paper and choice== Rock) or (value == Rock and choice == Scissors):
        await ctx.send('You have beaten the Game Master')
        return 0
    else:
        await ctx.send('Error in Player and GM comaprison test')
        return 0

    
    


client.run('NzkzMTQ1ODUwOTk3NjM3MTUx.X-oAog.gr7FO3YP5pb2sYz2dWJmW39La3o')
