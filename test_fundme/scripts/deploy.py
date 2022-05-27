from brownie import accounts, FundMe

def deploy_test_fundme():
    account = accounts[0]

    fund_me = FundMe.deploy({"from": account})
    
    fund_txn = fund_me.fund(value=value)


def main():
    deploy_test_fundme()