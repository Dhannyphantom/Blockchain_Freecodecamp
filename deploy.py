from solcx import compile_standard, install_solc
import json

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