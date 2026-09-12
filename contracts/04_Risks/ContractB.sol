// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ContractB is ERC20, Ownable {
    constructor() ERC20("Inflation Token", "INFT") Ownable(msg.sender) {
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Risk: Owner co the mint token vo han lam loang gia tri
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
}