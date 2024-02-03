from Import import *
from hugchat import hugchat
from hugchat.login import Login
 

def getConfig(mode="Token"):
    with open("Config.json", "r") as f:
        data = json.load(f)
    if mode == "Token":
        return data["BotToken"]
    elif mode == "Email":
        return data["HugChatEmail"]
    elif mode == "Password":
        return data["HugChatPassword"]

intents = discord.Intents.all()
bot = discord.Bot(intents=intents)
token = getConfig()

@bot.event
async def on_ready():
    try:
        os.system("cls")
        sign = Login(email=getConfig("Email"), passwd=getConfig("Password"))
        cookies = sign.login()
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    except:
        os.system("cls")
        print(Fore.RED + "Hiba, helytelen a megadott jelszó vagy e-mail." + Fore.RESET)
        await bot.close()
    print(Fore.LIGHTBLUE_EX + f"Bejelentkezve mint {bot.user.name}\n" + Fore.RED + "Developer • 1bali1" + Fore.RESET)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Fejlesztő </> 1bali1"))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

try:
    bot.run(token)
except:
    os.system("cls")
    print(Fore.RED + "Hiba történt a bot elindítása közben, mert helytelen a megadott bot token." + Fore.RESET)