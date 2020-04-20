import sys
from .Second import *

def first_func():
    print("Hello from First", file=sys.stderr)
    second_func()