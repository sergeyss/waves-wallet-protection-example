import pywaves
import requests


class PyWaves2Sig(pywaves.ParallelPyWaves):

    def __init__(self):
        super.__init__()

        self.NODE = 'https://nodes-testnet.wavesnodes.com/'
        self.CHAIN = 'testnet'
        self.CHAIN_ID = 'T'

    def wrapper(self, api, postData='', host='', headers=''):
        # global OFFLINE
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
