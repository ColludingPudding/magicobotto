import discord
import os
import requests
from discord.ext import commands

from keepalive import keepalive

client = commands.Bot(command_prefix='$')

magic_code = os.environ['DISCORD_TOKEN']

def dad_jokes():
  url = 'https://icanhazdadjoke.com'
  headers = {
    'Accept': 'text/plain',
    'User-Agent': 'Steve the bot 1.0',
    'From': 'muzume.work@gmail.com'  # This is another valid field
  }
  r = requests.get(url, headers=headers)
  return r.text

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  # Rice
  if message.content.startswith('Cum'):
    await message.channel.send('Yum', delete_after=3.0)

  await client.process_commands(message)

@client.command(name='number', help='Send a random number trivia')
async def number(ctx, number='random?min=0&max=9999',type='trivia'):
  response = requests.get(f'http://numbersapi.com/{number}/{type}')
  await ctx.send(response.text)

@client.command(name='waifu', help='Send a random waifu image')
async def waifugenerator(ctx, arg1='sfw', arg2='waifu'):
  rep = requests.get(f'https://api.waifu.pics/{arg1}/{arg2}')
  waifu = rep.text[8:-3]
  await ctx.send(waifu)

@client.command(name='catto', help='Send a random cat pic')
async def catto(ctx):
  await ctx.send('https://cataas.com/cat')
  '''
  # teaching Steve how to be nice
  message_text = message.content.strip().upper().split()
  for word in message_text:
    if word in swear_list:
      await message.channel.send('Watch your language young man')
      break
  '''
'''
  # teaching Steve how to be a perfect dad
  if message.content.startswith('$teve joke'):
    await message.channel.send(dad_jokes())

  if message.content.startswith('$teve catto'):
    await message.channel.send('https://cataas.com/cat')

  if message.content.startswith('$waifu'):
    commands = message.content.split()
    if len(commands) != 1:
      type = commands[1].lower()
      cate = commands[2].lower()
      await message.channel.send(waifu(type,cate))
    else:
      await message.channel.send(waifu())
'''
keepalive()
client.run(magic_code)