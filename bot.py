
import discord
from dotenv import load_dotenv
import sahibinden
import vitrin
from time import gmtime, strftime
####################################################################################################################

car_url = "https://www.sahibinden.com/kategori-vitrin?viewType=Gallery&category=3530&sorting=date_desc"

estate_url = "https://www.sahibinden.com/kategori-vitrin?viewType=Classic&category=3518&sorting=date_desc"

ismakineleri_url = "https://www.sahibinden.com/kategori-vitrin?viewType=Classic&category=23065&sorting=date_desc"

motor_url = "https://www.sahibinden.com/kategori-vitrin?viewType=Classic&category=3532&sorting=date_desc"

arazi_url = "https://www.sahibinden.com/kategori-vitrin?viewType=Classic&category=3531&sorting=date_desc"

hino_fb110 = "https://www.sahibinden.com/ticari-araclar-kamyon-kamyonet-hino-fb-fb-110?sorting=date_desc"

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
        await message.channel.send(f"hino yeni --> Yeni yüklenen HİNO FB-110 ilanlarını yollar !! ")

    elif message.content.lower() == 'araba yeni':
        response = (vitrin.main(car_url))
        await message.author.create_dm()
        #await message.author.dm_channel.send(f"-----------------------------------------------------------------------------------")
        #await message.author.dm_channel.send(f"{message.author.mention} --> {response[0]}")
        await message.author.dm_channel.send(f"------------------------------------------------------------------------------------ARABA İLANLARI----------------------------------------------------------------------------------")
        for i in range(1,len(response)):
            await message.author.dm_channel.send(f"{i} - {message.author.mention} --> {response[i]}")
        
        await message.channel.send(f"{time} - {message.author.mention} --> En yeni ARABA ilanları gönderildi !!")
        print(f'{client.user} ARABA mesajı {message.author} yolladı!')

    elif message.content.lower() == 'emlak yeni':
        response = (vitrin.main(estate_url))
        await message.author.create_dm()
        #await message.author.dm_channel.send(f"-----------------------------------------------------------------------------------")
        #await message.author.dm_channel.send(f"{message.author.mention} --> {response[0]}")
        await message.author.dm_channel.send(f"------------------------------------------------------------------------------------EMLAK İLANLARI----------------------------------------------------------------------------------")
        for i in range(1,len(response)):
            await message.author.dm_channel.send(f"{i} - {message.author.mention} --> {response[i]}")
        
        await message.channel.send(f"{time} - {message.author.mention} --> En yeni EMLAK ilanları gönderildi !!")
        print(f'{client.user} EMLAK mesajı {message.author} yolladı!')
    
    elif message.content.lower() == 'arazi yeni':
        response = (vitrin.main(arazi_url))
        await message.author.create_dm()
        #await message.author.dm_channel.send(f"-----------------------------------------------------------------------------------")
        #await message.author.dm_channel.send(f"{message.author.mention} --> {response[0]}")
        await message.author.dm_channel.send(f"------------------------------------------------------------------------------------ARAZİ-SUV İLANLARI----------------------------------------------------------------------------------")
        for i in range(1,len(response)):
            await message.author.dm_channel.send(f"{i} - {message.author.mention} --> {response[i]}")
        
        await message.channel.send(f"{time} - {message.author.mention} --> En yeni ARAZİ-SUV ilanları gönderildi !!")
        print(f'{client.user} ARAZİ-SUV mesajı {message.author} yolladı!')

    elif message.content.lower() == 'ismakinesi yeni':
        response = (vitrin.main(ismakineleri_url))
        await message.author.create_dm()
        #await message.author.dm_channel.send(f"-----------------------------------------------------------------------------------")
        #await message.author.dm_channel.send(f"{message.author.mention} --> {response[0]}")
        await message.author.dm_channel.send(f"------------------------------------------------------------------------------------İŞ MAKİNESİ İLANLARI----------------------------------------------------------------------------------")
        for i in range(1,len(response)):
            await message.author.dm_channel.send(f"{i} - {message.author.mention} --> {response[i]}")
        
        await message.channel.send(f"{time} - {message.author.mention} --> En yeni İŞ MAKİNESİ ilanları gönderildi !!")
        print(f'{client.user} İŞ MAKİNESİ {message.author} yolladı!')
    
    elif message.content.lower() == 'motor yeni':
        response = (vitrin.main(motor_url))
        await message.author.create_dm()
        #await message.author.dm_channel.send(f"-----------------------------------------------------------------------------------")
        #await message.author.dm_channel.send(f"{message.author.mention} --> {response[0]}")
        await message.author.dm_channel.send(f"------------------------------------------------------------------------------------MOTOR İLANLARI----------------------------------------------------------------------------------")
        for i in range(1,len(response)):
            await message.author.dm_channel.send(f"{i} - {message.author.mention} --> {response[i]}")
        
        await message.channel.send(f"{time} - {message.author.mention} --> En yeni MOTOR ilanları gönderildi !!")
        print(f'{client.user} MOTORLARI {message.author} yolladı!')

    elif message.content.lower() == 'hino yeni':
        response = (sahibinden.main(hino_fb110))
        await message.author.create_dm()
        #await message.author.dm_channel.send(f"-----------------------------------------------------------------------------------")
        #await message.author.dm_channel.send(f"{message.author.mention} --> {response[0]}")
        await message.author.dm_channel.send(f"------------------------------------------------------------------------------------HİNO FB-110 İLANLARI----------------------------------------------------------------------------------")
        for i in range(1,len(response)):
            await message.author.dm_channel.send(f"{i} - {message.author.mention} --> {response[i]}")
        
        await message.channel.send(f"{time} - {message.author.mention} --> En yeni HİNO FB-110 ilanları gönderildi !!")
        print(f'{client.user} HİNO FB-110 {message.author} yolladı!')


    else:
        await message.channel.send(f"{time} - {message.author.mention} --> INVALID COMMAND TRY AGAIN")
        print(f'{client.user} mesajı {message.author} yolladı!')

client.run("TOKENNNNNNNN")
