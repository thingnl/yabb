import sys

from btceapi import btceapi
    
if len(sys.argv) == 1:
        key_file = "key_file"
else:
        key_file = sys.argv[1]



handler = btceapi.KeyHandler(key_file, resaveOnDeletion=True)

#print len(btceapi.all_currencies)

pointer = 0
balance = []
curname = []

for key in handler.getKeys():
        conn = btceapi.BTCEConnection()
        t = btceapi.TradeAPI(key, handler=handler)

        print "Getting balance information........"
        try:                                            # curencies and balances
                r = t.getInfo(connection = conn)
                for key in handler.getKeys():
                        for currency in btceapi.all_currencies:
                                balance.append(1)
                                curname.append(1)
                                balance[pointer] = getattr(r, "balance_" + currency)
                                curname[pointer] = currency
                                print curname[pointer], '{:10.5f}'.format(balance[pointer])
                                pointer += 1
        except:
                whatever = "voutje bedankt"

        balance.append(1)                               # Add some space for the totals
        curname.append(1)
        balance[-1] = 0
        curname[-1] = "tot"

        print "Checking for any open orders......."
        try:                                            # add currency stuck in orders
                r = t.getInfo(connection = conn)
                orders = t.orderList(connection = conn)
                for o in orders:
                        #print "  processing order: " + str(o.order_id),
    #, o.type, o.pair, o.amount
                        pointer = 0                                
                        if o.pair == "btc_usd":
                                if o.type == "sell":
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "btc":
                                                        balance[pointer] = balance[pointer] + o.amount
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount))
                                                pointer += 1
                                else:
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "usd":
                                                        balance[pointer] = balance[pointer] + o.amount * o.rate
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount * o.rate))
                                                pointer += 1
                        elif o.pair == "ltc_btc":
                                if o.type == "sell":
                                        for p in range(0,len(balance)):        
                                                #print pointer, curname[pointer]
                                                if curname[pointer] == "ltc":
                                                        balance[pointer] = balance[pointer] + o.amount
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount))
                                                pointer += 1
                                else:
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "btc":
                                                        balance[pointer] = balance[pointer] + o.amount * o.rate
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount * o.rate))
                                                pointer += 1
                        elif o.pair == "btc_rur":
                                if o.type == "sell":
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "btc":
                                                        balance[pointer] = balance[pointer] + o.amount
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount))
                                                pointer += 1
                                else:
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "rur":
                                                        balance[pointer] = balance[pointer] + o.amount * o.rate
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount * o.rate))
                                                pointer += 1
                        elif o.pair == "btc_eur":
                                if o.type == "sell":
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "btc":
                                                        balance[pointer] = balance[pointer] + o.amount
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount))
                                                pointer += 1
                                else:
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "eur":
                                                        balance[pointer] = balance[pointer] + o.amount * o.rate
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount * o.rate))
                                                pointer += 1
                        elif o.pair == "ltc_usd":
                                if o.type == "sell":
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "ltc":
                                                        balance[pointer] = balance[pointer] + o.amount
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount))
                                                pointer += 1
                                else:
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "usd":
                                                        balance[pointer] = balance[pointer] + o.amount * o.rate
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount * o.rate))
                                                pointer += 1
                        elif o.pair == "ltc_rur":
                                if o.type == "sell":
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "ltc":
                                                        balance[pointer] = balance[pointer] + o.amount
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount))
                                                pointer += 1
                                else:
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "rur":
                                                        balance[pointer] = balance[pointer] + o.amount * o.rate
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount * o.rate))
                                                pointer += 1
                        elif o.pair == "nmc_btc":
                                if o.type == "sell":
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "nmc":
                                                        balance[pointer] = balance[pointer] + o.amount
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount))
                                                pointer += 1
                                else:
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "btc":
                                                        balance[pointer] = balance[pointer] + o.amount * o.rate
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount * o.rate))
                                                pointer += 1
                        elif o.pair == "usd_rur":
                                if o.type == "sell":
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "usd":
                                                        balance[pointer] = balance[pointer] + o.amount
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount))
                                                pointer += 1
                                else:
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "rur":
                                                        balance[pointer] = balance[pointer] + o.amount * o.rate
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount * o.rate))
                                                pointer += 1
                        elif o.pair == "eur_usd":
                                if o.type == "sell":
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "eur":
                                                        balance[pointer] = balance[pointer] + o.amount
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount))
                                                pointer += 1
                                else:
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "usd":
                                                        balance[pointer] = balance[pointer] + o.amount * o.rate
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount * o.rate))
                                                pointer += 1
                        elif o.pair == "nvc_btc":
                                if o.type == "sell":
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "nvc":
                                                        balance[pointer] = balance[pointer] + o.amount
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount))
                                                pointer += 1
                                else:
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "btc":
                                                        balance[pointer] = balance[pointer] + o.amount * o.rate
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount * o.rate))
                                                pointer += 1
                        elif o.pair == "trc_btc":
                                if o.type == "sell":
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "trc":
                                                        balance[pointer] = balance[pointer] + o.amount
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount))
                                                pointer += 1
                                else:
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "btc":
                                                        balance[pointer] = balance[pointer] + o.amount * o.rate
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount * o.rate))
                                                pointer += 1
                        elif o.pair == "ppc_btc":
                                if o.type == "sell":
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "ppc":
                                                        balance[pointer] = balance[pointer] + o.amount
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount))
                                                pointer += 1
                                else:
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "btc":
                                                        balance[pointer] = balance[pointer] + o.amount * o.rate
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount * o.rate))
                                                pointer += 1
                        elif o.pair == "ftc_btc":
                                if o.type == "sell":
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "ftc":
                                                        balance[pointer] = balance[pointer] + o.amount
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount))
                                                pointer += 1
                                else:
                                        for p in range(0,len(balance)):        
                                                if curname[pointer] == "btc":
                                                        balance[pointer] = balance[pointer] + o.amount * o.rate
                         #                               print "Order found with " + curname[pointer] + " worth " + str('{:10.5f}'.format(o.amount * o.rate))
                                                pointer += 1
        except:
                whatever = "voutje bedankt"

        print "Balance corrected for order........"
        r = 0
        for p in range(0,len(curname)):
                print curname[r], '{:10.5f}'.format(balance[r])
                r += 1



        print "Converting all curencies to BTC...."        
        r = 0
        print "Startbalance = " + str(balance[-1])
        for p in range(0,len(curname)-1):
                print "  processing currency: " + curname[r],
                if curname[r] == "btc":
                        balance[-1] = balance[-1] + balance[r]
                        print str('{:10.5f}'.format(balance[-1])), str('{:10.5f}'.format(balance[r]))
                elif curname[r] == "ltc":
                        history = btceapi.getTradeHistory("ltc_btc")
                        balance[-1] = balance[-1] + ( history[0].price * balance[r] )
                        print str('{:10.5f}'.format(balance[-1])), str('{:10.5f}'.format(history[0].price)), str('{:10.5f}'.format(balance[r])), str('{:10.5f}'.format(history[0].price * balance[r]))
                elif curname[r] == "usd":
                        history = btceapi.getTradeHistory("btc_usd")
                        balance[-1] = balance[-1] + ( balance[r] / history[0].price )
                        print str('{:10.5f}'.format(balance[-1])), str('{:10.5f}'.format(history[0].price)), str('{:10.5f}'.format(balance[r])), str('{:10.5f}'.format(balance[r] / history[0].price))
                elif curname[r] == "rur":
                        history = btceapi.getTradeHistory("btc_rur")
                        balance[-1] = balance[-1] + ( history[0].price * balance[r] )
                        print str('{:10.5f}'.format(balance[-1])), str('{:10.5f}'.format(history[0].price)), str('{:10.5f}'.format(balance[r])), str('{:10.5f}'.format(history[0].price * balance[r]))
                elif curname[r] == "eur":
                        history = btceapi.getTradeHistory("btc_eur")
                        balance[-1] = balance[-1] + ( history[0].price * balance[r] )
                        print str('{:10.5f}'.format(balance[-1])), str('{:10.5f}'.format(history[0].price)), str('{:10.5f}'.format(balance[r])), str('{:10.5f}'.format(history[0].price * balance[r]))
                elif curname[r] == "nmc":
                        history = btceapi.getTradeHistory("nmc_btc")
                        balance[-1] = balance[-1] + ( history[0].price * balance[r] )
                        print str('{:10.5f}'.format(balance[-1])), str('{:10.5f}'.format(history[0].price)), str('{:10.5f}'.format(balance[r])), str('{:10.5f}'.format(history[0].price * balance[r]))
                elif curname[r] == "nvc":
                        history = btceapi.getTradeHistory("nvc_btc")
                        balance[-1] = balance[-1] + ( history[0].price * balance[r] )
                        print str('{:10.5f}'.format(balance[-1])), str('{:10.5f}'.format(history[0].price)), str('{:10.5f}'.format(balance[r])), str('{:10.5f}'.format(history[0].price * balance[r]))
                elif curname[r] == "trc":
                        history = btceapi.getTradeHistory("trc_btc")
                        balance[-1] = balance[-1] + ( history[0].price * balance[r] )
                        print str('{:10.5f}'.format(balance[-1])), str('{:10.5f}'.format(history[0].price)), str('{:10.5f}'.format(balance[r])), str('{:10.5f}'.format(history[0].price * balance[r]))
                elif curname[r] == "ppc":
                        history = btceapi.getTradeHistory("ppc_btc")
                        balance[-1] = balance[-1] + ( history[0].price * balance[r] )
                        print str('{:10.5f}'.format(balance[-1])), str('{:10.5f}'.format(history[0].price)), str('{:10.5f}'.format(balance[r])), str('{:10.5f}'.format(history[0].price * balance[r]))
                elif curname[r] == "ftc":
                        history = btceapi.getTradeHistory("ftc_btc")
                        balance[-1] = balance[-1] + ( history[0].price * balance[r] )
                        print str('{:10.5f}'.format(balance[-1])), str('{:10.5f}'.format(history[0].price)), str('{:10.5f}'.format(balance[r])), str('{:10.5f}'.format(history[0].price * balance[r]))
                r += 1

        print
        print "Total wallet value is approximately " + str('{:10.5f}'.format(balance[-1])), "BTC"
        print




