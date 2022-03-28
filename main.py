import os
from dotenv import load_dotenv
load_dotenv()
import discord
import nltk
import gensim
from gensim.models import Word2Vec as w2v
from gensim.test.utils import common_texts
from gensim.models import KeyedVectors

BOT_TOKEN = os.getenv('BOT_TOKEN')
PUBLIC_KEY = os.getenv('PUBLIC_KEY')
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # ignore bot's command
    if message.author == client.user:
        return
    print(message.content)
    await message.channel.send("Hello!")

client.run(os.getenv('BOT_TOKEN'))
model = w2v(sentences=common_texts, vector_size=100, window=5, min_count=1, workers=4)

print(model.similarity('hello', 'goodbye'))