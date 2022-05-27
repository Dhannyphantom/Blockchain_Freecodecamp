from brownie import FundMe
from scripts.reusable_scripts import get_account

def fund():
    account = get_account()
    fund_me = FundMe[-1]
    entrance_fee = fund_me.getEntranceFee()
    print(f"Entrance Fee: {entrance_fee}")
    print("Funding... ")
    deploy_txn = fund_me.fund({"from": account, "value": entrance_fee})
    deploy_txn.wait(1)
    print("Funded!")

def withdraw():
    account = get_account()
    fund_me = FundMe[-1]
    print("Withrawing funds...")
    fund_me.withdraw({"from": account})
    print("Withdrawn!")

def main():
    fund()
    withdraw()