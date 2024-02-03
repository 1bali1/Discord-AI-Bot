
from Import import *

intents = discord.Intents.all()
bot = discord.Bot(intents = intents)
userCooldowns = {}

class events(commands.Cog,name="events"):
    def __init__ (self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message):
       
        if message.author.bot:
            return
        aiChannels = AI.getChats()
        if str(message.guild.id) in aiChannels:
            if message.channel.id == aiChannels[str(message.guild.id)]["ChannelID"]:
     

                try:
             
                    channel = self.bot.get_channel(aiChannels[str(message.guild.id)]["ChannelID"])
                    userId = message.author.id
                
                    currentTime = time.time()

                    textR = "`Csak 15 másodpercenként tehetsz fel kérdést a botnak.`"
                    if userId in userCooldowns and currentTime - userCooldowns[userId] < 15:
                        await message.reply(textR)
                        return
                    userCooldowns[userId] = currentTime
            
                    result = await bot.loop.run_in_executor(None, AI.ask, message.content)
                    await message.reply(result[0])
                    index = 1
                    for i in result:
                        await channel.send(result[index])
                        index += 1

                    
                    return 
              
        
                except:
                    None

def setup(bot):
    bot.add_cog(events(bot))





