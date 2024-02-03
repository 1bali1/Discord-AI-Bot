
from Import import *

intents = discord.Intents.all()

bot = discord.Bot(intents = intents)

class setaichannel(commands.Cog,name="setaichannel"):
    def __init__ (self, bot):
        self.bot = bot
    @bot.command(name="set-ai-channel", description="Set an ai channel!", description_localizations={
        "hu": "Állítsd be az AI csatornát!"
    })
    async def setAiChannel(self,ctx, channel:Option(discord.TextChannel, "Choose which channel you want to set!", description_localizations={
        "hu": "Válaszd ki, melyik csatornát szeretnéd beállítani!"
    })):
        await ctx.defer()

        textQ = "`Sikeresen beállítottad az AI csatornát!`"
        textR = "`Sikeresen átállítottad az AI csatornát!`"

        dataChats = AI.getChats()
        if str(ctx.guild.id) not in dataChats:
            AI.openChats(ctx.guild.id)
            AI.updateChat(ctx.guild.id, channel.id, "ChannelID")
            AI.updateChat(ctx.guild.id, ctx.guild.id, "ServerID")
            await ctx.respond(textQ)
        else:
            AI.updateChat(ctx.guild.id, channel.id, "ChannelID")
            AI.updateChat(ctx.guild.id, ctx.guild.id, "ServerID")
            await ctx.respond(textR)

    @setAiChannel.error
    async def change(self,ctx, error):

        if isinstance(error, MissingPermissions):
            embed = discord.Embed(title="Hiba!", description="A parancs használatához nincs elegendő jogosultságod.", color=discord.Color.red(), timestamp=datetime.now())
            embed.add_field(name="**Szükséges jogosultság**", value="`Rendszergazda`")

            embed.set_footer(text=f"{bot.user.name} • Set AI", icon_url=bot.user.avatar.url)
            try:
                embed.set_author(icon_url=ctx.author.avatar.url, name=ctx.user.name)
            except:
                embed.set_author(icon_url="https://cdn.discordapp.com/attachments/1144189462973267998/1180824745072132097/rounded-in-photoretrica.png?ex=657ed3bd&is=656c5ebd&hm=5a85caf8db8ddfb0c1e493df6f84be06dfe725accbd2bfabc733fd362fd993a4&", name=ctx.user.name)
            await ctx.respond(embed=embed)
def setup(bot):
    bot.add_cog(setaichannel(bot))





