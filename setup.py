from cx_Freeze import setup, Executable

base = None    

executables = [Executable("Vchecker.py", base=base)]

packages = ["__future__","os","json","requests","wget","bs4","queue"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<any name>",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)