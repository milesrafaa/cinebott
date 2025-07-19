import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.slash_command(name="resumo", description="Veja o resumo")
async def resumo(ctx: discord.ApplicationContext):
    await ctx.respond("por enquanto não tem nada!")

# Para rodar o bot, substitua 'SEU_TOKEN_AQUI' pelo token do seu bot
bot.run('MTM5NTkzMjI3MDE3NDQwNDY3OQ.GS6Plp.-NUcLIicdSoYXX3SkmdAY1yOcdP8WWxzjAhV5Y') 
# bot.run('SEU_TOKEN_AQUI')
