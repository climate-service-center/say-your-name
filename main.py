from os.path import dirname, basename, isfile, join
import glob
import importlib

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and basename(f) != "main.py"]

for m in __all__:
    i = importlib.import_module(m)
    getattr(i, f"say_hello")()
