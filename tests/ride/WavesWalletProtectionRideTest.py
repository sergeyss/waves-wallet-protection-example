import unittest
import pywaves

from wwp.service.PyWaves2Sig import PyWaves2Sig

OWNER_SEED = "road effort twist shield sugar song item garbage mosquito child wasp room loop someone veteran"

WITHDRAW1_ADDRESS = "3NCyS63RHgNBTTzZSCneiZEbp4sG2xtmeBE"
WITHDRAW2_ADDRESS = "3N78XpUJ1VjSmsPr3vMKdPEEo6fRE7NyBJF"
RESTRICTED_ADDRESS = "3NCjREHB7dUFCzPhdy9g8oWhJy4YQyPaGmv"

SMART_CONTRACT_TX_FEE = pywaves.DEFAULT_SMART_FEE + pywaves.DEFAULT_BASE_FEE
SMART_CONTRACT_FALSE_RESULT_MESSAGE = "Transaction is not allowed by account-script"
SMART_CONTRACT_THROW_MESSAGE = "transaction is not permitted"


WAVES_AMOUNT = 1110000


class WavesWalletProtectionRideTest(unittest.TestCase):

    __pyWaves2Sig = PyWaves2Sig()

    def test001TransferWithout2Sig(self):
        ownerAddress = pywaves.Address(seed=OWNER_SEED)
        for recipient in [WITHDRAW1_ADDRESS, WITHDRAW2_ADDRESS]:
            recipientAddress = pywaves.Address(address=recipient)
            response = ownerAddress.sendWaves(recipientAddress, WAVES_AMOUNT, txFee=SMART_CONTRACT_TX_FEE)
            self.assertIsNotNone(response['error'])
            self.assertEqual(response['message'], SMART_CONTRACT_FALSE_RESULT_MESSAGE)

        recipientAddress = pywaves.Address(address=RESTRICTED_ADDRESS)
        response = ownerAddress.sendWaves(recipientAddress, WAVES_AMOUNT, txFee=SMART_CONTRACT_TX_FEE)
        self.assertIsNotNone(response['error'])
        self.assertTrue(SMART_CONTRACT_THROW_MESSAGE in response['message'])

        arbitraryAddress = pywaves.Address(privateKey=None)
        response = ownerAddress.sendWaves(arbitraryAddress, WAVES_AMOUNT, txFee=SMART_CONTRACT_TX_FEE)
        self.assertIsNotNone(response['error'])
        self.assertTrue(SMART_CONTRACT_THROW_MESSAGE in response['message'])
