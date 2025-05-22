# htx-python
Python SDK (sync and async) for Htx cryptocurrency exchange with Rest and WS capabilities.

- You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/htx)
- You can check Htx's docs here: [Docs](https://www.google.com/search?q=google+htx+cryptocurrency+exchange+api+docs)
- Github repo: https://github.com/ccxt/htx-python
- Pypi package: https://pypi.org/project/htx


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

main()
```

### Async

```Python
import sys
import asyncio
from htx import HtxAsync

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = HtxAsync({})
    ob =  await instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = await instance.fetch_balance()
    # order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```



### Websockets

```Python
import sys
from htx import HtxWs

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = HtxWs({})
    while True:
        ob = await instance.watch_order_book("BTC/USDC")
        print(ob)
        # orders = await instance.watch_orders("BTC/USDC")

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```





#### Raw call

You can also construct custom requests to available "implicit" endpoints

```Python
        request = {
            'type': 'candleSnapshot',
            'req': {
                'coin': coin,
                'interval': tf,
                'startTime': since,
                'endTime': until,
            },
        }
        response = await instance.public_post_info(request)
```


## Available methods

### REST Unified

- `create_contract_order_request(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_market_buy_order_with_cost(self, symbol: str, cost: float, params={})`
- `create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_orders(self, orders: List[OrderRequest], params={})`
- `create_spot_order_request(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_trailing_percent_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, trailingPercent=None, trailingTriggerPrice=None, params={})`
- `fetch_account_id_by_type(self, type: str, marginMode: Str = None, symbol: Str = None, params={})`
- `fetch_accounts(self, params={})`
- `fetch_balance(self, params={})`
- `fetch_borrow_interest(self, code: Str = None, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_closed_contract_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_closed_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_closed_spot_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_contract_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_currencies(self, params={})`
- `fetch_deposit_address(self, code: str, params={})`
- `fetch_deposit_addresses_by_network(self, code: str, params={})`
- `fetch_deposit_withdraw_fees(self, codes: Strings = None, params={})`
- `fetch_deposits(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_rate_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_rate(self, symbol: str, params={})`
- `fetch_funding_rates(self, symbols: Strings = None, params={})`
- `fetch_isolated_borrow_rates(self, params={})`
- `fetch_last_prices(self, symbols: Strings = None, params={})`
- `fetch_ledger(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_leverage_tiers(self, symbols: Strings = None, params={})`
- `fetch_liquidations(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `fetch_markets_by_type_and_sub_type(self, type: Str, subType: Str, params={})`
- `fetch_markets(self, params={})`
- `fetch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `fetch_open_interest_history(self, symbol: str, timeframe='1h', since: Int = None, limit: Int = None, params={})`
- `fetch_open_interest(self, symbol: str, params={})`
- `fetch_open_interests(self, symbols: Strings = None, params={})`
- `fetch_open_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_order_book(self, symbol: str, limit: Int = None, params={})`
- `fetch_order_trades(self, id: str, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_order(self, id: str, symbol: Str = None, params={})`
- `fetch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_position(self, symbol: str, params={})`
- `fetch_positions(self, symbols: Strings = None, params={})`
- `fetch_settlement_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_spot_order_trades(self, id: str, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_spot_orders_by_states(self, states, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_spot_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_status(self, params={})`
- `fetch_ticker(self, symbol: str, params={})`
- `fetch_tickers(self, symbols: Strings = None, params={})`
- `fetch_time(self, params={})`
- `fetch_trades(self, symbol: str, since: Int = None, limit: Int = 1000, params={})`
- `fetch_trading_fee(self, symbol: str, params={})`
- `fetch_trading_limits_by_id(self, id: str, params={})`
- `fetch_trading_limits(self, symbols: Strings = None, params={})`
- `fetch_withdraw_addresses(self, code: str, note=None, networkCode=None, params={})`
- `fetch_withdrawals(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `borrow_cross_margin(self, code: str, amount: float, params={})`
- `borrow_isolated_margin(self, symbol: str, code: str, amount: float, params={})`
- `cancel_all_orders_after(self, timeout: Int, params={})`
- `cancel_all_orders(self, symbol: Str = None, params={})`
- `cancel_order(self, id: str, symbol: Str = None, params={})`
- `cancel_orders(self, ids, symbol: Str = None, params={})`
- `close_position(self, symbol: str, side: OrderSide = None, params={})`
- `cost_to_precision(self, symbol, cost)`
- `describe(self)`
- `network_code_to_id(self, networkCode: str, currencyCode: Str = None)`
- `network_id_to_code(self, networkId: Str = None, currencyCode: Str = None)`
- `nonce(self)`
- `repay_cross_margin(self, code: str, amount, params={})`
- `repay_isolated_margin(self, symbol: str, code: str, amount, params={})`
- `set_leverage(self, leverage: Int, symbol: Str = None, params={})`
- `set_position_mode(self, hedged: bool, symbol: Str = None, params={})`
- `transfer(self, code: str, amount: float, fromAccount: str, toAccount: str, params={})`
- `try_get_symbol_from_future_markets(self, symbolOrMarketId: str)`
- `withdraw(self, code: str, amount: float, address: str, tag=None, params={})`

### REST Raw

- `v2public_get_reference_currencies(request)`
- `v2public_get_market_status(request)`
- `v2private_get_account_ledger(request)`
- `v2private_get_account_withdraw_quota(request)`
- `v2private_get_account_withdraw_address(request)`
- `v2private_get_account_deposit_address(request)`
- `v2private_get_account_repayment(request)`
- `v2private_get_reference_transact_fee_rate(request)`
- `v2private_get_account_asset_valuation(request)`
- `v2private_get_point_account(request)`
- `v2private_get_sub_user_user_list(request)`
- `v2private_get_sub_user_user_state(request)`
- `v2private_get_sub_user_account_list(request)`
- `v2private_get_sub_user_deposit_address(request)`
- `v2private_get_sub_user_query_deposit(request)`
- `v2private_get_user_api_key(request)`
- `v2private_get_user_uid(request)`
- `v2private_get_algo_orders_opening(request)`
- `v2private_get_algo_orders_history(request)`
- `v2private_get_algo_orders_specific(request)`
- `v2private_get_c2c_offers(request)`
- `v2private_get_c2c_offer(request)`
- `v2private_get_c2c_transactions(request)`
- `v2private_get_c2c_repayment(request)`
- `v2private_get_c2c_account(request)`
- `v2private_get_etp_reference(request)`
- `v2private_get_etp_transactions(request)`
- `v2private_get_etp_transaction(request)`
- `v2private_get_etp_rebalance(request)`
- `v2private_get_etp_limit(request)`
- `v2private_post_account_transfer(request)`
- `v2private_post_account_repayment(request)`
- `v2private_post_point_transfer(request)`
- `v2private_post_sub_user_management(request)`
- `v2private_post_sub_user_creation(request)`
- `v2private_post_sub_user_tradable_market(request)`
- `v2private_post_sub_user_transferability(request)`
- `v2private_post_sub_user_api_key_generation(request)`
- `v2private_post_sub_user_api_key_modification(request)`
- `v2private_post_sub_user_api_key_deletion(request)`
- `v2private_post_sub_user_deduct_mode(request)`
- `v2private_post_algo_orders(request)`
- `v2private_post_algo_orders_cancel_all_after(request)`
- `v2private_post_algo_orders_cancellation(request)`
- `v2private_post_c2c_offer(request)`
- `v2private_post_c2c_cancellation(request)`
- `v2private_post_c2c_cancel_all(request)`
- `v2private_post_c2c_repayment(request)`
- `v2private_post_c2c_transfer(request)`
- `v2private_post_etp_creation(request)`
- `v2private_post_etp_redemption(request)`
- `v2private_post_etp_transactid_cancel(request)`
- `v2private_post_etp_batch_cancel(request)`
- `public_get_common_symbols(request)`
- `public_get_common_currencys(request)`
- `public_get_common_timestamp(request)`
- `public_get_common_exchange(request)`
- `public_get_settings_currencys(request)`
- `private_get_account_accounts(request)`
- `private_get_account_accounts_id_balance(request)`
- `private_get_account_accounts_sub_uid(request)`
- `private_get_account_history(request)`
- `private_get_cross_margin_loan_info(request)`
- `private_get_margin_loan_info(request)`
- `private_get_fee_fee_rate_get(request)`
- `private_get_order_openorders(request)`
- `private_get_order_orders(request)`
- `private_get_order_orders_id(request)`
- `private_get_order_orders_id_matchresults(request)`
- `private_get_order_orders_getclientorder(request)`
- `private_get_order_history(request)`
- `private_get_order_matchresults(request)`
- `private_get_query_deposit_withdraw(request)`
- `private_get_margin_loan_orders(request)`
- `private_get_margin_accounts_balance(request)`
- `private_get_cross_margin_loan_orders(request)`
- `private_get_cross_margin_accounts_balance(request)`
- `private_get_points_actions(request)`
- `private_get_points_orders(request)`
- `private_get_subuser_aggregate_balance(request)`
- `private_get_stable_coin_exchange_rate(request)`
- `private_get_stable_coin_quote(request)`
- `private_post_account_transfer(request)`
- `private_post_futures_transfer(request)`
- `private_post_order_batch_orders(request)`
- `private_post_order_orders_place(request)`
- `private_post_order_orders_submitcancelclientorder(request)`
- `private_post_order_orders_batchcancelopenorders(request)`
- `private_post_order_orders_id_submitcancel(request)`
- `private_post_order_orders_batchcancel(request)`
- `private_post_dw_withdraw_api_create(request)`
- `private_post_dw_withdraw_virtual_id_cancel(request)`
- `private_post_dw_transfer_in_margin(request)`
- `private_post_dw_transfer_out_margin(request)`
- `private_post_margin_orders(request)`
- `private_post_margin_orders_id_repay(request)`
- `private_post_cross_margin_transfer_in(request)`
- `private_post_cross_margin_transfer_out(request)`
- `private_post_cross_margin_orders(request)`
- `private_post_cross_margin_orders_id_repay(request)`
- `private_post_stable_coin_exchange(request)`
- `private_post_subuser_transfer(request)`
- `status_public_spot_get_api_v2_summary_json(request)`
- `status_public_future_inverse_get_api_v2_summary_json(request)`
- `status_public_future_linear_get_api_v2_summary_json(request)`
- `status_public_swap_inverse_get_api_v2_summary_json(request)`
- `status_public_swap_linear_get_api_v2_summary_json(request)`
- `spot_public_get_v2_market_status(request)`
- `spot_public_get_v1_common_symbols(request)`
- `spot_public_get_v1_common_currencys(request)`
- `spot_public_get_v2_settings_common_currencies(request)`
- `spot_public_get_v2_reference_currencies(request)`
- `spot_public_get_v1_common_timestamp(request)`
- `spot_public_get_v1_common_exchange(request)`
- `spot_public_get_v1_settings_common_chains(request)`
- `spot_public_get_v1_settings_common_currencys(request)`
- `spot_public_get_v1_settings_common_symbols(request)`
- `spot_public_get_v2_settings_common_symbols(request)`
- `spot_public_get_v1_settings_common_market_symbols(request)`
- `spot_public_get_market_history_candles(request)`
- `spot_public_get_market_history_kline(request)`
- `spot_public_get_market_detail_merged(request)`
- `spot_public_get_market_tickers(request)`
- `spot_public_get_market_detail(request)`
- `spot_public_get_market_depth(request)`
- `spot_public_get_market_trade(request)`
- `spot_public_get_market_history_trade(request)`
- `spot_public_get_market_etp(request)`
- `spot_public_get_v2_etp_reference(request)`
- `spot_public_get_v2_etp_rebalance(request)`
- `spot_private_get_v1_account_accounts(request)`
- `spot_private_get_v1_account_accounts_account_id_balance(request)`
- `spot_private_get_v2_account_valuation(request)`
- `spot_private_get_v2_account_asset_valuation(request)`
- `spot_private_get_v1_account_history(request)`
- `spot_private_get_v2_account_ledger(request)`
- `spot_private_get_v2_point_account(request)`
- `spot_private_get_v2_account_deposit_address(request)`
- `spot_private_get_v2_account_withdraw_quota(request)`
- `spot_private_get_v2_account_withdraw_address(request)`
- `spot_private_get_v2_reference_currencies(request)`
- `spot_private_get_v1_query_deposit_withdraw(request)`
- `spot_private_get_v1_query_withdraw_client_order_id(request)`
- `spot_private_get_v2_user_api_key(request)`
- `spot_private_get_v2_user_uid(request)`
- `spot_private_get_v2_sub_user_user_list(request)`
- `spot_private_get_v2_sub_user_user_state(request)`
- `spot_private_get_v2_sub_user_account_list(request)`
- `spot_private_get_v2_sub_user_deposit_address(request)`
- `spot_private_get_v2_sub_user_query_deposit(request)`
- `spot_private_get_v1_subuser_aggregate_balance(request)`
- `spot_private_get_v1_account_accounts_sub_uid(request)`
- `spot_private_get_v1_order_openorders(request)`
- `spot_private_get_v1_order_orders_order_id(request)`
- `spot_private_get_v1_order_orders_getclientorder(request)`
- `spot_private_get_v1_order_orders_order_id_matchresult(request)`
- `spot_private_get_v1_order_orders_order_id_matchresults(request)`
- `spot_private_get_v1_order_orders(request)`
- `spot_private_get_v1_order_history(request)`
- `spot_private_get_v1_order_matchresults(request)`
- `spot_private_get_v2_reference_transact_fee_rate(request)`
- `spot_private_get_v2_algo_orders_opening(request)`
- `spot_private_get_v2_algo_orders_history(request)`
- `spot_private_get_v2_algo_orders_specific(request)`
- `spot_private_get_v1_margin_loan_info(request)`
- `spot_private_get_v1_margin_loan_orders(request)`
- `spot_private_get_v1_margin_accounts_balance(request)`
- `spot_private_get_v1_cross_margin_loan_info(request)`
- `spot_private_get_v1_cross_margin_loan_orders(request)`
- `spot_private_get_v1_cross_margin_accounts_balance(request)`
- `spot_private_get_v2_account_repayment(request)`
- `spot_private_get_v1_stable_coin_quote(request)`
- `spot_private_get_v1_stable_coin_exchange_rate(request)`
- `spot_private_get_v2_etp_transactions(request)`
- `spot_private_get_v2_etp_transaction(request)`
- `spot_private_get_v2_etp_limit(request)`
- `spot_private_post_v1_account_transfer(request)`
- `spot_private_post_v1_futures_transfer(request)`
- `spot_private_post_v2_point_transfer(request)`
- `spot_private_post_v2_account_transfer(request)`
- `spot_private_post_v1_dw_withdraw_api_create(request)`
- `spot_private_post_v1_dw_withdraw_virtual_withdraw_id_cancel(request)`
- `spot_private_post_v2_sub_user_deduct_mode(request)`
- `spot_private_post_v2_sub_user_creation(request)`
- `spot_private_post_v2_sub_user_management(request)`
- `spot_private_post_v2_sub_user_tradable_market(request)`
- `spot_private_post_v2_sub_user_transferability(request)`
- `spot_private_post_v2_sub_user_api_key_generation(request)`
- `spot_private_post_v2_sub_user_api_key_modification(request)`
- `spot_private_post_v2_sub_user_api_key_deletion(request)`
- `spot_private_post_v1_subuser_transfer(request)`
- `spot_private_post_v1_trust_user_active_credit(request)`
- `spot_private_post_v1_order_orders_place(request)`
- `spot_private_post_v1_order_batch_orders(request)`
- `spot_private_post_v1_order_auto_place(request)`
- `spot_private_post_v1_order_orders_order_id_submitcancel(request)`
- `spot_private_post_v1_order_orders_submitcancelclientorder(request)`
- `spot_private_post_v1_order_orders_batchcancelopenorders(request)`
- `spot_private_post_v1_order_orders_batchcancel(request)`
- `spot_private_post_v2_algo_orders_cancel_all_after(request)`
- `spot_private_post_v2_algo_orders(request)`
- `spot_private_post_v2_algo_orders_cancellation(request)`
- `spot_private_post_v2_account_repayment(request)`
- `spot_private_post_v1_dw_transfer_in_margin(request)`
- `spot_private_post_v1_dw_transfer_out_margin(request)`
- `spot_private_post_v1_margin_orders(request)`
- `spot_private_post_v1_margin_orders_order_id_repay(request)`
- `spot_private_post_v1_cross_margin_transfer_in(request)`
- `spot_private_post_v1_cross_margin_transfer_out(request)`
- `spot_private_post_v1_cross_margin_orders(request)`
- `spot_private_post_v1_cross_margin_orders_order_id_repay(request)`
- `spot_private_post_v1_stable_coin_exchange(request)`
- `spot_private_post_v2_etp_creation(request)`
- `spot_private_post_v2_etp_redemption(request)`
- `spot_private_post_v2_etp_transactid_cancel(request)`
- `spot_private_post_v2_etp_batch_cancel(request)`
- `contract_public_get_api_v1_timestamp(request)`
- `contract_public_get_heartbeat(request)`
- `contract_public_get_api_v1_contract_contract_info(request)`
- `contract_public_get_api_v1_contract_index(request)`
- `contract_public_get_api_v1_contract_query_elements(request)`
- `contract_public_get_api_v1_contract_price_limit(request)`
- `contract_public_get_api_v1_contract_open_interest(request)`
- `contract_public_get_api_v1_contract_delivery_price(request)`
- `contract_public_get_market_depth(request)`
- `contract_public_get_market_bbo(request)`
- `contract_public_get_market_history_kline(request)`
- `contract_public_get_index_market_history_mark_price_kline(request)`
- `contract_public_get_market_detail_merged(request)`
- `contract_public_get_market_detail_batch_merged(request)`
- `contract_public_get_v2_market_detail_batch_merged(request)`
- `contract_public_get_market_trade(request)`
- `contract_public_get_market_history_trade(request)`
- `contract_public_get_api_v1_contract_risk_info(request)`
- `contract_public_get_api_v1_contract_insurance_fund(request)`
- `contract_public_get_api_v1_contract_adjustfactor(request)`
- `contract_public_get_api_v1_contract_his_open_interest(request)`
- `contract_public_get_api_v1_contract_ladder_margin(request)`
- `contract_public_get_api_v1_contract_api_state(request)`
- `contract_public_get_api_v1_contract_elite_account_ratio(request)`
- `contract_public_get_api_v1_contract_elite_position_ratio(request)`
- `contract_public_get_api_v1_contract_liquidation_orders(request)`
- `contract_public_get_api_v1_contract_settlement_records(request)`
- `contract_public_get_index_market_history_index(request)`
- `contract_public_get_index_market_history_basis(request)`
- `contract_public_get_api_v1_contract_estimated_settlement_price(request)`
- `contract_public_get_api_v3_contract_liquidation_orders(request)`
- `contract_public_get_swap_api_v1_swap_contract_info(request)`
- `contract_public_get_swap_api_v1_swap_index(request)`
- `contract_public_get_swap_api_v1_swap_query_elements(request)`
- `contract_public_get_swap_api_v1_swap_price_limit(request)`
- `contract_public_get_swap_api_v1_swap_open_interest(request)`
- `contract_public_get_swap_ex_market_depth(request)`
- `contract_public_get_swap_ex_market_bbo(request)`
- `contract_public_get_swap_ex_market_history_kline(request)`
- `contract_public_get_index_market_history_swap_mark_price_kline(request)`
- `contract_public_get_swap_ex_market_detail_merged(request)`
- `contract_public_get_v2_swap_ex_market_detail_batch_merged(request)`
- `contract_public_get_index_market_history_swap_premium_index_kline(request)`
- `contract_public_get_swap_ex_market_detail_batch_merged(request)`
- `contract_public_get_swap_ex_market_trade(request)`
- `contract_public_get_swap_ex_market_history_trade(request)`
- `contract_public_get_swap_api_v1_swap_risk_info(request)`
- `contract_public_get_swap_api_v1_swap_insurance_fund(request)`
- `contract_public_get_swap_api_v1_swap_adjustfactor(request)`
- `contract_public_get_swap_api_v1_swap_his_open_interest(request)`
- `contract_public_get_swap_api_v1_swap_ladder_margin(request)`
- `contract_public_get_swap_api_v1_swap_api_state(request)`
- `contract_public_get_swap_api_v1_swap_elite_account_ratio(request)`
- `contract_public_get_swap_api_v1_swap_elite_position_ratio(request)`
- `contract_public_get_swap_api_v1_swap_estimated_settlement_price(request)`
- `contract_public_get_swap_api_v1_swap_liquidation_orders(request)`
- `contract_public_get_swap_api_v1_swap_settlement_records(request)`
- `contract_public_get_swap_api_v1_swap_funding_rate(request)`
- `contract_public_get_swap_api_v1_swap_batch_funding_rate(request)`
- `contract_public_get_swap_api_v1_swap_historical_funding_rate(request)`
- `contract_public_get_swap_api_v3_swap_liquidation_orders(request)`
- `contract_public_get_index_market_history_swap_estimated_rate_kline(request)`
- `contract_public_get_index_market_history_swap_basis(request)`
- `contract_public_get_linear_swap_api_v1_swap_contract_info(request)`
- `contract_public_get_linear_swap_api_v1_swap_index(request)`
- `contract_public_get_linear_swap_api_v1_swap_query_elements(request)`
- `contract_public_get_linear_swap_api_v1_swap_price_limit(request)`
- `contract_public_get_linear_swap_api_v1_swap_open_interest(request)`
- `contract_public_get_linear_swap_ex_market_depth(request)`
- `contract_public_get_linear_swap_ex_market_bbo(request)`
- `contract_public_get_linear_swap_ex_market_history_kline(request)`
- `contract_public_get_index_market_history_linear_swap_mark_price_kline(request)`
- `contract_public_get_linear_swap_ex_market_detail_merged(request)`
- `contract_public_get_linear_swap_ex_market_detail_batch_merged(request)`
- `contract_public_get_v2_linear_swap_ex_market_detail_batch_merged(request)`
- `contract_public_get_linear_swap_ex_market_trade(request)`
- `contract_public_get_linear_swap_ex_market_history_trade(request)`
- `contract_public_get_linear_swap_api_v1_swap_risk_info(request)`
- `contract_public_get_swap_api_v1_linear_swap_api_v1_swap_insurance_fund(request)`
- `contract_public_get_linear_swap_api_v1_swap_adjustfactor(request)`
- `contract_public_get_linear_swap_api_v1_swap_cross_adjustfactor(request)`
- `contract_public_get_linear_swap_api_v1_swap_his_open_interest(request)`
- `contract_public_get_linear_swap_api_v1_swap_ladder_margin(request)`
- `contract_public_get_linear_swap_api_v1_swap_cross_ladder_margin(request)`
- `contract_public_get_linear_swap_api_v1_swap_api_state(request)`
- `contract_public_get_linear_swap_api_v1_swap_cross_transfer_state(request)`
- `contract_public_get_linear_swap_api_v1_swap_cross_trade_state(request)`
- `contract_public_get_linear_swap_api_v1_swap_elite_account_ratio(request)`
- `contract_public_get_linear_swap_api_v1_swap_elite_position_ratio(request)`
- `contract_public_get_linear_swap_api_v1_swap_liquidation_orders(request)`
- `contract_public_get_linear_swap_api_v1_swap_settlement_records(request)`
- `contract_public_get_linear_swap_api_v1_swap_funding_rate(request)`
- `contract_public_get_linear_swap_api_v1_swap_batch_funding_rate(request)`
- `contract_public_get_linear_swap_api_v1_swap_historical_funding_rate(request)`
- `contract_public_get_linear_swap_api_v3_swap_liquidation_orders(request)`
- `contract_public_get_index_market_history_linear_swap_premium_index_kline(request)`
- `contract_public_get_index_market_history_linear_swap_estimated_rate_kline(request)`
- `contract_public_get_index_market_history_linear_swap_basis(request)`
- `contract_public_get_linear_swap_api_v1_swap_estimated_settlement_price(request)`
- `contract_private_get_api_v1_contract_sub_auth_list(request)`
- `contract_private_get_api_v1_contract_api_trading_status(request)`
- `contract_private_get_swap_api_v1_swap_sub_auth_list(request)`
- `contract_private_get_swap_api_v1_swap_api_trading_status(request)`
- `contract_private_get_linear_swap_api_v1_swap_sub_auth_list(request)`
- `contract_private_get_linear_swap_api_v1_swap_api_trading_status(request)`
- `contract_private_get_linear_swap_api_v1_swap_cross_position_side(request)`
- `contract_private_get_linear_swap_api_v1_swap_position_side(request)`
- `contract_private_get_linear_swap_api_v3_unified_account_info(request)`
- `contract_private_get_linear_swap_api_v3_fix_position_margin_change_record(request)`
- `contract_private_get_linear_swap_api_v3_swap_unified_account_type(request)`
- `contract_private_get_linear_swap_api_v3_linear_swap_overview_account_info(request)`
- `contract_private_post_api_v1_contract_balance_valuation(request)`
- `contract_private_post_api_v1_contract_account_info(request)`
- `contract_private_post_api_v1_contract_position_info(request)`
- `contract_private_post_api_v1_contract_sub_auth(request)`
- `contract_private_post_api_v1_contract_sub_account_list(request)`
- `contract_private_post_api_v1_contract_sub_account_info_list(request)`
- `contract_private_post_api_v1_contract_sub_account_info(request)`
- `contract_private_post_api_v1_contract_sub_position_info(request)`
- `contract_private_post_api_v1_contract_financial_record(request)`
- `contract_private_post_api_v1_contract_financial_record_exact(request)`
- `contract_private_post_api_v1_contract_user_settlement_records(request)`
- `contract_private_post_api_v1_contract_order_limit(request)`
- `contract_private_post_api_v1_contract_fee(request)`
- `contract_private_post_api_v1_contract_transfer_limit(request)`
- `contract_private_post_api_v1_contract_position_limit(request)`
- `contract_private_post_api_v1_contract_account_position_info(request)`
- `contract_private_post_api_v1_contract_master_sub_transfer(request)`
- `contract_private_post_api_v1_contract_master_sub_transfer_record(request)`
- `contract_private_post_api_v1_contract_available_level_rate(request)`
- `contract_private_post_api_v3_contract_financial_record(request)`
- `contract_private_post_api_v3_contract_financial_record_exact(request)`
- `contract_private_post_api_v1_contract_cancel_after(request)`
- `contract_private_post_api_v1_contract_order(request)`
- `contract_private_post_api_v1_contract_batchorder(request)`
- `contract_private_post_api_v1_contract_cancel(request)`
- `contract_private_post_api_v1_contract_cancelall(request)`
- `contract_private_post_api_v1_contract_switch_lever_rate(request)`
- `contract_private_post_api_v1_lightning_close_position(request)`
- `contract_private_post_api_v1_contract_order_info(request)`
- `contract_private_post_api_v1_contract_order_detail(request)`
- `contract_private_post_api_v1_contract_openorders(request)`
- `contract_private_post_api_v1_contract_hisorders(request)`
- `contract_private_post_api_v1_contract_hisorders_exact(request)`
- `contract_private_post_api_v1_contract_matchresults(request)`
- `contract_private_post_api_v1_contract_matchresults_exact(request)`
- `contract_private_post_api_v3_contract_hisorders(request)`
- `contract_private_post_api_v3_contract_hisorders_exact(request)`
- `contract_private_post_api_v3_contract_matchresults(request)`
- `contract_private_post_api_v3_contract_matchresults_exact(request)`
- `contract_private_post_api_v1_contract_trigger_order(request)`
- `contract_private_post_api_v1_contract_trigger_cancel(request)`
- `contract_private_post_api_v1_contract_trigger_cancelall(request)`
- `contract_private_post_api_v1_contract_trigger_openorders(request)`
- `contract_private_post_api_v1_contract_trigger_hisorders(request)`
- `contract_private_post_api_v1_contract_tpsl_order(request)`
- `contract_private_post_api_v1_contract_tpsl_cancel(request)`
- `contract_private_post_api_v1_contract_tpsl_cancelall(request)`
- `contract_private_post_api_v1_contract_tpsl_openorders(request)`
- `contract_private_post_api_v1_contract_tpsl_hisorders(request)`
- `contract_private_post_api_v1_contract_relation_tpsl_order(request)`
- `contract_private_post_api_v1_contract_track_order(request)`
- `contract_private_post_api_v1_contract_track_cancel(request)`
- `contract_private_post_api_v1_contract_track_cancelall(request)`
- `contract_private_post_api_v1_contract_track_openorders(request)`
- `contract_private_post_api_v1_contract_track_hisorders(request)`
- `contract_private_post_swap_api_v1_swap_balance_valuation(request)`
- `contract_private_post_swap_api_v1_swap_account_info(request)`
- `contract_private_post_swap_api_v1_swap_position_info(request)`
- `contract_private_post_swap_api_v1_swap_account_position_info(request)`
- `contract_private_post_swap_api_v1_swap_sub_auth(request)`
- `contract_private_post_swap_api_v1_swap_sub_account_list(request)`
- `contract_private_post_swap_api_v1_swap_sub_account_info_list(request)`
- `contract_private_post_swap_api_v1_swap_sub_account_info(request)`
- `contract_private_post_swap_api_v1_swap_sub_position_info(request)`
- `contract_private_post_swap_api_v1_swap_financial_record(request)`
- `contract_private_post_swap_api_v1_swap_financial_record_exact(request)`
- `contract_private_post_swap_api_v1_swap_user_settlement_records(request)`
- `contract_private_post_swap_api_v1_swap_available_level_rate(request)`
- `contract_private_post_swap_api_v1_swap_order_limit(request)`
- `contract_private_post_swap_api_v1_swap_fee(request)`
- `contract_private_post_swap_api_v1_swap_transfer_limit(request)`
- `contract_private_post_swap_api_v1_swap_position_limit(request)`
- `contract_private_post_swap_api_v1_swap_master_sub_transfer(request)`
- `contract_private_post_swap_api_v1_swap_master_sub_transfer_record(request)`
- `contract_private_post_swap_api_v3_swap_financial_record(request)`
- `contract_private_post_swap_api_v3_swap_financial_record_exact(request)`
- `contract_private_post_swap_api_v1_swap_cancel_after(request)`
- `contract_private_post_swap_api_v1_swap_order(request)`
- `contract_private_post_swap_api_v1_swap_batchorder(request)`
- `contract_private_post_swap_api_v1_swap_cancel(request)`
- `contract_private_post_swap_api_v1_swap_cancelall(request)`
- `contract_private_post_swap_api_v1_swap_lightning_close_position(request)`
- `contract_private_post_swap_api_v1_swap_switch_lever_rate(request)`
- `contract_private_post_swap_api_v1_swap_order_info(request)`
- `contract_private_post_swap_api_v1_swap_order_detail(request)`
- `contract_private_post_swap_api_v1_swap_openorders(request)`
- `contract_private_post_swap_api_v1_swap_hisorders(request)`
- `contract_private_post_swap_api_v1_swap_hisorders_exact(request)`
- `contract_private_post_swap_api_v1_swap_matchresults(request)`
- `contract_private_post_swap_api_v1_swap_matchresults_exact(request)`
- `contract_private_post_swap_api_v3_swap_matchresults(request)`
- `contract_private_post_swap_api_v3_swap_matchresults_exact(request)`
- `contract_private_post_swap_api_v3_swap_hisorders(request)`
- `contract_private_post_swap_api_v3_swap_hisorders_exact(request)`
- `contract_private_post_swap_api_v1_swap_trigger_order(request)`
- `contract_private_post_swap_api_v1_swap_trigger_cancel(request)`
- `contract_private_post_swap_api_v1_swap_trigger_cancelall(request)`
- `contract_private_post_swap_api_v1_swap_trigger_openorders(request)`
- `contract_private_post_swap_api_v1_swap_trigger_hisorders(request)`
- `contract_private_post_swap_api_v1_swap_tpsl_order(request)`
- `contract_private_post_swap_api_v1_swap_tpsl_cancel(request)`
- `contract_private_post_swap_api_v1_swap_tpsl_cancelall(request)`
- `contract_private_post_swap_api_v1_swap_tpsl_openorders(request)`
- `contract_private_post_swap_api_v1_swap_tpsl_hisorders(request)`
- `contract_private_post_swap_api_v1_swap_relation_tpsl_order(request)`
- `contract_private_post_swap_api_v1_swap_track_order(request)`
- `contract_private_post_swap_api_v1_swap_track_cancel(request)`
- `contract_private_post_swap_api_v1_swap_track_cancelall(request)`
- `contract_private_post_swap_api_v1_swap_track_openorders(request)`
- `contract_private_post_swap_api_v1_swap_track_hisorders(request)`
- `contract_private_post_linear_swap_api_v1_swap_lever_position_limit(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_lever_position_limit(request)`
- `contract_private_post_linear_swap_api_v1_swap_balance_valuation(request)`
- `contract_private_post_linear_swap_api_v1_swap_account_info(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_account_info(request)`
- `contract_private_post_linear_swap_api_v1_swap_position_info(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_position_info(request)`
- `contract_private_post_linear_swap_api_v1_swap_account_position_info(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_account_position_info(request)`
- `contract_private_post_linear_swap_api_v1_swap_sub_auth(request)`
- `contract_private_post_linear_swap_api_v1_swap_sub_account_list(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_sub_account_list(request)`
- `contract_private_post_linear_swap_api_v1_swap_sub_account_info_list(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_sub_account_info_list(request)`
- `contract_private_post_linear_swap_api_v1_swap_sub_account_info(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_sub_account_info(request)`
- `contract_private_post_linear_swap_api_v1_swap_sub_position_info(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_sub_position_info(request)`
- `contract_private_post_linear_swap_api_v1_swap_financial_record(request)`
- `contract_private_post_linear_swap_api_v1_swap_financial_record_exact(request)`
- `contract_private_post_linear_swap_api_v1_swap_user_settlement_records(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_user_settlement_records(request)`
- `contract_private_post_linear_swap_api_v1_swap_available_level_rate(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_available_level_rate(request)`
- `contract_private_post_linear_swap_api_v1_swap_order_limit(request)`
- `contract_private_post_linear_swap_api_v1_swap_fee(request)`
- `contract_private_post_linear_swap_api_v1_swap_transfer_limit(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_transfer_limit(request)`
- `contract_private_post_linear_swap_api_v1_swap_position_limit(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_position_limit(request)`
- `contract_private_post_linear_swap_api_v1_swap_master_sub_transfer(request)`
- `contract_private_post_linear_swap_api_v1_swap_master_sub_transfer_record(request)`
- `contract_private_post_linear_swap_api_v1_swap_transfer_inner(request)`
- `contract_private_post_linear_swap_api_v3_swap_financial_record(request)`
- `contract_private_post_linear_swap_api_v3_swap_financial_record_exact(request)`
- `contract_private_post_linear_swap_api_v1_swap_order(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_order(request)`
- `contract_private_post_linear_swap_api_v1_swap_batchorder(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_batchorder(request)`
- `contract_private_post_linear_swap_api_v1_swap_cancel(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_cancel(request)`
- `contract_private_post_linear_swap_api_v1_swap_cancelall(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_cancelall(request)`
- `contract_private_post_linear_swap_api_v1_swap_switch_lever_rate(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_switch_lever_rate(request)`
- `contract_private_post_linear_swap_api_v1_swap_lightning_close_position(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_lightning_close_position(request)`
- `contract_private_post_linear_swap_api_v1_swap_order_info(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_order_info(request)`
- `contract_private_post_linear_swap_api_v1_swap_order_detail(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_order_detail(request)`
- `contract_private_post_linear_swap_api_v1_swap_openorders(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_openorders(request)`
- `contract_private_post_linear_swap_api_v1_swap_hisorders(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_hisorders(request)`
- `contract_private_post_linear_swap_api_v1_swap_hisorders_exact(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_hisorders_exact(request)`
- `contract_private_post_linear_swap_api_v1_swap_matchresults(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_matchresults(request)`
- `contract_private_post_linear_swap_api_v1_swap_matchresults_exact(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_matchresults_exact(request)`
- `contract_private_post_linear_swap_api_v1_linear_cancel_after(request)`
- `contract_private_post_linear_swap_api_v1_swap_switch_position_mode(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_switch_position_mode(request)`
- `contract_private_post_linear_swap_api_v3_swap_matchresults(request)`
- `contract_private_post_linear_swap_api_v3_swap_cross_matchresults(request)`
- `contract_private_post_linear_swap_api_v3_swap_matchresults_exact(request)`
- `contract_private_post_linear_swap_api_v3_swap_cross_matchresults_exact(request)`
- `contract_private_post_linear_swap_api_v3_swap_hisorders(request)`
- `contract_private_post_linear_swap_api_v3_swap_cross_hisorders(request)`
- `contract_private_post_linear_swap_api_v3_swap_hisorders_exact(request)`
- `contract_private_post_linear_swap_api_v3_swap_cross_hisorders_exact(request)`
- `contract_private_post_linear_swap_api_v3_fix_position_margin_change(request)`
- `contract_private_post_linear_swap_api_v3_swap_switch_account_type(request)`
- `contract_private_post_linear_swap_api_v3_linear_swap_fee_switch(request)`
- `contract_private_post_linear_swap_api_v1_swap_trigger_order(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_trigger_order(request)`
- `contract_private_post_linear_swap_api_v1_swap_trigger_cancel(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_trigger_cancel(request)`
- `contract_private_post_linear_swap_api_v1_swap_trigger_cancelall(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_trigger_cancelall(request)`
- `contract_private_post_linear_swap_api_v1_swap_trigger_openorders(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_trigger_openorders(request)`
- `contract_private_post_linear_swap_api_v1_swap_trigger_hisorders(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_trigger_hisorders(request)`
- `contract_private_post_linear_swap_api_v1_swap_tpsl_order(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_tpsl_order(request)`
- `contract_private_post_linear_swap_api_v1_swap_tpsl_cancel(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_tpsl_cancel(request)`
- `contract_private_post_linear_swap_api_v1_swap_tpsl_cancelall(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_tpsl_cancelall(request)`
- `contract_private_post_linear_swap_api_v1_swap_tpsl_openorders(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_tpsl_openorders(request)`
- `contract_private_post_linear_swap_api_v1_swap_tpsl_hisorders(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_tpsl_hisorders(request)`
- `contract_private_post_linear_swap_api_v1_swap_relation_tpsl_order(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_relation_tpsl_order(request)`
- `contract_private_post_linear_swap_api_v1_swap_track_order(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_track_order(request)`
- `contract_private_post_linear_swap_api_v1_swap_track_cancel(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_track_cancel(request)`
- `contract_private_post_linear_swap_api_v1_swap_track_cancelall(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_track_cancelall(request)`
- `contract_private_post_linear_swap_api_v1_swap_track_openorders(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_track_openorders(request)`
- `contract_private_post_linear_swap_api_v1_swap_track_hisorders(request)`
- `contract_private_post_linear_swap_api_v1_swap_cross_track_hisorders(request)`

### WS Unified

- `describe(self)`
- `watch_ticker(self, symbol: str, params={})`
- `watch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `watch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `watch_order_book(self, symbol: str, limit: Int = None, params={})`
- `watch_order_book_snapshot(self, client, message, subscription)`
- `watch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `get_order_channel_and_message_hash(self, type, subType, market=None, params={})`
- `watch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_positions(self, symbols: Strings = None, since: Int = None, limit: Int = None, params={})`
- `watch_balance(self, params={})`
- `pong(self, client, message)`
- `get_url_by_market_type(self, type, isLinear=True, isPrivate=False, isFeed=False)`
- `subscribe_public(self, url, symbol, messageHash, method=None, params={})`
- `subscribe_private(self, channel, messageHash, type, subtype, params={}, subscriptionParams={})`
- `authenticate(self, params={})`

## Contribution
- Give us a star :star:
- Fork and Clone! Awesome
- Select existing issues or create a new issue.