// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_msg_package:msg/MyMessage.idl
// generated code does not contain a copyright notice

#ifndef MY_MSG_PACKAGE__MSG__DETAIL__MY_MESSAGE__STRUCT_H_
#define MY_MSG_PACKAGE__MSG__DETAIL__MY_MESSAGE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/MyMessage in the package my_msg_package.
/**
  * MyMessage.msg
 */
typedef struct my_msg_package__msg__MyMessage
{
  int32_t data;
} my_msg_package__msg__MyMessage;

// Struct for a sequence of my_msg_package__msg__MyMessage.
typedef struct my_msg_package__msg__MyMessage__Sequence
{
  my_msg_package__msg__MyMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_msg_package__msg__MyMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_MSG_PACKAGE__MSG__DETAIL__MY_MESSAGE__STRUCT_H_
