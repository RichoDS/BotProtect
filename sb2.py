# -*- coding: utf-8 -*-
"""ððð ðððððð ððððððððððð"""
from line import *
from datetime import datetime, timedelta
from time import sleep
from threading import Thread
from multiprocessing import Pool,Process
from urllib.parse import urlencode
from shutil import copyfile
import subprocess as cmd
import platform
import requests, json
import LineService, Menu, time, signal, livejson, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
from Naked.toolshed.shell import execute_js 
from random import randint

""" START """

with open('tokenJs.json', 'r') as bolo:
     pin = json.load(bolo)
cl = LINE(pin['token1'])
pin['token1'] = cl.authToken
ka = LINE(pin['token2'])
pin['token2'] = ka.authToken

print ("\nãPikaBot Succes Run ")

linePoll = OEPoll(cl)

Amin = [cl,ka]
mid = cl.getProfile().mid
Amid = ka.getProfile().mid

Lea=["u59b46277260804a6df4223ff39359ac7","ubfadc54d7069d649efc84a11abb646eb","u2c3ea49bff7baadbded41e6892527fdb","u5f4bb402470b14b2d4f839a3bd5ec611"]

Bots=[mid,Amid]
Zie = Bots+Lea
botlist=[cl,ka]

mulai   = time.time()

Leakiller = livejson.File('settSB.json')
LiproSett = livejson.File('settSB.json')
wait = {"blacklist":{},"Member":[]}
cctv = {"cyduk":{},"point":{},"sidermem":{}}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def Rchat(self,to):
    self.removeAllMessages(op.param2)
    self.sendMessage(to,"done removed chat")
Smid = ["ubfadc54d7069d649efc84a11abb646eb"] # MID INI JANGAN DI GANTI ATAU DI BUANG !!!!!
def Res(self,to):
    self.sendMessage(to,"ðð²ð´ðª ððªð­ð²ð»")

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d D %02d H %02d M %02d S' % (days, hours, mins, secs)

def restartProgram():
	print ('##----- RUNNING BOT RESTARTED -----##')
	python = sys.executable
	os.execl(python, python, *sys.argv)

def command(text):
    pesan = text.lower()
    if pesan.startswith(Leakiller["keyCmd"]):
        cmd = pesan.replace(Leakiller["keyCmd"],"")
    else:
        cmd = "command"
    return cmd

def bot(op):
      try:
          global time
          global ast
          global groupParam
          global multiprocessing
          global subprocess
          global threading
          if op.type == 11:
            if op.param1 in Leakiller["proqr"]:
                if op.param2 in Zie or op.param2 in Leakiller["Bots"] or op.param2 in Leakiller["admin"]:pass
                else:
                    Z = cl.getCompactGroup(op.param1)
                    if Z.preventedJoinByTicket == False:
                        Z.preventedJoinByTicket = True
                        random.choice(Amin).updateGroup(Z)
                        random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                    else:
                        random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
  
            if op.param2 in wait["blacklist"]:
                G = cl.getCompactGroup(op.param1)
                if G.preventedJoinByTicket == False:
                    G.preventedJoinByTicket = True
                    random.choice(Amin).updateGroup(G)
                    random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                else:
                    random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])

          if op.type == 17:
                    for x in wait["blacklist"]:
                        random.choice(Amin).kickoutFromGroup(op.param1, [x])

          if op.type == 32:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in Zie and op.param2 not in Leakiller["Bots"] and op.param2 not in Leakiller["admin"]:
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                        except:pass
                else:pass

          if op.type == 32:
            if op.param3 in Zie or op.param3 in Leakiller["admin"] or op.param3 in Leakiller["Bots"]:
                if op.param2 not in Zie and op.param2 not in Leakiller["Bots"] and op.param2 not in Leakiller["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param3])
                        except:pass
                else:pass

          if op.type == 19:
            if Amid in op.param3:
                if op.param2 not in Zie and op.param2 not in Leakiller["Bots"] and op.param2 not in Leakiller["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        ka.acceptGroupInvitation(op.param1)
                    except:pass
                else:pass
                return

            if mid in op.param3:
                if op.param2 not in Zie and op.param2 not in Leakiller["Bots"] and op.param2 not in Leakiller["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:pass
                else:pass
                return
            if op.type == 19:
                if op.param3 in Lea:
                    if op.param2 not in Zie:
                        wait["blacklist"][op.param2] = True
                        try:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.findAndAddContactsByMid(op.param3)
                            ka.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                cl.findAndAddContactsByMid(op.param3)
                                cl.inviteIntoGroup(op.param1,[op.param3])
                            except:pass
                    else:pass
                    return

                if op.param3 in Leakiller["Bots"]:
                    if op.param2 not in Zie or op.param2 not in Leakiller["Bots"] or op.param2 not in Leakiller["admin"]:
                        wait["blacklist"][op.param2] = True
                        try:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                cl.inviteIntoGroup(op.param1,[op.param3])
                            except:pass
                    else:pass
                    return

                if op.param3 in Leakiller["admin"]:
                    if op.param2 not in Zie or op.param2 not in Leakiller["Bots"] or op.param2 not in Leakiller["admin"]:
                        wait["blacklist"][op.param2] = True
                        try:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.findAndAddContactsByMid(op.param3)
                            ka.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.findAndAddContactsByMid(op.param3)
                                kb.inviteIntoGroup(op.param1,[op.param3])
                            except:pass
                    else:pass
                    return

          if op.type == 0:
              return

          if op.type == 5:
            if Leakiller["autoAdd"] == True:
                if op.param2 not in Zie:
                    cl.findAndAddContactsByMid(op.param1)
                    if (Leakiller["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, Leakiller["message"])

          if op.type == 11:
            if op.param1 in Leakiller["intaPoint"]:
                if op.param2 in Zie and op.param2 in Leakiller["Bots"] and op.param2 not in Leakiller["admin"]:
                    pass
                else:
                    X = cl.getGroup(op.param1)
                    if X.preventedJoinByTicket == True:
                        pass
                    else:
                        cl.updateGroup(X)
                        invsend = 0
                        Ti = cl.reissueGroupTicket(op.param1)
                        ka.acceptGroupInvitationByTicket(op.param1,Ti)

          if op.type == 13:
            if mid in op.param3:
                if Leakiller["autoJoin"] == True:
                    if op.param2 not in Zie and op.param2 not in Leakiller["Bots"] and op.param2 not in Leakiller["admin"]:
                        cl.acceptGroupInvitation(op.param1)
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        if Leakiller["bypas"] == True:
                            cl.inviteIntoGroup(op.param1,Amid)
                            ka.acceptGroupInvitation(op.param1)
                            ran=[ka,cl]
                            dex=random.choice(ran)
                            x = cl.getGroup(op.param1)
                            if x.invitee == None:nama = []
                            else:nama = [contact.mid for contact in x.invitee]
                            target = []
                            for a in nama:
                              if a not in Lea and a not in Bots and a not in Leakiller["admin"] and a not in Leakiller["Bots"]:
                                  target.append(a)
                            cmd = 'bypass.js gid={} token={}'.format(op.param1, dek.authToken)
                            nami = [contact.mid for contact in x.members]
                            tarsih = []
                            for s in nami:
                              if s not in Lea and s not in Bots and s not in Leakiller["admin"] and s not in Leakiller["Bots"]:
                                  tarsih.append(s)
                            for y in target:
                                cmd += ' uid={}'.format(y)
                            for k in tarsih:
                                cmd += ' uid={}'.format(k)
                            success = execute_js(cmd)
                            
            if Amid in op.param3:
                if Leakiller["autoJoin"] == True:
                    if op.param2 not in Zie and op.param2 not in Leakiller["Bots"] and op.param2 not in Leakiller["admin"]:
                        ka.acceptGroupInvitation(op.param1)
                        ka.leaveGroup(op.param1)
                    else:
                        ka.acceptGroupInvitation(op.param1)
          if op.type == 13:
            if op.param1 in Leakiller["proInvite"]:
                if op.param2 in Zie or op.param2 in Leakiller["Bots"] or op.param2 in Leakiller["admin"]:
                    pass
                else:
                    try:
                        if op.param3 in Zie or op.param3 in Leakiller["Bots"] or op.param3 in Leakiller["admin"]:
                            pass
                        else:
                            if op.param2 not in Zie and op.param2 not in Leakiller["Bots"] and op.param2 not in Leakiller["admin"]:
                                wait["blacklist"][op.param2] = True
                                anu = cl.getCompactGroup(op.param1)
                                if anu.invitee is not None:
                                    pipo = [a.mid for a in anu.invitee]
                                    for target in pipo:
                                      if target in op.param3 and target not in Zie and target not in Leakiller["Bots"] and target not in Leakiller["admin"]:
                                        wait["blacklist"][target] = True
                                        random.choice(botlist).cancelGroupInvitation(op.param1,[target])
                                        random.choice(botlist).kickoutFromGroup(op.param1,[target])
                                    random.choice(botlist).kickoutFromGroup(op.param1,[op.param2])
                            else:pass
                    except:
                        pass
            else:
                if op.param3 in Zie or op.param3 in Leakiller["Bots"] or op.param3 in Leakiller["admin"]:pass
                else:
                    inv1 = op.param3.replace('\x1e',',')
                    inv2 = inv1.split(',')
                    for i in inv2:
                      if i in wait["blacklist"]:
                        try:
                            ka.cancelGroupInvitation(op.param1,[i])
                        except:
                            try:
                                cl.cancelGroupInvitation(op.param1,[i])
                            except:pass
                        try:
                            if op.param2 not in Zie and op.param2 not in Leakiller["Bots"] and op.param2 not in Leakiller["admin"]:
                                wait["blacklist"][op.param2] = True
                                for i in botlist:
                                    i.kickoutFromGroup(op.param1,[op.param2])
                        except:pass
                if op.param2 not in wait["blacklist"]:pass
                else:
                    inv1 = op.param3.replace('\x1e',',')
                    inv2 = inv1.split(',')
                    for i in inv2:
                        wait["blacklist"][i] = True
                        try:
                            ka.cancelGroupInvitation(op.param1,[i])
                        except:
                            try:
                                cl.cancelGroupInvitation(op.param1,[i])
                            except:pass
                        try:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

          if op.type == 15:
            if op.param1 in Leakiller["leaveMsg"]:
                if op.param2 not in Zie and op.param2 not in Leakiller["admin"] and op.param2 not in Leakiller["Bots"]:
                    return
                else:
                    cl.sendMessage(op.param1, Leakiller["leftmsg"])

          if op.type == 17:
            if op.param1 in Leakiller["welcome"]:
                if op.param2 in Zie or op.param2 in Leakiller["Bots"] or op.param2 in Leakiller["admin"]:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

          if op.type == 19:
            if op.param1 in Leakiller["proKick"]:
                if op.param2 in Zie or op.param2 in Leakiller["Bots"] or op.param2 in Leakiller["admin"]:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                        except:pass
                    try:
                        if op.param2 not in Zie and op.param2 not in Leakiller["Bots"] and op.param2 not in Leakiller["admin"]:
                            wait["blacklist"][op.param2] = True
                            if op.param3 not in wait["blacklist"]:
                                try:
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                    except:pass
                                try:
                                    ka.findAndAddContactsByMid(op.param3)
                                    time.sleep(3)
                                    ka.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(op.param3)
                                        time.sleep(3)
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                    except:pass
                            else:pass
                        else:pass
                    except:pass

          if op.type == 32:
            if op.param1 in Leakiller["proCancel"]:
                if op.param2 in Zie or op.param2 in Leakiller["Bots"] or op.param2 in Leakiller["admin"]:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                        except:pass
                    try:
                        if op.param2 not in Zie and op.param2 not in Leakiller["Bots"] and op.param2 not in Leakiller["admin"]:
                            wait["blacklist"][op.param2] = True
                            if op.param3 not in wait["blacklist"]:
                                try:
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                    except:pass
                                try:
                                    ka.findAndAddContactsByMid(op.param3)
                                    time.sleep(3)
                                    ka.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(op.param3)
                                        time.sleep(3)
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                    except:pass
                            else:pass
                        else:pass
                    except:pass
          if op.type == 55:
            try:
                if op.param1 in Leakiller["readPoint"]:
                   if op.param2 in Leakiller["readMember"][op.param1]:pass
                   else:Leakiller["readMember"][op.param1][op.param2] = True
                else:pass
            except:pass


          if op.type in [25,26]:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            keyt = Leakiller["keyCmd"]
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if Leakiller["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"âââââââââââââââ\nâ â¢â²á´Êá´á´á´ sá´Éªá´á´á´Êâ³\nâ â¢ sá´á´Éªá´ : " + msg.contentMetadata["STKID"] +"\nâ â¢ sá´á´á´á´É¢Éªá´ : " + msg.contentMetadata["STKPKGID"] + "\nâ â¢ sá´á´á´ á´Ê : " + msg.contentMetadata["STKVER"] + "\nâ â¢ " + "line://shop/detail/" + msg.contentMetadata["STKPKGID"] +"\nâââââââââââââââ")
               if msg.contentType == 13:
                 if Leakiller["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"âââââââââââââââ\nâ â¢ É´á´á´á´ : " + msg.contentMetadata["displayName"] + "\nâ â¢ á´Éªá´ : " + msg.contentMetadata["mid"] + "\nâ â¢ sá´á´á´á´s : " + contact.statusMessage + "\nâ â¢ á´Éªá´á´á´Êá´ á´ÊÊ : http://dl.profile.line-cdn.net/" + contact.pictureStatus + "\nâââââââââââââââ")
                        cl.sendImageWithURL(msg.to, image)

               if msg.contentType == 13:
                 if msg._from in Lea:
                  if Leakiller["abots"] == True:
                    if msg.contentMetadata["mid"] in Leakiller["Bots"]:
                        cl.sendMessage(msg.to,"á´¡á´s Êá´á´ ÒÊÉªá´É´á´")
                    else:
                        Leakiller["Bots"][msg.contentMetadata["mid"]] = True
                        cl.sendMessage(msg.to,"sá´á´á´á´s á´á´á´ Êá´á´s")
                 if Leakiller["dbots"] == True:
                    if msg.contentMetadata["mid"] in Leakiller["Bots"]:
                        del Leakiller["Bots"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"sá´á´á´á´s Êá´á´á´á´ á´ Êá´á´s")
                    else:
                        cl.sendMessage(msg.to,"á´á´É´á´á´á´á´ É´á´á´ ÉªÉ´ ÊÉªsá´ Êá´á´s")
                 if msg._from in Lea:
                  if Leakiller["addadmin"] == True:
                    if msg.contentMetadata["mid"] in Leakiller["admin"]:
                        cl.sendMessage(msg.to,"á´¡á´s á´á´á´ÉªÉ´")
                    else:
                        Leakiller["admin"][msg.contentMetadata["mid"]] = True
                        cl.sendMessage(msg.to,"sá´á´á´á´s á´á´á´ á´á´á´ÉªÉ´")
                 if Leakiller["deladmin"] == True:
                    if msg.contentMetadata["mid"] in Leakiller["admin"]:
                        del Leakiller["admin"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"sá´á´á´á´s Êá´á´á´á´ á´ á´á´á´ÉªÉ´")
                    else:
                        cl.sendMessage(msg.to,"á´á´É´á´á´á´á´ É´á´á´ ÉªÉ´ ÊÉªsá´ á´á´á´ÉªÉ´")
                 if msg._from in Lea:
                  if Leakiller["ablacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"á´¡á´s ÊÊá´á´á´ÊÉªsá´")
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        cl.sendMessage(msg.to,"sá´á´á´á´s á´á´á´ ÉªÉ´ ÊÊá´á´á´ÊÉªsá´")
                 if Leakiller["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"sá´á´á´á´s Êá´á´á´á´ á´ ÊÊá´á´á´ÊÉªsá´")
                    else:
                        cl.sendMessage(msg.to,"á´á´É´á´á´á´á´ É´á´á´ ÉªÉ´ ÊÊá´á´á´ÊÉªsá´")

               if msg.toType == 2:
                 if msg._from in Lea:
                   if Leakiller["gPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     Leakiller["gPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "sá´á´á´á´s á´á´á´á´á´á´ É¢Êá´á´á´ á´Éªá´á´á´á´á´")

               if msg.contentType == 1:
                       if msg._from in Lea:
                           if Leakiller["DPicture"] == True:
                               for cc in [cl,ka]:
                                   path = cc.downloadObjectMsg(msg_id)
                                   Leakiller["DPicture"] = False
                                   cc.updateProfilePicture(path)
                                   cc.sendMessage(msg.to, "sá´á´á´á´s á´Êá´É´É¢á´ á´Éªsá´Êá´Ê á´Éªá´á´á´Êá´")

               if msg.contentType == 1:
                 if msg._from in Lea:
                   if mid in Leakiller["cPicture"]:
                     path = cl.downloadObjectMsg(msg_id)
                     del Leakiller["cPicture"][mid]
                     cl.updateProfilePicture(path)
                     cl.sendMessage(msg.to,"sá´á´á´á´s á´á´á´á´á´á´ á´Éªsá´Êá´Ê á´Éªá´á´á´Êá´")
                   if Amid in Leakiller["cPicture"]:
                     path1 = ka.downloadObjectMsg(msg_id)
                     del Leakiller["cPicture"][Amid]
                     ka.updateProfilePicture(path1)
                     ka.sendMessage(msg.to,"sá´á´á´á´s á´á´á´á´á´á´ á´Éªsá´Êá´Ê á´Éªá´á´á´Êá´")

               if msg.contentType == 0:
                    if Leakiller["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        commandM = command(text)
                        commandM = commandM.strip()

                    for cmd in commandM.split('.'):
                        if msg._from in Lea:
                            if cmd.startswith("1run "):
                                cust = cmd.split("1run ")[1]
                                os.system('nohup python3 %s.py jp &'%cust)
                                cl.sendMessage(msg.to, "Êá´É´É´ÉªÉ´É¢ á´Êá´á´á´á´á´ {} sá´á´á´á´ss".format(cust))
                            elif cmd.startswith("1kill "):
                               cust = cmd.split("1kill ")[1]
                               try:
                                   p = subprocess.Popen(['ps', 'ax'], stdout=subprocess.PIPE)
                                   out, err = p.communicate()
                                   for line in out.splitlines():
                                       if '%s.py'%cust in line.decode("utf-8"):
                                           pid = int(line.split(None, 1)[0])
                                           os.kill(pid, signal.SIGKILL)
                               except:
                                   pass
                               cl.sendMessage(msg.to,' succes kill %s'%cust)
                            elif cmd == '1run':
                                try:
                                    n = 0
                                    r = ''
                                    p = subprocess.Popen(['ps', 'ax'], stdout=subprocess.PIPE)
                                    out, err = p.communicate()
                                    for line in out.splitlines():
                                        if 'python3' in line.decode('utf-8'):
                                            name = line.decode('utf-8').split('python3')[1]
                                            if '.py' in name and '4ang' not in name:
                                                r += '%s: %s\n'%(n,name.replace('.py',''))
                                                n += 1
                                    if len(r) > 0:
                                        cl.sendMessage(msg.to,r.rstrip())
                                    else:
                                        cl.sendMessage(msg.to,'empy project run')
                                except:
                                    cl.sendMessage(msg.to,'error')

                            elif cmd == "friend":
                               Flist(cl,to)
                            elif cmd == "allfriend":
                               for d in Amin:
                                   Flist(d,to)

                            elif cmd == 'bot:room':
                                a = []
                                b = cl.getGroup(to)
                                lss = cl.refreshContacts()
                                for i in b.members:
                                  if i.mid not in mid:
                                     a.append(i.mid)
                                     if i.mid not in lss:
                                        cl.findAndAddContactsByMid(i.mid)
                                     time.sleep(3)
                                if a == []:
                                   cl.sendMessage(to,"Nothing to added.")
                                else:cl.sendMessage(to,'Add whitelist')

                            elif cmd == 'bot1:room':
                                a = []
                                b = ka.getGroup(to)
                                lss = ka.refreshContacts()
                                for i in b.members:
                                  if i.mid not in Amid:
                                     a.append(i.mid)
                                     if i.mid not in lss:
                                        ka.findAndAddContactsByMid(i.mid)
                                     time.sleep(3)
                                if a == []:
                                   ka.sendMessage(to,"Nothing to added.")
                                else:ka.sendMessage(to,'Add whitelist')

                            elif cmd.startswith("tkn "):
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               if pesan == "":
                                   setKey = "" if not Leakiller['keyCmd'] else Leakiller['keyCmd']
                               else:
                                   setKey = pesan
                               cl.sendMessage(to, str(setKey))
                        if msg._from in Lea or msg._from in Leakiller["admin"]:
                          if cmd == "menu":cl.sendMessage(to, Menu.help(keyt))
                          if cmd == "menu1":cl.sendMessage(to, Menu.helpset(keyt))
                          if cmd == "menu2":cl.sendMessage(to, Menu.helpbot(keyt))

                          if cmd == "settbot":
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                eltime = time.time() - mulai
                                md = "â­ââââââââââââ\nâ°ââ¦ á´Éªá´á´ Êá´á´ â§\n\n"
                                md+="  ãon ==ð²  <|>  ð´ == offã\n\n"
                                if msg.to in LiproSett["proqr"]:md+="  ãð²ã á´Êá´á´á´á´á´ ÊÉªÉ´á´ \n"
                                else:md+="  ãð´ã á´Êá´á´á´á´á´ ÊÉªÉ´á´ \n"
                                if msg.to in LiproSett["proKick"]:md+="  ãð²ã á´Êá´á´á´á´á´ á´Éªá´á´ \n"
                                else:md+="  ãð´ã á´Êá´á´á´á´á´ á´Éªá´á´ \n"
                                if msg.to in LiproSett["proCancel"]:md+="  ãð²ã á´Êá´á´á´á´á´ á´á´É´á´á´Ê \n"
                                else:md+="  ãð´ã á´Êá´á´á´á´á´ á´á´É´á´á´Ê \n"
                                if msg.to in LiproSett["proInvite"]:md+="  ãð²ã á´Êá´á´á´á´á´ ÉªÉ´á´ Éªá´á´ \n"
                                else:md+="  ãð´ã á´Êá´á´á´á´á´ ÉªÉ´á´ Éªá´á´ \n"
                                if msg.to in LiproSett["intaPoint"]:md+="  ãð²ã sá´á´á´ á´á´á´á´ á´á´ÉªÉ´á´ \n"
                                else:md+="  ãð´ã sá´á´á´ á´á´á´á´ á´á´ÉªÉ´á´ \n"
                                if LiproSett["bypas"] == True:md+="  ãð²ã ÊÊá´á´ss á´É´á´ÊÊá´ \n"
                                else:md+="  ãð´ã ÊÊá´á´ss á´Éªsá´ÊÊá´ \n"
                                if LiproSett["autoJoin"] == True:md+="  ãð²ã á´'á´á´ÉªÉ´ É¢Êá´á´á´ \n"
                                else:md+="  ãð´ã á´'á´á´ÉªÉ´ É¢Êá´á´á´ \n"
                                if LiproSett["autoJoinTicket"] == True:md+="  ãð²ã á´'á´á´ÉªÉ´ á´Éªá´á´á´á´ \n"
                                else:md+="  ãð´ã á´'á´á´ÉªÉ´ á´Éªá´á´á´á´ \n"
                                if LiproSett["contact"] == True:md+="  ãð²ã á´Êá´á´á´ á´á´É´á´á´á´á´ \n"
                                else:md+="  ãð´ã á´Êá´á´á´ á´á´É´á´á´á´á´ \n"
                                if LiproSett["sticker"] == True:md+="  ãð²ã á´Êá´á´á´ sá´Éªá´á´á´Ê \n"
                                else:md+="  ãð´ã á´Êá´á´á´ sá´Éªá´á´á´Ê \n"
                                if LiproSett["detectMention"] == True:md+="  ãð²ã Êá´sá´á´É´ á´á´É´á´Éªá´É´ \n"
                                else:md+="  ãð´ã Êá´sá´á´É´ á´á´É´á´Éªá´É´ \n"
                                if LiproSett["autoAdd"] == True:md+="  ãð²ã á´á´á´ á´á´É´á´á´á´á´ \n"
                                else:md+="  ãð´ã á´á´á´ á´á´É´á´á´á´á´ \n"
                                if LiproSett["LikeOn"] == True:md+="  ãð²ã ÊÉªá´á´ & á´á´á´á´á´É´á´ \n"
                                else:md+="  ãð´ã ÊÉªá´á´ & á´á´á´á´á´É´á´ \n"
                                if LiproSett["checkPost"] == True:md+="  ãð²ã á´Êá´á´á´ á´á´sá´ \n"
                                else:md+="  ãð´ã á´Êá´á´á´ á´á´sá´ \n"
                                if LiproSett["Unsend"] == True:md+="  ãð²ã á´'á´É´sá´É´á´ á´sÉ¢ \n"
                                else:md+="  ãð´ã á´'á´É´sá´É´á´ á´sÉ¢ \n"
                                if msg.to in LiproSett["welcome"]:md+="  ãð²ã á´sÉ¢ á´¡á´ÊÊá´á´á´á´ \n"
                                else:md+="  ãð´ã á´sÉ¢ á´¡á´ÊÊá´á´á´á´ \n"
                                if msg.to in LiproSett["leaveMsg"]:md+="  ãð²ã á´sÉ¢ Êá´á´á´ á´ \n"
                                else:
                                    md+="  ãð´ã á´sÉ¢ Êá´á´á´ á´ \n\n"
                                    md+="  â"+ datetime.strftime(timeNow,'%H:%M:%S')+"  ð "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n"
                                    md+="   Êá´É´ "+waktu(eltime)+"\n"
                                    md+="â­ââââââââââââ\nã á´Éªá´á´ Êá´á´ ã\nâ°ââââââââââââ"
                                cl.sendReplyMessage(msg_id, to, str(md))

                          if cmd == "me" or text.lower() == 'me':
                                ca = cl.getContact(msg._from)
                                lip = ("ãá´Ê É´á´á´á´ã\n ") + ca.displayName
                                cl.sendMessage(to, lip),cl.sendContact(msg.to,sender)

                          if cmd == 'bypas on':
                              if Leakiller["bypas"] == True:
                                  cl.sendMessage(to,"bypass was on")
                              else:
                                  Leakiller["bypas"] = True
                                  cl.sendMessage(to,"bypass enable mode")

                          if cmd == 'bypas off':
                              if Leakiller["bypas"] == False:
                                  cl.sendMessage(to,"bypass was off")
                              else:
                                  Leakiller["bypas"] = False
                                  cl.sendMessage(to,"bypass disable mode")

                          if "gname " in cmd:
                                X = cl.getGroup(msg.to)
                                X.name = msg.text.replace("gname ","")
                                cl.updateGroup(X)

                          if "mid " in cmd:
                               if 'MENTION' in msg.contentMetadata.keys()!= None:
                                   names = re.findall(r'@(\w+)', text)
                                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                   mentionees = mention['MENTIONEES']
                                   lists = []
                                   for mention in mentionees:
                                       if mention["M"] not in lists:
                                           lists.append(mention["M"])
                                   ret_ = ""
                                   for ls in lists:
                                       ret_ += "{}".format(str(ls))
                                   cl.sendMessage(to, str(ret_),{'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+'M', 'AGENT_NAME': 'Mention', 'AGENT_LINK': 'http://line.me/ti/p/~{}'.format(cl.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + cl.getProfile().picturePath})

                          if "info " in cmd:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                               key = ast.literal_eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "â¢ Nama : "+str(mi.displayName)+"\nâ¢ Mid : " +key1+"\nâ¢ Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                          if cmd == "mybot":
                               cl.sendContact(msg.to, mid)
                               time.sleep(0.15)
                               ka.sendContact(msg.to, Amid)

                          if cmd == "myrechat":
                               try:cl.removeAllMessages(op.param2)
                               except:pass

                          if cmd == "reject":
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                  cl.sendReplyMessage(msg_id, to, "Êá´ÊÊá´sÉªÊ á´á´Êá´á´ sá´Êá´É´Êá´á´ {} á´É´á´á´É´É¢á´É´ É¢Êá´á´".format(str(len(ginvited))))
                              else:
                                  cl.sendReplyMessage(msg_id, to, "á´Éªá´á´á´ á´á´á´ á´É´á´á´É´É¢á´É´ Êá´É´É¢ á´á´Êá´á´É´á´á´")

                          if cmd == "leave allgrup":
                            group = cl.getGroupIdsJoined()
                            for i in group:
                                cl.sendMessage(i,"Êá´á´ Êá´á´á´ á´ á´ÊÊ É¢Êá´á´á´ ")
                                cl.leaveGroup(i)
                                ka.leaveGroup(i)
                                cl.sendMessage(msg.to,"sá´á´á´á´s Êá´á´á´ á´ á´ÊÊ É¢Êá´á´")
                          if cmd.startswith("openqr no "):
                                if msg.toType == 2:
                                    text = cmd.split(" ")
                                    number = text[2]
                                    if number.isdigit():
                                        groups = cl.getGroupIdsJoined()
                                        if int(number) < len(groups) and int(number) >= 0:
                                            groupid = groups[int(number)]
                                            try:
                                                X = cl.getGroup(groupid)
                                                X.preventedJoinByTicket = False
                                                cl.updateGroup(X)
                                                gurl = cl.reissueGroupTicket(groupid)
                                                cl.sendMessage(msg.to,"This link Group For u can it Bro... \nline://ti/g/" + gurl)
                                            except:
                                                cl.sendMessage(msg.to," Gagal Bro ")
                          if cmd.startswith("leave to "):
                                text = cmd.split(" ")
                                number = text[2]
                                if number.isdigit():
                                    groups = cl.getGroupIdsJoined()
                                    if int(number) < len(groups) and int(number) >= 0:
                                        groupid = groups[int(number)]
                                        try:
                                            groupname = cl.getGroup(groupid).name
                                            cl.leaveGroup(groupid)
                                            ka.leaveGroup(groupid)
                                            cl.sendMessage(msg.to,"Successfully  Leave from %s"%groupname)
                                        except:
                                            cl.sendMessage(msg.to," Leave Gagal Bro ")
                          if cmd == "rechat":
                              for i in botlist:
                                  Rchat(i,to)
                          if cmd.startswith("bcg: "):
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"[ ÊÊá´á´á´á´á´sá´ ]\n" + str(pesan))
                          if cmd == "mykey":
                               cl.sendMessage(msg.to, "á´á´Ê É´á´á´¡ã " + str(Leakiller["keyCmd"]) + " ã")
                          if cmd.startswith("setkey "):
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "á´Êá´É´É¢á´ á´á´Ê Òá´ÉªÊá´á´")
                               else:
                                   Leakiller["keyCmd"] = str(key).lower()
                                   cl.sendMessage(msg.to, "sá´á´á´á´s á´á´á´ á´á´Ê á´á´ã{}ã".format(str(key).lower()))
                          if cmd == "resetkey":
                               Leakiller["keyCmd"]=""
                               cl.sendMessage(msg.to, "sá´á´á´á´s Êá´ssá´á´ á´á´Ê á´á´á´á´á´É´á´")
                          if cmd == "/reboot":
                               cl.sendMessage(msg.to, "á´¡á´Éªá´ÉªÉ´É¢ á´ sá´á´á´É´á´")
                               restartProgram()
                          if cmd == "ginfo":
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "ÑÑÑÑÏÑÏÏ"
                                    gTicket = "ÑÄ±âÎ±k Î±âÎ±"
                                else:
                                    gQr = "ÑÑÑÐ²ÏkÎ±"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "  â¢â»ãgÑÏÏ Ä±Î·ÆÏãâ»â¢\n\n Î·Î±Ð¼Î± gÑÏÏÏ : {}".format(G.name)+ "\nÄ±â gÑÏÏÏ : {}".format(G.id)+ "\ncÑÑÎ±ÑÏÑ gÑÏÏÏ : {}".format(G.creator.displayName)+ "\ncÑÑÎ±ÑÑ ÑÄ±Ð¼Ñ gÑÏÏÏ : {}".format(str(timeCreated))+ "\nÅÄ±sÑÐ¼ÑÐ¼Ð²ÑÑ : {}".format(str(len(G.members)))+ "\nÅÄ±sÑ Ä±Î·ÑµÄ±ÑÑ : {}".format(gPending)+ "\ngÑÏÏÏ qÑ : {}".format(gQr)+ "\nÑÄ±ckÑÑ gÑÏÏÏ : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))
                          if cmd.startswith("infogrup"):
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "No file"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "  â¢â» List Grup Info â»â¢\n"
                                ret_ += "\nâ¬ Nama Group : {}".format(G.name)
                                ret_ += "\nâ¬ ID Group : {}".format(G.id)
                                ret_ += "\nâ¬ Pembuat : {}".format(gCreator)
                                ret_ += "\nâ¬ Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\nâ¬ Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\nâ¬ Jumlah Pending : {}".format(gPending)
                                ret_ += "\nâ¬ Group Qr : {}".format(gQr)
                                ret_ += "\nâ¬ Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass
                          if cmd.startswith("infomem"):
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "â "+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"â Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\nãTotal %i Membersã" % len(G.members))
                            except:
                                pass
                          if cmd.startswith("leave: "):
                            text = cmd.replace("leave: ","")
                            gid = cl.getGroupIdsJoined()
                            for i in gid:
                                x = cl.getGroup(i).name
                                if x == text:
                                    try:
                                        ka.leaveGroup(i)
                                        cl.leaveGroup(i)
                                        cl.sendMessage(msg.to,"Succes leave in group %s"%text)
                                    except:
                                        cl.sendMessage(msg.to,"gagal leave dari grup %s"%text)
                          if cmd == "friendlist":
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "â  " + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"âââ[ FRIEND LIST ]\nâ\n"+ma+"â\nâââ[ Totalã"+str(len(gid))+"ãFriends ]")
                          if cmd == "gruplist":
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "â  " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"âââ[ GROUP LIST ]\nâ\n"+ma+"â\nâââ[ Totalã"+str(len(gid))+"ãGroups ]")
                          if cmd == "ourl":
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                gurl = cl.reissueGroupTicket(msg.to)
                                cl.sendMessage(msg.to,"line://ti/g/" + gurl)
                          if cmd == "curl":
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "á´á´É´á´ á´Êá´sá´ Ç«ÊÂ°")
#===========================================#
                          if cmd == "runtime":
                                eltime = time.time() - mulai
                                cl.sendMessage(to, "Bot Run : "+eltime)
                          if cmd == "pictgrup":
                              if msg.toType == 2:
                                Leakiller["gPicture"] = True
                                cl.sendMessage(msg.to,"á´Êá´á´sá´ sá´É´á´ á´Éªá´á´")
                          if cmd == "updp bot":
                                Leakiller["DPicture"] = True
                                cl.sendMessage(msg.to,"á´Êá´á´sá´ sá´É´á´ á´Éªá´á´")
                          if 'dpbot ' in cmd:
                              spl = cmd.replace('dpbot ','')
                              if spl == 'me':
                                  Leakiller["cPicture"][mid] = True
                                  cl.sendMessage(msg.to,"á´Êá´á´sá´ sá´É´á´ á´Éªá´á´")
                              if spl == '1':
                                  Leakiller["cPicture"][Amid] = True
                                  ka.sendMessage(msg.to, "á´á´Êá´sá´ sá´É´á´ á´Éªá´á´ Êá´ss")
                          if cmd.startswith("name: "):
                            separate = text.split(" ")
                            string = text.replace(separate[0] + " ","")
                            if string == "":
                               setKey = "" if not Leakiller['keyCmd'] else Leakiller['keyCmd']
                            else:
                               setKey = string
                            profile = cl.getProfile()
                            profile.displayName = string
                            cl.updateProfile(profile)
                            cl.sendMessage(msg.to,"Succes " + str(string) + "")
                          if cmd.startswith("z1cn: "):
                            separate = text.split(" ")
                            string = text.replace(separate[0] + " ","")
                            if string == "":
                               setKey = "" if not Leakiller['keyCmd'] else Leakiller['keyCmd']
                            else:
                               setKey = string
                            profile = ka.getProfile()
                            profile.displayName = string
                            ka.updateProfile(profile)
                            ka.sendMessage(msg.to,"Succes " + str(string) + "")
                          if cmd.startswith("allcn: "):
                            separate = text.split(" ")
                            string = text.replace(separate[0] + " ","")
                            for x in Amin:
                              if string == "":
                                 setKey = "" if not Leakiller['keyCmd'] else Leakiller['keyCmd']
                              else:
                                 setKey = string
                              profile = x.getProfile()
                              profile.displayName = string
                              x.updateProfile(profile)
                              x.sendMessage(msg.to,"Succes " + str(string) + "")
                          if cmd == "tag" or text.lower() == 'mention':
                                group = cl.getGroup(msg.to)
                                k = len(group.members)//20
                                for j in range(k+1):
                                    aa = []
                                    for x in group.members[j*20 : (j+1)*20]:
                                        aa.append(x.mid)
                                    try:
                                        arrData = ""
                                        textx = "âââââââââââââââââââ\nâ â¢ . "
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
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += "â â¢ . ".format(str(b))
                                            else:
                                                textx += "âââââââââââââââââââ\nâââââââââââââââââââ\n  ã á´á´á´á´Ê á´á´á´Êá´Ê : {} ã\nâââââââââââââââââââ".format(str(len(aa)))
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))

                                                except:
                                                    no = " "
                                        msg.to = msg.to
                                        msg.text = textx
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage(to, textx,{'AGENT_NAME':'[ Mentions ]', 'AGENT_LINK': 'line://ti/p/~{}'.format(cl.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + cl.getProfile().picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                    except Exception as e:
                                        cl.sendText(msg.to,str(e))
                          if cmd == "bots":
                                ma = ""
                                a = 0
                                for m_id in Leakiller["Bots"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"| ãisÏ BÌ¶Ñ³Ïàª½ â¢\n\n"+ma+"ÏÏÏÎ±â : ã%sã BÌ¶Ñ³Ïàª½" %(str(len(Leakiller["Bots"]))))
                          if cmd == "adminlist":
                                mb = ""
                                b = 0
                                for m_id in Leakiller["admin"]:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"| Î±âÐ¼ià¸ Ð²ÏÏs â¢\n\n"+mb+"\nÏÏÏÎ±â :ã%sã Î±âÐ¼ià¸" %(str(len(Leakiller["admin"]))))
                          if cmd == "respon":
                              for i in Amin:
                                  Res(i,to)
                          if cmd == "rs":
                              a = cl.getContact(msg._from).displayName
                              for i in botlist:
                                  i.sendMessage(to, "ï½»â° "+ a)
                          if cmd == 'midku':
                              cl.sendMessage(msg.to,mid+'","'+Amid)
                          if 'lp ' in cmd:
                              spl = cmd.replace('lp ','')
                              for i in botlist:
                                  i.sendMessage(msg.to,spl)
                          if cmd == "inv":
                                try:
                                    cl.inviteIntoGroup(msg.to,Bots)
                                    for i in botlist:
                                        i.acceptGroupInvitation(msg.to)
                                except:
                                    pass
                          if cmd == "allbot:in" or text.lower() == "come":
                                G = cl.getCompactGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                for i in botlist:
                                    i.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)

                          if cmd.startswith("bypass"):
                                try:
                                    jser = threading.Thread(target=Save, args=(to, wait["Member"])).start()
                                except:
                                    cl.sendMessage(to,"Gagal BroW")
                          if cmd.startswith("qr no "):
                                if msg.toType == 2:
                                    text = cmd.split(" ")
                                    number = text[2]
                                    if number.isdigit():
                                        groups = cl.getGroupIdsJoined()
                                        if int(number) < len(groups) and int(number) >= 0:
                                            groupid = groups[int(number)]
                                            try:
                                                X = cl.getGroup(groupid)
                                                X.preventedJoinByTicket = False
                                                cl.updateGroup(X)
                                                gurl = cl.reissueGroupTicket(groupid)
                                                cl.sendMessage(msg.to,"This link Group For u can it Bro... \nline://ti/g/" + gurl)
                                            except:
                                                cl.sendMessage(msg.to," Gagal Bro ")

                          if cmd == "allbot:out":
                              try:
                                  G = cl.getGroup(msg.to)
                                  ka.sendMessage(msg.to, "ââ¤ sÑÑ Ï Ð¼ÑÐ¼Ð²ÑÑð "+str(G.name))
                                  for i in botlist:
                                      i.leaveGroup(msg.to)
                              except:
                                  pass
                          if cmd == "/bye":
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "ââ¤ sÑÑ Ï Ð¼ÑÐ¼Ð²ÑÑ  "+str(G.name))
                                cl.leaveGroup(msg.to)
                          if cmd == "speed" or cmd == "sp":
                                    Speed(cl,to)
                          if cmd == "!sp":
                                jb=botlist
                                for i in jb:
                                    Sp(i,to)
                          if cmd == "lurk on":
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Leakiller['readPoint'][msg.to] = msg_id
                                 Leakiller['readMember'][msg.to] = {}
                                 cl.sendMessage(msg.to, "Lurking berhasil diaktifkan\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                          if cmd == "lurk off":
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Leakiller['readPoint'][msg.to]
                                 del Leakiller['readMember'][msg.to]
                                 cl.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                          if cmd == "lurkers":
                            if msg.to in Leakiller['readPoint']:
                                if Leakiller['readMember'][msg.to] != {}:
                                    aa = []
                                    for x in Leakiller['readMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n  [ Lurkers ]\n1. ".format(str(len(aa)))
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
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nâ¬ Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nâ Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Leakiller['readPoint'][msg.to]
                                        del Leakiller['readMember'][msg.to]
                                    except:
                                        pass
                                    Leakiller['readPoint'][msg.to] = msg.id
                                    Leakiller['readMember'][msg.to] = {}
                                else:
                                    cl.sendMessage(msg.to, "User kosong...")
                            else:
                                cl.sendMessage(msg.to, "Ketik lurking on ")
                          if cmd == "sider on":
                              try:
                                  cl.sendMessage(msg.to, "á´Êá´á´á´ sÉªá´á´Ê á´á´á´Êá´Ê á´ÊÊÊá´á´á´Ê á´É´")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True
                          if cmd == "sider off":
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "á´Êá´á´á´ sÉªá´á´Ê á´á´á´Êá´Ê á´ÊÊÊá´á´á´Ê á´ÒÒ")
                              else:
                                  cl.sendMessage(msg.to, "á´Êá´á´á´ sÉªá´á´Ê á´á´á´Êá´Ê á´¡á´s á´ÒÒ")
                          if cmd.startswith("max: "):
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Leakiller["Maxlimit"] = num
                                cl.sendMessage(msg.to,"á´ÊÊÊá´á´á´Ê sá´á´á´ á´á´É´á´Éªá´É´ ÉªÉ´ :" +strnum)
                          if cmd.startswith("scall: "):
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Leakiller["limit"] = num
                                cl.sendMessage(msg.to,"á´ÊÊÊá´á´á´Ê sá´á´á´ á´á´ÊÊ ÉªÉ´ :" +strnum)
                          if cmd.startswith("stag "):
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = ast.literal_eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Leakiller["Maxlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))
                                    else:
                                        cl.sendMessage(msg.to,"Jumlah melebihi 1000")
                          if cmd == "scall":
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(Leakiller["limit"])
                                cl.sendMessage(to, "sá´á´á´á´s sá´É´á´ {} sá´á´á´ á´á´ÊÊ".format(str(Leakiller["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                         cl.acquireGroupCallRoute(to)
                                         cl.inviteIntoGroupCall(to, contactIds=members)
                                     except:
                                         pass
                                else:
                                    cl.sendMessage(to,"Jumlah melebihi batas")
                          if 'Spam: ' in cmd:
                              korban = cmd.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      ka.sendMessage(midd, str(Leakiller["spamMsg"]))
                          if 'id line: ' in cmd:
                              msgs = cmd.replace('id line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)
                          if 'welcome ' in cmd:
                              spl = cmd.replace('welcome ','')
                              if spl == 'on':
                                  if msg.to in Leakiller["welcome"]:
                                       msgs = "á´¡á´s á´É´"
                                  else:
                                       Leakiller["welcome"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "á´ÊÊÊá´á´á´Ê á´É´ ÉªÉ´ É¢Êá´á´á´ : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "ãsá´É´á´ á´á´ssá´É¢á´ á´¡á´Êá´á´á´á´ã" + msgs)
                              elif spl == 'off':
                                    if msg.to in Leakiller["welcome"]:
                                         del Leakiller["welcome"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "á´ÊÊÊá´á´á´Ê á´ÒÒ ÉªÉ´ É¢Êá´á´á´ : " +str(ginfo.name)
                                    else:
                                         msgs = "á´¡á´s á´ÒÒ"
                                    cl.sendMessage(msg.to, "ãsá´É´á´ á´á´ssá´É¢á´ á´¡á´Êá´á´á´á´ ã" + msgs)
                          if 'left ' in cmd:
                              spl = cmd.replace('left ','')
                              if spl == 'on':
                                  if msg.to in Leakiller["leaveMsg"]:
                                       msgs = "á´¡á´s á´É´"
                                  else:
                                       Leakiller["leaveMsg"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "á´ÊÊÊá´á´á´Ê á´É´ ÉªÉ´ É¢Êá´á´á´ : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "ãsá´É´á´ á´á´ssá´É¢á´ Êá´á´á´ á´ã" + msgs)
                              elif spl == 'off':
                                    if msg.to in Leakiller["leaveMsg"]:
                                         del Leakiller["leaveMsg"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "á´ÊÊÊá´á´á´Ê á´ÒÒ ÉªÉ´ É¢Êá´á´á´ : " +str(ginfo.name)
                                    else:
                                         msgs = "á´¡á´s á´ÒÒ"
                                    cl.sendMessage(msg.to, "ãsá´É´á´ á´á´ssá´É¢á´ Êá´á´á´ á´ã" + msgs)
                          if 'proqr ' in cmd:
                              spl = cmd.replace('proqr ','')
                              if spl == 'on':
                                  if msg.to in Leakiller["proqr"]:
                                       msgs = "á´¡á´s á´É´"
                                  else:
                                       Leakiller["proqr"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "á´ÊÊÊá´á´á´Ê á´É´ ÉªÉ´ É¢Êá´á´á´ : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "ãá´Êá´á´á´á´á´Éªá´É´ ÊÉªÉ´á´ã" + msgs)
                              elif spl == 'off':
                                    if msg.to in Leakiller["proqr"]:
                                         del Leakiller["proqr"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "á´ÊÊÊá´á´á´Ê á´ÒÒ ÉªÉ´ É¢Êá´á´á´ : " +str(ginfo.name)
                                    else:
                                         msgs = "á´¡á´s á´ÒÒ"
                                    cl.sendMessage(msg.to, "ãá´Êá´á´á´á´á´Éªá´É´ ÊÉªÉ´á´ã" + msgs)
                          if 'prokick ' in cmd:
                              spl = cmd.replace('prokick ','')
                              if spl == 'on':
                                  if msg.to in Leakiller["proKick"]:
                                       msgs = "á´¡á´s á´É´"
                                  else:
                                       Leakiller["proKick"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "á´ÊÊÊá´á´á´Ê á´É´ ÉªÉ´ É¢Êá´á´á´ : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "ãá´Êá´á´á´á´á´ á´Éªá´á´ã" + msgs)
                              elif spl == 'off':
                                    if msg.to in Leakiller["proKick"]:
                                         del Leakiller["proKick"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "á´ÊÊÊá´á´á´Ê á´ÒÒ ÉªÉ´ É¢Êá´á´á´ : " +str(ginfo.name)
                                    else:
                                         msgs = "á´¡á´s á´ÒÒ"
                                    cl.sendMessage(msg.to, "ãá´Êá´á´á´á´á´ á´Éªá´á´ã" + msgs)
                          if 'proinvite ' in cmd:
                              spl = cmd.replace('proinvite ','')
                              if spl == 'on':
                                  if msg.to in Leakiller["proInvite"]:
                                       msgs = "á´¡á´s á´É´"
                                  else:
                                       Leakiller["proInvite"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "á´ÊÊÊá´á´á´Ê á´É´ ÉªÉ´ É¢Êá´á´á´ : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "ãá´Êá´á´á´á´á´ ÉªÉ´á´ Éªá´á´ã" + msgs)
                              elif spl == 'off':
                                    if msg.to in Leakiller["proInvite"]:
                                         del Leakiller["proInvite"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "á´ÊÊÊá´á´á´Ê á´ÒÒ ÉªÉ´ É¢Êá´á´á´ : " +str(ginfo.name)
                                    else:
                                         msgs = "á´¡á´s á´ÒÒ"
                                    cl.sendMessage(msg.to, "ãá´Êá´á´á´á´á´ ÉªÉ´á´ Éªá´á´ã" + msgs)
                          if 'procancel ' in cmd:
                              spl = cmd.replace('procancel ','')
                              if spl == 'on':
                                  if msg.to in Leakiller["proCancel"]:
                                       msgs = "á´¡á´s á´É´"
                                  else:
                                       Leakiller["proCancel"] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "á´ÊÊÊá´á´á´Ê á´É´ ÉªÉ´ É¢Êá´á´á´ : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "ãá´Êá´á´á´á´á´ á´á´É´á´á´Êã" + msgs)
                              elif spl == 'off':
                                    if msg.to in Leakiller["proCancel"]:
                                         Leakiller["proCancel"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "á´ÊÊÊá´á´á´Ê á´ÒÒ ÉªÉ´ É¢Êá´á´á´ : " +str(ginfo.name)
                                    else:
                                         msgs = "á´¡á´s á´ÒÒ"
                                    cl.sendMessage(msg.to, "ãá´Êá´á´á´á´á´ á´á´É´á´á´Êã" + msgs)
                          if 'protect ' in cmd:
                              spl = cmd.replace('protect ','')
                              if spl == 'on':
                                  if msg.to in Leakiller["proqr"]:
                                       msgs = ""
                                  else:
                                       Leakiller["proqr"][msg.to] = True
                                  if msg.to in Leakiller["proKick"]:
                                      msgs = ""
                                  else:
                                       Leakiller["proKick"][msg.to] = True
                                  if msg.to in Leakiller["proInvite"]:
                                      msgs = ""
                                  else:
                                       Leakiller["proInvite"][msg.to] = True
                                  if msg.to in Leakiller["proCancel"]:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "á´¡á´s á´É´ ÉªÉ´ É¢Êá´á´á´ : " +str(ginfo.name)
                                  else:
                                       Leakiller["proCancel"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "á´ÊÊÊá´á´á´Ê á´É´ ÉªÉ´ É¢Êá´á´á´ : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "ãá´ÊÊ á´Êá´á´á´á´á´Éªá´É´ã" + msgs)
                              elif spl == 'off':
                                    if msg.to in Leakiller["proqr"]:
                                         del Leakiller["proqr"][msg.to]
                                    else:
                                         msgs = ""
                                    if msg.to in Leakiller["proKick"]:
                                         del Leakiller["proKick"][msg.to]
                                    else:
                                         msgs = ""
                                    if msg.to in Leakiller["proInvite"]:
                                         del Leakiller["proInvite"][msg.to]
                                    else:
                                         msgs = ""
                                    if msg.to in Leakiller["proCancel"]:
                                         del Leakiller["proCancel"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "á´ÊÊÊá´á´á´Ê á´ÒÒ ÉªÉ´ É¢Êá´á´á´ : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "á´¡á´s á´ÒÒ ÉªÉ´ É¢Êá´á´á´ : " +str(ginfo.name)
                                    cl.sendMessage(msg.to, "ãá´ÊÊ á´Êá´á´á´á´á´Éªá´É´ã" + msgs)
                          if 'inta ' in cmd:
                              spl = cmd.replace('inta ','')
                              if spl == 'on':
                                  if msg.to in Leakiller["intaPoint"]:
                                       msgs = "á´¡á´s á´É´"
                                  else:
                                       Leakiller["intaPoint"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "á´ÊÊÊá´á´á´Ê á´É´ ÉªÉ´ É¢Êá´á´á´ : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "ãÉªÉ´á´á´ á´á´ÉªÉ´á´ã" + msgs)
                              elif spl == 'off':
                                    if msg.to in Leakiller["intaPoint"]:
                                         del Leakiller["intaPoint"][msg.to]
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "á´ÊÊÊá´á´á´Ê á´ÒÒ ÉªÉ´ É¢Êá´á´á´ : " +str(ginfo.name)
                                    else:
                                         msgs = "á´¡á´s á´ÒÒ"
                                    cl.sendMessage(msg.to, "ãÉªÉ´á´á´ á´á´ÉªÉ´á´ã" + msgs)
                          if "bot kick " in cmd:
                              if 'MENTION' in msg.contentMetadata.keys():
                                  mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  for mention in mentions['MENTIONEES']:
                                      uid = mention['M']
                                      if uid in Lea or uid in Bots or uid in Leakiller["Bots"]:
                                          continue
                                      try:
                                          random.choice(botlist).kickoutFromGroup(msg.to, [uid])
                                          wait["blacklist"][uid] = True
                                      except:
                                          cl.sendMessage(msg.to,"ÊÉªá´Éªá´Êá´sá´á´Ê")
                          if "invite" in cmd:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                               key = ast.literal_eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target in wait["blacklist"]:
                                       cl.sendMessage(msg.to, "sá´ÊÊÊ á´á´É´á´á´á´á´ ÉªÉ´ ÊÊá´á´á´ÊÉªsá´")
                                   else:
                                       try:
                                           ka.findAndAddContactsByMid(target)
                                           ka.inviteIntoGroup(msg.to, [target])
                                       except:
                                           ka.sendMessage(msg.to, "sá´ÊÊÊ!! á´á´ÊÉ¢á´á´ ÉªÉ´á´ Éªá´á´ É´á´á´ Òá´á´É´á´ á´Ê Êá´á´s ÊÉªá´Éªá´ ÉªÉ´á´ Éªá´á´")
                          if "kiss " in cmd:
                              if 'MENTION' in msg.contentMetadata.keys():
                                  mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  for mention in mentions['MENTIONEES']:
                                      uid = mention['M']
                                      if uid in Lea or uid in Bots or uid in Leakiller["Bots"]:
                                          continue
                                      try:
                                          cl.kickoutFromGroup(msg.to, [uid])
                                      except:
                                          cl.sendMessage(msg.to,"ÊÉªá´Éªá´Êá´sá´á´Ê")
                          if "@cancelin" in cmd:
                               group = cl.getGroup(msg.to)
                               if group.invitee is None:
                                   cl.sendMessage(op.message.to, "kÏsÏÎ·g Ð²Ïss ")
                               else:
                                   nama = [contact.mid for contact in group.invitee]
                                   for x in nama:
                                     if x not in Lea and x not in Bots and x not in Leakiller["Bots"] and x not in Leakiller["admin"]:
                                       cl.cancelGroupInvitation(msg.to, [x])
                                       time.sleep(0.3)
                                   cl.sendMessage(to, "âÏÎ·Ñ.")
                          if "bot cancel" in cmd:
                               group = cl.getGroup(msg.to)
                               if group.invitee is None:
                                   cl.sendMessage(op.message.to, "kÏsÏÎ·g Ð²Ïss ")
                               else:
                                   nama = [contact.mid for contact in group.invitee]
                                   for x in nama:
                                     for j in [cl,ka]:
                                       if x not in Lea and x not in Bots and x not in Leakiller["Bots"] and x not in Leakiller["admin"]:
                                         j.cancelGroupInvitation(msg.to, [x])
                                         time.sleep(0.3)
                                   cl.sendMessage(to, "âÏÎ·Ñ.")
                          if "addadmin " in cmd:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                               key = ast.literal_eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target in Leakiller["admin"]:
                                       cl.sendMessage(msg.to,"ÏÎ±s Ä±Î· Î±âÐ¼Ä±Î·")
                                   else:
                                       try:
                                           Leakiller["admin"][target] = True
                                           cl.sendMessage(msg.to,"sÏccÑs Î±ââ Î±âÐ¼Ä±Î·")
                                       except:
                                           pass
                          if "addbot " in cmd:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                               key = ast.literal_eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target in Leakiller["Bots"]:
                                       cl.sendMessage(msg.to,"ÏÎ±s Ä±Î· Ð²ÏÑs")
                                   else:
                                       try:
                                           Leakiller["Bots"][target] = True
                                           cl.sendMessage(msg.to,"sÏccÑs Î±ââ Ð²ÏÑs")
                                       except:
                                           pass
                          if "deladmin " in cmd:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                               key = ast.literal_eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Leakiller["admin"]:
                                       cl.sendMessage(msg.to,"Î·ÏÑ Ä±Î· Î±âÐ¼Ä±Î·")
                                   else:
                                       try:
                                           del Leakiller["admin"][target]
                                           cl.sendMessage(msg.to,"sÏccÑs âÑÅÑÑÑ Î±âÐ¼Ä±Î·")
                                       except:
                                           pass
                          if "delbot " in cmd:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                               key = ast.literal_eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Leakiller["Bots"]:
                                       cl.sendMessage(msg.to,"Î·ÏÑ Ä±Î· Êá´á´s")
                                   else:
                                       try:
                                           del Leakiller["Bots"][target]
                                           cl.sendMessage(msg.to,"sÏccÑs âÑÅÑÑÑ Ð²ÏÑs")
                                       except:
                                           pass
                          if "addcontact" in cmd:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                               key = ast.literal_eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                 for c in [cl,ka,kb,kc,kd,ke]:
                                   gid = c.getAllContactIds()
                                   if target in gid:
                                       c.sendMessage(msg.to,"á´á´ÊÉ¢á´á´ á´¡á´s ÉªÉ´ á´á´É´á´á´á´á´ ÊÉªsá´")
                                   else:
                                       try:
                                           bit = c.getContact(target)
                                           time.sleep(2)
                                           c.findAndAddContactsByMid(bit.mid)
                                           time.sleep(2)
                                           c.sendMessage(msg.to,"sá´á´á´á´s á´á´á´á´á´ á´á´É´á´á´á´á´ " + c.getContact(target).displayName)
                                       except:
                                           cl.sendMessage(msg.to,"Êá´á´s ÊÉªá´Éªá´ á´á´á´ á´á´É´á´á´á´á´")
                          if cmd.startswith("join to "):
                                text = cmd.split(" ")
                                number = text[2]
                                if number.isdigit():
                                    groups = cl.getGroupIdsJoined()
                                    if int(number) < len(groups) and int(number) >= 0:
                                        groupid = groups[int(number)]
                                        try:
                                            cl.findAndAddContactsByMid(sender)
                                            cl.inviteIntoGroup(groupid,[sender])
                                            groupname = cl.getGroup(groupid).name
                                            cl.sendMessage(msg.to,"Successfully invite %s"%groupname)
                                        except:
                                            cl.sendMessage(msg.to," Invite banned Bro " + cl.getContact(sender).displayName)

                          if cmd == "groups":
                                gid = cl.getGroupIdsJoined()
                                num = 0
                                g = ""
                                for i in gid:
                                    g += "%i - " % num + "%s" % (cl.getGroup(i).name + "(%s)\n" % (str (len (cl.getGroup(i).members))))
                                    num = (num+1)
                                cl.sendMessage(msg.to,"Group List:\n\n"+ g + "Total Groups : " + str(len(gid)))

                          if cmd == "cbot" or text.lower() == 'clear bot':
                              ang = cl.getContacts(Leakiller["Bots"])
                              mc = "%i Ð²ÏÏs " % len(ang)
                              cl.sendMessage(msg.to,"á´á´É´á´ á´Êá´á´Ê " +mc)
                              Leakiller["Bots"] = {}
                          if cmd == "cadmin" or text.lower() == 'clear admin':
                              ang = cl.getContacts(Leakiller["admin"])
                              mc = "%i á´á´á´ÉªÉ´ " % len(ang)
                              cl.sendMessage(msg.to,"á´á´É´á´ á´Êá´á´Ê " +mc)
                              Leakiller["admin"] = {}
                          if cmd == "admin:on" or text.lower() == 'admin:on':
                                Leakiller["addadmin"] = True
                                cl.sendMessage(msg.to,"sá´É´á´ á´á´É´á´á´á´á´...")
                          if cmd == "admin:del" or text.lower() == 'admin:del':
                                Leakiller["deladmin"] = True
                                cl.sendMessage(msg.to,"sá´É´á´ á´á´É´á´á´á´á´...")
                          if cmd == "admin:off" or text.lower() == 'admin off':
                                Leakiller["addadmin"] = False
                                cl.sendMessage(msg.to,"á´ÊÊÊá´á´á´Ê á´ÒÒ")
                          if cmd == "deladmin:off" or text.lower() == 'deladmin off':
                                Leakiller["deladmin"] = False
                                cl.sendMessage(msg.to,"á´ÊÊÊá´á´á´Ê á´ÒÒ")
                          if cmd == "bot:on" or text.lower() == 'bot on':
                                Leakiller["abots"] = True
                                cl.sendMessage(msg.to,"sá´É´á´ á´á´É´á´á´á´á´...")
                          if cmd == "bot:off" or text.lower() == 'bot off':
                                Leakiller["abots"] = False
                                cl.sendMessage(msg.to,"á´ÊÊÊá´á´á´Ê á´ÒÒ")
                          if cmd == "bot:del" or text.lower() == 'bot del':
                                Leakiller["dbots"] = True
                                cl.sendMessage(msg.to,"sá´É´á´ á´á´É´á´á´á´á´...")
                          if cmd == "delbot:off" or text.lower() == 'delbot off':
                                Leakiller["dbots"] = False
                                cl.sendMessage(msg.to,"á´ÊÊÊá´á´á´Ê á´ÒÒ")
                          if cmd == "allrefresh" or text.lower() == 'refresh':
                                Leakiller["addadmin"] = False
                                Leakiller["deladmin"] = False
                                Leakiller["abots"] = False
                                Leakiller["dbots"] = False
                                Leakuller["ablacklist"] = False
                                Leakiller["dblacklist"] = False
                                Leakiller["LikeOn"] = False
                                cl.sendMessage(msg.to," ââ¤ Sudah done direfresh...")
                          if cmd == "killban":
                                if msg.toType == 2:
                                    group = cl.getGroup(msg.to)
                                    gMembMids = [contact.mid for contact in group.members]
                                    matched_list = []
                                    for tag in wait["blacklist"]:
                                        matched_list+=filter(lambda str: str == tag, gMembMids)
                                    if matched_list == []:
                                        pass
                                    for jj in matched_list:
                                        try:
                                            klist=[cl,ka]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[jj])
                                            print (msg.to,[jj])
                                        except:
                                            pass
                          if cmd == "ctbot" or text.lower() == 'ctbot':
                                ma = ""
                                for i in Leakiller["Bots"]:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                          if cmd == "ctban" or text.lower() == 'ctbanlist':
                                ma = ""
                                for i in wait["blacklist"]:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                          if cmd == "contact:on" or text.lower() == 'contact on':
                                Leakiller["contact"] = True
                                cl.sendMessage(msg.to,"á´Êá´á´á´ á´á´á´á´ÉªÊ á´á´É´á´á´á´á´ á´ÊÊÊá´á´á´Ê á´É´")
                          if cmd == "contact:off" or text.lower() == 'contact off':
                                Leakiller["contact"] = False
                                cl.sendMessage(msg.to,"á´Êá´á´á´ á´á´á´á´ÉªÊ á´á´É´á´á´á´á´ á´ÊÊÊá´á´á´Ê á´ÒÒ")
                          if cmd == "respon:on" or text.lower() == 'respon on':
                                Leakiller["detectMention"] = True
                                cl.sendMessage(msg.to,"Êá´sá´á´É´ á´á´É´á´Éªá´É´ á´ÊÊÊá´á´á´Ê á´É´")
                          if cmd == "respon:off" or text.lower() == 'respon off':
                                Leakiller["detectMention"] = False
                                cl.sendMessage(msg.to,"Êá´sá´á´É´ á´á´É´á´Éªá´É´ á´ÊÊÊá´á´á´Ê á´ÒÒ")
                          if cmd == "autojoin:on" or text.lower() == 'autojoin on':
                                Leakiller["autoJoin"] = True
                                cl.sendMessage(msg.to,"á´á´á´á´á´á´ÉªÉ´ á´ÊÊÊá´á´á´Ê á´É´")
                          if cmd == "autojoin:off" or text.lower() == 'autojoin off':
                                Leakiller["autoJoin"] = False
                                cl.sendMessage(msg.to,"á´á´á´á´á´á´ÉªÉ´ á´ÊÊÊá´á´á´Ê á´ÒÒ")
                          if cmd == "like:on" or text.lower() == 'like on':
                              Leakiller["LikeOn"] = True
                              cl.sendMessage(msg.to,"á´á´á´á´ÊÉªá´á´ á´ÊÊÊá´á´á´Ê á´É´")
                          if cmd == "like:off" or text.lower() == 'like off':
                              Leakiller["LikeOn"] = False
                              cl.sendMessage(msg.to,"á´á´á´á´ÊÉªá´á´ á´ÊÊÊá´á´á´Ê á´ÒÒ")
                          if cmd == "scan:on" or text.lower() == 'scan on':
                                Leakiller["checkmid"] = True
                                cl.sendMessage(msg.to,"á´Êá´á´á´ á´Éªá´ á´á´É´á´á´á´á´ á´ÊÊÊá´á´á´Ê á´É´")
                          if cmd == "scan:off" or text.lower() == 'scan off':
                                Leakiller["checkmid"] = False
                                cl.sendMessage(msg.to,"á´Êá´á´á´ á´Éªá´ á´á´É´á´á´á´á´ á´ÊÊÊá´á´á´Ê á´ÒÒ")
                          if cmd == "post:on" or text.lower() == 'post on':
                                Leakiller["checkPost"] = True
                                cl.sendMessage(msg.to,"á´á´á´á´á´á´ á´á´sá´ á´ÊÊÊá´á´á´Ê á´É´")
                          if cmd == "post:off" or text.lower() == 'post off':
                                Leakiller["checkPost"] = False
                                cl.sendMessage(msg.to,"á´á´á´á´á´á´ á´á´sá´ á´ÊÊÊá´á´á´Ê á´ÒÒ")
                          if cmd == "unsend:on" or text.lower() == 'unsend on':
                                Leakiller["Unsend"] = True
                                cl.sendMessage(msg.to,"á´á´á´á´á´á´ á´É´sá´É´á´ á´á´ssá´É¢á´ á´ÊÊÊá´á´Ê á´É´")
                          if cmd == "unsend:off" or text.lower() == 'unsend off':
                                Leakiller["Unsend"] = False
                                cl.sendMessage(msg.to,"á´á´á´á´á´á´ á´É´sá´É´á´ á´á´ssá´É¢á´ á´ÊÊÊá´á´Ê á´ÒÒ")
                          if cmd == "autoadd:on" or text.lower() == 'autoadd on':
                                Leakiller["autoAdd"] = True
                                cl.sendMessage(msg.to,"á´á´á´á´ á´á´á´ á´ÊÊÊá´á´Ê á´É´")
                          if cmd == "autoadd:off" or text.lower() == 'autoadd off':
                                Leakiller["autoAdd"] = False
                                cl.sendMessage(msg.to,"á´á´á´á´ á´á´á´ á´ÊÊÊá´á´Ê á´ÒÒ")
                          if cmd == "sticker:on" or text.lower() == 'sticker on':
                                Leakiller["sticker"] = True
                                cl.sendMessage(msg.to,"á´Êá´á´á´ sá´Éªá´á´á´Ê á´ÊÊÊá´á´Ê á´É´")
                          if cmd == "sticker:off" or text.lower() == 'sticker off':
                                Leakiller["sticker"] = False
                                cl.sendMessage(msg.to,"á´Êá´á´á´ sá´Éªá´á´á´Ê á´ÊÊÊá´á´Ê á´ÒÒ")
                          if cmd == "jticket:on" or text.lower() == 'jticket on':
                                Leakiller["autoJoinTicket"] = True
                                cl.sendMessage(msg.to,"á´á´á´á´ á´á´ÉªÉ´ á´Éªá´á´á´á´ á´ÊÊÊá´á´Ê á´É´")
                          if cmd == "jticket:off" or text.lower() == 'jticket off':
                                Leakiller["autoJoinTicket"] = False
                                cl.sendMessage(msg.to,"á´á´á´á´ á´á´ÉªÉ´ á´Éªá´á´á´á´ á´ÊÊÊá´á´Ê á´ÒÒ")
                          if "ban " in cmd:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                               key = ast.literal_eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target in wait["blacklist"]:
                                       cl.sendMessage(msg.to,"á´á´É´á´á´á´á´ á´¡á´s ÉªÉ´ ÊÊá´á´á´ÊÉªsá´")
                                   else:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"sá´á´á´á´s á´á´á´ á´á´ ÊÊá´á´á´ÊÉªsá´")
                                       except:
                                           pass
                          if "delbl " in cmd:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                               key = ast.literal_eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in wait["blacklist"]:
                                       cl.sendMessage(msg.to,"á´á´É´á´á´á´á´ É´á´á´ ÉªÉ´ ÊÊá´á´á´ÊÉªsá´")
                                   else:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"sá´á´á´á´s Êá´á´á´á´ á´ ÉªÉ´ ÊÊá´á´á´ÊÉªsá´")
                                       except:
                                           pass
                          if cmd == "ban:on" or text.lower() == 'ban on':
                                Leakiller["ablacklist"] = True
                                cl.sendMessage(msg.to,"sá´É´á´ á´á´É´á´á´á´á´...")
                          if cmd == "ban:off" or text.lower() == 'ban off':
                                Leakiller["ablacklist"] = False
                                cl.sendMessage(msg.to,"á´ÊÊÊá´á´á´Ê á´ÒÒ")
                          if cmd == "unban:on" or text.lower() == 'unban on':
                                Leakiller["dblacklist"] = True
                                cl.sendMessage(msg.to,"sá´É´á´ á´á´É´á´á´á´á´...")
                          if cmd == "unban:off" or text.lower() == 'unban off':
                                Leakiller["dblacklist"] = False
                                cl.sendMessage(msg.to,"á´ÊÊÊá´á´á´Ê á´ÒÒ")
                          if cmd == "banlist" or text.lower() == 'blacklist':
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"| Terciduk â\n\n"+ma+"\nTotal : ã%sã Terciduk " %(str(len(wait["blacklist"]))))
                          if cmd == "cban" or text.lower() == 'cban':
                              ang = cl.getContacts(wait["blacklist"])
                              mc = "%i Tersangka " % len(ang)
                              cl.sendMessage(msg.to,"Di Ampuni " +mc)
                              wait["blacklist"] = {}
                          if 'add: ' in cmd:
                              ang = cmd.replace('add: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Leakiller["message"] = ang
                                  cl.sendMessage(msg.to, "ãá´á´ssá´É¢á´ á´á´á´ã :\n\nã{}ã".format(str(ang)))
                          if 'left: ' in cmd:
                              ang = cmd.replace('left: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Leakiller["leftmsg"] = ang
                                  cl.sendMessage(msg.to, "ãá´á´ssá´É¢á´ Êá´á´á´ á´ã :\n\nã{}ã".format(str(ang)))
                          if 'welcome: ' in cmd:
                              ang = cmd.replace('welcome: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Leakiller["sambutan"] = ang
                                  cl.sendMessage(msg.to, "ãá´á´ssá´É¢á´ á´¡á´ÊÊá´á´á´á´ã :\n\nã{}ã".format(str(ang)))
                          if 'tag: ' in cmd:
                              ang = cmd.replace('tag: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Leakiller["msgTag"] = ang
                                  cl.sendMessage(msg.to, "ãá´á´ssá´É¢á´ á´á´É´á´Éªá´É´ã:\n\nã{}ã".format(str(ang)))
                          if 'spam: ' in cmd:
                              ang = cmd.replace('spam: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Leakiller["spamMsg"] = ang
                                  cl.sendMessage(msg.to, "ãá´á´ssá´É¢á´ sá´á´á´ã :\n\nã{}ã".format(str(ang)))
                          if 'sider: ' in cmd:
                              znf = cmd.replace('sider: ','')
                              if znf in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Leakiller["siderMsg"] = znf
                                  cl.sendMessage(msg.to, "ãá´á´ssá´É¢á´ sÉªá´á´Êã:\n\nã{}ã".format(str(znf)))
                          if 'invmid ' in cmd:
                              znf = cmd.replace('invmid ','')
                              try:
                                  cl.findAndAddContactsByMid(znf)
                                  cl.sendContact(to,znf)
                              except Exception as e:
                                  traceback.print_exc()
                                  
                          if cmd == "cekmsg":
                               cl.sendMessage(msg.to, "ãá´á´ssá´É¢á´ á´á´á´ã :\nã " + str(Leakiller["message"]) + " ã")
                               cl.sendMessage(msg.to, "ãá´á´ssá´É¢á´ sÉªá´á´Êã:\nã " + str(Leakiller["siderMsg"]) + " ã")
                               cl.sendMessage(msg.to, "ãá´á´ssá´É¢á´ á´á´É´á´Éªá´É´ã:\nã " + str(Leakiller["msgTag"]) + " ã")
                               cl.sendMessage(msg.to, "ãá´á´ssá´É¢á´ sá´á´á´ã:\nã " + str(Leakiller["spamMsg"]) + " ã")
                               cl.sendMessage(msg.to, "ãá´á´ssá´É¢á´ á´¡á´ÊÊá´á´á´á´ã:\nã " + str(Leakiller["sambutan"]) + " ã")
                               cl.sendMessage(msg.to, "ãá´á´ssá´É¢á´ Êá´á´á´ á´ã:\nã " + str(Leakiller["leftmsg"]) + " ã")
#===========JOIN TICKET============#
                          if "/ti/g/" in msg.text.lower():
                              if Leakiller["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     ka.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     if group.id in Leakiller["intaPoint"]:pass
                                     else:
                                         Leakiller["intaPoint"][group.id] = True
                                     cl.sendMessage(msg.to, "sá´á´á´á´s á´á´ÉªÉ´ : %s" % str(group.name))
                                     if Leakiller["bypas"] == True:
                                       for eXec in []:
                                         x = cl.getCompactGroup(group.id)
                                         nerma = x.id
                                         if x.invitee == None:nama = []
                                         else:nama = [contact.mid for contact in x.invitee]
                                         target = []
                                         for a in nama:
                                           if a not in Lea and a not in Bots and a not in Leakiller["admin"] and a not in Leakiller["Bots"]:
                                               target.append(a)
                                         cmd = 'bypass.js gid={} token={}'.format(nerma, eXec.authToken)
                                         nami = [contact.mid for contact in x.members]
                                         tarsih = []
                                         for s in nami:
                                           if s not in Lea and s not in Bots and s not in Leakiller["admin"] and s not in Leakiller["Bots"]:
                                               tarsih.append(s)
                                         for y in target:
                                             cmd += ' uid={}'.format(y)
                                         for k in tarsih:
                                             cmd += ' uid={}'.format(k)
                                         success = execute_js(cmd)


                          if cmd == "cleanse":
                               if msg.toType == 2:
                                  group = cl.getGroup(msg.to)
                                  nama = [contact.mid for contact in group.members]
                                  for x in nama:
                                      if x not in Zie:
                                          if x not in Leakiller["Bots"]:
                                              if x not in Leakiller["admin"]:
                                                  try:
                                                      klist=[cl,ka]
                                                      ang=random.choice(klist)
                                                      ang.kickoutFromGroup(msg.to,[x])
                                                  except:
                                                      print ("limit")
                          if msg.text.lower() in ["check"]:
                                anu = cl.getGroup(msg.to)
                                oncom = ["ub7081271bf7414f6af87a999bb5f07d7"] #MID PUSKUN
                                for _mid in oncom:
                                    message="â­âá´Éªá´á´ Êá´á´ââ\n"
                                    try:
                                        cl.kickoutFromGroup(msg.to,[_mid])
                                        message+="âãâÒÊá´sÊãá´Éªá´á´\n"
                                    except:
                                        message+="âãâ¹ ÊÉªá´Éªá´ãá´Éªá´á´\n"
                                    try:
                                        ka.kickoutFromGroup(msg.to,[_mid])
                                        message+="âãâÒÊá´sÊãá´Éªá´á´\n"
                                    except:
                                        message+="âãâ¹ ÊÉªá´Éªá´ãá´Éªá´á´\n"
                                    message+="â°âââââââââ"
                                    cl.sendMessage(msg.to,message)
      except Exception as e:
          print(e)

def Flist(self,to):
    ma = "â­ââââââââââââ\nâ°ââ¦ Friend List â§\n\n"
    a = 0
    gid = self.getAllContactIds()
    for i in gid:
        G = self.getContact(i)
        a = a + 1
        end = "\n"
        ma += "âÎ " + str(a) + ". " +G.displayName+ "\n"
    self.sendMessage(to,ma+"\nâ­ââã "+str(len(gid))+"  Friends  ã\nâ°ââââââââââââ")
def Sp(self,to):
      get_group_time_start = time.time()
      get_group = self.getGroupIdsJoined()
      get_group_time = time.time() - get_group_time_start
      self.sendMessage(to, "[ ~G : %.4f â¡]" % (get_group_time/2))

def Speed(self,to):
      get_group_time_start = time.time()
      get_group = self.getGroupIdsJoined()
      get_group_time = time.time() - get_group_time_start
      get_contact_time_start = time.time()
      get_contact = self.getContact(mid)
      get_contact_time = time.time() - get_contact_time_start
      get_profile_time_start = time.time()
      get_profile = self.getProfile()
      get_profile_time = time.time() - get_profile_time_start
      self.sendMessage(to, "[ ~P : %.4f â¡]\n[ ~C : %.4f â¡]\n[ ~G : %.4f â¡]" % (get_profile_time/2,get_contact_time/2,get_group_time/2))

def likePost(self, mid, postId, likeType=1001):
    if mid is None:
        mid = cl.profile.mid
    if likeType not in [1001,1002,1003,1004,1005,1006]:
        raise Exception('Invalid parameter likeType')
    params = {'homeId': mid, 'sourceType': 'TIMELINE'}
    url = cl.server.urlEncode(cl.server.LINE_TIMELINE_API, '/v23/like/create', params)
    data = {'likeType': likeType, 'postId': postId, 'actorId': mid}
    r = cl.server.postContent(url, data=data, headers=cl.server.channelHeaders)
    return r.json()

def createComment(self, mid, postId, text):
    if mid is None:
        mid = self.profile.mid
    params = {'homeId': mid, 'sourceType': 'TIMELINE'}
    url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v39/comment/create.json', params)
    data = {'commentText': text, 'activityExternalId': postId, 'actorId': mid}
    data = json.dumps(data)
    r = self.server.postContent(url, data=data, headers=self.server.timelineHeaders)
    return r.json()

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "ãreader {} memberã\nhai ka.. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+Leakiller["siderMsg"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\nâââ[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\nâââ[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "ãMember Join {}ã\Wellcome ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+Leakiller["sambutan"]+"\ndi group : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\nâââ[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\nâââ[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))


while True:
    try:
        ops = linePoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                    linePoll.setRevision(op.revision)
                    thread = threading.Thread(target=bot, args=(op,))
                    thread.start()
    except Exception as e:
        print(e)

