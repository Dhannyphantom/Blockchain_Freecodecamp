from brownie import accounts, SimpleStorage

def test_deploy():
    # ARRANGE
    account = accounts[0]
    # ACT
    simple_storage = SimpleStorage.deploy({"from": account})
    initial_value = simple_storage.retrieve()
    expected = 0
    # ASSET
    assert expected == initial_value

def test_storage():
    # ARRANGE
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # ACT
    expected = 15
    store_transaction = simple_storage.store(expected, {"from": account})
    store_transaction.wait(1)
    # ASSERT
    assert expected == simple_storage.retrieve()