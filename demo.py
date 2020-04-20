# Normal library imports
#NOTE:  imports declared in imported functions need to be
#       manually added here for now...
import sys
import math
import time
#etc...

# Imports compatible with normal python execution but will
# be grabbed by our pre-compilation script with #IMPORT tag
#TODO:  import specific_tokens is not currently supported
#IMPORT
from lib.Util import *
#NOTE:  need to order dependencies manually
#TODO:  dependency tree resolution
from lib.Second import *
from lib.First import *
#ENDIMPORT

def run():
    init_t = time.time()
    first_func()
    debug_time(f"Time:", init_t, time.time())

run()