import unittest
import sys
import os
import pathlib
import shutil

sys.path.insert(0, "../")
from pdfrotate.pdf import *

# Copy the test file, so we don't overwrite it
path = pathlib.Path(__file__).parent.resolve()
input = os.path.join(path, "input.pdf")
workingFile = os.path.join(path, "test_output.pdf")
shutil.copy(input, workingFile)

foo = pdf(workingFile)

print(foo.doc.can_save_incrementally())
foo.rotate()
foo.rotate()
# foo.saveIncremental()
foo.save()

pass
