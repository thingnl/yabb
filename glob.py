from time import strftime
from timeit import default_timer

global totbuyo
global totsello
global totmiso
global starttime
global runtime
global openbalance
global closebalance


totbuyo         = 0                                             # Total placed buy orders
totsello        = 0                                             # Total placed sell orders
totmiso         = 0                                             # Total missed orders (no coins, API errors or order rejected)
starttime 	= strftime('%d-%m-%Y %H:%M')                    # run start time
runtime 	= default_timer()                             	# time program is running in seconds
openbalance     = 0
closebalance    = 0
