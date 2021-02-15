import unittest
import pywaves

from wwp.service.PyWaves2Sig import PyWaves2Sig

OWNER_SEED = "road effort twist shield sugar song item garbage mosquito child wasp room loop someone veteran"

WITHDRAW1_ADDRESS = "3NCyS63RHgNBTTzZSCneiZEbp4sG2xtmeBE"
WITHDRAW2_ADDRESS = "3N78XpUJ1VjSmsPr3vMKdPEEo6fRE7NyBJF"

SMART_CONTRACT_TX_FEE = pywaves.DEFAULT_SMART_FEE + pywaves.DEFAULT_BASE_FEE
SMART_CONTRACT_FALSE_RESULT_MESSAGE = "Transaction is not allowed by account-script"
SMART_CONTRACT_THROW_MESSAGE = "transaction is not permitted"

WAVES_AMOUNT = 111000

ETH_ASSET = pywaves.Asset("BrmjyAWT5jjr3Wpsiyivyvg5vDuzoX2s93WgiexXetB3")
BTC_ASSET = pywaves.Asset("DWgwcZTMhSvnyYCoWLRUXXSH1RSkzThXLJhww9gwkqdn")


class WavesWalletProtectionRideTest(unittest.TestCase):

    __ownerAddress2Sig = pywaves.Address(seed=OWNER_SEED, pywaves=PyWaves2Sig())
    __ownerAddress = pywaves.Address(seed=OWNER_SEED)

    def test001TransferWithout2Sig(self):
        for recipient in [WITHDRAW1_ADDRESS, WITHDRAW2_ADDRESS]:
            recipientAddress = pywaves.Address(address=recipient)
            response = self.__ownerAddress.sendWaves(recipientAddress, WAVES_AMOUNT, txFee=SMART_CONTRACT_TX_FEE)
            self.assertIsNotNone(response['error'])
            self.assertEqual(response['message'], SMART_CONTRACT_FALSE_RESULT_MESSAGE)

        arbitraryAddress = pywaves.Address(privateKey=None)
        response = self.__ownerAddress.sendWaves(arbitraryAddress, WAVES_AMOUNT, txFee=SMART_CONTRACT_TX_FEE)
        self.assertIsNotNone(response['error'])
        self.assertTrue(SMART_CONTRACT_THROW_MESSAGE in response['message'])

    def test002TransferWithin2Sig(self):
        for recipient in [WITHDRAW1_ADDRESS, WITHDRAW2_ADDRESS]:
            recipientAddress = pywaves.Address(address=recipient)
            response = self.__ownerAddress2Sig.sendWaves(recipientAddress, WAVES_AMOUNT, txFee=SMART_CONTRACT_TX_FEE)
            self.assertIsNone(response.get('error'))

        arbitraryAddress = pywaves.Address(privateKey=None)
        response = self.__ownerAddress2Sig.sendWaves(arbitraryAddress, WAVES_AMOUNT, txFee=SMART_CONTRACT_TX_FEE)
        self.assertIsNotNone(response['error'])
        self.assertTrue(SMART_CONTRACT_THROW_MESSAGE in response['message'])

    def test003OrderWithout2Sig(self):
        assetPair = pywaves.AssetPair(BTC_ASSET, pywaves.WAVES)
        response = self.__ownerAddress.buy(assetPair, 1, 1)
        self.assertIsNotNone(response['error'])
        self.assertTrue(SMART_CONTRACT_THROW_MESSAGE in response['message'])


    def test004OrderWithin2Sig(self):
        pass
