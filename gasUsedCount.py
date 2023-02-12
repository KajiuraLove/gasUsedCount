from web3 import Web3

# 创建Web3连接
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/<YOUR-PROJECT-ID>"))

# 要查询的账户地址
address = "0x<ACCOUNT-ADDRESS>"

# 计算账户总的gas费用
total_gas_spent = 0
for i in range(w3.eth.getTransactionCount(address)):
    tx = w3.eth.getTransactionByBlock(i, address)
    total_gas_spent += tx["gasPrice"] * tx["gas"]

print("Account {} spent a total of {} wei on gas fees.".format(address, total_gas_spent))
