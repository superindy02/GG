#ππ§π­ππ«ππ¬[ππ¨π₯π₯π²] π.π_π½πππ update 02-12-2020
#Thank For Aki DEVAN ,Ben,Igo,Dzul DK
#Thank for Β°β’α΄ΚΙͺα΄β’GRIND KILLER
#Thank for ELFOX
#Supported by Babysha,dira,onay,padel,firman
#πππ πππ¦π’π₯π²[BONE TO REBORN] Ibal v2β’ & friend
#ππ¨π«π©π‘π’π§πππ¨π­π¬
#Thank  For Greet 
#all family famz kebotan
import pantek
from pantek import *
from akad.ttypes import *
from datetime import datetime
import pytz, pafy, null, time, asyncio, random, multiprocessing, timeit, sys, json, ctypes, codecs, tweepy, threading, glob, re, ast, six, os, subprocess, wikipedia, atexit, urllib, urllib.parse, urllib3, string, tempfile, shutil, unicodedata
from humanfriendly import format_timespan, format_size, format_number, format_length
import html5lib
import requests,json,urllib3
from random import randint
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
from time import sleep
from zalgo_text import zalgo
from threading import Thread,Event
import wikipedia as wiki
requests.packages.urllib3.disable_warnings()
from tmp.Instagram import InstagramScraper
from Naked.toolshed.shell import execute_js 
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest


botStart = time.time()
msg_dict = {}
msg_dict1 = {}

#======Login Via Email Bagi Kalian Yg gk tau apa itu Token===================

dollypk = LINE("topnetworking01@gmail.com","a201399")
dollypk.log("Auth Token : " + str(dollypk.authToken))

pk = LINE("@gmail.com","pw")
pk.log("Auth Token : " + str(pk.authToken))

pk2 = LINE("@gmail.com","pw")
pk2.log("Auth Token : " + str(pk2.authToken))

pk3 = LINE("@gmail.com","pw")
pk3.log("Auth Token : " + str(pk3.authToken))

pkjs = LINE("@gmail.com","pw")
pkjs.log("Auth Token : " + str(pkjs.authToken))

poll = OEPoll(dollypk)
call = dollypk
print ("LOGIN READY ")
print ("PROSES")
print ("οΈ»β¦Μ΅Μ΅ΝΜΏΜΏΜΏΜΏβ€βPANTEK α΅β±Λ‘Λ‘α΅Κ³ ")
print ("======1%\n=======50%\n=========100%")
print (" α΄Κα΄Ι΄α΄sΒ α΄α΄Β α΄ΚΚα΄ΚΒ sα΄‘α΄ ")
print (" α΄Κα΄Ι΄α΄sΒ α΄α΄Β α΄ΚΒ³ ")
print (" α΄α΄α΄α΄Β sα΄α΄ΚΒ α΄Ι΄α΄Β Κα΄ΚΚα΄s ")
print ("\n\
= = = = = = = = = = = =        =====               === \n\
= = = = = = = = = = = = =      =====            === \n\
=======          ====== =      =====         === \n\
=======           ====== =     =====      ===\n\
=======           =======      =====    === \n\
=======           ======       ===== ===\n\
=================              ===== ===\n\
================               =====     ===\n\
=======                        =====      ===  \n\
=======                        =====         ===\n\
=======                        =====           ===\n\
=======                        =====             === \n")
print("LOGIN SUKSES")
print ("BOT PROTECT SIAP DI GUNAKAN\n   ππ§π­ππ«ππ¬[ππ¨π₯π₯π²] π.π_π½πππ \n\n")
#==========mid kalian ya dan mid induk nya================================
creator = ["u3a4cc9a5d0da4077d7dc6cd4f405517c"]
owner = ["mid"]
admin = ["mid"]
staff = ["mid"]

mid = dollypk.getProfile().mid
Amid = pk.getProfile().mid
Bmid = pk2.getProfile().mid
Cmid = pk3.getProfile().mid
Zmid = pkjs.getProfile().mid
KAC = [dollypk,pk,pk2,pk3]
ABC = [pk,pk2,pk3]
Bots = [mid,Amid,Bmid,Cmid,Zmid]
Pkbot = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []
welcome = []
#==============Respon Bot====================
responsename1 = pk.getProfile().displayName
responsename2 = pk2.getProfile().displayName
responsename3 = pk3.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoRead':False,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":True,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "selfbot":True,
    "mention":"Sider terus sampe mata lu buta",
    "Respontag":"Tag Fix Sampah",
    "welcome":"Selamat datang semoga betah dan jangan lupa cek note",
    "comment":"Like like & like by π.πΒ°π½πππ",
    "message":"Kenapa Lu add yaealah\nlu block aja lah\npenting tag group aja\natau pc Admin cantik\nline.me/ti/p/~mina59.",
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention Userγ{}γ\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\nβββ[ {} ]".format(str(dollypk.getGroup(to).name))
                except:
                    no = "\nβββ[ Success ]"
        dollypk.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        dollypk.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Sider Userγ{}γ\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\nβββ[ {} ]".format(str(dollypk.getGroup(to).name))
                except:
                    no = "\nβββ[ Success ]"
        dollypk.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        dollypk.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masukγ{}γ\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = dollypk.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\nβββ[ {} ]".format(str(dollypk.getGroup(to).name))
                except:
                    no = "\nβββ[ Success ]"
        dollypk.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        dollypk.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = dollypk.getAllContactIds()
        gid = dollypk.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"π Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\nβͺ Group : "+str(len(gid))+"\nβͺ Teman : "+str(len(teman))+"\nβͺ Expired : In "+hari+"\nβͺ Version : Lupa Anjir\nβͺCreator: ππ§π­ππ«ππ¬[ππ¨π₯π₯π²]\nβͺTeam: π.πΒ°π½πππ\n\n        Supported by\nβͺAki Devan\nβͺELFOX\nβͺBen\nβͺIGO\nβͺπππ πππ¦π’π₯π² Ibal & Friend\nβͺππ¨π«π©π‘π’π§πππ¨π­π¬\nβͺΒ°β’α΄ΚΙͺα΄β’GRIND KILLER\nβͺβπ±πππ πππππππβ \n\n        π.πΒ°π½πππ 2020\n\nβͺ Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nβͺ Runtime : \n β’ "+bot
        dollypk.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        dollypk.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "     βπ.πΒ°πππΌππ½πππβ\n" +\
                  "βͺ" + key + "Me\n" + \
                  "βͺ" + key + "Status\n" + \
                  "βͺ" + key + "About\n" + \
                  "βͺ" + key + "Restart\n" + \
                  "βͺ" + key + "Runtime\n" + \
                  "βͺ" + key + "Creator\n" + \
                  "βͺ" + key + "Sprespon\n" + \
                  "βͺ" + key + "Ginfo\n" + \
                  "βͺ" + key + "Open\n" + \
                  "βͺ" + key + "Close\n" + \
                  "βͺ" + key + "Url grup\n" + \
                  "βͺ" + key + "Gruplist\n" + \
                  "βͺ" + key + "Infogrupγangkaγ\n" + \
                  "βͺ" + key + "Infomemγangkaγ\n" + \
                  "βͺ" + key + "Remove chat\n" + \
                  "βͺ" + key + "Lurkingγon/offγ\n" + \
                  "βͺ" + key + "Lurkers\n" + \
                  "βͺ" + key + "Siderγon/offγ\n" + \
                  "βͺ" + key + "Updatefoto\n" + \
                  "βͺ" + key + "Updategrup\n" + \
                  "βͺ" + key + "allup\n" + \
                  "βͺ" + key + "Broadcast:γTextγ\n" + \
                  "βͺ" + key + "Notagγon/offγ\n" + \
                  "βͺ" + key + "Stickerγon/offγ\n" + \
                  "βͺ" + key + "Responγon/offγ\n" + \
                  "βͺ" + key + "Contactγon/offγ\n" + \
                  "βͺ" + key + "Autojoinγon/offγ\n" + \
                  "βͺ" + key + "Autoaddγon/offγ\n" + \
                  "βͺ" + key + "Welcomeγon/offγ\n" + \
                  "βͺ" + key + "Autoleaveγon/offγ\n" + \
                  "βͺ" + key + "Admin:on\n" + \
                  "βͺ" + key + "Admin:repeat\n" + \
                  "βͺ" + key + "Staff:on\n" + \
                  "βͺ" + key + "Staff:repeat\n" + \
                  "βͺ" + key + "Bot:on\n" + \
                  "βͺ" + key + "Bot:repeat\n" + \
                  "βͺ" + key + "Adminadd\n" + \
                  "βͺ" + key + "Admindell\n" + \
                  "βͺ" + key + "Staffadd\n" + \
                  "βͺ" + key + "Staffdell\n" + \
                  "βͺ" + key + "Botadd\n" + \
                  "βͺ" + key + "Botdell\n" + \
                  "βͺ" + key + "Refresh\n" + \
                  "βͺ" + key + "Listbot\n" + \
                  "βͺ" + key + "Listadmin\n" + \
                  "βͺ" + key + "Listprotect\n" + \
                  "βͺBot Kalian error pc admin\n" +\
                  "βͺ" + key + "  http://line.me/ti/p/~babyvio.\n\n" +\
                  "          βπ.πΒ°πππΌππ½πππβ"
    return helpMessage

def helppro():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "     βπ.πΒ°πππΌππ½πππβ\n" +\
                  "βͺ" + key + "      βHELP Protectβ\n" + \
                  "βͺ" + key + "pk in/out\n" + \
                  "βͺ" + key + "Byeme\n" + \
                  "βͺ" + key + "ajs join/bye\n" + \
                  "βͺ" + key + "ajs stay\n" + \
                  "βͺ" + key + "LeaveγNamagrupγ\n" + \
                  "βͺ" + key + "allproγon/offγ\n" + \
                  "βͺ" + key + "Protecturlγon/offγ\n" + \
                  "βͺ" + key + "Protectjoinγon/offγ\n" + \
                  "βͺ" + key + "Protectkickγon/offγ\n" + \
                  "βͺ" + key + "Protectcancelγon/offγ\n" + \
                  "βͺ" + key + "Antijsγon/offγ\n" + \
                  "βͺ" + key + "Ghostγon/offγ\n" + \
                  "βͺ" + key + "pkKickγ@γ\n" + \
                  "βͺ" + key + "Listprotect\n" + \
                  "βͺBot Kalian error pc admin\n" +\
                  "βͺ" + key + "  http://line.me/ti/p/~babyvio.\n\n" +\
                  "          βπ.πΒ°πππΌππ½πππβ"
                  
    return helpMessage2

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "     βπ.πΒ°πππΌππ½πππβ\n" +\
                  "βͺ" + key + "Blc\n" + \
                  "βͺ" + key + "Ban:on\n" + \
                  "βͺ" + key + "Unban:on\n" + \
                  "βͺ" + key + "Ban\n" + \
                  "βͺ" + key + "Unban\n" + \
                  "βͺ" + key + "Talkban\n" + \
                  "βͺ" + key + "Untalkban\n" + \
                  "βͺ" + key + "Talkban:on\n" + \
                  "βͺ" + key + "Untalkban:on\n" + \
                  "βͺ" + key + "Banlist\n" + \
                  "βͺ" + key + "Talkbanlist\n" + \
                  "βͺ" + key + "Clearban\n" + \
                  "βͺ" + key + "Refresh\n" + \
                  "βͺ" + key + "Cek sider\n" + \
                  "βͺ" + key + "Cek spam\n" + \
                  "βͺ" + key + "Cek pesan \n" + \
                  "βͺ" + key + "Cek respon \n" + \
                  "βͺ" + key + "Cek welcome\n" + \
                  "βͺ" + key + "Set sider:\n" + \
                  "βͺ" + key + "Set spam:\n" + \
                  "βͺ" + key + "Set pesan:\n" + \
                  "βͺ" + key + "Set respon:\n" + \
                  "βͺ" + key + "Set welcome:\n" + \
                  "βͺ" + key + "Myname:\n" + \
                  "βͺ" + key + "pkname:\n" + \
                  "βͺ" + key + "pk2name:\n" + \
                  "βͺ" + key + "pk3name:\n" + \
                  "βͺ" + key + "pkup\n" + \
                  "βͺ" + key + "pk2up\n" + \
                  "βͺ" + key + "pk3up\n" + \
                  "βͺ" + key + "  http://line.me/ti/p/~babyvio.\n\n" +\
                  "          βπ.πΒ°πππΌππ½πππβ"
                  
    return helpMessage1

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if dollypk.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            dollypk.reissueGroupTicket(op.param1)
                            X = dollypk.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            dollypk.updateGroup(X)
                            dollypk.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if pk.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                pk.reissueGroupTicket(op.param1)
                                X = pk.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                pk.updateGroup(X)
                                dollypk.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if pk2.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    pk2.reissueGroupTicket(op.param1)
                                    X = pk2.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    pk2.updateGroup(X)
                                    dollypk.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if pk3.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        pk3.reissueGroupTicket(op.param1)
                                        X = pk3.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        pk3.updateGroup(X)
                                        dollypk.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if dollypk.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            dollypk.reissueGroupTicket(op.param1)
                                            X = dollypk.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            dollypk.updateGroup(X)
                                            dollypk.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if pk.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                pk.reissueGroupTicket(op.param1)
                                                X = pk.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                pk.updateGroup(X)
                                                dollypk.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        dollypk.acceptGroupInvitation(op.param1)
                        ginfo = dollypk.getGroup(op.param1)
                        dollypk.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        dollypk.leaveGroup(op.param1)
                    else:
                        dollypk.acceptGroupInvitation(op.param1)
                        ginfo = dollypk.getGroup(op.param1)
                        dollypk.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        dollypk.acceptGroupInvitation(op.param1)
                        ginfo = dollypk.getGroup(op.param1)
                        dollypk.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        dollypk.acceptGroupInvitation(op.param1)
                        ginfo = dollypk.getGroup(op.param1)
                        dollypk.sendMessage(op.param1,"Haii " + str(ginfo.name))
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        pk.acceptGroupInvitation(op.param1)
                        ginfo = pk.getGroup(op.param1)
                        pk.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        pk.leaveGroup(op.param1)
                    else:
                        pk.acceptGroupInvitation(op.param1)
                        ginfo = pk.getGroup(op.param1)
                        pk.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        pk2.acceptGroupInvitation(op.param1)
                        ginfo = pk2.getGroup(op.param1)
                        pk.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        pk2.leaveGroup(op.param1)
                    else:
                        pk2.acceptGroupInvitation(op.param1)
                        ginfo = pk2.getGroup(op.param1)
                        pk2.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        pk3.acceptGroupInvitation(op.param1)
                        ginfo = pk3.getGroup(op.param1)
                        pk3.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        pk3.leaveGroup(op.param1)
                    else:
                        pk3.acceptGroupInvitation(op.param1)
                        ginfo = pk3.getGroup(op.param1)
                        pk3.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = dollypk.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            dollypk.cancelGroupInvitation(op.param1,[_mid])
                            dollypk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            group = pk.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                pk.cancelGroupInvitation(op.param1,[_mid])
                                pk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                group = pk2.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    pk2.cancelGroupInvitation(op.param1,[_mid])
                                    pk2.kickoutFromGroup(op.param1, [_mid])
                            except:
                                try:
                                    group = pk3.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        pk3.cancelGroupInvitation(op.param1,[_mid])
                                        pk3.kickoutFromGroup(op.param1, [_mid])
                                except:
                                    pass

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = dollypk.getGroup(op.param1)
                contact = dollypk.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                dollypk.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	pk3.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                pk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    pk2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        dollypk.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        dollypk.sendMessage(op.param1, wait["message"])

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

        if op.type == 19:
            try:
                if op.param1 in ghost:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = dollypk.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dollypk.updateGroup(G)
                        invsend = 0
                        Ticket = dollypk.reissueGroupTicket(op.param1)
                        pkjs.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pkjs.kickoutFromGroup(op.param1,[op.param2])
                        pkjs.leaveGroup(op.param1)
                        X = dollypk.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        dollypk.updateGroup(X)
            except:
                pass             
                
        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        pkjs.acceptGroupInvitation(op.param1)
                        G = pkjs.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        pkjs.updateGroup(G)
                        Ticket = pkjs.reissueGroupTicket(op.param1)
                        dollypk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pk2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pk3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pkjs.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = True
                        pkjs.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        pkjs.leaveGroup(op.param1)
                        dollypk.inviteIntoGroup(op.param1,[Zmid])
                        dollypk.inviteIntoGroup(op.param1,[admin])
                    else:
                        pass
                        
                if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        dollypk.kickoutFromGroup(op.param1,[op.param2])
                        dollypk.findAndAddContactsByMid(op.param3)
                        dollypk.inviteIntoGroup(op.param1,[Zmid])
                        dollypk.sendMessage(op.param1,"=AntiJS Invited=")
                    else:
                        dollypk.kickoutFromGroup(op.param1,[op.param2])
                        dollypk.findAndAddContactsByMid(op.param3)
                        dollypk.inviteIntoGroup(op.param1,[Zmid])
                        dollypk.sendMessage(op.param1,"=AntiJS Invited=")
                        
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            dollypk.kickoutFromGroup(op.param1,[op.param2])
                            dollypk.findAndAddContactsByMid(op.param3)
                            dollypk.inviteIntoGroup(op.param1,[op.param3])
                            dollypk.sendMessage(op.param1,"=Admin Invited=")
            except:
                pass
                
        if op.type == 32:
            if op.param3 in Bmid:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                     wait["blacklist"][op.param2] = True
                     try:
                         random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                         random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                         dollypk.sendMessage(op.param1, "ProtectJs Jgn di Cancel")
                     except:
                         pass
            return
#-------------------------------------------------------------------------------                
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            pk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                pk2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    pk3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        pk.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            pk2.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                dollypk.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        pk.kickoutFromGroup(op.param1,[op.param2])
                        pk.inviteIntoGroup(op.param1,[op.param3])
                        dollypk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            pk2.kickoutFromGroup(op.param1,[op.param2])
                            pk2.inviteIntoGroup(op.param1,[op.param3])
                            dollypk.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                pk3.kickoutFromGroup(op.param1,[op.param2])
                                pk3.inviteIntoGroup(op.param1,[op.param3])
                                dollypk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = pk.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    pk.kickoutFromGroup(op.param1,[op.param2])
                                    pk.updateGroup(G)
                                    Ticket = pk.reissueGroupTicket(op.param1)
                                    dollypk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    pk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    pk2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    pk3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = pk.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    pk.updateGroup(G)
                                    Ticket = pk.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        pk.kickoutFromGroup(op.param1,[op.param2])
                                        pk.inviteIntoGroup(op.param1,[op.param3])
                                        dollypk.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            pk2.kickoutFromGroup(op.param1,[op.param2])
                                            pk2.inviteIntoGroup(op.param1,[op.param3])
                                            dollypk.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        pk2.kickoutFromGroup(op.param1,[op.param2])
                        pk2.inviteIntoGroup(op.param1,[op.param3])
                        pk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            pk3.kickoutFromGroup(op.param1,[op.param2])
                            pk3.inviteIntoGroup(op.param1,[op.param3])
                            pk.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                dollypk.kickoutFromGroup(op.param1,[op.param2])
                                dollypk.inviteIntoGroup(op.param1,[op.param3])
                                pk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = pk2.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    pk2.kickoutFromGroup(op.param1,[op.param2])
                                    pk2.updateGroup(G)
                                    Ticket = pk2.reissueGroupTicket(op.param1)
                                    dollypk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    pk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    pk2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    pk3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = pk2.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    pk2.updateGroup(G)
                                    Ticket = pk2.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        pk2.kickoutFromGroup(op.param1,[op.param2])
                                        pk2.inviteIntoGroup(op.param1,[op.param3])
                                        pk.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            pk3.kickoutFromGroup(op.param1,[op.param2])
                                            pk3.inviteIntoGroup(op.param1,[op.param3])
                                            pk.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        pk3.kickoutFromGroup(op.param1,[op.param2])
                        pk3.inviteIntoGroup(op.param1,[op.param3])
                        pk2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            dollypk.kickoutFromGroup(op.param1,[op.param2])
                            dollypk.inviteIntoGroup(op.param1,[op.param3])
                            pk2.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                pk.kickoutFromGroup(op.param1,[op.param2])
                                pk.inviteIntoGroup(op.param1,[op.param3])
                                pk2.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = pk3.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    pk3.kickoutFromGroup(op.param1,[op.param2])
                                    pk3.updateGroup(G)
                                    Ticket = pk3.reissueGroupTicket(op.param1)
                                    dollypk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    pk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    pk2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    pk3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = pk3.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    pk3.updateGroup(G)
                                    Ticket = pk3.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        pk.kickoutFromGroup(op.param1,[op.param2])
                                        pk.inviteIntoGroup(op.param1,[op.param3])
                                        pk2.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            pk3.kickoutFromGroup(op.param1,[op.param2])
                                            pk3.inviteIntoGroup(op.param1,[op.param3])
                                            pk2.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        dollypk.kickoutFromGroup(op.param1,[op.param2])
                        dollypk.inviteIntoGroup(op.param1,[op.param3])
                        pk3.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            pk.kickoutFromGroup(op.param1,[op.param2])
                            pk.inviteIntoGroup(op.param1,[op.param3])
                            pk3.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                pk2.kickoutFromGroup(op.param1,[op.param2])
                                pk2.inviteIntoGroup(op.param1,[op.param3])
                                pk3.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = dollypk.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    dollypk.kickoutFromGroup(op.param1,[op.param2])
                                    dollypk.updateGroup(G)
                                    Ticket = dollypk.reissueGroupTicket(op.param1)
                                    dollypk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    pk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    pk2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    pk3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = dollypk.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    dollypk.updateGroup(G)
                                    Ticket = dollypk.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        dollypk.kickoutFromGroup(op.param1,[op.param2])
                                        dollypk.inviteIntoGroup(op.param1,[op.param3])
                                        pk3.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            pk.kickoutFromGroup(op.param1,[op.param2])
                                            pk.inviteIntoGroup(op.param1,[op.param3])
                                            pk3.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        dollypk.kickoutFromGroup(op.param1,[op.param2])
                        dollypk.findAndAddContactsByMid(op.param1,admin)
                        dollypk.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            pk.kickoutFromGroup(op.param1,[op.param2])
                            pk.findAndAddContactsByMid(op.param1,admin)
                            pk.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                pk2.kickoutFromGroup(op.param1,[op.param2])
                                pk2.findAndAddContactsByMid(op.param1,admin)
                                pk2.inviteIntoGroup(op.param1,admin)
                            except:
                                pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        pk.kickoutFromGroup(op.param1,[op.param2])
                        pk.findAndAddContactsByMid(op.param1,staff)
                        pk.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            pk2.kickoutFromGroup(op.param1,[op.param2])
                            pk2.findAndAddContactsByMid(op.param1,staff)
                            pk2.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                pk3.kickoutFromGroup(op.param1,[op.param2])
                                pk3.findAndAddContactsByMid(op.param1,staff)
                                pk3.inviteIntoGroup(op.param1,staff)
                            except:
                                pass

                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["ARreadPoint"]:
                   if op.param2 in Setmain["ARreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["ARreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = dollypk.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = dollypk.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        dollypk.sendImageWithURL(op.param1, image)                        
                        
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           dollypk.sendMessage(msg.to, wait["Respontag"])
                           dollypk.sendMessage(msg.to, None, contentMetadata={"STKID":"7839705","STKPKGID":"1192862","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           dollypk.mentiontag(msg.to,[msg._from])
                           dollypk.sendMessage(msg.to, "Jangan tag gw kena sepak lu")
                           dollypk.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    dollypk.sendMessage(msg.to,"γCek ID Stickerγ\nβͺSTKID : " + msg.contentMetadata["STKID"] + "\nβͺSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nβͺSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\nγLink Stickerγ" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    dollypk.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = dollypk.getContact(msg.contentMetadata["mid"])
                        path = dollypk.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        dollypk.sendMessage(msg.to,"βͺNama : " + msg.contentMetadata["displayName"] + "\nβͺMID : " + msg.contentMetadata["mid"] + "\nβͺStatus Msg : " + contact.statusMessage + "\nβͺPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        dollypk.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    dollypk.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\nγLink Stickerγ" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    dollypk.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = dollypk.getContact(msg.contentMetadata["mid"])
                        path = dollypk.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        dollypk.sendMessage(msg.to,"βͺNama : " + msg.contentMetadata["displayName"] + "\nβͺMID : " + msg.contentMetadata["mid"] + "\nβͺStatus Msg : " + contact.statusMessage + "\nβͺPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        dollypk.sendImageWithURL(msg.to, image)
#==========ADD Bots====================
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        dollypk.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        dollypk.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        dollypk.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        dollypk.sendMessage(msg.to,"Contact itu bukan anggota bot Pkbot")
#===========ADD STAFF===================
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        dollypk.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        dollypk.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        dollypk.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        dollypk.sendMessage(msg.to,"Contact itu bukan staff")
#============ADD ADMIN================
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        dollypk.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        dollypk.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        dollypk.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        dollypk.sendMessage(msg.to,"Contact itu bukan admin")
#=============ADD BLACKLIST===========
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        dollypk.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        dollypk.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        dollypk.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        dollypk.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#==============TALKBAN=============
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        dollypk.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        dollypk.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        dollypk.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        dollypk.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#===========UPDATE FOTO================
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = dollypk.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            dollypk.sendMessage(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = dollypk.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     dollypk.updateGroupPicture(msg.to, path)
                     dollypk.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["ARfoto"]:
                            path = dollypk.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][mid]
                            dollypk.updateProfilePicture(path)
                            dollypk.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["ARfoto"]:
                            path = pk.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Amid]
                            pk.updateProfilePicture(path)
                            pk.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["ARfoto"]:
                            path = pk2.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Bmid]
                            pk2.updateProfilePicture(path)
                            pk2.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["ARfoto"]:
                            path = pk3.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Cmid]
                            pk3.updateProfilePicture(path)
                            pk3.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Zmid in Setmain["ARfoto"]:
                            path = pkjs.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Zmid]
                            pkjs.updateProfilePicture(path)
                            pkjs.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = pk.downloadObjectMsg(msg_id)
                     path2 = pk2.downloadObjectMsg(msg_id)
                     path3 = pk3.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     pk.updateProfilePicture(path1)
                     pk.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     pk2.updateProfilePicture(path2)
                     pk2.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     pk3.updateProfilePicture(path3)
                     pk3.sendMessage(msg.to, "Berhasil mengubah foto profile bot")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        dollypk.sendChatChecked(msg.to, msg_id)
                        pk.sendChatChecked(msg.to, msg_id)
                        pk2.sendChatChecked(msg.to, msg_id)
                        pk3.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               dollypk.sendMessage(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                dollypk.sendMessage(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                dollypk.sendMessage(msg.to, "Selfbot dinonaktifkan")
                                            
                        elif cmd == "helpbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage2 = helppro()
                               dollypk.sendMessage(msg.to, str(helpMessage2))
                                            
                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               dollypk.sendMessage(msg.to, str(helpMessage1))

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "   βπ.πΒ°πππΌπππππα΄ΎΚ³α΅α΅α΅αΆα΅β\n"
                                if wait["sticker"] == True: md+="βͺSticker β\n"
                                else: md+="βͺSticker β\n"
                                if wait["contact"] == True: md+="βͺ Contact β\n"
                                else: md+="βͺ Contactβ\n"
                                if wait["talkban"] == True: md+="βͺ Talkban β\n"
                                else: md+="βͺ Talkban β\n"
                                if wait["Mentionkick"] == True: md+="βͺ Notag β\n"
                                else: md+="βͺ Notag β\n"
                                if wait["detectMention"] == True: md+="βͺ Respon β\n"
                                else: md+="βͺ Respon β\n"
                                if wait["autoJoin"] == True: md+="βͺAutojoin β\n"
                                else: md+="βͺAutojoin β\n"
                                if wait["autoAdd"] == True: md+="βͺAutoadd β\n"
                                else: md+="βͺAutoadd β\n"
                                if msg.to in welcome: md+="βͺWelcome β\n"
                                else: md+="βͺWelcome β\n"
                                if wait["autoLeave"] == True: md+="βͺAutoleave β\n"
                                else: md+="βͺAutoleave β\n"
                                if msg.to in protectqr: md+="βͺ Protecturl β\n"
                                else: md+="βͺ Protecturl β\n"
                                if msg.to in protectjoin: md+="βͺ Protectjoin β\n"
                                else: md+="βͺ Protectjoin β\n"
                                if msg.to in protectkick: md+="βͺ Protectkick β\n"
                                else: md+="βͺ Protectkick β\n"
                                if msg.to in protectcancel: md+="βͺ Protectcancel β\n"
                                else: md+="βͺ Protectcancel β\n"
                                if msg.to in protectinvite: md+="βͺ Protectinvite β\n"
                                else: md+="βͺ Protectinvite β\n"
                                if msg.to in protectantijs: md+="βͺ Antijs β\n"
                                else: md+="βͺ Antijs β\n"  
                                if msg.to in ghost: md+="βͺ Ghost β\n"
                                else: md+="βͺ Ghost β\n"                                   
                                dollypk.sendMessage(msg.to, md+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "creator" or text.lower() == 'owner':
                            if msg._from in admin:
                               dollypk.sendMessage(msg.to, "Ni Creator kami yang receh nya minta ampun")
                               dollypk.sendContact(to, "u3a4cc9a5d0da4077d7dc6cd4f405517c")

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                               dollypk.sendMessage(msg.to, "       π.π πππππ½πππ \nβͺProtect Bots\nβͺVersion Lupa\nβͺTeam=π.π πππΌππ½πππ\nβͺCreator=ππ§π­ππ«ππ¬[ππ¨π₯π₯π²]\n\n       Supported by:\nβ’Aki Devan\nβ’Ben \nβ’IGO \nβ’ELFOX\nβ’πππ πππ¦π’π₯π² Ibal & Friend\nβ’Β°β’α΄ΚΙͺα΄β’GRIND KILLER\nβ’βπ±πππ πππππππβ\n\n         π.π_π½πππ  2020\n")
                               dollypk.sendMessage(msg.to, "Info Bot Silahkan Chat Admin")
                               dollypk.sendContact(to, "u3a4cc9a5d0da4077d7dc6cd4f405517c")
                               dollypk.sendContact(to, "u8ac815b1df367a956f5fa81b29a3c73d")

                        elif text.lower() == "mid":
                               dollypk.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = dollypk.getContact(key1)
                               dollypk.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               dollypk.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = dollypk.getContact(key1)
                               dollypk.sendMessage(msg.to, "βͺNama : "+str(mi.displayName)+"\nβͺMid : " +key1+"\nβͺStatus Msg"+str(mi.statusMessage))
                               dollypk.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(dollypk.getContact(key1)):
                                   dollypk.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   dollypk.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   dollypk.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   pk.removeAllMessages(op.param2)
                                   pk2.removeAllMessages(op.param2)
                                   pk3.removeAllMessages(op.param2)
                                   pkjs.removeAllMessages(op.param2)
                                   dollypk.sendMessage(msg.to,"done ")
                               except:
                                   pass

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = dollypk.getGroupIdsJoined()
                               for group in saya:
                                   dollypk.sendMessage(group,"ΚΚα΄α΄α΄α΄α΄κ±α΄ ΚΚ\n       π.πΒ°π½πππ\n" + str(pesan))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               dollypk.sendMessage(msg.to, "γMykeyγ\nSetkey bot muγ " + str(Setmain["keyCommand"]) + " γ")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   dollypk.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   dollypk.sendMessage(msg.to, "γSetkeyγ\nSetkey diganti jadiγ{}γ".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               dollypk.sendMessage(msg.to, "γSetkeyγ\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               dollypk.sendMessage(msg.to, "βͺSabar nyet agak lama\nBot receh soal nya")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               dollypk.sendMessage(msg.to, "done jangan bawa war\nLimit ntar π±")
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               dollypk.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = dollypk.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(dollypk.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                dollypk.sendMessage(msg.to, "γ π.πΒ°ππππα΄ΎΚ³α΅α΅α΅αΆα΅ γGrup Info\n\nNama Group : {}".format(G.name)+ "\nβͺID Group : {}".format(G.id)+ "\nβͺPembuat : {}".format(G.creator.displayName)+ "\nβͺWaktu Dibuat : {}".format(str(timeCreated))+ "\nβͺJumlah Member : {}".format(str(len(G.members)))+ "\nβͺJumlah Pending : {}".format(gPending)+ "\nβͺGroup Qr : {}".format(gQr)+ "\nβͺGroup Ticket : {}".format(gTicket))
                                dollypk.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                dollypk.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                dollypk.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = dollypk.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = dollypk.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(dollypk.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "βͺγ π.πΒ°ππππα΄ΎΚ³α΅α΅α΅αΆα΅γ Grup Info\n"
                                ret_ += "\nβͺNama Group : {}".format(G.name)
                                ret_ += "\nβͺID Group : {}".format(G.id)
                                ret_ += "\nβͺPembuat : {}".format(gCreator)
                                ret_ += "\nβͺWaktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\nβͺJumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\nβͺJumlah Pending : {}".format(gPending)
                                ret_ += "\nβͺGroup Qr : {}".format(gQr)
                                ret_ += "\nβͺGroup Ticket : {}".format(gTicket)
                                ret_ += ""
                                dollypk.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = dollypk.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = dollypk.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "βͺ"+ str(no) + ". " + mem.displayName
                                dollypk.sendMessage(to,"βͺGroup Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\nγTotal %i Membersγ" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = dollypk.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = dollypk.getGroup(i)
                                if ginfo == group:
                                    pk.leaveGroup(i)
                                    pk2.leaveGroup(i)
                                    pk3.leaveGroup(i)
                                    dollypk.sendMessage(msg.to,"βͺBerhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "fiendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = dollypk.getAllContactIds()
                               for i in gid:
                                   G = dollypk.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "β  " + str(a) + ". " +G.displayName+ "\n"
                               dollypk.sendMessage(msg.to,"βββ[ FRIEND LIST ]\nβ\n"+ma+"β\nβββ[ Totalγ"+str(len(gid))+"γFriends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = dollypk.getGroupIdsJoined()
                               for i in gid:
                                   G = dollypk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "β  " + str(a) + ". " +G.name+ "\n"
                               dollypk.sendMessage(msg.to,"βββ[ GROUP LIST ]\nβ\n"+ma+"β\nβββ[ Totalγ"+str(len(gid))+"γGroups ]")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = dollypk.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   dollypk.updateGroup(X)
                                   dollypk.sendMessage(msg.to, "βͺUrl Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = dollypk.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   dollypk.updateGroup(X)
                                   dollypk.sendMessage(msg.to, "βͺUrl Closed")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = dollypk.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      dollypk.updateGroup(x)
                                   gurl = dollypk.reissueGroupTicket(msg.to)
                                   dollypk.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                dollypk.sendMessage(msg.to,"βͺKirim fotonya")

                        elif cmd == "allup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                dollypk.sendMessage(msg.to,"βͺKirim fotonya")
                                
                        elif cmd == "pkup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ARfoto"][mid] = True
                                dollypk.sendMessage(msg.to,"βͺKirim fotonya ")
                                
                        elif cmd == "pk1up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Amid] = True
                                pk.sendMessage(msg.to,"βͺKirim fotonya ")
                                
                        elif cmd == "pk2up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Bmid] = True
                                pk2.sendMessage(msg.to,"βͺKirim fotonya ")
                                
                        elif cmd == "pk3up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Cmid] = True
                                pk3.sendMessage(msg.to,"βͺKirim fotonya ")
                                
                        elif cmd == "jsup":
                            if msg._from in admin:
                                Setmain["ARfoto"][Zmid] = True
                                pkjs.sendMessage(msg.to,"βͺKirim fotonya ")

                        elif cmd.startswith("name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = dollypk.getProfile()
                                profile.displayName = string
                                dollypk.updateProfile(profile)
                                dollypk.sendMessage(msg.to,"βͺNama diganti jadi " + string + "")

                        elif cmd.startswith("pk1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = pk.getProfile()
                                profile.displayName = string
                                pk.updateProfile(profile)
                                pk.sendMessage(msg.to,"βͺNama diganti jadi " + string + "")

                        elif cmd.startswith("pk2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = pk2.getProfile()
                                profile.displayName = string
                                pk2.updateProfile(profile)
                                pk2.sendMessage(msg.to,"βͺNama diganti jadi " + string + "")

                        elif cmd.startswith("pk3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = pk3.getProfile()
                                profile.displayName = string
                                pk3.updateProfile(profile)
                                pk3.sendMessage(msg.to,"βͺNama diganti jadi " + string + "")

                        elif cmd.startswith("jsname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = pkjs.getProfile()
                                profile.displayName = string
                                pkjs.updateProfile(profile)
                                pkjs.sendMessage(msg.to,"βͺNama diganti jadi " + string + "")

#==============CMD List============================#

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +dollypk.getContact(m_id).displayName + "\n"
                                dollypk.sendMessage(msg.to,"βͺγ π.πΒ°ππππα΄ΎΚ³α΅α΅α΅αΆα΅γ\n\n"+ma+"\nTotalγ%sγ Bots" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +dollypk.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +dollypk.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +dollypk.getContact(m_id).displayName + "\n"
                                dollypk.sendMessage(msg.to,"βͺList ADMIN \n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotalγ%sγγπ.πΒ°ππππα΄ΎΚ³α΅α΅α΅αΆα΅ γ " %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +dollypk.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +dollypk.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +dollypk.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +dollypk.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +dollypk.getGroup(group).name + "\n"
                                dollypk.sendMessage(msg.to,"βͺList Protect\n\nβͺPROTECT URL :\n"+ma+"\nβͺPROTECT KICK :\n"+mb+"\nβͺPROTECT JOIN :\n"+md+"\nβͺPROTECT INVITE:\n"+md+"\nβͺPROTECT CANCEL:\n"+mc+"\nTotalγ%sγβͺGrup " %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel))))

                        elif cmd == "rname":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                pk.sendMessage(msg.to,responsename1)
                                pk2.sendMessage(msg.to,responsename2)
                                pk3.sendMessage(msg.to,responsename3)

#==============PROTECT===================
                        elif cmd == "invitebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Bmid,Cmid,Amid]
                                    dollypk.inviteIntoGroup(msg.to, anggota)
                                    pk2.acceptGroupInvitation(msg.to)
                                    pk3.acceptGroupInvitation(msg.to)
                                    pk.acceptGroupInvitation(msg.to)
                                except:
                                    pass
                                
                        elif cmd == "ajs stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = dollypk.getGroup(msg.to)
                                    dollypk.inviteIntoGroup(msg.to, [Zmid])
                                    dollypk.sendMessage(msg.to,"βͺGrup "+str(ginfo.name)+"Kami amanin")
                                except:
                                    pass
    
                        elif cmd == "pk in":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = dollypk.getGroup(msg.to)
                                ginfo = dollypk.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                dollypk.updateGroup(G)
                                invsend = 0
                                Ticket = dollypk.reissueGroupTicket(msg.to)
                                pk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                pk2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                pk3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = pk3.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                pk3.updateGroup(G)
                                pk.sendMessage(msg.to,"Bot1 Stay")
                                pk2.sendMessage(msg.to,"Bot2 Stay")
                                pk3.sendMessage(msg.to," Bot3 Stay")
                                pkjs.sendMessage(msg.to,"ajs Stay")
                                dollypk.sendMessage(msg.to,"Stay sambil anu")

                        elif cmd == "pk out":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = dollypk.getGroup(msg.to)
                                pk.sendMessage(msg.to, "Pamit Dulu penting Chat Admin\n "+str(G.name))
                                pk.sendContact(to, "u3a4cc9a5d0da4077d7dc6cd4f405517c")
                                pk.sendContact(to, "ue0730b00558542cf28a9256e57b308cc")
                                pk.leaveGroup(msg.to)
                                pk2.leaveGroup(msg.to)
                                pk3.leaveGroup(msg.to)
                                
                        elif cmd == "byeme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = dollypk.getGroup(msg.to)
                                dollypk.sendMessage(msg.to, "Bye bye fams "+str(G.name))
                                dollypk.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = dollypk.getGroupIdsJoined()
                                for i in gid:
                                    h = dollypk.getGroup(i).name
                                    if h == ng:
                                        pk.sendMessage(i, "Invite kalau di butuhkan lagi")
                                        pk.leaveGroup(i)
                                        pk2.leaveGroup(i)
                                        pk3.leaveGroup(i)
                                        dollypk.sendMessage(to,"Berhasil keluar dari grup " +h)

                        elif cmd == "pk1":
                            if msg._from in admin:
                                G = dollypk.getGroup(msg.to)
                                ginfo = dollypk.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                dollypk.updateGroup(G)
                                invsend = 0
                                Ticket = dollypk.reissueGroupTicket(msg.to)
                                pk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = pk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                pk.updateGroup(G)

                        elif cmd == "pk2":
                            if msg._from in admin:
                                G = dollypk.getGroup(msg.to)
                                ginfo = dollypk.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                dollypk.updateGroup(G)
                                invsend = 0
                                Ticket = dollypk.reissueGroupTicket(msg.to)
                                pk2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = pk2.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                pk2.updateGroup(G)

                        elif cmd == "pk3":
                            if msg._from in admin:
                                G = dollypk.getGroup(msg.to)
                                ginfo = dollypk.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                dollypk.updateGroup(G)
                                invsend = 0
                                Ticket = dollypk.reissueGroupTicket(msg.to)
                                pk3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = pk3.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                pk3.updateGroup(G)

                        elif cmd == "ajs join":
                            if msg._from in admin:
                                G = dollypk.getGroup(msg.to)
                                ginfo = dollypk.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                dollypk.updateGroup(G)
                                invsend = 0
                                Ticket = dollypk.reissueGroupTicket(msg.to)
                                pkjs.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = pkjs.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                pkjs.updateGroup(G)

                        elif cmd == "ajs bye":
                            if msg._from in admin:
                                G = dollypk.getGroup(msg.to)
                                pkjs.leaveGroup(msg.to)

                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = dollypk.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = dollypk.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = dollypk.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                dollypk.sendMessage(msg.to, "βͺπ.πΒ°α΄ΎΚ³α΅α΅α΅αΆα΅ \nRespon\n\n  βͺγ Get Profileγ\n   %.10f\n βͺγGet Contactγ\n   %.10f\n βͺγGet Groupγ\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif text.lower() == 'speed':
                        	if msg._from in admin:
                                 start = time.time()
                                 dollypk.sendMessage(to, "βͺLumayan Buat mainan")
                                 elapsed_time = time.time() - start
                                 dollypk.sendMessage(to,format(str(elapsed_time)))

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['ARreadPoint'][msg.to] = msg_id
                                 Setmain['ARreadMember'][msg.to] = {}
                                 dollypk.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                           
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['ARreadPoint'][msg.to]
                                 del Setmain['ARreadMember'][msg.to]
                                 dollypk.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['ARreadPoint']:
                                if Setmain['ARreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['ARreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(dollypk.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        dollypk.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['ARreadPoint'][msg.to]
                                        del Setmain['ARreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['ARreadPoint'][msg.to] = msg.id
                                    Setmain['ARreadMember'][msg.to] = {}
                                else:
                                    dollypk.sendMessage(msg.to, "User kosong...")
                            else:
                                dollypk.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  dollypk.sendMessage(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  dollypk.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  dollypk.sendMessage(msg.to, "Sudak tidak aktif")

                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = dollypk.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  dollypk.sendMessage(msg.to, "γDiaktifkanγ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = dollypk.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    dollypk.sendMessage(msg.to, "γDinonaktifkanγ\n" + msgs)

                        elif 'Protecturl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = dollypk.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  dollypk.sendMessage(msg.to, "γDiaktifkanγ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = dollypk.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    dollypk.sendMessage(msg.to, "γDinonaktifkanγ\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = dollypk.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  dollypk.sendMessage(msg.to, "γDiaktifkanγ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = dollypk.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    dollypk.sendMessage(msg.to, "γDinonaktifkanγ\n" + msgs)

                        elif 'protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = dollypk.getGroup(msg.to)
                                       msgs = "Protect invite diaktifkan\nDi Group : " +str(ginfo.name)
                                  dollypk.sendMessage(msg.to, "γDiaktifkanγ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = dollypk.getGroup(msg.to)
                                         msgs = "Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    dollypk.sendMessage(msg.to, "γDinonaktifkanγ\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = dollypk.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  dollypk.sendMessage(msg.to, "γDiaktifkanγ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = dollypk.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    dollypk.sendMessage(msg.to, "γDinonaktifkanγ\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = dollypk.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  dollypk.sendMessage(msg.to, "γDiaktifkanγ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = dollypk.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    dollypk.sendMessage(msg.to, "γDinonaktifkanγ\n" + msgs)

                        elif 'Antijs ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Antijs ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "Anti JS sudah aktif"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = dollypk.getGroup(msg.to)
                                       msgs = "Anti JS Diaktifkan\nDi Group : " +str(ginfo.name)
                                  dollypk.sendMessage(msg.to, "γDiaktifkanγ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = dollypk.getGroup(msg.to)
                                         msgs = "Anti JS Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Anti JS Sudah Tidak Aktif"
                                    dollypk.sendMessage(msg.to, "γDinonaktifkanγ\n" + msgs)
                                    
                        elif 'Ghost ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Ghost sudah aktif"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = dollypk.getGroup(msg.to)
                                       msgs = "Ghost Diaktifkan\nDi Group : " +str(ginfo.name)
                                  dollypk.sendMessage(msg.to, "γDiaktifkanγ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = dollypk.getGroup(msg.to)
                                         msgs = "Ghost Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost Sudah Tidak Aktif"
                                    dollypk.sendMessage(msg.to, "γDinonaktifkanγ\n" + msgs)                                    

                        elif 'allpro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('allpro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = dollypk.getGroup(msg.to)
                                      msgs = "βͺSemua protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = dollypk.getGroup(msg.to)
                                      msgs = "βͺBerhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  dollypk.sendMessage(msg.to, "γDiaktifkanγ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = dollypk.getGroup(msg.to)
                                         msgs = "βͺBerhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = dollypk.getGroup(msg.to)
                                         msgs = "βͺSemua protect sudah off\nDi Group : " +str(ginfo.name)
                                    dollypk.sendMessage(msg.to, "γDinonaktifkanγ\n" + msgs)

#==============KICK==================
                        elif ("jskick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = dollypk.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           dollypk.updateGroup(G)
                                           invsend = 0
                                           Ticket = dollypk.reissueGroupTicket(msg.to)
                                           pkjs.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           pkjs.kickoutFromGroup(msg.to, [target])
                                           pkjs.leaveGroup(msg.to)
                                           dollypk.inviteIntoGroup(msg.to, [Zmid])
                                           X = dollypk.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           dollypk.updateGroup(X)
                                       except:
                                           pass

                        elif ("pkkick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           dollypk.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           dollypk.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           dollypk.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Pkbot:
                                       try:
                                           admin.remove(target)
                                           dollypk.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Pkbot:
                                       try:
                                           staff.remove(target)
                                           dollypk.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Pkbot:
                                       try:
                                           Bots.remove(target)
                                           dollypk.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                dollypk.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "admin:repeat" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                dollypk.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                dollypk.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                dollypk.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                dollypk.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                dollypk.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                dollypk.sendMessage(msg.to,"Berhasil di Refresh...")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = dollypk.getContact(i)
                                    dollypk.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = dollypk.getContact(i)
                                    dollypk.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = dollypk.getContact(i)
                                    dollypk.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                dollypk.sendMessage(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                dollypk.sendMessage(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                dollypk.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                dollypk.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                dollypk.sendMessage(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                dollypk.sendMessage(msg.to,"Auto respon dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                dollypk.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                dollypk.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                dollypk.sendMessage(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                dollypk.sendMessage(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                dollypk.sendMessage(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                dollypk.sendMessage(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "read on" or text.lower() == 'autoread on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = True
                                dollypk.sendMessage(msg.to,"Auto add diaktifkan")

                        elif cmd == "read off" or text.lower() == 'autoread off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = False
                                dollypk.sendMessage(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                dollypk.sendMessage(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                dollypk.sendMessage(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                dollypk.sendMessage(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                dollypk.sendMessage(msg.to,"Autojoin Tiket dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           dollypk.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           dollypk.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                dollypk.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                dollypk.sendMessage(msg.to,"Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           dollypk.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           dollypk.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                dollypk.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                dollypk.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                dollypk.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +dollypk.getContact(m_id).displayName + "\n"
                                dollypk.sendMessage(msg.to,"βͺBlacklist User\n\n"+ma+"\nTotalγ%sγBlacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                dollypk.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +dollypk.getContact(m_id).displayName + "\n"
                                dollypk.sendMessage(msg.to,"βͺTalkban User\n\n"+ma+"\nTotalγ%sγTalkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    dollypk.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = dollypk.getContact(i)
                                        dollypk.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = dollypk.getContacts(wait["blacklist"])
                              mc = "γ%iγUser Blacklist" % len(ragets)
                              dollypk.sendMessage(msg.to,"Sukses membersihkan " +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  dollypk.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  dollypk.sendMessage(msg.to, "γPesan Msgγ\nPesan Msg diganti jadi :\n\nγ{}γ".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  dollypk.sendMessage(msg.to, "βͺGagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  dollypk.sendMessage(msg.to, "γWelcome Msgγ\nβͺWelcome Msg diganti jadi :\n\nγ{}γ".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  dollypk.sendMessage(msg.to, "βͺGagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  dollypk.sendMessage(msg.to, "γRespon Msgγ\nβͺRespon Msg diganti jadi :\n\nγ{}γ".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  dollypk.sendMessage(msg.to, "βͺGagal mengganti Spam")
                              else:
                                  Setmain["ARmessage1"] = spl
                                  dollypk.sendMessage(msg.to, "γSpam Msgγ\nβͺSpam Msg diganti jadi :\n\nγ{}γ".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  dollypk.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  dollypk.sendMessage(msg.to, "γSider Msgγ\nβͺSider Msg diganti jadi :\n\nγ{}γ".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               dollypk.sendMessage(msg.to, "γPesan Msgγ\nβͺPesan Msg mu :\n\nγ " + str(wait["message"]) + " γ")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               dollypk.sendMessage(msg.to, "γWelcome Msgγ\nβͺWelcome Msg mu :\n\nγ " + str(wait["welcome"]) + " γ")

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               dollypk.sendMessage(msg.to, "γRespon Msgγ\nβͺRespon Msg mu :\n\nγ " + str(wait["Respontag"]) + " γ")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               dollypk.sendMessage(msg.to, "γSpam Msgγ\nβͺSpam Msg mu :\n\nγ " + str(Setmain["ARmessage1"]) + " γ")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               dollypk.sendMessage(msg.to, "γSider Msgγ\nβͺSider Msg mu :\n\nγ " + str(wait["mention"]) + " γ")
                               
                        elif cmd == "pkrespon" or msg.text.lower == "respon":
                            if msg._from in admin:
                               dollypk.sendMessage(to,"π°π ππ«π π‘ππ«π, ππ§π ππ₯π°ππ²π¬ π°π’π₯π₯ ππ π‘ππ«π")
                               pk.sendMessage(to,"π°π ππ«π π‘ππ«π, ππ§π ππ₯π°ππ²π¬ π°π’π₯π₯ ππ π‘ππ«π")
                               pk2.sendMessage(to,"π°π ππ«π π‘ππ«π, ππ§π ππ₯π°ππ²π¬ π°π’π₯π₯ ππ π‘ππ«π")
                               pk3.sendMessage(to,"π°π ππ«π π‘ππ«π, ππ§π ππ₯π°ππ²π¬ π°π’π₯π₯ ππ π‘ππ«π")
                               pkjs.sendMessage(to,"π°π ππ«π π‘ππ«π, ππ§π ππ₯π°ππ²π¬ π°π’π₯π₯ ππ π‘ππ«π")
                               
                        elif cmd == "promo" or msg.text.lower == "order":
                      	  if msg._from in admin:
                       	    dollypk.sendMessage(to,"          π.π πππππ½πππ \n   βͺOpen Orderβͺ\n\nπΉοΈVPS CONOHA NON RENEW\n2 Core 1GB = 100k \n3 Core 2GB =200k\n4 Core 4GB = 360k \n\nπΉοΈVPS CONOHA RENEW\n2 Core 1GB =120k\n3 Core 2GB = 240k\n4 Core 4GB = 420k \n\nπΉοΈVPS LINODE \n1 Core 2GB = 50k \n2 Core 4GB = 100K \n4 Core 8GB = 200K \n6 Core 16GB = 350K\n\n            βͺOpen Orderβͺ\nβͺscript Bot cl = 200K\nβͺscript Selfbot only =150k\nβͺscript Self Template=400K\n         βͺOpen Sewa/Rentalβͺ\nβͺSewa Pro Go= 300k/7 Bot\nβͺNambah asis Pc aja\nβͺSewa pro python= Harga pc\nβͺSewa Protect Cl Bot= 25K/Bot\n\nβͺPembuatan Bot kuis=30K/Bulan\nSoal,Nick Bot Atas nama kalian\n\nβͺJasa Protect=50k/Room\nMenggunakan Pro Go[Golang] \n\nβͺToken primery 5k/token\nβͺ1 nomer 1 token\nβͺ Juga open gift tikel ya mslah harga selalu berubah\n\nminat ? tanya2? chat id di bawah\nline.me/ti/p/~mina59.")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = dollypk.findGroupByTicket(ticket_id)
                                     dollypk.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     dollypk.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group1 = pk.findGroupByTicket(ticket_id)
                                     pk.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     pk.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group2 = pk2.findGroupByTicket(ticket_id)
                                     pk2.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     pk2.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group3 = pk3.findGroupByTicket(ticket_id)
                                     pk3.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     pk3.sendMessage(msg.to, "Masuk : %s" % str(group.name))

    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
