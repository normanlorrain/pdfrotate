import unittest
import sys
import os
import pathlib

sys.path.insert(0, "../")
from pdfrotate.pdf import *


path = pathlib.Path(__file__).parent.resolve()
foo = os.path.join(path, "input.pdf")

backup = BackupFile(foo)
pass
del backup
pass

backup2 = BackupFile(foo)
backup2.keep = True
pass
del backup2
pass
