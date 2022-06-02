from scripts.reusable_scripts import get_account
from scripts.deploy import deploy_fund_me, LOCAL_CHAIN_VAR
from brownie import network, accounts, exceptions
import pytest


def can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee()
    txFund = fund_me.fund({"value": entrance_fee, "from": account})
    txFund.wait(1)
    assert fund_me.addressToAmount(account.address) == entrance_fee
    txWithdraw = fund_me.withdraw({"from": account})
    txWithdraw.wait(1)
    assert fund_me.addressToAmount(account.address) == 0


def only_owner_can_withdraw():
    if network.show_active() not in LOCAL_CHAIN_VAR:
        pytest.skip("Only Local Testing")
    bad_actor = accounts.add()
    fund_me = deploy_fund_me()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
