from Import import *
import json
from hugchat import hugchat
from hugchat.login import Login
from deep_translator import GoogleTranslator   
chatFile = "database/Chat.json"

def getConfig(mode="Email"):
    with open("Config.json", "r") as f:
        data = json.load(f)
    if mode == "Email":
        return data["HugChatEmail"]
    elif mode == "Password":
        return data["HugChatPassword"]

def updateChat(user,change = 0,mode="ChannelID"):
    data =  getChats()
    data[str(user)][mode] = change


    with open(chatFile, "w") as f:
        json.dump(data,f, indent=4)
   

def openChats(channel):
    data =  getChats()

    if str(channel) in data:
        return False
    
    else:
            data[str(channel)] = {}
            data[str(channel)]["ChannelID"] = 0
            data[str(channel)]["ServerID"] = 0

    with open(chatFile, "w") as f:
        json.dump(data,f, indent=4)
    return

def getChats():
    with open(chatFile, "r") as f:
        data = json.load(f)
    return data


def ask(prompt):

    email = str(getConfig("Email"))
    password = str(getConfig("Password"))
    sign = Login(email=email, passwd=password)
    cookies = sign.login()
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())


    needToBeTranslated = GoogleTranslator(source='auto', target='en').translate(str(f"{prompt}")) #Igen, tudom mi a bajod ezzel a sorral

    response = chatbot.chat(str(needToBeTranslated))
    
    translated = GoogleTranslator(source='auto', target='hu').translate(str(response))


 
    if len(translated) > 2000:
       
        response = []
        chunks = [translated[i:i + 2000] for i in range(0, len(translated), 2000)]
        response.extend(chunks)
       
        return response
    else:
        return [translated]
        