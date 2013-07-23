from time import strftime
from timeit import default_timer

global totbuyo
global totsello
global totmiso
global starttime
global runtime
global openbalance
global closebalance
global connectw
global connecta
global totcano
global botright
global lastrate
global balancec
global balancea
global balanceo
global tickbuy
global ticksell
global trends
global orders
global ordbuy
global ordsell

totbuyo         = 0                                             # Total placed buy orders
totsello        = 0                                             # Total placed sell orders
totmiso         = 0                                             # Total missed orders (no coins, API errors or order rejected)
starttime 	= strftime('%d-%m-%Y %H:%M')                    # run start time
runtime 	= default_timer()                             	# time program is running in seconds
openbalance     = 0
closebalance    = 0
connectw        = False
connecta	= False                                         # connect api
totcano         = 0
botright	= []                                            # bot rights
lastrate	= ""                                            # last rate traded at
balancec	= []                                            # currencies
balancea	= []                                            # balance
balanceo        = []                                            # prev balance
tickbuy		= ""                                            # ticker buy orders
ticksell	= ""                                            # ticker sell orders
trends		= ""                                            # trend indicators
orders		= ""                                            # open orders
ordbuy		= 0                                             # open buy orders
ordsell		= 0                                             # open sell orders



