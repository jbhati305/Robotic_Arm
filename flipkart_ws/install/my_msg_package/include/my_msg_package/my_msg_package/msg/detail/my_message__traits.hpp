// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from my_msg_package:msg/MyMessage.idl
// generated code does not contain a copyright notice

#ifndef MY_MSG_PACKAGE__MSG__DETAIL__MY_MESSAGE__TRAITS_HPP_
#define MY_MSG_PACKAGE__MSG__DETAIL__MY_MESSAGE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "my_msg_package/msg/detail/my_message__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace my_msg_package
{

namespace msg
{

inline void to_flow_style_yaml(
  const MyMessage & msg,
  std::ostream & out)
{
  out << "{";
  // member: data
  {
    out << "data: ";
    rosidl_generator_traits::value_to_yaml(msg.data, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MyMessage & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: data
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "data: ";
    rosidl_generator_traits::value_to_yaml(msg.data, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MyMessage & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace my_msg_package

namespace rosidl_generator_traits
{

[[deprecated("use my_msg_package::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const my_msg_package::msg::MyMessage & msg,
  std::ostream & out, size_t indentation = 0)
{
  my_msg_package::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use my_msg_package::msg::to_yaml() instead")]]
inline std::string to_yaml(const my_msg_package::msg::MyMessage & msg)
{
  return my_msg_package::msg::to_yaml(msg);
}

template<>
inline const char * data_type<my_msg_package::msg::MyMessage>()
{
  return "my_msg_package::msg::MyMessage";
}

template<>
inline const char * name<my_msg_package::msg::MyMessage>()
{
  return "my_msg_package/msg/MyMessage";
}

template<>
struct has_fixed_size<my_msg_package::msg::MyMessage>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<my_msg_package::msg::MyMessage>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<my_msg_package::msg::MyMessage>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MY_MSG_PACKAGE__MSG__DETAIL__MY_MESSAGE__TRAITS_HPP_
