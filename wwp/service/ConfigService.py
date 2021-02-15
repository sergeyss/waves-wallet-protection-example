import json
import os
import logging
from pathlib import Path
from pywaves import Address, pywaves
from wwp.util.SingletonWrapper import singleton


@singleton
class ConfigService:
    """
    Loads system configuration.
    """

    def __init__(self):
        self.__logger = logging.getLogger(self.__class__.__name__)

        configFileName = "wwp-config.json"
        configFilePaths = (configFileName,
                           Path.home().__str__() + os.sep + configFileName,
                           Path.home().__str__() + os.sep + ".wwp" + os.sep + configFileName)

        for cf in configFilePaths:
            if Path(cf).exists():
                with open(cf) as configFile:
                    jsonConfig = json.load(configFile)

                self.__node = jsonConfig.get('node', pywaves.NODE).strip()
                self.__chain = jsonConfig.get('chain', pywaves.CHAIN).strip()
                self.__chainId = jsonConfig.get('chainId', pywaves.CHAIN_ID).strip()
                self.__matcher = jsonConfig.get('matcher', pywaves.MATCHER).strip()
                self.__generateKeyPair(jsonConfig['seed'])
                return

    @property
    def node(self) -> str:
        """
        Returns node.
        :return: node.
        """
        return self.__node

    @property
    def chain(self) -> str:
        """
        Returns chain.
        :return: chain.
        """
        return self.__chain

    @property
    def chainId(self) -> str:
        """
        Returns chainId.
        :return: chainId.
        """
        return self.__chainId

    @property
    def matcher(self) -> str:
        """
        Returns matcher.
        :return: matcher.
        """
        return self.__matcher

    @property
    def publicKey(self) -> str:
        """
        Returns public key.
        :return: public key.
        """
        return self.__publicKey

    @property
    def privateKey(self) -> str:
        """
        Returns private key.
        :return: private key.
        """
        return self.__privateKey

    def __generateKeyPair(self, seed: str) -> None:
        """
        Generates key pair by seed.
        :param seed: seed
        """
        address = Address(seed=seed)
        self.__publicKey = address.publicKey
        self.__privateKey = address.privateKey


if __name__ == '__main__':
    newAddress = Address(privateKey=None)
    print("-----------------------------------------------------")
    print("SEED:\n%s" % newAddress.seed)
    print("-----------------------------------------------------")
    print("PUBLIC KEY:\n%s" % newAddress.publicKey)
    print("-----------------------------------------------------")
