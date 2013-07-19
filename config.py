# BTC-e settings
# Contains the link to the BTC-e webpage. Used to monitor network availability
btceurl		=	"http://btc-e.com"

# Your BTC-e api key. Find it using Profile/API keys under Key
btceapikey	=	"xxxxxxxx-xxxxxxxx-xxxxxxxx-xxxxxxxx-xxxxxxxx"

# Your BTC-e api secret. Find it using Profile/API keys under Secret
btceapisec	=	"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Socket timeout, waittime on connects	
btcesoctim	=	5

# Play a sound on network errors. 
btcealrsnd	=	False

# Trade settings
tradepair	=	"btc_usd"
tradebase	=	"btc"		# Base currency
tradecost	=	0.2		# Costs per trade as %
tradeamtbuy	=	1.51		# Amount of currency per buy, minimum 0.1
tradeamtsell	=	1.50		# Amount of currency per sell, minimum 0.1
tradeinterval	=	30		# Seconds between runs
tradeitvmod	=	10		# Interval change seconds
tradesimmod	=	True		# Simulate or actual trading on startup True = Sim only
trademaxblife	=	900		# Kill buy orders after x seconds, 0 is disable
trademaxslife	=	1800		# Kill sell orders after x seconds, 0 is disable
trademaxbuy	=	15		# Max open buy orders, no new orders if x orders are open
trademaxsell	=	15		# Max open sell orders, no new orders if x orders are open
tradeonhold	=	True		# Hold trading on startup?
tradeendcnl	=	False		# Cancel all open orders on exit?
tradecnlpro	=	True		# Cancel only current Traid-Pair orders (if applicable)

tradelowlim	=       0.0012		# Lower limit for sfb & sfc trading
tradehighlim	=	15.667		# Upper limit for sfs & sfc trading
tradeprcbuy	=	0.15		# write buy n% below current last trade rate while pat trading
tradeprcsell	=	0.4		# write sell n% above current last trade rate while pat trading

tradepoa	=	"none"		# Set to none, no compensation will take place
tradestyle	=	"pat"

# Visibility setting
shownetwork	=	True
showtrade	=	True
showbalance	=	True
showticker	=	True
showtrend	=	True
showordcnt	=	True
showorders	=	True
showkeys	=	True

# Log settings
logenable	=	True		# Master log setting
logfile		=	"./yabb.log"	# Logfile
logconnect	=	True		# Log connection errors
logtrade	=	True		# Log trade information
logorders	=	True		# Log actual/simulated orders
logbalance	=	True		# Log balance information on startup/shutdown
logrun		=	True		# Log start/end to file

