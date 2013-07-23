from os import system, name
from sys import exit, stdin, stdout, version_info
from time import strftime, sleep
from timeit import default_timer

import urllib2
import threading
import socket
import datetime

import select
import string
import collections
import requests

import trading                                          # Trading functions
import functions                                        # General functions
import config                                           # Configuration parameters
import glob                                             # Global (yes it's ugly... but works great...)

from btceapi import btceapi                             # alanmcintyre / btce-api

class c:						# ansi colors
	blu = '\033[94m'
	grn = '\033[32m'
        yel = '\033[1;33m'
	red = '\033[91m'
	inv = '\033[1m\033[47m'
	bup = '\033[1;37m\033[42m'
	bdn = '\033[1;37m\033[41m'
	rst = '\033[0m'
	lgr = '\33[37m'
	udl = '\033[0m\033[4m'

global connectw, connecta
global handler
global balancec, balancea
global botright
global orders, ordbuy, ordsell
global tickbuy, ticksell, trends
global lastrate
global totcano

		
connectw 	= False							# conenct web
connecta	= False							# connect api
handler 	= "Empty String "					# connection handle

balancec	= []							# currencies
balancea	= []							# balance
balanceo        = []                                                    # prev balance
botright	= []							# bot rights
orders		= ""							# open orders
ordbuy		= 0							# open buy orders
ordsell		= 0							# open sell orders
tickbuy		= ""							# ticker buy orders
ticksell	= ""							# ticker sell orders
trends		= ""							# trend indicators
lastrate	= ""							# last rate traded at
totcano         = 0                                                     # you do the math......

def updateticker():                                                     # Calc SMA over last 5, 10, 20, 50 en 150 trades
	global tickbuy, ticksell, trends, lastrate
	bala 	= 	[]
	balb 	= 	[]
	balc 	= 	[]
	bald 	= 	[]
	bale 	= 	[]
	balf 	= 	[]
	history	=	""
	try:
		history = btceapi.getTradeHistory(config.tradepair)
               	connecta = True
		p = 0
		for t in history:
		        bala.append(1)
		        balb.append(1)
		        balc.append(1)
		        bald.append(1)
		        bale.append(1)
		        balf.append(1)
		        bala[p]=t.tid
		        balb[p]=t.trade_type
		        balc[p]=t.amount
		        bald[p]=t.price
		        bale[p]=t.pair
		        bale[p]=t.date
		        p+=1
		tickbuy = "Buy " + c.grn
		ticksell = "Sell" + c.red
		for p in range(0,7):
		        if balb[p] == "bid":
		                tickbuy = tickbuy + str('{:10.5f}'.format(bald[p]))
		                ticksell = ticksell + "          "
		        else:
		                tickbuy = tickbuy + "          "
		                ticksell = ticksell + str('{:10.5f}'.format(bald[p]))
		tickbuy = tickbuy + c.rst
		ticksell = ticksell + c.rst

		trends = ""
		if bald[0] > sum(bald[0:5])/5:
	        	trends = "over x trades, 5: up     "
		elif bald[0] < sum(bald[0:5])/5:
		        trends = "over x trades, 5: down   "
		else:
		        trends = "over x trades, 5: stand  "
	        if bald[0] > sum(bald[0:10])/10:
	                trends = trends + "10: up     "
	        elif bald[0] < sum(bald[0:10])/10:
	                trends = trends + "10: down   "
	        else:
	                trends = trends + "10: stand  "
	        if bald[0] > sum(bald[0:20])/20:
	                trends = trends + "20: up     "
	        elif bald[0] < sum(bald[0:20])/20:
	                trends = trends + "20: down   "
	        else:
	                trends = trends + "20: stand  "
	        if bald[0] > sum(bald[0:50])/50:
	                trends = trends + "50: up     "
	        elif bald[0] < sum(bald[0:50])/50:
	                trends = trends + "50: down   "
	        else:
	                trends = trends + "50: stand  "
	        if bald[0] > sum(bald[0:150])/150:
	                trends = trends + "150: up"
	        elif bald[0] < sum(bald[0:150])/150:
	                trends = trends + "150: down"
	        else:
	                trends = trends + "150: stand"
		lastrate = bald[0]
        except Exception as e:
                if config.logconnect:
			functions.writelog(str(e))
                        functions.writelog("Connect: API Connect failed (get trade history).")
                connecta = False
# def_updateticker()

def checkordage(handler):
	global orders, totcano
	for key in handler.getKeys():
		try:
	               	conn = btceapi.BTCEConnection()
	               	t = btceapi.TradeAPI(key, handler=handler)
	               	for o in orders:
                                if (config.tradecnlpro == True and o.pair == config.tradepair) or config.tradecnlpro == False:
                		        if o.type == 'sell':
				                if config.trademaxslife > 0:
		                                        tdelta = datetime.datetime.now() - o.timestamp_created
	                                                if tdelta.total_seconds() > config.trademaxslife:
	                       	                                if config.tradesimmod:
	                       	                                        if config.logorders:
	                       	                                                functions.writelog("Orders: Simulation: Cancelling sell order " + str(o.order_id) + " due to age.")
	                       	                                else:
	                       	                                	if config.logorders:
	                       	                                                functions.writelog("Orders: Cancelling sell order " + str(o.order_id) +" due to age.")
	                       	                                                try:
	                       	                                                        t.cancelOrder(o.order_id)            # kill the order!!!
	                                                                                totcano += 1
                         	                                                        connecta = True
	                       	                                                except:
	                       	                                                      	if config.logconnect:
                            	                                                      		functions.writelog(str(e))
                               	                                                               	functions.writelog("Connect: Unable to cancel sell order " + str(o.order_id) +" due to age.")
                               	                                                               	connecta = False
			                else:
				                if config.trademaxblife > 0:
                                                        tdelta = datetime.datetime.now() - o.timestamp_created
                                                        if tdelta.total_seconds() > config.trademaxblife:
                                                                if config.tradesimmod:
                                                                        if config.logorders:
                                                                                functions.writelog("Orders: Simulation: Cancelling buy order " + str(o.order_id) + " due to age.")
                                                                else:
                                                                	if config.logorders:
                                                                                functions.writelog("Orders: Cancelling buy order " + str(o.order_id) +" due to age.")
                                                                                try:
                                                                                        t.cancelOrder(o.order_id)            # kill the order!!!
	                                                                                totcano += 1
               	                       	                                                connecta = True
                                                                                except:
                                                                                        if config.logconnect:
                                                                                                functions.writelog(str(e))
                                                                                                functions.writelog("Connect: Unable to cancel buy order " + str(o.order_id) +" due to age.")
                                                                                                connecta = False
	        except Exception as e:
                        functions.writelog("Exception in checking age...")
	                if config.logconnect:
	                	functions.writelog(str(e))
	                	functions.writelog("Connect: API Connect failed (check order age).")
	                connecta = False
# def_checkordage()

def cancelall(handler):
	global orders, totcano
	for key in handler.getKeys():
		try:
	               	conn = btceapi.BTCEConnection()
	               	t = btceapi.TradeAPI(key, handler=handler)
	               	for o in orders:
                                if config.tradecnlpro:
                                        if o.pair == config.tradepair:
				                if o.type == 'sell':
                                                        if config.logorders:
                                                                functions.writelog("Orders: Cancelling sell order " + str(o.order_id) +" due to manual cancel.")
	                        	                try:
	                        	                        t.cancelOrder(o.order_id)            # kill the order!!!
                                                                totcano += 1
	                        	                        connecta = True
	                        	                except:
	                        	                        if config.logconnect:
	                               	                                functions.writelog(str(e))
	                               	                                functions.writelog("Connect: Unable to cancel sell order " + str(o.order_id) +" due to manual cancel.")
	                               	                        connecta = False
				                else:
                                                        if config.logorders:
                                                                functions.writelog("Orders: Cancelling buy order " + str(o.order_id) +" due to manual cancel.")
				                        try:
	                                                        t.cancelOrder(o.order_id)            # kill the order!!!
                                                                totcano += 1
	                                                        connecta = True
	                                                except:
	                                                        if config.logconnect:
	                                                                functions.writelog(str(e))
	                                                                functions.writelog("Connect: Unable to cancel buy order " + str(o.order_id) +" due to manual cancel.")
	                                                        connecta = False
                                else:
                                        if config.logorders:
                                                functions.writelog("Orders: Cancelling sell order " + str(o.order_id) +" due to manual cancel.")
	                                        try:
	                        	                t.cancelOrder(o.order_id)            # kill the order!!!
                                                        totcano += 1
	                        	                connecta = True
	                        	        except:
	                        	                if config.logconnect:
	                               	                        functions.writelog(str(e))
	                               	                        functions.writelog("Connect: Unable to cancel sell order " + str(o.order_id) +" due to manual cancel.")
	                               	                connecta = False
				        else:
                                                if config.logorders:
                                                        functions.writelog("Orders: Cancelling buy order " + str(o.order_id) +" due to manual cancel.")
				                try:
	                                                t.cancelOrder(o.order_id)            # kill the order!!!
                                                        totcano += 1
	                                                connecta = True
	                                        except:
	                                                if config.logconnect:
	                                                        functions.writelog(str(e))
	                                                        functions.writelog("Connect: Unable to cancel buy order " + str(o.order_id) +" due to manual cancel.")
	                                                connecta = False
	        except Exception as e:
	                if config.logconnect:
	                	functions.writelog(str(e))
	                	functions.writelog("Connect: API Connect failed (check order age).")
	                connecta = False
# def_cancelall()


def getorders(handler):
	global orders
	orders = ""
        for key in handler.getKeys():
                try:
	                conn = btceapi.BTCEConnection()
	                t = btceapi.TradeAPI(key, handler=handler)
			orders = t.orderList(connection = conn)
	                connecta = True
                except Exception as e:
			if str(e) <> "OrderList call failed with error: no orders":
				if config.logconnect:
					functions.writelog(str(e))
					functions.writelog("Connect: API Connect failed (get orders).")
	                        connecta = False
# def_getorders()


def getrights(handler, botright):
        for key in handler.getKeys():
		try:
	                conn = btceapi.BTCEConnection()
	                t = btceapi.TradeAPI(key, handler=handler)
			r = t.getInfo(connection = conn)
			botright[0] = r.info_rights
			botright[1] = r.trade_rights
			botright[2] = r.withdraw_rights
                        connecta = True
                except Exception as e:
			botright[0] = ""
			botright[1] = ""
			botright[2] = ""
			if config.logconnect:
				functions.writelog(str(e))
				functions.writelog("Connect: API Connect failed (get rights).")
                        connecta = False
# def_getrights()


def getcurrency(balancec, balancea, balanceo):
        p = 0
        for currency in btceapi.all_currencies:
		balancec.append(1)
                balancea.append(1)
                balanceo.append(1)
                balancec[p] = currency
		balancea[p] = 0
		balanceo[p] = 0
                p += 1
# def_getcurrency()

def getbalance(handler, balancec, balancea, balanceo):
	global connecta
	for key in handler.getKeys():
		conn = btceapi.BTCEConnection()
		t = btceapi.TradeAPI(key, handler=handler)
		try:
			connecta = True
			r = t.getInfo(connection = conn)
			for p in range(0,len(balancec)):
				balanceo[p] = balancea[p]
       				balancea[p] = getattr(r, "balance_" + balancec[p])
				p += 1
		except Exception as e:
			if config.logconnect:
				functions.writelog(str(e))
				functions.writelog("Connect: API Connect failed (get balance).")
		        connecta = False
# def_getbalance()




def startconnect(handler):
        try:
                with open('key_file'): 
                        key_file = "key_file"
                        handler = btceapi.KeyHandler(key_file, resaveOnDeletion=True)
        	        return handler;
        except IOError:
                functions.createkeyfile()
# def_startconnect()

def chknw():
	global connectw
	try:
		url = urllib2.urlopen(config.btceurl, timeout = config.btcesoctim )
	except Exception as e:
		connectw = False
		if config.logconnect:
			functions.writelog(str(e))
			functions.writelog("Connect: Connection to webpage failed.")
		if config.btcealrsnd:
			print "\a"						# Sound bell if no network
	else:
		connectw = True
# def_chknw()

def logstart(handler):
	if config.logenable:
		if config.logrun:
			if config.logtrade:
				functions.writelog("Trade: Trading pair " + config.tradepair) 
				if config.tradestyle == "sfb":
					functions.writelog("Trade: Tradestyle set to Slow Fixed Buy.")
					functions.writelog("Trade: On buy using " + str(config.tradelowlim) + " as max rate.")
				elif config.tradestyle == "sfs":
					functions.writelog("Trade: Tradestyle set to Slow Fixed Sell.")
					functions.writelog("Trade: On sell using " + str(config.tradehighlim) + " as min rate.")
				elif config.tradestyle == "sfc":
					functions.writelog("Trade: Tradestyle set to Slow Fixed Combined.")
					functions.writelog("Trade: On buy using " + str(config.tradelowlim) + " as max rate.")
					functions.writelog("Trade: On sell using " + str(config.tradehighlim) + " as min rate.")
				elif config.tradestyle == "pat":
					functions.writelog("Trade: Tradestyle set to PAired Trading.")
					functions.writelog("Trade: On buy using " + str(config.tradeprcbuy) + "% downward margin.")
					functions.writelog("Trade: On sell using " + str(config.tradeprcsell) + "% upward margin.")
				elif config.tradestyle == "vab":
					functions.writelog("Trade: Tradestyle set to VAriable Buy.")
					functions.writelog("Trade: On buy using " + str(config.tradeprcbuy) + "% downward margin.")
				elif config.tradestyle == "vas":
					functions.writelog("Trade: Tradestyle set to VAriable Sell.")
					functions.writelog("Trade: On sell using " + str(config.tradeprcsell) + "% upward margin.")
				if config.tradepoa == "none":
					functions.writelog("Trade: Not compensating amount or price on orders.")
				elif config.tradepoa == "price":
					functions.writelog("Trade: Compensating order prices.")
				elif config.tradepoa == "amount":
					functions.writelog("Trade: Compensating order amounts.")
				functions.writelog("Trade: Max buy orders " + str(config.trademaxbuy))
				functions.writelog("Trade: Max sell orders " + str(config.trademaxsell))
				functions.writelog("Trade: Trade interval " + str(config.tradeinterval) + " seconds.")
				if config.trademaxblife > 0:
					functions.writelog("Trade: Buy orders will expire in  " + str(config.trademaxblife) + " seconds." )
				else:
					functions.writelog("Trade: Buy orders will not expire." )
                                if config.trademaxslife > 0:
                                        functions.writelog("Trade: Sell orders will expire in  " + str(config.trademaxslife) + " seconds." )
                                else:
                                        functions.writelog("Trade: Sell orders will not expire." )
				if config.tradeendcnl:
					functions.writelog("Trade: All open orders will be cancelled on program exit.")
				else:
					functions.writelog("Trade: Open orders will not be cancelled on program exit.")
				if config.tradesimmod:
					functions.writelog("Trade: Starting yabb in simulation mode.")
				else:
					functions.writelog("Trade: Starting yabb in trading mode.")
				if config.tradeonhold:
					functions.writelog("Trade: Starting yabb in trading hold mode, holding new orders.")
				else:
					functions.writelog("Trade: Starting yabb in trading mode, not holding placement of new orders.")

		if config.logbalance:
			functions.writelog("Balance: Opening balance:")
			for p in range(0,len(balancec)):
	                	functions.writelog("Balance: " + balancec[p]+ " = " +  str('{0:f}'.format(balancea[p]))) 
                        glob.openbalance = functions.getbtcbalance(handler)
                        functions.writelog("Balance: Including open orders in BTC: " + str(glob.openbalance))

# def_logstart

def show():
	global totbuyo
	system('cls' if name=='nt' else 'clear')
	print " "
	print c.udl + (70 * " ") + "yabb v0.1" + c.rst
	print " Started:", glob.starttime, "   Last run:", strftime('%d-%m-%Y %H:%M'), 
	print "     runtime:", str(datetime.timedelta(seconds=round(default_timer() - glob.runtime)))

	if config.shownetwork:
		print (79 * "_")
		print " Trading:",
	        if not config.tradesimmod:
	                print c.grn + u"\u26AB" + c.rst,
	        else:
	                print c.red + u"\u26AB" + c.rst,
		print "  BTC-e:",
	        if connectw:
			print c.grn + u"\u26AB" + c.rst,
	        else:
	                print c.red + u"\u26AB" + c.rst,
		print "  API:",
	        if connecta:
	                print c.grn + u"\u26AB" + c.rst,
	        else:
	                print c.red + u"\u26AB" + c.rst,
		print "  Info:",
	        if botright[0]:
	                print c.grn + u"\u26AB" + c.rst,
	        else:
	                print c.red + u"\u26AB" + c.rst,
	        print "  Trade:",
	        if botright[1]:
	                print c.grn + u"\u26AB" + c.rst,
	        else:
	                print c.red + u"\u26AB" + c.rst,
	        print "  Withdraw:",
	        if botright[2]:
	                print c.grn + u"\u26AB" + c.rst
	        else:
	                print c.red + u"\u26AB" + c.rst

	if config.showtrade:
		print (79 * "_")
		print " Trade settings: "
		print "  - trading pair .", c.inv + config.tradepair + c.rst,
		print "     - buy per . . . . . .", c.inv + string.rjust(str(config.tradeamtbuy),7) + c.rst
		print "  - interval . . .", c.inv + string.rjust(str(config.tradeinterval),3) + c.rst,
		print "         - sell per. . . . . .", c.inv + string.rjust(str(config.tradeamtsell),7) + c.rst
		print "  - interval mod .", c.inv + string.rjust(str(config.tradeitvmod),3) + c.rst,
		print "         - price change up . .", c.inv + string.rjust(str(config.tradeprcbuy),7)+ c.rst + "%"
		print "  - trade cost . .", c.inv + string.rjust(str(config.tradecost),7)+ c.rst + "%",
		print "    - price change down .", c.inv + string.rjust(str(config.tradeprcsell),7)+ c.rst + "%"

	if config.showbalance:
		print (79 * "_")
	        print " Balance: ",
		for p in range(0, len(balancec),3):
			print " "
			if balancea[p] == balanceo[p] and balancea[p] <> 0:
				print "  - " + '{:4s}'.format(balancec[p]), c.inv + '{:16.8f}'.format(balancea[p]) + c.rst,
			elif balancea[p] > balanceo[p]:
				print "  - " + '{:4s}'.format(balancec[p]), c.bup + '{:16.8f}'.format(balancea[p]) + c.rst,
			elif balancea[p] == 0:
				print "  - " + '{:4s}'.format(balancec[p]), c.lgr + '{:16.8f}'.format(balancea[p]) + c.rst,
			else:
				print "  - " + '{:4s}'.format(balancec[p]), c.bdn + '{:16.8f}'.format(balancea[p]) + c.rst,
			if p+1 < len(balancec):
		                if balancea[p+1] == balanceo[p+1] and balancea[p+1] <> 0:
		                        print "  - " + '{:4s}'.format(balancec[p+1]), c.inv + '{:16.8f}'.format(balancea[p+1]) + c.rst,
		                elif balancea[p+1] > balanceo[p+1]:
		                        print "  - " + '{:4s}'.format(balancec[p+1]), c.bup + '{:16.8f}'.format(balancea[p+1]) + c.rst,
				elif balancea[p+1] == 0:
	                                print "  - " + '{:4s}'.format(balancec[p+1]), c.lgr + '{:16.8f}'.format(balancea[p+1]) + c.rst,
		                else:
		                        print "  - " + '{:4s}'.format(balancec[p+1]), c.bdn + '{:16.8f}'.format(balancea[p+1]) + c.rst,
	                if p+2 < len(balancec):
	                       if balancea[p+2] == balanceo[p+2] and balancea[p+2] <> 0:
	                                print "  - " + '{:4s}'.format(balancec[p+2]), c.inv + '{:16.8f}'.format(balancea[p+2]) + c.rst,
	                       elif balancea[p+2] > balanceo[p+2]:
	                                print "  - " + '{:4s}'.format(balancec[p+2]), c.bup + '{:16.8f}'.format(balancea[p+2]) + c.rst,
	                       elif balancea[p+2] == 0:
	                                print "  - " + '{:4s}'.format(balancec[p+2]), c.lgr + '{:16.8f}'.format(balancea[p+2]) + c.rst,
	                       else:
	                                print "  - " + '{:4s}'.format(balancec[p+2]), c.bdn + '{:16.8f}'.format(balancea[p+2]) + c.rst,
		print " "							# needed for newline

	if config.showticker:
		print (79 * "_")
		print " Ticker:"
		print " " + tickbuy
		print " " + ticksell	

        if config.showtrend:
                print (79 * "_")
                print " SMA:"
                print " " + trends

        if config.showordcnt:
		print (79 * "_")
                print " Total -Buy orders:" + str(glob.totbuyo) + " -Sell orders:" + str(glob.totsello) + " -Cancelled orders:" + str(totcano) + " -Missed orders:" + str(glob.totmiso)

	if config.showorders:
                ordbuy = 0
                ordsell = 0
	        for o in orders:
			if o.type == "buy":
		        	ordbuy += 1
			else:
		        	ordsell += 1
		print (79 * "_")
		print " Open orders (" + str(ordbuy) + "/" + str(ordsell) + "): "
		print " id       Type  Pair         Rate           Amount          Created"
	        for o in orders:
	        	print '{:9}'.format(o.order_id),
			if o.type == "buy":
		        	print c.grn + '{:5}'.format(o.type) + c.rst,
			else:
		        	print c.red + '{:5}'.format(o.type) + c.rst,
	        	print '{:9}'.format(o.pair),
	        	print '{:16.8f}'.format(o.rate),
	        	print '{:16.8f}'.format(o.amount),
                        if (config.tradecnlpro == True and o.pair == config.tradepair) or config.tradecnlpro == False:
                                if o.type == "sell":
                                        if config.trademaxslife <> 0:           # Will they expire?
                                                tdelta = int((((functions.timestamp(datetime.datetime.now())-functions.timestamp(o.timestamp_created))*100)/config.trademaxslife))
                                                tts = str(o.timestamp_created)
                                                if int(tdelta) < 25:                                              # Less then 25% passed = black
                                                        print c.grn + tts[0:2] + c.rst + tts[2:19]
                                                elif int(tdelta) < 50:                                            # Less then 50% passed = green
                                                        print c.grn + tts[0:6] + c.rst + tts[6:19]
                                                elif int(tdelta) < 75:                                            # Less then 75% passed = yellow
                                                        print c.yel + tts[0:12] + c.rst + tts[12:19]
                                                elif int(tdelta) < 90:                                            # Less then 90% passed = red
                                                        print c.red + tts[0:17] + c.rst + tts[17:19]
                                                else:                                                             # About to get cancelled.... = red
                                                        print c.red + tts + c.rst
                                        else:
                                                print o.timestamp_created                                       # Not aging but is trading pair
                                else:
                                        if config.trademaxblife <> 0:           # Will they expire?
                                                tdelta = int((((functions.timestamp(datetime.datetime.now())-functions.timestamp(o.timestamp_created))*100)/config.trademaxblife))
                                                tts = str(o.timestamp_created)
                                                if int(tdelta) < 25:                                              # Less then 25% passed = black
                                                        print c.grn + tts[0:2] + c.rst + tts[2:19]
                                                elif int(tdelta) < 50:                                            # Less then 50% passed = green
                                                        print c.grn + tts[0:6] + c.rst + tts[6:19]
                                                elif int(tdelta) < 75:                                            # Less then 75% passed = yellow
                                                        print c.yel + tts[0:12] + c.rst + tts[12:19]
                                                elif int(tdelta) < 90:                                            # Less then 90% passed = red
                                                        print c.red + tts[0:17] + c.rst + tts[17:19]
                                                else:                                                           # About to get cancelled.... = red
                                                        print c.red + tts + c.rst
                                        else:
                                                print o.timestamp_created                                       # Not aging but is trading pair.
                        else:
                                print c.blu + str(o.timestamp_created) + c.rst                                  # Not aging and not trading pair.

	if config.showkeys:
		print (79 * "_")
		print         " q = quit  | + = increase wait | l = logfile",
                if config.logenable:
                        print "off",
                else:
                        print "on ",
                print " | r = reload config           "
		print         " p = pause | - = decrease wait | s = simmode",
	        if config.tradesimmod:
	                print "off  | h =", 
	        else:
	                print "on   | h =", 
	        if config.tradeonhold:
	                print "resume trading " 
	        else:
	                print "hold trades    "
		print         "                               | t = trade now",
                print "   | C = cancel all trades "

	print (79 * "_")
        print "                                    Enter your choice or wait for next cycle: ",
	stdout.flush()
	return
# def_show()

def main():
	global handler, orders, ordbuy, ordsell, connecta

        if version_info<(2,7,3):
                print("\n")
                print("You need python 2.7.3 or later to run this script\n")
                exit(1)


	ordbuy = 0
	ordsell = 0
	connecta =  False
	keypress = " "							# user input var
	runstatus = 1							# execution loop control
	for t in range(0,3):
		botright.append("")
	chknw()								# Is btc-e online
	handler = startconnect(handler)					# Open a connection
	getcurrency(balancec, balancea, balanceo)			# Get currencies
	getbalance(handler, balancec, balancea, balanceo)		# Get balance per currency
	getrights(handler, botright)
	logstart(handler)
	updateticker()
	getorders(handler)
	while runstatus == 1: 
		show()							# update the screen
		rlist, _, _ = select.select([stdin], [], [], config.tradeinterval)
								 	# get input or timeout
		if rlist:						# something was entered
			keypress = stdin.readline().strip() 	# get the user input without \n
			if keypress == "q":				# quit the bot
				runstatus = 0				

			if keypress == "C":				# Cancel all trades)
                                if config.logrun:
                                       functions.writelog("Run: Cancel all trades requested.")
	        		print "                                   Cancelling all open orders.  "		# Reloaded
                                cancelall(handler)
			        getorders(handler)                                                                      # Check active orders

			if keypress == "t":				# reload the config file (changed settings?)
                                if config.logrun:
                                       functions.writelog("Run: Manual trade triggered.")
                                if config.tradeonhold:                  # Trading paused?
                                       functions.writelog("Run: Overriding tradeonhold = True.")
			        checkordage(handler)                                                    # Check if orders need canceling
			        if connecta:								# api is working
				        trading.dotrade(handler, lastrate, balancec, balancea)		# Check and perform trading
			if keypress == "r":				# reload the config file (changed settings?)
				reload(config)
                                if config.logrun:
                                        functions.writelog("Run: Configuration file 'config.py' reloaded.")
	        		print "                                   Configuration settings reloaded.  "		        # Reloaded
                                sleep(2)
			if keypress == "p":				# pause execution
				system('cls' if name=='nt' else 'clear')
                                if config.logrun:
                                        functions.writelog("Run: Execution paused.")
				print "                Execution paused, press Enter to continue..."
 				stdin.readline()
                                if config.logrun:
                                        functions.writelog("Run: Execution resumed.")
                        if keypress == "s":
                                if config.tradesimmod:
                                        config.tradesimmod = False
                                        if config.logrun:
                                                functions.writelog("Run: Switching trademode to Trade.")
                                else:
                                        config.tradesimmod = True
                                        if config.logrun:
                                                functions.writelog("Run: Switching trademode to Simulation.")
                        if keypress == "h":
                                #functions.writelog("Testing: config.tradeonhold = " + str(config.tradeonhold))
                                if config.tradeonhold:
                                        config.tradeonhold = False
                                        if config.logrun:
                                                functions.writelog("Run: Resuming trading after hold.")
                                else:
                                        config.tradeonhold = True
                                        if config.logrun:
                                                functions.writelog("Run: Hold on all new trading.")
			if keypress == "l":
				if config.logenable:
					if config.logrun:
						functions.writelog("Run: Switching logmode off.")
					config.logenable = False
				else:
					config.logenable = True
					if config.logrun:
						functions.writelog("Run: Switching logmode on.")
			if keypress == "+":                             # increase trade interval
				config.tradeinterval = config.tradeinterval + config.tradeitvmod 
				if config.logrun:
					functions.writelog("Run: Trade interval increased to " + str(config.tradeinterval) + " seconds.")
                        if keypress == "-":                             # decrease trade interval
                                config.tradeinterval = config.tradeinterval - config.tradeitvmod  
				if config.tradeinterval < 1:
					config.tradeinterval = 1	# keep trade interval positive
				if config.logrun:
					functions.writelog("Run: Trade interval decreased to " + str(config.tradeinterval) + " seconds.")
		else:
			print (55 * '\b'),
			print "Running trades & updating indices.                     "		        # terminated
			chknw()
                        if not config.tradeonhold:                                                      # Trading paused?
			        checkordage(handler)                                                    # Check if orders need canceling
			        if connecta:								# api is working
				        trading.dotrade(handler, lastrate, balancec, balancea)		# Check and perform trading
			getrights(handler, botright)                                                    # Get trading bot rights
        		updateticker()                                                          # Update the ticker
                        if config.showorders:
			        getorders(handler)                                                      # Check active orders
                        if config.showbalance:
        			getbalance(handler, balancec, balancea, balanceo)                       # Get updated bbbbbalance information

	#return
# def_main()


system('cls' if name=='nt' else 'clear')
print "                Starting Yet Another Bitcoin Bot..."

if config.logenable:
	if config.logrun:
		functions.writelog("----------------------------------------------------------------------------")
		functions.writelog("Run: Yabb starting.")

main()									                # call main procedure

system('cls' if name=='nt' else 'clear')				                # clear screen

if config.tradeendcnl:
        cancelall(handler)

if config.logbalance:
	functions.writelog("Balance: Closing balance:")
	for p in range(0,len(balancec)):
               	functions.writelog("Balance: " + balancec[p]+ " = " +  str('{0:f}'.format(balancea[p]))) 
        glob.closebalance = functions.getbtcbalance(handler)
        functions.writelog("Balance: Including open orders in BTC: " + str(glob.closebalance))
        print " "
        print "                 Opening balance was " + str(glob.openbalance)		# terminated
        print "                 Closing balance is  " + str(glob.closebalance)		# terminated
        print " "

print "                   YABB terminated on user request.   "		                # terminated
print " "

if config.logenable:
	if config.logrun:
		functions.writelog("Run: Yabb processing terminated.")
# done....
