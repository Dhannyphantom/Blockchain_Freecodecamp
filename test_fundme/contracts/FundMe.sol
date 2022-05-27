// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    
    mapping (address=>uint) public addressToAmount;

    function fund() public payable {
        addressToAmount[msg.sender] += msg.value
    }

    function getVersion() public view returns (uint) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface()
    }

}