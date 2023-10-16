import discord
from discord.ext import commands

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        print(message.content)

        if message.content == 'ping':
            await message.channel.send('pong')


def create_bot() -> discord.Client:
    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)

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
