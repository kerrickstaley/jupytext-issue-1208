# %%
import os
import sys
sys.modules[__name__].__path__ = [os.getcwd()]
sys.modules['foo'] = sys.modules[__name__]

# %%
import util
from foo.bar import baz

# %%
util.my_print(f'executed foo/__init__.py as {__name__}')
