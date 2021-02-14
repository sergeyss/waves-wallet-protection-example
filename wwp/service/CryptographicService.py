import os

import base58
import pywaves.crypto as crypto

from wwp.service.ConfigService import ConfigService
from wwp.util.SingletonWrapper import singleton


@singleton
class CryptographicService:
    """
    Provides second signature.
    """

    def __init__(self):
        self.__configService = ConfigService()

    def signRandomMessage(self) -> tuple:
        """
        Signs random message.
        :return: message and its signature (bytes)
        """
        message = os.urandom(16).hex()
        signature = crypto.sign(self.__configService.privateKey, message.encode())
        return base58.b58encode(message.encode()), signature
