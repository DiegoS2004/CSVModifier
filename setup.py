from cx_Freeze import setup, Executable

# Define build options
build_exe_options = {
    "packages": ["tkinter", "pandas"],  # Include additional packages used by your app
    "includes": [],  # Use this if cx_Freeze misses importing any modules
    "excludes": [],  # Exclude modules you don't need
    "include_files": []  # Include any non-Python files you need in your executable
}

# Target executable
executables = [
    Executable("CSVModifier.py", base="Win32GUI")  # Use "Win32GUI" to avoid launching a command prompt window on Windows
]

setup(
    name="CSVModifier",
    version="0.1",
    description="My CSV modification application!",
    options={"build_exe": build_exe_options},
    executables=executables
)
