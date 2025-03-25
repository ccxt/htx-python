import os
import sys
import asyncio

root = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
sys.path.append(root + '/')

from htx import HtxAsync

# ********** on Windows, uncomment below ********** 
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = HtxAsync({})
    await instance.load_markets()
    symbol = "BTC/USDC"

    # fetch ticker
    ticker = await instance.fetch_ticker(symbol)
    print(ticker)

    # create order
    order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 123456.789)
    print(order)

    # close after you finish
    await instance.close()

asyncio.run(main())

