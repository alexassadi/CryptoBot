import logging

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing stocks_main.py (not when importing it)

    binance = BinanceClient("QbhPadgbjhYLyAhxg3P5rY4vMChU8WGXO8unmJrrRGdJbmF7SqsUSzZ8YQTk5OfW",
                            "UEoN8b6yn1Ag5bngWdNXY9LzplgFX3NWmoHXHNI9oBj6Zd4IM0ugtPqHGjnoKJMu",
                            testnet=False, futures=False)
    bitmex = BitmexClient("rQ18WCTlNbqcoivG2q_89vG9", "khK3iaJvbYVQi0U8l8eW87z-P3MsC5sa0OfsXrHgdQ-5bTBo", testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()
