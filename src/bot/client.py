import discord
from rasa.core.agent import Agent
from gpt.gepeto import generate_prompt

class MyClient(discord.Client):

    user_messages = {}

    def create_agent(self):
        self.agent = Agent.load("rasa_3x/models/20231023-214837-nuclear-puffin.tar.gz")

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        
        output = await self.agent.handle_text(message.content)

        try:
            await message.channel.send(output[0]['text'])
        except:
            await message.channel.send("I'm thinking...")
            self.user_messages[message.author] = self.user_messages.get(message.author, [])
            self.user_messages[message.author].append({
                                                    "role": "user",
                                                    "content": message.content
                                                })
            gpt_prompt = generate_prompt(self.user_messages[message.author])
            self.user_messages[message.author].append(gpt_prompt)

            if len(gpt_prompt["content"]) > 2000:
                await message.channel.send(gpt_prompt["content"][:2000])
                await message.channel.send(gpt_prompt["content"][2000:])
            else:
                await message.channel.send(gpt_prompt["content"])



def create_bot() -> discord.Client:
    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)

    client.create_agent()

    return client
