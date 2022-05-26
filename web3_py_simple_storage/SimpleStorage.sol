// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract SimpleStorage {
    uint favoriteNumber;
    mapping(string => uint) public nameToFavNumber;

    struct Person {
        string name;
        uint number;
    }

    Person[] public people;

    function store(uint num) public {
        favoriteNumber = num;
    }

    function addPerson(string memory name, uint num) public {
        // CODE BELOW ALSO WORKS, AT LEAST I THINK
        // Person newPerson = Person({name: name, number: num});
        people.push(Person(name, num));
        nameToFavNumber[name] = num;
    }

    function retrieve() public view returns (uint) {
        return favoriteNumber;
    }
    
}