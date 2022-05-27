from brownie import accounts, config, SimpleStorage, network
import os

def deploy_simple_storage():
    # account = accounts.add(config["wallets"]["from_key"])
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    initial_value = simple_storage.retrieve()
    print(initial_value)
    store_transaction = simple_storage.store(16, {"from": account})
    store_transaction.wait(1)
    updated_value = simple_storage.retrieve()
    print(updated_value)

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_simple_storage()