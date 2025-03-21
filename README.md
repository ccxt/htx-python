# htx-python
Python SDK (sync and async) for Htx cryptocurrency exchange with Rest and WS capabilities.

You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/htx)
You can check Htx's docs here: [Docs](https://ccxt.com)

*This package derives from CCXT and allows you to call pretty much every endpoint by either using the unified CCXT API or calling the endpoints directly*

## Installation

```
pip install htx
```

## Usage

### Sync

```Python
from htx import HtxSync

def main():
    instance = HtxSync({})
    ob =  instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = instance.fetch_balance()
    # order = instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)
```

### Async

```Python
import asyncio
from htx import HtxAsync

async def main():
    instance = HtxAsync({})
    ob =  await instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = await instance.fetch_balance()
    # order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

asyncio.run(main())
```

### Websockets

```Python
from htx import HtxWs

async def main():
    instance = HtxWs({})
    while True:
        ob = await instance.watch_order_book("BTC/USDC")
        print(ob)
        # orders = await instance.watch_orders("BTC/USDC")
```

