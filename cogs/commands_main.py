import discord
from discord import app_commands
from discord.ext import commands
import requests

class command_kaguya(commands.Cog):

    @app_commands.command(name="conversor", description="Esse comando converte o valor de uma criptomoeda escolhida para a outra. EXEMPLO: Convert Bitcoin para Real Brasileiro")
    async def binance(self,ctx, coin, base):
        try:
            response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")
            data = response.json()
            price = data.get('price')
        
            if price:
                await ctx.send(f"Valor do par {coin.upper()}/{base.upper()} é ${price}")
            else:
                await ctx.send(f"O par {coin.upper}/{base.upper} é inválido!")
        except Exception as error:
            await ctx.send('Ops... deu algum erro >.<')
            print(error)
    
    
async def setup(client):
    await client.add_cog(command_kaguya(client))
    