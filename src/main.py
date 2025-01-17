import asyncio

from src.order_book import OrderBook


async def main():
    order_book = OrderBook(base_asset='ETH', quote_asset="USDC")  # Example for Ethereum

    await order_book.update()

    order_book._visualize_order_book()

if __name__ == "__main__":
    asyncio.run(main())
