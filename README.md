# htx-python
Python SDK (sync and async) for Htx with Rest and WS capabilities.

You can check Htx's docs here: [Docs](https://ccxt.com)


You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/htx)

*This package derives from CCXT and allows you to call pretty much every endpoint by either using the unified CCXT API or calling the endpoints directly*

## Installation

```
pip install htx
```

## Usage

### Async

```Python
from htx import HtxAsync

async def main():
    instance = HtxAsync({})
    order = await instance.create_order(__EXAMPLE_SYMBOL__, "limit", "buy", 1, 100000)
```

### Sync

```Python
from htx import HtxSync

def main():
    instance = HtxSync({})
    order =  instance.create_order(__EXAMPLE_SYMBOL__, "limit", "buy", 1, 100000)
```

### Websockets

```Python
from htx import HtxWs

async def main():
    instance = HtxWs({})
    while True:
        orders = await instance.watch_orders(__EXAMPLE_SYMBOL__)
```

