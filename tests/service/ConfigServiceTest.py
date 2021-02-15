import unittest
import base58

from wwp.service.ConfigService import ConfigService


class ConfigServiceTest(unittest.TestCase):
    """
    ConfigService tests
    """

    __configService = ConfigService()

    def test01InitConfigService(self):
        self.assertIsNotNone(self.__configService)
        self.assertIsNotNone(self.__configService.node)
        self.assertIsNotNone(self.__configService.chain)
        self.assertIsNotNone(self.__configService.chainId)
        self.assertIsNotNone(self.__configService.privateKey)
        self.assertIsNotNone(self.__configService.publicKey)

        try:
            base58.b58decode(self.__configService.publicKey)
            base58.b58decode(self.__configService.privateKey)
        except Exception as e:
            self.fail(str(e))


if __name__ == '__main__':
    unittest.main()
