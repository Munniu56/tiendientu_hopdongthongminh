// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

/// @title Hợp đồng Quản lý Sinh viên
/// @notice Cho phép thêm sinh viên và truy xuất thông tin theo ID
contract StudentRegistry {
    // Định nghĩa cấu trúc dữ liệu Sinh viên
    struct Student {
        string name;
        uint8 age;
        bool isEnrolled;
    }

    // Biến lưu trữ chủ sở hữu hợp đồng
    address public immutable i_owner;

    // Mapping từ Mã sinh viên (ID) sang Thông tin sinh viên
    mapping(uint256 => Student) private s_students;

    // Tổng số sinh viên đã đăng ký
    uint256 public s_totalStudents;

    // Sự kiện phát ra khi thêm sinh viên mới
    event StudentAdded(uint256 indexed studentId, string name, uint8 age);

    // Custom Error kiểm tra quyền quản trị
    error Unauthorized();
    error StudentAlreadyExists(uint256 studentId);

    modifier onlyOwner() {
        if (msg.sender != i_owner) revert Unauthorized();
        _;
    }

    constructor() {
        i_owner = msg.sender;
    }

    /// @notice Hàm thêm sinh viên mới vào hệ thống
    /// @param _id Mã số sinh viên
    /// @param _name Tên sinh viên
    /// @param _age Tuổi sinh viên
    function addStudent(
        uint256 _id,
        string calldata _name,
        uint8 _age
    ) external onlyOwner {
        if (s_students[_id].isEnrolled) revert StudentAlreadyExists(_id);

        s_students[_id] = Student({
            name: _name,
            age: _age,
            isEnrolled: true
        });

        s_totalStudents++;

        emit StudentAdded(_id, _name, _age);
    }

    /// @notice Hàm lấy thông tin sinh viên theo ID
    function getStudent(uint256 _id)
        external
        view
        returns (string memory name, uint8 age, bool isEnrolled)
    {
        Student memory student = s_students[_id];
        return (student.name, student.age, student.isEnrolled);
    }
}