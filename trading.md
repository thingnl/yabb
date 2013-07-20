#Trading#

Yabb supports multiple trading styles. Future version of yabb will include more trade styles.

The active trade style is set in **config.py** using the **tradestyle** keyword. Additional parameters need to be set to function properly.

Currently supported trade styles are:


## PAired Trading (pat) ##
Balances permitting, PAired Trading will create a buy and a sell order or every trade run, depending on the settings you choose.


Example:

Based in the following settings in config.py

- tradestyle = pat
- tradepair = ltc_btc
- tradecost = 0.2
- tradeamtbuy = 1.51
- tradeamtsell = 1.50
- tradeinterval = 30
- tradepoa = price
- trademaxblife = 900
- trademaxslife = 1800
- tradeprcbuy = 0.15
- tradeprcsell = 0.20


In this example we are trading ltc for btc in pat style. When buying, we buy 1.51 ltc, when selling we sell 1.5 ltc. Cost of trading is 0.2% per trade. We want the trading cost compensated for in the price. On buy orders we want a 0.15% margin, on sell orders we want a 0.20% margin (total profit on combined buy and sell will be 0.15% + 0.20% = 0.35% combined). We are performing a trade run every 30 seconds. Buy orders will have a minimum life of 15 minutes, sell orders are kept open for 30 minutes (unless buy or sell orders are filled).

Note: margins of 0.15% and 0.20% seems very small, but compared to the average movement of ltc trade prices, they are ok. 10 time 0.35% profit is still 3.5% profit. Larger margins just means that more orders will not be filled, tying up your currencies.  

Suppose the last ltc-btc trade (buy or sell) on BTC-e was a 0.1 ltc sell @ 0.03210 btc, the following trades will be send to BTC-e:

The buy order:

- original order would be: buy 1.51 ltc @ 0.03210
 
Compensate (pay less) for 0.15 profit margin:
 
- compansated order would be: 1.51 ltc @ 0.03205185
 
Trade cost of 0.2% are compensated in price
 
- compentsated order would be: 1.51 ltc @ 0.031987746
 
So the final buy order should be for: buy 1.51 ltc @ 0.03199


The sell order:

- original order would be: sell 1.50 ltc @ 0.03210
 
Compensate (ask more) for 0.20 profit margin:
 
- compansated order would be: 1.50 ltc @ 0.0321642
 
Trade cost of 0.2% are compensated in price
 
- compentsated order would be: 1.50 ltc @ 0.032228528
 
So the final sell order should be for: buy 1.50 ltc @ 0.0322


## VAriable Buy (vab) ##
The buy part of the PAired Trading style. If need be can be used seperately from selling. 

## VAriable Sell (vas) ##
The sell part of the PAired Trading style. If need be can be used seperately from buying.


## Slow Fixed Combined (sfc) ##
Slow Fixed Combined is a combination of Slow Fixed Buy and Slow Fixed Sell. It basicly behaves like pat trading, but in addition has a bottom and top price. Buy orders will only be created if the last trade on BTC-e was under a certain price. Sell orders will only be created if the last trade on BTC-e is above a certain price.

Example:

Based in the following settings in config.py

- tradestyle = sfc
- tradepair = ltc_btc
- tradecost = 0.2
- tradeamtbuy = 1.51
- tradeamtsell = 1.50
- tradeinterval = 30
- tradepoa = amount
- trademaxblife = 900
- trademaxslife = 1800
- tradelowlim = 0.03200
- tradehighlim = 0.3220

In this example we are trading ltc for btc in sfc style. When buying, we buy 1.51 ltc, when selling we sell 1.5 ltc. Cost of trading is 0.2% per trade. We want the trading cost compensated for in the amount traded. Only if the price is below 0.03200, wel will buy. Sell orders require a minimum price of 0.3220. We are performing a trade run every 30 seconds. Buy orders will have a minimum life of 15 minutes, sell orders are kept open for 30 minutes (unless buy or sell orders are filled).

Suppose the last ltc-btc trade (buy or sell) on BTC-e was a 0.1 ltc sell @ 0.03210 btc, the following trades will be send to BTC-e:

The buy order:
- Bottom price level of 0.03200 was not reached, so no buy order is created.

The sell order:
- Top price level of 0.03220 was also not reached, so no sell order is created.



Suppose the last ltc-btc trade (buy or sell) on BTC-e was a 0.1 ltc buy @ 0.03199 btc, the following trades will be send to BTC-e:

The buy order:
- original order would be: buy 1.51 ltc @ 0.03199
 
Trade cost of 0.2% are compensated in amount
 
- compentsated order would be: 1.513026052 ltc @ 0.03199
 
So the final buy order should be for: buy 1.5130 ltc @ 0.03199


The sell order:

- Again, the top price level of 0.03220 was also not reached, so no sell order is created.


## Slow Fixed Buy (sfb) ##
The buy part of the Slow Fixed Combined style. Usefull for selling large amounts of currency above a certain price taking advantage of rising prices. 


## Slow Fixed Sell (sfs) ##
The sell part of the Slow Fixed Combined style. Usefull for buying large amounts of currency below a certain price taking advantage of falling prices.

 
