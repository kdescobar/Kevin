INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_TESTPY testpy)

FIND_PATH(
    TESTPY_INCLUDE_DIRS
    NAMES testpy/api.h
    HINTS $ENV{TESTPY_DIR}/include
        ${PC_TESTPY_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    TESTPY_LIBRARIES
    NAMES gnuradio-testpy
    HINTS $ENV{TESTPY_DIR}/lib
        ${PC_TESTPY_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(TESTPY DEFAULT_MSG TESTPY_LIBRARIES TESTPY_INCLUDE_DIRS)
MARK_AS_ADVANCED(TESTPY_LIBRARIES TESTPY_INCLUDE_DIRS)

