from solcx import compile_standard, install_solc
import json
from web3 import Web3

my_solc_verion = "0.6.0"

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
        }
    },
    solc_version=my_solc_verion
)

with open("./compiled_code.json", "w") as file:
    json.dump(compiled_sol, file )

# TO DEPLOY WE NEED ;
# 1. BYTECODE / BYTECODE OBJECT
# 2. ABI

bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# TO CONNECT TO GANACHE
w3 = Web3(Web3.HTTPPROVIDER("http://127.0.0.1:7545"))

print(w3.isConnected())