// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_msg_package:msg/MyMessage.idl
// generated code does not contain a copyright notice

#ifndef MY_MSG_PACKAGE__MSG__DETAIL__MY_MESSAGE__BUILDER_HPP_
#define MY_MSG_PACKAGE__MSG__DETAIL__MY_MESSAGE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_msg_package/msg/detail/my_message__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_msg_package
{

namespace msg
{

namespace builder
{

class Init_MyMessage_data
{
public:
  Init_MyMessage_data()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_msg_package::msg::MyMessage data(::my_msg_package::msg::MyMessage::_data_type arg)
  {
    msg_.data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_msg_package::msg::MyMessage msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_msg_package::msg::MyMessage>()
{
  return my_msg_package::msg::builder::Init_MyMessage_data();
}

}  // namespace my_msg_package

#endif  // MY_MSG_PACKAGE__MSG__DETAIL__MY_MESSAGE__BUILDER_HPP_
