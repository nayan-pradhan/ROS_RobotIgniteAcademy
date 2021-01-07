cmake_minimum_required(VERSION 3.0.2)
project(my_custom_srv_msg_pkg)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)

add_service_files(
  FILES
  MyCustomServiceMessage.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs  # Or other packages containing msgs
)

catkin_package(
 CATKIN_DEPENDS rospy message_runtime
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)