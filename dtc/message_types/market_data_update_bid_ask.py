
import json
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateBidAsk(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 bid_price=None,
                 bid_quantity=None,
                 ask_price=None,
                 ask_quantity=None,
                 date_time=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_BID_ASK
        self.SymbolID = symbol_id
        self.BidPrice = bid_price
        self.BidQuantity = bid_quantity
        self.AskPrice = ask_price
        self.AskQuantity = ask_quantity
        self.DateTime = date_time

