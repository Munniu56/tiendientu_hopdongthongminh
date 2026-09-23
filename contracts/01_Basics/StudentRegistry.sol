// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title Hop dong quan ly thong tin sinh vien (Student Registry)
/// @notice Cho phep them moi va tra cuu thong tin sinh vien, toi uu hoa gas
contract StudentRegistry {
    // Dinh nghia cau truc du lieu Student
    // Su dung bytes32 thay vi string giup toi uu hoa gas vi chi chiem dung 1 storage slot
    struct Student {
        uint256 id;
        bytes32 name;
        address wallet;
        bool isActive;
    }

    // Mapping tra cuu thong tin sinh vien theo dia chi vi
    mapping(address => Student) public students;

    // Mang luu danh sach dia chi vi de dem tong so sinh vien
    address[] public studentList;

    // Custom errors giup toi uu gas khi xay ra loi
    error InvalidAddress();
    error StudentAlreadyExists(address wallet);
    error StudentNotFound(address wallet);

    // Su kien duoc phat ra khi them sinh vien moi thanh cong
    event StudentAdded(uint256 indexed id, bytes32 indexed name, address indexed wallet);

    /// @notice Ham them sinh vien moi vao he thong
    /// @dev Ap dung mau thiet ke Checks-Effects-Interactions
    /// @param _id Ma so dinh danh cua sinh vien
    /// @param _name Ten sinh vien duoi dang bytes32
    /// @param _wallet Dia chi vi cua sinh vien
    function addStudent(
        uint256 _id,
        bytes32 _name,
        address _wallet
    ) external {
        // 1. Checks: Kiem tra tinh hop le cua du lieu dau vao
        if (_wallet == address(0)) {
            revert InvalidAddress();
        }
        if (students[_wallet].isActive) {
            revert StudentAlreadyExists(_wallet);
        }

        // 2. Effects: Thay doi trang thai luu tru tren blockchain
        students[_wallet] = Student({
            id: _id,
            name: _name,
            wallet: _wallet,
            isActive: true
        });

        studentList.push(_wallet);

        // 3. Interactions: Phat sinh event ghi log sau khi thay doi state
        emit StudentAdded(_id, _name, _wallet);
    }

    /// @notice Ham tra cuu thong tin chi tiet cua sinh vien theo dia chi vi
    /// @param _wallet Dia chi vi cua sinh vien can tra cuu
    /// @return id Ma so sinh vien
    /// @return name Ten sinh vien (bytes32)
    /// @return wallet Dia chi vi
    /// @return isActive Trang thai hoat dong
    function getStudent(address _wallet)
        external
        view
        returns (
            uint256 id,
            bytes32 name,
            address wallet,
            bool isActive
        )
    {
        Student memory student = students[_wallet];
        if (!student.isActive) {
            revert StudentNotFound(_wallet);
        }

        return (student.id, student.name, student.wallet, student.isActive);
    }

    /// @notice Ham lay tong so luong sinh vien da dang ky
    /// @return So luong sinh vien trong danh sach
    function getStudentCount() external view returns (uint256) {
        return studentList.length;
    }
}
