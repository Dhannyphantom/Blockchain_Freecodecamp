from brownie import FundMe, MockV3Aggregator, accounts, network, config
from scripts.reusable_scripts import get_account, deploy_mocks

def deploy_fund_me():
    account = get_account()
    conn_network = network.show_active()

    if conn_network != "development":
        price_feed_address = config["networks"][conn_network]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(price_feed_address, {"from": account}, publish_source=config["networks"][conn_network].get("verify"))
    print(f"Contract deployed to {fund_me.address} Yay!!!!!!")

def main():
    deploy_fund_me()