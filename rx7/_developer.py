import sys
import platform



python_path = sys.executable
lookup_path = sys.path



def reload(module):
    import importlib
    importlib.reload(module)


def add_module_dir(path:str):
    sys.path.append(path)


def python_version(sep=False) -> str|tuple:
    if sep:
        return platform.python_version_tuple()
    return platform.python_version()


def run_path(path:str):
    import runpy
    return runpy.runpath(path)
