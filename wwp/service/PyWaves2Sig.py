import json

import base58
import pywaves
import requests

from wwp.service.ConfigService import ConfigService
from wwp.service.CryptographicService import CryptographicService


class PyWaves2Sig(pywaves.ParallelPyWaves):
    """
    Adds to any transaction second signature.
    """

    def __init__(self):
        super().__init__()

        self.__configService = ConfigService()
        self.__cryptographicService = CryptographicService()

        self.setNode(node=self.__configService.node,
                     chain=self.__configService.chain,
                     chain_id=self.__configService.chainId)

        pywaves.setNode(node=self.__configService.node,
                        chain=self.__configService.chain,
                        chain_id=self.__configService.chainId)

    def wrapper(self, api, postData='', host='', headers=''):
        if postData:
            postData = self.__appendSecondSign(postData)

        return super().wrapper(api, postData, host, headers)

    def __appendSecondSign(self, postData: str) -> str:
        data = json.loads(postData)
        proofs = data.get('proofs', [])

        if len(proofs) == 0:
            return postData

        message, signature = self.__cryptographicService.signRandomMessage()
        proofs.append(message)
        proofs.append(signature)

        return json.dumps(data)
