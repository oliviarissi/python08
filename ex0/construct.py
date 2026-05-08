#!/usr/bin/env python3

import sys
import os
import site


if sys.prefix == sys.base_prefix:
    print("MATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {sys.prefix}")
    print("""Virtual Environment: None detected

WARNING: You're in the global environment!
The machines can see everything you install.

To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env\\Scripts\\activate # On Windows

Then run this program again.""")

else:
    print("MATRIX STATUS: Welcome to the construct\n")

    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}\n")
    print("""SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.

Package installation path:""")
    print(site.getsitepackages()[0])
