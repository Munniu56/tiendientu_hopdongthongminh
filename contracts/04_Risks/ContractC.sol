// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ContractC is ERC20, Ownable {
    mapping(address => bool) public isBlacklisted;

    constructor() ERC20("Blacklist Token", "BLTK") Ownable(msg.sender) {
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Risk: Owner co the dua vi nguoi dung vao danh sach den
    function setBlacklist(address _user, bool _status) public onlyOwner {
        isBlacklisted[_user] = _status;
    }

    function _update(address from, address to, uint256 value) internal override {
        require(!isBlacklisted[from], "Sender is blacklisted");
        super._update(from, to, value);
    }
}