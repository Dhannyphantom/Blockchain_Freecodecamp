from brownie import FundMe, accounts

def deploy_fund_me():
    account = accounts[0]
    fund_me = FundMe.deploy({"from": account})

def main():
    deploy_fund_me()