import pywaves

from wwp.service.ConfigService import ConfigService
from wwp.service.CryptographicService import CryptographicService
from wwp.service.PyWaves2Sig import PyWaves2Sig

configService = ConfigService()
print("public key: %s" % configService.publicKey)
print("private key: %s" % configService.privateKey)
print("node: %s" % configService.node)
print("chain: %s" % configService.chain)
print("chainId: %s" % configService.chainId)

cryptographicService = CryptographicService()
print("message: %s\nsignature: %s" % cryptographicService.signRandomMessage())

seedSender = "jar middle share trial vocal verb whip obey stove punch voice noodle defy black hire"
addressSender = pywaves.Address(seed=seedSender, pywaves=PyWaves2Sig())

withdrawAddress = "3NCyS63RHgNBTTzZSCneiZEbp4sG2xtmeBE"
addressRecipient = pywaves.Address(address=withdrawAddress)
response = addressSender.sendWaves(addressRecipient,
                                   1110000,
                                   txFee=pywaves.DEFAULT_SMART_FEE + pywaves.DEFAULT_BASE_FEE)
print("recipient address: %s\nresponse:\n%s" % (withdrawAddress, response))

withdrawAddress = "3N78XpUJ1VjSmsPr3vMKdPEEo6fRE7NyBJF"
addressRecipient = pywaves.Address(address=withdrawAddress)
response = addressSender.sendWaves(addressRecipient,
                                   1120000,
                                   txFee=pywaves.DEFAULT_SMART_FEE + pywaves.DEFAULT_BASE_FEE)
print("recipient address: %s\nresponse:\n%s" % (withdrawAddress, response))

withdrawAddress = "3NCjREHB7dUFCzPhdy9g8oWhJy4YQyPaGmv"
addressRecipient = pywaves.Address(address=withdrawAddress)
response = addressSender.sendWaves(addressRecipient,
                                   1130000,
                                   txFee=pywaves.DEFAULT_SMART_FEE + pywaves.DEFAULT_BASE_FEE)
print("recipient address: %s\nresponse:\n%s" % (withdrawAddress, response))
