# Configuration by config.py #

The following parameters can be se using the config.py file. Changes require a reload of the file by either restarting yabb or by using the "r" from the UI.

Note: Using the "r" when changing trade type can interfere with open orders (not cancelled of not created due to outdated balance information). You may want to restart yabb instead.

For information on types of numbers check [Wikipedia](http://en.wikipedia.org/wiki/List_of_types_of_numbers).


## btcealrsnd ##
Whether or not a sound will be produced to alert you to network problems (preventing trading). 

Default value: **False**

Currently allowed values are:

- **True**: Yabb will audibly alert you to network problems
- **False**: Yabb will not audibly alert you to network problems


## btceapikey ##
Your BTC-e trade API key. On first run, yabb will copy and save this key to a file called key_file. This file is needed by the btceapi software. In future versions, this should no longer be needed. Whenever changing this kry, be sure to delete the key_file to force an update to the btceapi software.


## btceapisec ##
Your BTC-e trade API secret. On first run, yabb will copy and save this secret to a file called key_file. This file is needed by the btceapi software. In future versions, this should no longer be needed. Whenever changing this secret, be sure to delete the key_file to force an update to the btceapi software.


## btcesoctim ##
Socket timeout in seconds. This is only one setting used in TCP communications. Actual timout's can take considerably longer. Values below 5 seconds can generate false positive log entries.

Default value: **5** (seconds)  

- Any natural number


## btceurl ##
The BTC-e website address. Used for checking network connectivity.

Default value: **http://btc-e.com**

Currently allowed values are:

- Any valid uniform resource locator


## logbalance ##
Whether or not to log balance information to the log. Setting can be overwritten by the logenable setting. In addition to the logfile, this settings controls whether or not a start and end balance in BTC is calculated and shown on exit. 

Default value: **True**

Currently allowed values are:

- **True**: Yabb will log balance information in the log
- **False**: Yabb will not log balance information in the log


## logconnect ##
Whether or not to log network information to the log. Setting can be overwritten by the logenable setting.

Default value: **True**

Currently allowed values are:

- **True**: Yabb will log network information in the log
- **False**: Yabb will not log network information in the log


## logenable ##
Enable/Disable logging to file. Can be switched from the UI with the "l" key.

Default value: **True**

Currently allowed values are:

- **True**: Yabb will enable logging to file
- **False**: Yabb will disable logging to file


## logfile ##
Name and location of the logfile used for logging information.

Default value: ./yabb.log

Currently allowed values are:

- Any valid path/file name combination supported by your OS.


## logorders ##
Whether or not to log order information to the log. Setting can be overwritten by the logenable setting.

Default value: **True**

Currently allowed values are:

- **True**: Yabb will log order information in the log
- **False**: Yabb will not log order information in the log


## logrun ##
Whether or not to log run information to the log. Setting can be overwritten by the logenable setting.

Default value: **True**

Currently allowed values are:

- **True**: Yabb will log run information in the log
- **False**: Yabb will not log run information in the log


## logtrade ##
Whether or not to log trade information to the log. Setting can be overwritten by the logenable setting.

Default value: **True**

Currently allowed values are:

- **True**: Yabb will log trade information in the log
- **False**: Yabb will not log trade information in the log


## showbalance ##
Whether or not to show balance information in the UI.

Default value: **True**

Currently allowed values are:

- **True**: Yabb will show balance information in the UI
- **False**: Yabb will not show balance information in the UI


## showkeys ##
Whether or not to show trend information in the UI.

Default value: **True**

Currently allowed values are:

- **True**: Yabb will show trend information in the UI
- **False**: Yabb will not show trend information in the UI


## shownetwork ##
Whether or not to show network information in the UI.

Default value: **True**

Currently allowed values are:

- **True**: Yabb will show network information in the UI
- **False**: Yabb will not show network information in the UI


## showordcnt ##
Whether or not to show order count information in the UI.

Default value: **True**

Currently allowed values are:

- **True**: Yabb will show order count information in the UI
- **False**: Yabb will not show order count information in the UI


## showorders ##
Whether or not to show order information in the UI.

Default value: **True**

Currently allowed values are:

- **True**: Yabb will show order information in the UI
- **False**: Yabb will not show order information in the UI

## showticker ##
Whether or not to show a ticker in the UI.

Default value: **True**

Currently allowed values are:

- **True**: Yabb will show a ticker in the UI
- **False**: Yabb will not show a ticker in the UI


## showtrade ##
Whether or not to show trade information in the UI.

Default value: **True**

Currently allowed values are:

- **True**: Yabb will show trade information in the UI
- **False**: Yabb will not show trade information in the UI


## showtrend ##
Whether or not to show trend information in the UI.

Default value: **True**

Currently allowed values are:

- **True**: Yabb will show trend information in the UI
- **False**: Yabb will not show trend information in the UI


## tradeamtbuy ##
Amount of currency to buy per trade. Depending on compensation and profit settings, this amount can change in actual trades. 

Default value: **1.51**

Currently allowed values are:

- Any positive real number with a 0.1 minumum


## tradeamtsell ##
Amount of currency to sell per trade. Depending on compensation and profit settings, this amount can change in actual trades. 

Default value: **1.50**

Currently allowed values are:

- Any positive real number with a 0.1 minimum


## tradebase ##
Trading base currency.

Currently not used but reserved for future development


## tradecnlpro ##
Whether or not yabb will remove (cancel) open orders outside the current trade pair when tradeendcnl is set to True. 

Default value: **False**

Currently allowed values are:

- **True**: Yabb will include other trade pair orders
- **False**: Yabb will not include other trade pair orders


## tradecost ##
Current cost percentage changed by BTC-e per trade. Used to calculate price and/or amount compensations.

Default value: **0.2**

Currently allowed values are:

- Any positive real number


## tradeendcnl ##
Whether or not yabb removes (cancels) open orders when ending. 

Default value: **False**

Currently allowed values are:

- **True**: Yabb will cancel open orders on exiting
- **False**: Yabb will not cancel open orders on exiting


## tradehighlim ##
The higher limit (price) used for sfs & sfc style trading.

Default value: **5**

Currently allowed values are:

- Any positive real number 



## tradeinterval ##
The amount of seconds between trade intervals.

Default value: **30** (seconds)

Currently allowed values are:

- Any natural number


## tradeitvmod ##
The amount of seconds added to, or substracted from, the wait time between trade intervals when using "+" or "-" in the UI.

Default value: **10** (seconds)

Currently allowed values are:

- Any natural number


## tradelowlim ##
The lower limit (price) used for sfb & sfc style trading.

Default value: **1**

Currently allowed values are:

- Any positive real number 


## trademaxblife ##
Minimum number of seconds that buy orders are allowed to stay open. Actual time is depending on several other factors like trade interval.

Default value: **900** (15 minutes)

Currently allowed values are:

- Any natural number 


## trademaxbuy ##
Maximum number of open buy orders including other pair trades. 

Default value: **15**

Currently allowed values are:

- Any natural number 


## trademaxsell ##
Maximum number of open sell orders including other pair trades. 

Default value: **15**

Currently allowed values are:

- Any natural number 


## trademaxslife ##
Minimum number of seconds that sell orders are allowed to stay open. Actual time is depending on several other factors like trade interval.

Default value: **1800** (30 minutes)

Currently allowed values are:

- Any natural number 


## tradeonhold ##
Whether or not yabb in started with trading on hold or not. This setting can be switched from the UI using "h". While on hold, the UI will keep updating.

Default value: **True**

Currently allowed values are:

- **True**: Yabb is started with trading on hold
- **False**: Yabb is started in active trading mode


## tradepair ##
The pair of alternate currencies that will be traded.

Default value: **btc_usd**

Currently allowed values are:

- **btc_eur**
- **btc_rur**
- **btc_usd**
- **eur_usd**
- **ftc_btc**
- **ltc_btc**
- **ltc_btc**
- **ltc_rur**
- **ltc_usd**
- **nmc_btc**
- **nvc_btc**
- **ppc_btc**
- **trc_btc**
- **usd_rur**


## tradepoa ##
Set desired compensation mode for prices, amount or both.

Default value: **none**

Currently allowed values are:

- **price**: Prices are compensated for trade costs
- **amount**: Amount to buy or sell is compensated for trade costs
- **none**: Neither price or amount is changed to compensate for trade costs


## tradeprcbuy ##
Percentage of requested profit that is substracted from buy prices.  

Default value: **1.50**

Currently allowed values are:

- Any rational number 


## tradeprcsell ##
Percentage of requested profit that is added to sell prices.  

Default value: **1.50**

Currently allowed values are:

- Any rational number  


## tradesimmod ##
Whether or not yabb in started in simulation mode or in trading mode.

Default value: **True**

Currently allowed values are:

- **True**: Yabb is started in simulation mode
- **False**: Yabb is started in trade mode


## tradestyle ##
Type of trading that is performed by yabb. For more information, see the trading document.

Default value: **pat**

Currently allowed values are:

- **pat**: **PA**ired **T**rading, try to buy and sell together with requested profit margin on ever run.
- **vab**: slow **VA**riable **B**uy, keep buying with requested percentage under current price
- **vas**: slow **VA**riable **S**ell. keep selling with requested percentage above current price
- **sfb**: **S**low **F**ixed **B**uy: keep buying while price is below requested price level
- **sfs**: **S**low **F**ixed **S**ell: keep selling while price is above requested price level
- **sfc**: **S**low **F**ixed **C**ombined: keep buying and selling while price is below/above requested price levels




