# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.19

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = C:\Users\daria\AppData\Local\JetBrains\Toolbox\apps\CLion\ch-0\211.6693.114\bin\cmake\win\bin\cmake.exe

# The command to remove a file.
RM = C:\Users\daria\AppData\Local\JetBrains\Toolbox\apps\CLion\ch-0\211.6693.114\bin\cmake\win\bin\cmake.exe -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "C:\Users\daria\Documents\study\facultate\anul 2\Semestrul 1\Retele de calculatoare\Lab\Lab2\H1_commandExecution_c_server"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "C:\Users\daria\Documents\study\facultate\anul 2\Semestrul 1\Retele de calculatoare\Lab\Lab2\H1_commandExecution_c_server\cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/H1_commandExecution_c_server.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/H1_commandExecution_c_server.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/H1_commandExecution_c_server.dir/flags.make

CMakeFiles/H1_commandExecution_c_server.dir/server.c.obj: CMakeFiles/H1_commandExecution_c_server.dir/flags.make
CMakeFiles/H1_commandExecution_c_server.dir/server.c.obj: ../server.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="C:\Users\daria\Documents\study\facultate\anul 2\Semestrul 1\Retele de calculatoare\Lab\Lab2\H1_commandExecution_c_server\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/H1_commandExecution_c_server.dir/server.c.obj"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\H1_commandExecution_c_server.dir\server.c.obj -c "C:\Users\daria\Documents\study\facultate\anul 2\Semestrul 1\Retele de calculatoare\Lab\Lab2\H1_commandExecution_c_server\server.c"

CMakeFiles/H1_commandExecution_c_server.dir/server.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/H1_commandExecution_c_server.dir/server.c.i"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E "C:\Users\daria\Documents\study\facultate\anul 2\Semestrul 1\Retele de calculatoare\Lab\Lab2\H1_commandExecution_c_server\server.c" > CMakeFiles\H1_commandExecution_c_server.dir\server.c.i

CMakeFiles/H1_commandExecution_c_server.dir/server.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/H1_commandExecution_c_server.dir/server.c.s"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S "C:\Users\daria\Documents\study\facultate\anul 2\Semestrul 1\Retele de calculatoare\Lab\Lab2\H1_commandExecution_c_server\server.c" -o CMakeFiles\H1_commandExecution_c_server.dir\server.c.s

# Object files for target H1_commandExecution_c_server
H1_commandExecution_c_server_OBJECTS = \
"CMakeFiles/H1_commandExecution_c_server.dir/server.c.obj"

# External object files for target H1_commandExecution_c_server
H1_commandExecution_c_server_EXTERNAL_OBJECTS =

H1_commandExecution_c_server.exe: CMakeFiles/H1_commandExecution_c_server.dir/server.c.obj
H1_commandExecution_c_server.exe: CMakeFiles/H1_commandExecution_c_server.dir/build.make
H1_commandExecution_c_server.exe: CMakeFiles/H1_commandExecution_c_server.dir/linklibs.rsp
H1_commandExecution_c_server.exe: CMakeFiles/H1_commandExecution_c_server.dir/objects1.rsp
H1_commandExecution_c_server.exe: CMakeFiles/H1_commandExecution_c_server.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="C:\Users\daria\Documents\study\facultate\anul 2\Semestrul 1\Retele de calculatoare\Lab\Lab2\H1_commandExecution_c_server\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable H1_commandExecution_c_server.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\H1_commandExecution_c_server.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/H1_commandExecution_c_server.dir/build: H1_commandExecution_c_server.exe

.PHONY : CMakeFiles/H1_commandExecution_c_server.dir/build

CMakeFiles/H1_commandExecution_c_server.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\H1_commandExecution_c_server.dir\cmake_clean.cmake
.PHONY : CMakeFiles/H1_commandExecution_c_server.dir/clean

CMakeFiles/H1_commandExecution_c_server.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" "C:\Users\daria\Documents\study\facultate\anul 2\Semestrul 1\Retele de calculatoare\Lab\Lab2\H1_commandExecution_c_server" "C:\Users\daria\Documents\study\facultate\anul 2\Semestrul 1\Retele de calculatoare\Lab\Lab2\H1_commandExecution_c_server" "C:\Users\daria\Documents\study\facultate\anul 2\Semestrul 1\Retele de calculatoare\Lab\Lab2\H1_commandExecution_c_server\cmake-build-debug" "C:\Users\daria\Documents\study\facultate\anul 2\Semestrul 1\Retele de calculatoare\Lab\Lab2\H1_commandExecution_c_server\cmake-build-debug" "C:\Users\daria\Documents\study\facultate\anul 2\Semestrul 1\Retele de calculatoare\Lab\Lab2\H1_commandExecution_c_server\cmake-build-debug\CMakeFiles\H1_commandExecution_c_server.dir\DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/H1_commandExecution_c_server.dir/depend
