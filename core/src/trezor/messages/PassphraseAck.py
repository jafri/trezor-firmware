# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class PassphraseAck(p.MessageType):
    MESSAGE_WIRE_TYPE = 42

    def __init__(
        self,
        passphrase: str = None,
        on_device: bool = None,
    ) -> None:
        self.passphrase = passphrase
        self.on_device = on_device

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('passphrase', p.UnicodeType, 0),
            2: ('on_device', p.BoolType, 0),
        }
