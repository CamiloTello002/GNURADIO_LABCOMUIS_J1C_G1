# Install script for directory: /home/labcom/Escritorio/cosas_de_ge_ene_u_radio/lab3/proyecto_1/gr-Modulos_D1A

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/gnuradio-Modulos_D1A" TYPE FILE FILES "/home/labcom/Escritorio/cosas_de_ge_ene_u_radio/lab3/proyecto_1/gr-Modulos_D1A/cmake/Modules/gnuradio-Modulos_D1AConfig.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/labcom/Escritorio/cosas_de_ge_ene_u_radio/lab3/proyecto_1/gr-Modulos_D1A/build/include/gnuradio/Modulos_D1A/cmake_install.cmake")
  include("/home/labcom/Escritorio/cosas_de_ge_ene_u_radio/lab3/proyecto_1/gr-Modulos_D1A/build/lib/cmake_install.cmake")
  include("/home/labcom/Escritorio/cosas_de_ge_ene_u_radio/lab3/proyecto_1/gr-Modulos_D1A/build/apps/cmake_install.cmake")
  include("/home/labcom/Escritorio/cosas_de_ge_ene_u_radio/lab3/proyecto_1/gr-Modulos_D1A/build/docs/cmake_install.cmake")
  include("/home/labcom/Escritorio/cosas_de_ge_ene_u_radio/lab3/proyecto_1/gr-Modulos_D1A/build/python/Modulos_D1A/cmake_install.cmake")
  include("/home/labcom/Escritorio/cosas_de_ge_ene_u_radio/lab3/proyecto_1/gr-Modulos_D1A/build/grc/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/labcom/Escritorio/cosas_de_ge_ene_u_radio/lab3/proyecto_1/gr-Modulos_D1A/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
