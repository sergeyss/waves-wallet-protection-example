from wwp.service.ConfigService import ConfigService
from wwp.service.CryptographicService import CryptographicService

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
