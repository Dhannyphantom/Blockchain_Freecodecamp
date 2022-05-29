from scripts.reusable_scripts import get_account
from scripts.deploy import deploy_fund_me

def can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee()
    print("Funding...")
    txFund = fund_me.fund({"value": entrance_fee, "from": account})
    txFund.wait(1)
    assert fund_me.addressToAmount(account.address) == entrance_fee
    print("Funded!")
    print("Withdrawing...")
    txWithdraw = fund_me.withdraw({"from": account})
    txWithdraw.wait(1)
    assert fund_me.addressToAmount(account.address) == 0
    print("Withdrawn")
