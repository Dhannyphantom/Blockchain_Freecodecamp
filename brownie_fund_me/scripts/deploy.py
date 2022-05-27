from brownie import FundMe, MockV3Aggregator, accounts, network, config
from scripts.reusable_scripts import get_account
from web3 import Web3

STARTER = 8
INITIAL = 2000

def deploy_fund_me():
    account = get_account()
    conn_network = network.show_active()

    if conn_network != "development":
        price_feed_address = config["networks"][conn_network]["eth_usd_price_feed"]
    else:
        print(f"The active network is {conn_network}")
        print("Deploying mocks")
        if len(MockV3Aggregator) < 1:
            MockV3Aggregator.deploy(STARTER, Web3.toWei(INITIAL, "ether"), {"from": account})
        print("Mocks Deployed!")
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(price_feed_address, {"from": account}, publish_source=config["networks"][conn_network].get("verify"))
    print(f"Contract deployed to {fund_me.address} Yay!!!!!!")

def main():
    deploy_fund_me()