import config, time
from btceapi import btceapi 

def writelog(logline):
        if config.logenable:
                with open(config.logfile,"a") as f:
                        line = str(time.strftime('%Y-%m-%d %H:%M:%S')) + " - " + logline + "\n"
                        f.write(line)
# def_writelog

