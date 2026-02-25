"""
Exemplo de integração com Discord
"""

import discord
from discord.ext import commands
from calculadora_chat import processar_mensagem, esta_calculando

# Configuração do bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.event
async def on_message(message):
    # Ignora mensagens do próprio bot
    if message.author == bot.user:
        return
    
    user_id = str(message.author.id)
    conteudo = message.content.strip()
    
    # Processa mensagem na calculadora
    resposta = processar_mensagem(user_id, conteudo)
    
    if resposta:
        await message.reply(resposta)
    
    # Processa comandos normais também
    await bot.process_commands(message)

# Comando alternativo
@bot.command()
async def calc(ctx):
    """Inicia a calculadora cumulativa."""
    user_id = str(ctx.author.id)
    resposta = processar_mensagem(user_id, "<calc>")
    await ctx.reply(resposta)

# Rode o bot
# bot.run('SEU_TOKEN_AQUI')
