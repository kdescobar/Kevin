INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_SYNCTEST synctest)

FIND_PATH(
    SYNCTEST_INCLUDE_DIRS
    NAMES synctest/api.h
    HINTS $ENV{SYNCTEST_DIR}/include
        ${PC_SYNCTEST_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    SYNCTEST_LIBRARIES
    NAMES gnuradio-synctest
    HINTS $ENV{SYNCTEST_DIR}/lib
        ${PC_SYNCTEST_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(SYNCTEST DEFAULT_MSG SYNCTEST_LIBRARIES SYNCTEST_INCLUDE_DIRS)
MARK_AS_ADVANCED(SYNCTEST_LIBRARIES SYNCTEST_INCLUDE_DIRS)

