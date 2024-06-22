cmake_minimum_required(VERSION 3.17.2...3.29)
project(${SKBUILD_PROJECT_NAME} LANGUAGES C Fortran)

find_package(
  Python
  COMPONENTS Interpreter Development.Module NumPy
  REQUIRED)

# F2PY headers
execute_process(
  COMMAND "${PYTHON_EXECUTABLE}" -c
          "import numpy.f2py; print(numpy.f2py.get_include())"
  OUTPUT_VARIABLE F2PY_INCLUDE_DIR
  OUTPUT_STRIP_TRAILING_WHITESPACE)

file(TO_CMAKE_PATH "${F2PY_INCLUDE_DIR}" F2PY_INCLUDE_DIRX)

add_library(fortranobject OBJECT "${F2PY_INCLUDE_DIRX}/fortranobject.c")
target_link_libraries(fortranobject PUBLIC Python::NumPy)
target_include_directories(fortranobject PUBLIC "${F2PY_INCLUDE_DIRX}")
set_property(TARGET fortranobject PROPERTY POSITION_INDEPENDENT_CODE ON)

file(TO_CMAKE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/pyeebls/eebls.f" EEBLS_F_FILE)
file(TO_CMAKE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/pyeebls/pyeebls.pyf" PYEEBLS_PYF_FILE)

file(TO_CMAKE_PATH "${CMAKE_CURRENT_BINARY_DIR}/_pyeebls-f2pywrappers.f" F2PYWRAPPERS_FILE)
file(TO_CMAKE_PATH "${CMAKE_CURRENT_BINARY_DIR}/_pyeeblsmodule.c" PYEEBLSMODULE_FILE)

add_custom_command(
  OUTPUT "${PYEEBLSMODULE_FILE}" "${F2PYWRAPPERS_FILE}"
  DEPENDS "${EEBLS_F_FILE}" "${PYEEBLS_PYF_FILE}"
  VERBATIM
  COMMAND "${Python_EXECUTABLE}" -m numpy.f2py
          "${EEBLS_F_FILE}" "${PYEEBLS_PYF_FILE}" -m _pyeebls)

python_add_library(
  _pyeebls MODULE "${PYEEBLSMODULE_FILE}"
  "${F2PYWRAPPERS_FILE}"
  "${EEBLS_F_FILE}" WITH_SOABI)
target_link_libraries(_pyeebls PRIVATE fortranobject)

install(TARGETS _pyeebls DESTINATION ./pyeebls/)
