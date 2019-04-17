# todo: make the properties also 'object oriented' to support different configs per different SeleneDriver instances
import itertools
import os
import time

from selenpy.common.environment import *
from selenpy.common.helpers import env

timeout = int(env(SELENE_TIMEOUT, 4))
poll_during_waits = float(env(SELENE_POLL_DURING_WAITS, 0.1))

