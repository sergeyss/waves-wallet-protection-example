import unittest

import base58

from wwp.service.CryptographicService import CryptographicService


class CryptographicServiceTest(unittest.TestCase):

    __cryptographicService = CryptographicService()

    def testCheckGeneratedMessageAndSign(self):
        message, signature = (None, None)
        try:
            message, signature = self.__cryptographicService.signRandomMessage()
            self.assertIsNotNone(message)
            self.assertIsNotNone(signature)
        except Exception as e:
            self.fail(str(e))

        try:
            base58.b58decode(message)
            base58.b58decode(signature)
        except Exception as e:
            self.fail(str(e))


if __name__ == '__main__':
    unittest.main()