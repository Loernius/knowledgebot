import discord

class Knowledgebot(discord.Client):
    async def on_ready(self):
        print('bot running as {0}'.format(self.user))
    
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
    
