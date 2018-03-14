from cx_Freeze import setup,Executable
includes = []
excludes = []
packages = []
filename = "inicio.py"
setup(
    name = 'Myapp',
    version = '0.1',
    description = 'Gui test',
    author = 'no',
    author_email = 'someting@my.org',
    options = {'build_exe': {'excludes':excludes,'packages':packages,'includes':includes}},
    executables = [Executable(filename, base = "Win32GUI", icon = None)])