// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

// import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
// import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "../node_modules/@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    
    mapping (address=>uint) public addressToAmount;

    function fund() public payable {
        addressToAmount[msg.sender] += msg.value;
    }

    // RINKEBY PRICE FEED ADDRESS IS USED

    function getVersion() public view returns (uint) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        return priceFeed.version();
    }

    function getPrice() public view returns (uint) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        (, int price,,,) = priceFeed.latestRoundData();
        return uint(price);
    }

}