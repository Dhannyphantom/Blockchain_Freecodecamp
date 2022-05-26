from solcx import compile_standard, install_solc
import json
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

my_solc_verion = "0.8.0"

install_solc(my_solc_verion)

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version=my_solc_verion,
)

with open("./compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# TO DEPLOY WE NEED ;
# 1. BYTECODE / BYTECODE OBJECT
# 2. ABI

bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# TO CONNECT TO GANACHE
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
my_address = "0x9A34FF6a186FDb53eE8FA845f3399511462cC674"
private_key = os.getenv("PRIVATE_KEY")

# Create Contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
nonce = w3.eth.getTransactionCount(my_address)


# TO DEPLOY WE NEED THREE THINGS
# 1: BUILD TRANSACTION
# 2: SIGN THE TRANSACTION
# 3: SEND THE TRANSACTION

transaction = SimpleStorage.constructor().buildTransaction({
  "chainId": chain_id, "nonce": nonce, "from": my_address, "gasPrice": w3.eth.gas_price  
})

sign_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

print("Deploying contract...")

send_txn = w3.eth.send_raw_transaction(sign_txn.rawTransaction)
txn_recepit = w3.eth.wait_for_transaction_receipt(send_txn)

print("Contract Deployed!")

simple_storage = w3.eth.contract(address=txn_recepit.contractAddress, abi=abi)
print(simple_storage.functions.retrieve().call())

store_txn = simple_storage.functions.store(15).buildTransaction({
    "chainId": chain_id, "nonce": nonce + 1, "gasPrice": w3.eth.gas_price, "from": my_address
})

sign_store_txn = w3.eth.account.sign_transaction(store_txn, private_key=private_key)

print("Updating contract...")

send_store_txn = w3.eth.send_raw_transaction(sign_store_txn.rawTransaction)
store_txn_receipt = w3.eth.wait_for_transaction_receipt(send_store_txn)

print("Contract updated...")
print(simple_storage.functions.retrieve().call())