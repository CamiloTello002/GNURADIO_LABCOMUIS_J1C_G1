find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_MODULOS_D1A gnuradio-Modulos_D1A)

FIND_PATH(
    GR_MODULOS_D1A_INCLUDE_DIRS
    NAMES gnuradio/Modulos_D1A/api.h
    HINTS $ENV{MODULOS_D1A_DIR}/include
        ${PC_MODULOS_D1A_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_MODULOS_D1A_LIBRARIES
    NAMES gnuradio-Modulos_D1A
    HINTS $ENV{MODULOS_D1A_DIR}/lib
        ${PC_MODULOS_D1A_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-Modulos_D1ATarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_MODULOS_D1A DEFAULT_MSG GR_MODULOS_D1A_LIBRARIES GR_MODULOS_D1A_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_MODULOS_D1A_LIBRARIES GR_MODULOS_D1A_INCLUDE_DIRS)
