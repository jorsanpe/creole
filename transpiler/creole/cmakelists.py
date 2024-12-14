def cmakelists(project_name):
    return f'''cmake_minimum_required(VERSION 3.17)
project({project_name})

set(CMAKE_VERBOSE_MAKEFILE ON)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${{CMAKE_CURRENT_SOURCE_DIR}}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${{CMAKE_CURRENT_SOURCE_DIR}}/bin)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${{CMAKE_CURRENT_SOURCE_DIR}}/bin)

file(GLOB_RECURSE APP_SOURCES src/*.c)

get_filename_component(full_path_main ${{CMAKE_CURRENT_SOURCE_DIR}}/main.c ABSOLUTE)
list(REMOVE_ITEM APP_SOURCES ${{full_path_main}})

# add_library(app-library OBJECT ${{APP_SOURCES}})
# target_compile_options(app-library PUBLIC -Werror)
add_executable({project_name} main.c)
'''
