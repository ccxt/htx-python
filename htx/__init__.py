import sys
import htx.ccxt as ccxt_module
sys.modules['ccxt'] = ccxt_module

from htx.ccxt import htx as HtxSync
from htx.ccxt.async_support.htx import htx as HtxAsync
from htx.ccxt.pro.htx import htx as HtxWs
