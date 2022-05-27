from brownie import FundMe, accounts
from scripts.reusable_scripts import get_account

def deploy_fund_me():
    account = get_account()
    fund_me = FundMe.deploy({"from": account}, publish_source=True)
    print(f"Contract deployed to {fund_me.address} Yay!!!!!!")

def main():
    deploy_fund_me()