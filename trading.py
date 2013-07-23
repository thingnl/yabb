import config, functions
import glob
from btceapi import btceapi

def tradesfb(handler):			                                # Slow Fixed Buy
	rate=0
	glob.lastrate=float(glob.lastrate)
	checkordcnt(handler)	
	if glob.ordbuy < config.trademaxbuy:					                                # Not to many open buy orders?
		if glob.lastrate < config.tradelowlim:			                                # Rate low enough?
			if config.tradepoa == "amount":
				amount = (config.tradeamtbuy*100)/(100-config.tradecost)
				rate = glob.lastrate
			elif config.tradepoa == "price":
				amount = config.tradeamtbuy
				rate = (glob.lastrate*(100-config.tradecost))/100
			else:
				amount = config.tradeamtbuy
				rate = glob.lastrate
			if amount < 0.1:				                                # BTC-e minimal order size
				amount = 0.1
			if (amount * rate ) <= checkbalance(config.tradepair[-3:]):	# Do we have enough pecunia
				if config.tradesimmod:							# Are we simulating?
					if config.logorders:
				                functions.writelog("Orders: Simulate: Placing buy order: " +  str(amount) + " @ " + str(rate) + " (original " + str(config.tradeamtbuy) + " @ " + str(glob.lastrate) +  ").")
				else:									# We are not simulating!
	                                conn = btceapi.BTCEConnection()
	                                t = btceapi.TradeAPI(config.btceapikey, handler=handler)
					traderesult = t.trade(config.tradepair, "buy", rate, amount)
					if traderesult:
						if config.logorders:
					                functions.writelog("Orders: Placing buy order " + str(traderesult.order_id) + ": " +  str(amount) + " @ " + str('{0:f}'.format(rate)) + " (original " + str(config.tradeamtbuy) + " @ " + str('{0:f}'.format(glob.lastrate)) + ").")
                                                glob.totbuyo += 1
                                        else:
                                                glob.totmiso += 1
                                                if config.logorders:
                                                        functions.writelog("Orders: Placing buy order failed by API.")
			else:						                                # We can't afford this.... 
		                functions.writelog("Orders: Buy order NOT placed: Balance insufficient. Balance: " +  str('{0:f}'.format(checkbalance(config.tradepair[-3:]))) + ", Required: " + str(amount * rate) +  ".")
                                glob.totmiso += 1
		else:							                                # Way to expensive
                        glob.totmiso += 1
			functions.writelog("Trade: Skip placing buy order. Current rate (" + str(glob.lastrate) + ") equal to or over lower limit (" + str(config.tradelowlim) + ").")
	else:								                                # To many open orders... maybe cancel a couple
                glob.totmiso += 1
		functions.writelog("Trade: Skip placing buy order. Max open buy order " + str(config.trademaxbuy) + " limit reached.")
# def_tradesfb()

def tradesfs(handler):                                                    # Slow fixed sell
        rate=0
        glob.lastrate=float(glob.lastrate)
        checkordcnt(handler)
        if glob.ordsell < config.trademaxsell:				                                # Not to many open sell orders?
                if glob.lastrate > config.tradehighlim:			                                # Rate high enough?
                        if config.tradepoa == "amount":
				amount = (config.tradeamtbuy * 100)/ (100 - config.tradecost)
                                rate = glob.lastrate
                        elif config.tradepoa == "price":
                                amount = config.tradeamtbuy
				rate = (glob.lastrate * 100)/(100 - config.tradecost)
                        else:
                                amount = config.tradeamtbuy
                                rate = glob.lastrate
                        if amount < 0.1:                                                                # BTC-e minimal order size
                                amount = 0.1
                        if amount <= checkbalance(config.tradepair[0:3]):            # Do we have enough to sell
                                if config.tradesimmod:                                                  # Are we simulating?
                                        if config.logorders:
                                                functions.writelog("Orders: Simulate: Placing sell order: " +  str(amount) + " @ " + str(rate) + " (original " + str(config.tradeamtbuy) + " @ " + str(glob.lastrate) +  ").")
                                else:                                                                   # We are not simulating!
                                        conn = btceapi.BTCEConnection()
                                        t = btceapi.TradeAPI(config.btceapikey, handler=handler)
                                        traderesult = t.trade(config.tradepair, "sell", rate, amount)
					if traderesult:
                                                glob.totsello += 1
	                                        if config.logorders:
	                                                functions.writelog("Orders: Placing sell order " + str(traderesult.order_id) + ": " +  str(amount) + " @ " + str('{0:f}'.format(rate)) + " (original " + str(config.tradeamtbuy) + " @ " + str('{0:f}'.format(glob.lastrate)) + ").")
                                        else:
                                                glob.totmiso += 1
                                                if config.logorders:
                                                        functions.writelog("Orders: Placing sell order failed by API.")
                        else:                                                                           # We can't afford this.... 
                                glob.totmiso += 1
                                functions.writelog("Orders: Sell order NOT placed: Balance insufficient. Balance: " +  str('{0:f}'.format(checkbalance(config.tradepair[0:3]))) + ", Required: " + str(amount) +  ".")
                else:                                                                                   # Way to expensive
                        glob.totmiso += 1
                        functions.writelog("Trade: Skip placing sell order. Current rate (" + str(glob.lastrate) + ") under minimal limit (" + str(config.tradehighlim) + ").")
        else:                                                                                           # To many open orders... maybe cancel a couple
                glob.totmiso += 1
                functions.writelog("Trade: Skip placing sell order. Max open sell order " + str(config.trademaxsell) + " limit reached.")
# def_tradesfs()

def tradesfc(handler):				                        # Slow Fixed Combined
	tradesfb(handler)
	tradesfs(handler)
# def_tradesfc()

################################################################
def tradesvb():                         # Slow variable buy
        p = 1
# def_tradesvb()
def tradesvs():                         # Slow variable sell
        p = 1
# def_tradesvs()
def tradesvc():                         # Slow variable combined  
        p = 1
# def_tradesvc()
################################################################

def tradevab(handler):							# VAriable Buy
	rate=0
        glob.lastrate=float(glob.lastrate)
        checkordcnt(handler)
        if glob.ordbuy < config.trademaxbuy:                                 				# Not to many open buy orders?
		comprate =  (glob.lastrate * (100 - config.tradeprcbuy)) / 100				# Compensate lastrate for buy percentage
                if config.tradepoa == "amount":
                        amount = (config.tradeamtbuy*100)/(100-config.tradecost)
                        rate = comprate
                elif config.tradepoa == "price":
                        amount = config.tradeamtbuy
                        rate = (comprate*(100-config.tradecost))/100
                else:
                        amount = config.tradeamtbuy
                        rate = comprate
                if amount < 0.1:                                					# BTC-e minimal order size
                        amount = 0.1
                if (amount * rate ) < checkbalance(config.tradepair[-3:]):          # Do we have enough pecunia
                        if config.tradesimmod:                                                          # Are we simulating?
                                if config.logorders:
                                        functions.writelog("Orders: Simulate: Placing buy order: " +  str(amount) + " @ " + str(rate) + " (original " + str(config.tradeamtbuy) + " @ " + str(glob.lastrate) +  ").")
                        else:                                                                           # We are not simulating!
                                try:
                                        conn = btceapi.BTCEConnection()
                                        t = btceapi.TradeAPI(config.btceapikey, handler=handler)
                                        traderesult = t.trade(config.tradepair, "buy", rate, amount)
                                        if traderesult:
                                                glob.totbuyo += 1
	                                        if config.logorders:
	                                                functions.writelog("Orders: Placing buy order " + str(traderesult.order_id) + ": " +  str(amount) + " @ " + str('{0:f}'.format(rate)) + " (original " + str(config.tradeamtbuy) + " @ " + str('{0:f}'.format(glob.lastrate)) + ").")
                                        else:
                                                glob.totmiso += 1
                                                if config.logorders:
	                                                functions.writelog("Orders: Placing buy order failed by API.")
                                except:
                                        glob.totmiso += 1
                                        if config.logorders:
                                                functions.writelog("Orders: API failed or order refused. Most likely a timing issue.")
		else:                                           					# We can't afford this.... 
                        glob.totmiso += 1
			functions.writelog("Orders: Buy order NOT placed: " + config.tradepair[-3:] + " balance insufficient. Balance: " +  str('{0:f}'.format(checkbalance(config.tradepair[-3:]))) + ", Required: " + str(amount * rate) +  ".")
	else:                                                           				# To many open orders... maybe cancel a couple
                glob.totmiso += 1
                functions.writelog("Trade: Skip placing buy order. Max open buy order " + str(config.trademaxbuy) + " limit reached.")
# def_tradevab()

def tradevas(handler):							# VAriable Sell
        rate=0
        glob.lastrate=float(glob.lastrate)
        checkordcnt(handler)
        if glob.ordsell < config.trademaxsell:                               				# Not to many open sell orders?
		comprate =  (glob.lastrate * (100 + config.tradeprcbuy)) / 100       			# Compensate lastrate for sell percentage
                if config.tradepoa == "amount":
                        amount = (config.tradeamtsell * 100)/ (100 - config.tradecost)
                        rate = comprate
                elif config.tradepoa == "price":
                        amount = config.tradeamtsell
                        rate = (comprate * 100)/(100 - config.tradecost)
                else:
                        amount = config.tradeamtsell
                        rate = comprate
                if amount < 0.1:                                					# BTC-e minimal order size
                        amount = 0.1
                if amount < checkbalance(config.tradepair[0:3]):                    # Do we have enough to sell
                        if config.tradesimmod:                                                          # Are we simulating?
                                if config.logorders:
                                        functions.writelog("Orders: Simulate: Placing sell order: " +  str(amount) + " @ " + str(rate) + " (original " + str(config.tradeamtbuy) + " @ " + str(glob.lastrate) +  ").")
                        else:                                                                           # We are not simulating!
                                try:
                                        conn = btceapi.BTCEConnection()
                                        t = btceapi.TradeAPI(config.btceapikey, handler=handler)
                                        traderesult = t.trade(config.tradepair, "sell", rate, amount)
                                        if traderesult:
                                                glob.totsello += 1
                                                if config.logorders:
                                                        functions.writelog("Orders: Placing sell order " + str(traderesult.order_id) + ": " +  str(amount) + " @ " + str('{0:f}'.format(rate)) + " (original " + str(config.tradeamtsell) + " @ " + str('{0:f}'.format(glob.lastrate)) + ").")
				        else:
                                                glob.totmiso += 1
                                                if config.logorders:
                                                        functions.writelog("Orders: Placing sell order failed by API.")
                                except:
                                        glob.totmiso += 1
                                        if config.logorders:
                                                functions.writelog("Orders: API failed or order refused. Most likely a timing issue.")
                else:                                                                                   # We can't afford this....
                        glob.totmiso += 1
			functions.writelog("Orders: Sell order NOT placed: " + config.tradepair[0:3] + " balance insufficient. Balance: " +  str('{0:f}'.format(checkbalance(config.tradepair[0:3]))) + ", Required: " + str(amount) +  ".")
	else:                                                           				# To many open orders... maybe cancel a couple
                glob.totmiso += 1
		functions.writelog("Trade: Skip placing sell order. Max open sell order " + str(config.trademaxsell) + " limit reached.")
# def_tradevas()


def tradepat(handler):							# PAired Trade
        tradevas(handler)
        tradevab(handler)
# def_tradepat()

################################################################
def tradefma():				# Fast moving average
	p = 1
# def_tradefma()
def tradesma():				# Slow moving average
	p = 1
# def_tradesma()
def tradeshl():				# Stochastic High-Low
	p = 1
# def_tradeshl()

################################################################

def dotrade(handler):
	if config.tradestyle == "sfb":
		tradesfb(handler)
	elif config.tradestyle == "sfs":
                tradesfs(handler)
	elif config.tradestyle == "sfc":
                tradesfc(handler)
	elif config.tradestyle == "vas":
                tradevas(handler)
	elif config.tradestyle == "vab":
                tradevab(handler)
	elif config.tradestyle == "pat":
                tradepat(handler)
	elif config.tradestyle == "fma":
                tradefma(handler)
	elif config.tradestyle == "sma":
                tradesma(handler)
	else:
                tradeshl()
# def_dotrade()

################################################################

def checkordcnt(handler):
        glob.ordbuy = 0                                                              # keep track n$
        glob.ordsell = 0                                                             # keep track n$
        for key in handler.getKeys():
                try:
                        conn = btceapi.BTCEConnection()
                        t = btceapi.TradeAPI(key, handler=handler)
                        glob.orders = t.orderList(connection = conn)
                        for o in glob.orders:
                                if o.type == "buy":
                                        glob.ordbuy += 1
                                else:
                                        glob.ordsell += 1
                except Exception as e:
                        if config.logconnect:
                                functions.writelog(str(e))
                                functions.writelog("Connection error: API Connect failed (check onumber open trades).")
                                glob.connecta = False
# def_checkordcnt()

################################################################

def checkbalance(currency):
        for p in range(0,len(glob.balancec)):
		if glob.balancec[p] == currency:
			rv = glob.balancea[p]
                p += 1
	return rv
# def_checkbalance()
