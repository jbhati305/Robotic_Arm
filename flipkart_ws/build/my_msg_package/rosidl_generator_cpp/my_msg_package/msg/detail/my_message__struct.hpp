// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_msg_package:msg/MyMessage.idl
// generated code does not contain a copyright notice

#ifndef MY_MSG_PACKAGE__MSG__DETAIL__MY_MESSAGE__STRUCT_HPP_
#define MY_MSG_PACKAGE__MSG__DETAIL__MY_MESSAGE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__my_msg_package__msg__MyMessage __attribute__((deprecated))
#else
# define DEPRECATED__my_msg_package__msg__MyMessage __declspec(deprecated)
#endif

namespace my_msg_package
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct MyMessage_
{
  using Type = MyMessage_<ContainerAllocator>;

  explicit MyMessage_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->data = 0l;
    }
  }

  explicit MyMessage_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->data = 0l;
    }
  }

  // field types and members
  using _data_type =
    int32_t;
  _data_type data;

  // setters for named parameter idiom
  Type & set__data(
    const int32_t & _arg)
  {
    this->data = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_msg_package::msg::MyMessage_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_msg_package::msg::MyMessage_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_msg_package::msg::MyMessage_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_msg_package::msg::MyMessage_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_msg_package::msg::MyMessage_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_msg_package::msg::MyMessage_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_msg_package::msg::MyMessage_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_msg_package::msg::MyMessage_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_msg_package::msg::MyMessage_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_msg_package::msg::MyMessage_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_msg_package__msg__MyMessage
    std::shared_ptr<my_msg_package::msg::MyMessage_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_msg_package__msg__MyMessage
    std::shared_ptr<my_msg_package::msg::MyMessage_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MyMessage_ & other) const
  {
    if (this->data != other.data) {
      return false;
    }
    return true;
  }
  bool operator!=(const MyMessage_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MyMessage_

// alias to use template instance with default allocator
using MyMessage =
  my_msg_package::msg::MyMessage_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace my_msg_package

#endif  // MY_MSG_PACKAGE__MSG__DETAIL__MY_MESSAGE__STRUCT_HPP_
