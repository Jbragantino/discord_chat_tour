import discord
from discord.ext import commands


def create_bot() -> commands.Bot:
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f"{bot.user.name} has connected to Discord!")

    @bot.command(name="history", help="Return a list of historical facts about a city")
    async def get_history(ctx: commands.Context, *city_name):
        city = " ".join(city_name)
        await ctx.send(f"It's history time about {city}")

    @bot.command(
        name="restaurants", help="Returns a list of interesting restaurants in a city"
    )
    async def get_restaurants(ctx: commands.Context, *city_name):
        city = " ".join(city_name)
        await ctx.send(f"Here are some restaurants in {city}")

    return bot
