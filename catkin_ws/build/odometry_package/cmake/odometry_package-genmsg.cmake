# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "odometry_package: 1 messages, 0 services")

set(MSG_I_FLAGS "-Iodometry_package:/home/user/catkin_ws/src/odometry_package/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(odometry_package_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/user/catkin_ws/src/odometry_package/msg/odometry_msg.msg" NAME_WE)
add_custom_target(_odometry_package_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "odometry_package" "/home/user/catkin_ws/src/odometry_package/msg/odometry_msg.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(odometry_package
  "/home/user/catkin_ws/src/odometry_package/msg/odometry_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/odometry_package
)

### Generating Services

### Generating Module File
_generate_module_cpp(odometry_package
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/odometry_package
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(odometry_package_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(odometry_package_generate_messages odometry_package_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/user/catkin_ws/src/odometry_package/msg/odometry_msg.msg" NAME_WE)
add_dependencies(odometry_package_generate_messages_cpp _odometry_package_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(odometry_package_gencpp)
add_dependencies(odometry_package_gencpp odometry_package_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS odometry_package_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(odometry_package
  "/home/user/catkin_ws/src/odometry_package/msg/odometry_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/odometry_package
)

### Generating Services

### Generating Module File
_generate_module_eus(odometry_package
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/odometry_package
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(odometry_package_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(odometry_package_generate_messages odometry_package_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/user/catkin_ws/src/odometry_package/msg/odometry_msg.msg" NAME_WE)
add_dependencies(odometry_package_generate_messages_eus _odometry_package_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(odometry_package_geneus)
add_dependencies(odometry_package_geneus odometry_package_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS odometry_package_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(odometry_package
  "/home/user/catkin_ws/src/odometry_package/msg/odometry_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/odometry_package
)

### Generating Services

### Generating Module File
_generate_module_lisp(odometry_package
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/odometry_package
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(odometry_package_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(odometry_package_generate_messages odometry_package_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/user/catkin_ws/src/odometry_package/msg/odometry_msg.msg" NAME_WE)
add_dependencies(odometry_package_generate_messages_lisp _odometry_package_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(odometry_package_genlisp)
add_dependencies(odometry_package_genlisp odometry_package_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS odometry_package_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(odometry_package
  "/home/user/catkin_ws/src/odometry_package/msg/odometry_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/odometry_package
)

### Generating Services

### Generating Module File
_generate_module_nodejs(odometry_package
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/odometry_package
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(odometry_package_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(odometry_package_generate_messages odometry_package_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/user/catkin_ws/src/odometry_package/msg/odometry_msg.msg" NAME_WE)
add_dependencies(odometry_package_generate_messages_nodejs _odometry_package_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(odometry_package_gennodejs)
add_dependencies(odometry_package_gennodejs odometry_package_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS odometry_package_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(odometry_package
  "/home/user/catkin_ws/src/odometry_package/msg/odometry_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/odometry_package
)

### Generating Services

### Generating Module File
_generate_module_py(odometry_package
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/odometry_package
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(odometry_package_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(odometry_package_generate_messages odometry_package_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/user/catkin_ws/src/odometry_package/msg/odometry_msg.msg" NAME_WE)
add_dependencies(odometry_package_generate_messages_py _odometry_package_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(odometry_package_genpy)
add_dependencies(odometry_package_genpy odometry_package_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS odometry_package_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/odometry_package)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/odometry_package
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(odometry_package_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/odometry_package)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/odometry_package
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(odometry_package_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/odometry_package)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/odometry_package
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(odometry_package_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/odometry_package)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/odometry_package
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(odometry_package_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/odometry_package)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/odometry_package\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/odometry_package
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(odometry_package_generate_messages_py std_msgs_generate_messages_py)
endif()
