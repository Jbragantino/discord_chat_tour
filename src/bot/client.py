import discord
from discord.ext import commands
from rasa.core.agent import Agent

class MyClient(discord.Client):
    def create_agent(self):
        self.agent = Agent.load("rasa_3x/models/20231017-214025-complex-salmon.tar.gz")

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        
        output = await self.agent.handle_text(message.content)

        print(message.content)

        await message.channel.send(output[0]['text'])


def create_bot() -> discord.Client:
    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)

    client.create_agent()

    return client
    

    # bot = commands.Bot(command_prefix="!", intents=intents)

    # @bot.event
    # async def on_ready():
    #     print(f"{bot.user.name} has connected to Discord!")

    # @bot.command(name="history", help="Return a list of historical facts about a city")
    # async def get_history(ctx: commands.Context, *city_name):
    #     city = " ".join(city_name)
    #     await ctx.send(f"It's history time about {city}")

    # @bot.command(
    #     name="restaurants", help="Returns a list of interesting restaurants in a city"
    # )
    # async def get_restaurants(ctx: commands.Context, *city_name):
    #     city = " ".join(city_name)
    #     await ctx.send(f"Here are some restaurants in {city}")

    # return bot
