from brownie import accounts,network, FundMe, config

def deploy_test_fundme():
    account = getAccount()

    fund_me = FundMe.deploy({"from": account})
    
    fund_txn = fund_me.getVersion()
    print(fund_txn)

def getAccount():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_test_fundme()