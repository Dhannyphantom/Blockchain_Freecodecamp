from brownie import network, accounts, config,MockV3Aggregator
from web3 import Web3

conn_network = network.show_active()
LOCAL_CHAIN_VAR = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 1

def get_account():
    if conn_network in LOCAL_CHAIN_VAR:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"The active network is {conn_network}")
    print("Deploying mocks")
    if len(MockV3Aggregator) < 1:
        MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()})
        print("Mocks Deployed!")