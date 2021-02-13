import pywaves
import requests
import base58
import json

from wwp.service.ConfigService import ConfigService
from wwp.service.CryptographicService import CryptographicService


class PyWaves2Sig(pywaves.ParallelPyWaves):

    def __init__(self):
        super().__init__()
        self.setNode(node='https://nodes-testnet.wavesnodes.com', chain='testnet', chain_id='T')

    def wrapper(self, api, postData='', host='', headers=''):
        if postData:  # postData must be checked more sophisticated
            postData = self.__appendSecondSign(postData)  # inject service to generate and create second sign

        if self.OFFLINE:
            offlineTx = {'api-type': 'POST' if postData else 'GET', 'api-endpoint': api, 'api-data': postData}
            return offlineTx
        if not host:
            host = self.NODE
        if postData:
            req = requests.post('%s%s' % (host, api), data=postData,
                                headers={'content-type': 'application/json'}).json()
        else:
            req = requests.get('%s%s' % (host, api), headers=headers).json()
        return req

    @staticmethod
    def __appendSecondSign(postData: str) -> str:
        data = json.loads(postData)
        proofs = data['proofs']

        contentHash = base58.b58encode(b'hash')  # hash of random content
        secondSign = base58.b58encode(b'sign')  # signed hash

        proofs.append(contentHash)
        proofs.append(secondSign)

        return json.dumps(data)


if __name__ == '__main__':
    configService = ConfigService()
    print("public key: %s" % configService.publicKey)
    print("private key: %s" % configService.privateKey)
    print("node: %s" % configService.node)
    print("chain: %s" % configService.chain)
    print("chainId: %s" % configService.chainId)

    cryptographicService = CryptographicService()
    print("message: %s\nsignature: %s" % cryptographicService.signRandomMessage())

    # due to built-in function 'balance' use pywaves instead of self.pywaves
    # pywaves.setNode(node='https://nodes-testnet.wavesnodes.com', chain='testnet', chain_id='T')
    #
    # seedSender = "trade latin maximum slot unfair segment outside holiday park monster choose leader all object poet"
    # addressSender = pywaves.Address(seed=seedSender, pywaves=PyWaves2Sig())
    #
    # seedRecipient = "detail grow legend inherit ridge happy bird element milk thank neutral ecology gun beach burger"
    # # in real world the only address is known. This is done to avoid the difficulty of getting an address
    # addressRecipient = pywaves.Address(seed=seedRecipient)
    #
    # addressSender.sendWaves(addressRecipient, 11000000, txFee=pywaves.DEFAULT_SMART_FEE + pywaves.DEFAULT_BASE_FEE)
