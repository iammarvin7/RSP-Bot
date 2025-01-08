import discord
import asyncio
from dotenv import load_dotenv
import os
import random
from updateSpreadsheet import UpdateLCname
from updateSpreadsheet import UpdateLCtime
from updateSpreadsheet import UpdateLCnum
from keep_alive import keep_alive

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

happy_emojis = ["🥳", "😊", "🎉", "🏆", "💪"]


@client.event
async def on_ready():
      print('Logged in as {0.user}!'.format(client))


@client.event
async def on_message(message):
      if message.author == client.user:
            return
      if message.content.startswith('hello') or message.content.startswith(
          'Hello'):
            await message.channel.send(
                f'Hello! {message.author}' +
                '\nDo you want me to help you adding you Leetcode to your Spreadsheet!'
            )

            response = await client.wait_for('message', timeout=60.0)
            if response.content.lower() == 'yes':
                  await message.channel.send(random.choice(happy_emojis))

                  await message.channel.send('Enter the LC number')
                  number_response = await client.wait_for('message',
                                                          timeout=60.0)
                  number = number_response.content
                  UpdateLCnum(number)
                  await message.channel.send(f'Number updated to {number}')
                  await asyncio.sleep(2)
                  await message.channel.send("Enter the Leetcode name")
                  name_response = await client.wait_for('message',
                                                        timeout=60.0)
                  name = name_response.content
                  UpdateLCname(name)

                  await message.channel.send(
                      "Was it Easy, Medium or Hard? (enter e, m, or h respectively)"
                  )
                  inp_response = await client.wait_for('message', timeout=60.0)
                  inp = inp_response.content.strip().upper(
                  )  # Ensure it's uppercase

                  await message.channel.send(
                      "What time did it take you? (HH:MM:SS format)")
                  time_response = await client.wait_for('message',
                                                        timeout=60.0)
                  input_value = time_response.content

                  UpdateLCtime(
                      inp, input_value
                  )  # Update the spreadsheet with the input values
                  await message.channel.send(
                      f'Successfully updated with input: {input_value}')
                  await asyncio.sleep(2)
                  await message.channel.send("You're all set!")

            else:
                  await message.channel.send(
                      "Alright, let me know if you need anything else.")


keep_alive()
token = os.getenv('TOKEN')

# Debug: Check if the token is loaded
if not token:
      raise ValueError(
          "Bot token not found! Ensure the .env file is properly configured and loaded."
      )

client.run(token)
