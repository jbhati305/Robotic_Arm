// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from my_msg_package:msg/MyMessage.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "my_msg_package/msg/detail/my_message__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace my_msg_package
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void MyMessage_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) my_msg_package::msg::MyMessage(_init);
}

void MyMessage_fini_function(void * message_memory)
{
  auto typed_message = static_cast<my_msg_package::msg::MyMessage *>(message_memory);
  typed_message->~MyMessage();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember MyMessage_message_member_array[1] = {
  {
    "data",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(my_msg_package::msg::MyMessage, data),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers MyMessage_message_members = {
  "my_msg_package::msg",  // message namespace
  "MyMessage",  // message name
  1,  // number of fields
  sizeof(my_msg_package::msg::MyMessage),
  MyMessage_message_member_array,  // message members
  MyMessage_init_function,  // function to initialize message memory (memory has to be allocated)
  MyMessage_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t MyMessage_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &MyMessage_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace my_msg_package


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<my_msg_package::msg::MyMessage>()
{
  return &::my_msg_package::msg::rosidl_typesupport_introspection_cpp::MyMessage_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, my_msg_package, msg, MyMessage)() {
  return &::my_msg_package::msg::rosidl_typesupport_introspection_cpp::MyMessage_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
