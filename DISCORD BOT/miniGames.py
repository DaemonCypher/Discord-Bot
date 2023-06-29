import discord
import random
from discord.ext import commands


#line what charecter is needed to activate commands
client = commands.Bot(command_prefix='.')

client = commands.Bot(command_prefix='.')
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

#aliases is another commmand that can be use 
@client.command(aliases=['CF'])
async def coinflip(ctx):
    from random import randint
    coin= (random.randint(0,99))
    if coin<49:
        await ctx.send(f'heads')
    else:
        await ctx.send(f'tails')


client.run('Token')
