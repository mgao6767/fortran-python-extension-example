import os
import sys

if sys.platform == "win32":  # Windows
    os.add_dll_directory(os.path.join(os.path.dirname(__file__), ".libs"))
