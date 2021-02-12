#import os
import random
import discord
from dotenv import load_dotenv
#import sahibinden
import vitrin
from time import gmtime, strftime
####################################################################################################################

car_url = "https://www.sahibinden.com/kategori-vitrin?viewType=Gallery&category=3530&sorting=date_desc"

estate_url = "https://www.sahibinden.com/kategori-vitrin?viewType=Classic&category=3518&sorting=date_desc"

ismakineleri_url = "https://www.sahibinden.com/kategori-vitrin?viewType=Classic&category=23065&sorting=date_desc"

motor_url = "https://www.sahibinden.com/kategori-vitrin?viewType=Classic&category=3532&sorting=date_desc"

arazi_url = "https://www.sahibinden.com/kategori-vitrin?viewType=Classic&category=3531&sorting=date_desc"

####################################################################################################################

time = strftime("%H:%M - %d/%m/%y", gmtime())

load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Merhaba {member.name}, sunucuya hoşgeldin !! Sunucu üzerinden !komutlar yazarak kullanmaya devam edebilirsin.')
    await member.dm_channel.send(f'Unutma bir işlem bitmeden diğeri için istekte bulunma bu senin işini kolaylaştıracaktır.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!komutlar':
        await message.channel.send(f"araba yeni --> Yeni yüklenen ARAÇLARI yollar !! ")
        await message.channel.send(f"emlak yeni --> Yeni yüklenen EMLAK ilanlarını yollar !! ")
        await message.channel.send(f"ismakinesi yeni --> Yeni yüklenen İŞ MAKİNESİ ilanlarını yollar !! ")
        await message.channel.send(f"motor yeni --> Yeni yüklenen MOTOR ilanlarını yollar !! ")
        await message.channel.send(f"arazi yeni --> Yeni yüklenen ARAZİ-SUV ilanlarını yollar !! ")

    elif message.content.lower() == 'araba yeni':
        response = (vitrin.main(car_url))
        await message.author.create_dm()
        #await message.author.dm_channel.send(f"-----------------------------------------------------------------------------------")
        #await message.author.dm_channel.send(f"{message.author.mention} --> {response[0]}")
        await message.author.dm_channel.send(f"------------------------------------------------------------------------------------ARABA İLANLARI----------------------------------------------------------------------------------")
        for i in range(1,len(response)):
            await message.author.dm_channel.send(f"{i} - {message.author.mention} --> {response[i]}")
        
        await message.channel.send(f"{time} - {message.author.mention} --> En yeni ARABA ilanları gönderildi !!")

    elif message.content.lower() == 'emlak yeni':
        response = (vitrin.main(estate_url))
        await message.author.create_dm()
        #await message.author.dm_channel.send(f"-----------------------------------------------------------------------------------")
        #await message.author.dm_channel.send(f"{message.author.mention} --> {response[0]}")
        await message.author.dm_channel.send(f"------------------------------------------------------------------------------------EMLAK İLANLARI----------------------------------------------------------------------------------")
        for i in range(1,len(response)):
            await message.author.dm_channel.send(f"{i} - {message.author.mention} --> {response[i]}")
        
        await message.channel.send(f"{time} - {message.author.mention} --> En yeni EMLAK ilanları gönderildi !!")
    
    elif message.content.lower() == 'arazi yeni':
        response = (vitrin.main(arazi_url))
        await message.author.create_dm()
        #await message.author.dm_channel.send(f"-----------------------------------------------------------------------------------")
        #await message.author.dm_channel.send(f"{message.author.mention} --> {response[0]}")
        await message.author.dm_channel.send(f"------------------------------------------------------------------------------------ARAZİ-SUV İLANLARI----------------------------------------------------------------------------------")
        for i in range(1,len(response)):
            await message.author.dm_channel.send(f"{i} - {message.author.mention} --> {response[i]}")
        
        await message.channel.send(f"{time} - {message.author.mention} --> En yeni ARAZİ-SUV ilanları gönderildi !!")

    elif message.content.lower() == 'ismakinesi yeni':
        response = (vitrin.main(ismakineleri_url))
        await message.author.create_dm()
        #await message.author.dm_channel.send(f"-----------------------------------------------------------------------------------")
        #await message.author.dm_channel.send(f"{message.author.mention} --> {response[0]}")
        await message.author.dm_channel.send(f"------------------------------------------------------------------------------------İŞ MAKİNESİ İLANLARI----------------------------------------------------------------------------------")
        for i in range(1,len(response)):
            await message.author.dm_channel.send(f"{i} - {message.author.mention} --> {response[i]}")
        
        await message.channel.send(f"{time} - {message.author.mention} --> En yeni İŞ MAKİNESİ ilanları gönderildi !!")
    
    elif message.content.lower() == 'motor yeni':
        response = (vitrin.main(motor_url))
        await message.author.create_dm()
        #await message.author.dm_channel.send(f"-----------------------------------------------------------------------------------")
        #await message.author.dm_channel.send(f"{message.author.mention} --> {response[0]}")
        await message.author.dm_channel.send(f"------------------------------------------------------------------------------------MOTOR İLANLARI----------------------------------------------------------------------------------")
        for i in range(1,len(response)):
            await message.author.dm_channel.send(f"{i} - {message.author.mention} --> {response[i]}")
        
        await message.channel.send(f"{time} - {message.author.mention} --> En yeni MOTOR ilanları gönderildi !!")
    else:
        await message.channel.send(f"{time} - {message.author.mention} --> INVALID COMMAND TRY AGAIN")





client.run("ODA5NDkyMzQyNTk0ODYzMTg1.YCV4fg.ZMLSy36OiR-Yf3VrENoxvq2ucrQ")
