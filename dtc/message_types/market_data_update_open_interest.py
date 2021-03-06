
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class MarketDataUpdateOpenInterest(BaseMessageType):
    def __init__(self,
                 symbol_id=None,
                 open_interest=None,
                 trading_session_date=None):
        self.Type = MessageTypes.MARKET_DATA_UPDATE_OPEN_INTEREST
        self.SymbolID = symbol_id
        self.OpenInterest = open_interest
        self.TradingSessionDate = trading_session_date

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return MarketDataUpdateOpenInterest(
             symbol_id=packet[0],
             open_interest=packet[1],
             trading_session_date=packet[2]
        )

    @staticmethod
    def from_message_long(message_obj):
        return MarketDataUpdateOpenInterest(
             symbol_id=message_obj.get('SymbolID'),
             open_interest=message_obj.get('OpenInterest'),
             trading_session_date=message_obj.get('TradingSessionDate')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return MarketDataUpdateOpenInterest.from_message_short(message_obj)
        else:
            return MarketDataUpdateOpenInterest.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "MarketDataUpdateOpenInterest"
