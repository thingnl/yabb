import config, time 
import glob
from os import system, name
from sys import exit
from btceapi import btceapi 

def writelog(logline):
        if config.logenable:
                with open(config.logfile,"a") as f:
                        line = str(time.strftime('%Y-%m-%d %H:%M:%S')) + " - " + logline + "\n"
                        f.write(line)
# def_writelog


def timestamp(date):
        return time.mktime(date.timetuple())
# def_timestamp


def createkeyfile():
        try:
                f = open("key_file", "wb",0)                                    # Create keyfile needed by btceapi
                f.write(config.btceapikey)                                      # Add api key
                f.write('\n')
                f.write(config.btceapisec)                                      # Add secure string
                f.write('\n')
                f.write(str(int(round(time.time()))))                           # Add "random" interger
                f.write('\n')
                f.flush()
                f.close()
                system('cls' if name=='nt' else 'clear')                  # clear screen
                print "     Configuration written, please restart YABB.  "      # terminated
                print " "
                exit()
        except IOError as (errno,strerror):
                print "I/O error({0}): {1}".format(errno, strerror)
# def_createkeyfile()


def getbtcbalance(handler):
        pointer = 0
        balance = []
        curname = []

        for key in handler.getKeys():
                conn = btceapi.BTCEConnection()
                t = btceapi.TradeAPI(key, handler=handler)

                try:                                            # curencies and balances
                        r = t.getInfo(connection = conn)
                        for key in handler.getKeys():
                                for currency in btceapi.all_currencies:
                                        balance.append(1)
                                        curname.append(1)
                                        balance[pointer] = getattr(r, "balance_" + currency)
                                        curname[pointer] = currency
                                        pointer += 1
                except:
                        whatever = "voutje bedankt"

                balance.append(1)                               # Add some space for the totals
                curname.append(1)
                balance[-1] = 0
                curname[-1] = "tot"

                try:                                            # add currency stuck in orders
                        r = t.getInfo(connection = conn)
                        glob.orders = t.orderList(connection = conn)
                        for o in glob.orders:
                                pointer = 0                                
                                if o.pair == "btc_usd":
                                        if o.type == "sell":
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "btc":
                                                                balance[pointer] = balance[pointer] + o.amount
                                                        pointer += 1
                                        else:
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "usd":
                                                                balance[pointer] = balance[pointer] + o.amount * o.rate
                                                        pointer += 1
                                elif o.pair == "ltc_btc":
                                        if o.type == "sell":
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "ltc":
                                                                balance[pointer] = balance[pointer] + o.amount
                                                        pointer += 1
                                        else:
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "btc":
                                                                balance[pointer] = balance[pointer] + o.amount * o.rate
                                                        pointer += 1
                                elif o.pair == "btc_rur":
                                        if o.type == "sell":
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "btc":
                                                                balance[pointer] = balance[pointer] + o.amount
                                                        pointer += 1
                                        else:
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "rur":
                                                                balance[pointer] = balance[pointer] + o.amount * o.rate
                                                        pointer += 1
                                elif o.pair == "btc_eur":
                                        if o.type == "sell":
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "btc":
                                                                balance[pointer] = balance[pointer] + o.amount
                                                        pointer += 1
                                        else:
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "eur":
                                                                balance[pointer] = balance[pointer] + o.amount * o.rate
                                                        pointer += 1
                                elif o.pair == "ltc_usd":
                                        if o.type == "sell":
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "ltc":
                                                                balance[pointer] = balance[pointer] + o.amount
                                                        pointer += 1
                                        else:
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "usd":
                                                                balance[pointer] = balance[pointer] + o.amount * o.rate
                                                        pointer += 1
                                elif o.pair == "ltc_rur":
                                        if o.type == "sell":
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "ltc":
                                                                balance[pointer] = balance[pointer] + o.amount
                                                        pointer += 1
                                        else:
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "rur":
                                                                balance[pointer] = balance[pointer] + o.amount * o.rate
                                                        pointer += 1
                                elif o.pair == "nmc_btc":
                                        if o.type == "sell":
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "nmc":
                                                                balance[pointer] = balance[pointer] + o.amount
                                                        pointer += 1
                                        else:
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "btc":
                                                                balance[pointer] = balance[pointer] + o.amount * o.rate
                                                        pointer += 1
                                elif o.pair == "usd_rur":
                                        if o.type == "sell":
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "usd":
                                                                balance[pointer] = balance[pointer] + o.amount
                                                        pointer += 1
                                        else:
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "rur":
                                                                balance[pointer] = balance[pointer] + o.amount * o.rate
                                                        pointer += 1
                                elif o.pair == "eur_usd":
                                        if o.type == "sell":
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "eur":
                                                                balance[pointer] = balance[pointer] + o.amount
                                                        pointer += 1
                                        else:
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "usd":
                                                                balance[pointer] = balance[pointer] + o.amount * o.rate
                                                        pointer += 1
                                elif o.pair == "nvc_btc":
                                        if o.type == "sell":
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "nvc":
                                                                balance[pointer] = balance[pointer] + o.amount
                                                        pointer += 1
                                        else:
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "btc":
                                                                balance[pointer] = balance[pointer] + o.amount * o.rate
                                                        pointer += 1
                                elif o.pair == "trc_btc":
                                        if o.type == "sell":
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "trc":
                                                                balance[pointer] = balance[pointer] + o.amount
                                                        pointer += 1
                                        else:
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "btc":
                                                                balance[pointer] = balance[pointer] + o.amount * o.rate
                                                        pointer += 1
                                elif o.pair == "ppc_btc":
                                        if o.type == "sell":
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "ppc":
                                                                balance[pointer] = balance[pointer] + o.amount
                                                        pointer += 1
                                        else:
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "btc":
                                                                balance[pointer] = balance[pointer] + o.amount * o.rate
                                                        pointer += 1
                                elif o.pair == "ftc_btc":
                                        if o.type == "sell":
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "ftc":
                                                                balance[pointer] = balance[pointer] + o.amount
                                                        pointer += 1
                                        else:
                                                for p in range(0,len(balance)):        
                                                        if curname[pointer] == "btc":
                                                                balance[pointer] = balance[pointer] + o.amount * o.rate
                                                        pointer += 1
                except:
                        whatever = "voutje bedankt"

                r = 0
                for p in range(0,len(curname)-1):
                        if curname[r] == "btc":
                                balance[-1] = balance[-1] + balance[r]
                        elif curname[r] == "ltc":
                                history = btceapi.getTradeHistory("ltc_btc")
                                balance[-1] = balance[-1] + ( history[0].price * balance[r] )
                        elif curname[r] == "usd":
                                history = btceapi.getTradeHistory("btc_usd")
                                balance[-1] = balance[-1] + ( balance[r] / history[0].price )
                        elif curname[r] == "rur":
                                history = btceapi.getTradeHistory("btc_rur")
                                balance[-1] = balance[-1] + ( history[0].price * balance[r] )
                        elif curname[r] == "eur":
                                history = btceapi.getTradeHistory("btc_eur")
                                balance[-1] = balance[-1] + ( history[0].price * balance[r] )
                        elif curname[r] == "nmc":
                                history = btceapi.getTradeHistory("nmc_btc")
                                balance[-1] = balance[-1] + ( history[0].price * balance[r] )
                        elif curname[r] == "nvc":
                                history = btceapi.getTradeHistory("nvc_btc")
                                balance[-1] = balance[-1] + ( history[0].price * balance[r] )
                        elif curname[r] == "trc":
                                history = btceapi.getTradeHistory("trc_btc")
                                balance[-1] = balance[-1] + ( history[0].price * balance[r] )
                        elif curname[r] == "ppc":
                                history = btceapi.getTradeHistory("ppc_btc")
                                balance[-1] = balance[-1] + ( history[0].price * balance[r] )
                        elif curname[r] == "ftc":
                                history = btceapi.getTradeHistory("ftc_btc")
                                balance[-1] = balance[-1] + ( history[0].price * balance[r] )
                        r += 1

                return balance[-1]
# def_getbtcbalance()




