
from dtc.enums.message_types import MessageTypes
from lib.base_message_type import BaseMessageType


class Logoff(BaseMessageType):
    def __init__(self,
                 reason=None,
                 do_not_reconnect=None):
        self.Type = MessageTypes.LOGOFF
        self.Reason = reason
        self.DoNotReconnect = do_not_reconnect

    @staticmethod
    def from_message_short(message_obj):
        packet = message_obj.get('F')
        return Logoff(
             reason=packet[0],
             do_not_reconnect=packet[1]
        )

    @staticmethod
    def from_message_long(message_obj):
        return Logoff(
             reason=message_obj.get('Reason'),
             do_not_reconnect=message_obj.get('DoNotReconnect')
        )

    @staticmethod
    def from_message(message_obj):
        if 'F' in message_obj:
            return Logoff.from_message_short(message_obj)
        else:
            return Logoff.from_message_long(message_obj)

    @staticmethod
    def get_message_type_name():
        return "Logoff"
