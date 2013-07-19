# UI #

This is a short description of the user interface. As you can configure the interface more or less to you own liking, some words on what information is presented and how you can control it, seem in order.


After starting yabb you will receive a short message after which the interface is presented.



## Version and run information: ##


                                                                 yabb v0.1
    Started: 18-07-2013 20:16Last run: 18-07-2013 20:18  runtime: 0:02:25

This line provides the yabb version number you are using, the time yabb was started, the time the last trade round was run and the total time yabb has been active.

This line can currently not be turned off.



## Trading information: ##
     Trading: .­   BTC-e: .   API: .   Info: .   Trade: .   Withdraw: .

Using red and green circles, this line indicates the following:

- Trading: Indicates if you are in trade or in sim mode. Switch by using the s key. Default status is set with **tradesimmod** = True/False in config.py.
- BTC-e: Indicates if the BTC-e website is reachable. A red dot indicates either network connection issues or BTC-e is actually down.
- API: Indicates if the BTC-e API is reachable. A red dot indicates either network connection issues or BTC-e is actually down.
- Info: Indicates if you API key is allowed to retreive information. 
- Trade: Indicates if you API key is allowed to actually trade.
- Withdraw: Indicates if you API key is allowed to withdraw funds. This function is currently NOT implemented at BTC-e side.
 
This line can be turned on/off by setting **shownetwork** = True/False in config.py. 

##  Trade settings: ##
      - trading pair . ltc_btc   - buy per . . . . . .1.51
      - interval . . .  30       - sell per. . . . . . 1.5
      - interval mod .  10       - price change up . .0.15%
      - trade cost . . 0.2%      - price change down . 0.4%
    
Depending on the trade style you have chosen, additional or less information will be displayed here. These settings indicate the values that are used to trigger actions while trading.

These lines can be turned on/off by setting **showtrade** = True/False in config.py.

##  Balance: ##
      - btc   1.58401165   - usd   0.00000025   - rur   0.00000000  
      - ltc   4.29517448   - nmc   0.00000000   - eur   0.00000000  
      - nvc   0.00000000   - trc   0.00000000   - ppc   0.00000000  
      - ftc   0.00000000  

Self explaining. Indicates your current balance after the last trade interval. Balances that have gone up will show in green, balances gone down will show red. Unchanged balances in black and 0 balances in light gray.

These lines can be turned on/off by setting **showbalance** = True/False in config.py.

##  Ticker: ##
     Buy    0.03217             0.03207
     Sell             0.03204            0.03208   0.03208   0.03208   0.03208

Displays the last 7 trades within the chosen traide pair. Less usefull if you use longer trade intervals.

These lines can be turned on/off by setting **showticker** = True/False in config.py.


## SMA: ##

     over x trades, 5: up 10: up 20: up 50: up 150: up

Calculates the Slow Moving Average indicates over the last 5, 10, 20, 50 & 150 trades withing you chosen trade pair.

This line can be turned on/off by setting **showtrend** = True/False in config.py.


## Order Counters: ##
     Total -Buy orders:3 -Sell orders:0 -Cancelled orders:13 -Missed orders:3

This line contains counters with the total number of:

- Buy orders: Orders that should result in a buy.
- Sell orders: Orders that should result in a sell.
- Cancelled orders: Orders that where cancelled either manually (C on menu) or due to their age.
- Missed orders: Orders that were not placed either due to insufficient funds or other, unknown reasons.

Any high number here might indicate that you trade settings might need changing. E.g. a high cancelled number might indicate that you trade expiration settings are a bit short.

This line can be turned on/off by setting **showordcnt** = True/False in config.py.
  

## Open orders (3/1):  

     id       Type  Pair    Rate        Amount      Created
     25580840 buy   ltc_btc 0.03188000   1.51000000 2013-07-18 19:59:15
     25584638 buy   ltc_btc 0.03205000   1.51000000 2013-07-18 20:18:39
     25581010 buy   ltc_btc 0.03188000   1.51000000 2013-07-18 19:59:58
     23835050 sell  trc_btc 0.00269000  99.80000000 2013-07-10 19:18:46
    
Actual order that are currently active on BTC-e. These include orders that you might put in manually and orders outside your chosen trade pair.

Between brackets are the total number of buy and sell orders.

Buy orders have their type (buy/sell) displayed in green/red.
The created timestamp is displayed using multiple colors:

- black: order will not expire
- blue: order is for currency other than currently chosen tade pair
- partial green: new or relatively new orders
- partial yellow: orders that are about halfway of their expiration time
- red or partial red: orders that are about to expire without being filled.

These lines can be turned on/off by setting **showorders** = True/False in config.py.


## User keys: ##
     q = quit  | + = increase wait | l = logfile off  | r = reload config   
     p = pause | - = decrease wait | s = simmode on   | h = hold trades
                                   | t = trade now    | C = cancel all trades 

These lines serve as a reminder for the yabb user. Function keys should be followed by pressing the [enter] key.
Keys have to following function:

- q: Quit yabb and drop back to the command line.
- p: Pause program execution. Nothing will be done, no trades will be made. Screen will not be updated.
- +: Increase the time between trade runs. The amount to increase can be set in config.py.
- -: Decrease the time between trade runs. Then amount to decrease can be set in config.py.
- l: Turn the "log to file" function completely on or of. Default setting is set in config.py.
- s: Switch between actual trading and simulation mode. Default setting is set in config.py.
- t: Will start a trade run immidiately. Any trade interval is ignored.
- r: Reloads the config.py file. Any changes made will be activated. Manual changes to f.i. the trade interval or the log mode, will be reset to their default values.
- h: Will hold any new trades. Active trades are allowed to complete or expire. Screen will continue to update.
- C: (Capital C) will try to cancel all open orders as quick as possible like a kind of Emergency Break. Depending on the config.py **tradecnlpro** setting, orders outside the tradepair are also cancelled.

These lines can be turned on/off by setting **showkeys** = True/False in config.py.



