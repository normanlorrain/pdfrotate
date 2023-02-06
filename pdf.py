import sys
import base64
import fitz
import pathlib
import os
from backup_file import BackupFile

print(fitz.__doc__)

width, height = fitz.paper_size("letter")


class pdf:
    def __init__(self, fname):
        # Be conservative and make a backup of the file first
        self.backup = BackupFile(fname)

        # Opening the PDF in memory, because during testing I found working with the
        # file on disk would lead to occasional file corruption.
        self.name = fname
        inputFile = open(fname, "rb")
        bytes = inputFile.read()
        inputFile.close()

        self.doc = fitz.Document(stream=bytes)

        self.page_count = len(self.doc)
        self.currentPage = 0

        # allocate storage for page display lists
        # dlist_tab = [None] * page_count

        title = "PyMuPDF display of '%s', pages: %i" % (fname, self.page_count)

    # ------------------------------------------------------------------------------
    # read the page data
    # ------------------------------------------------------------------------------
    def get_page(self, pno, zoom=False, max_size=None):
        global width, height

        pixmap = self.doc.get_page_pixmap(
            pno,
        )  # *, matrix: matrix_like = Identity, dpi=None, colorspace: Colorspace = csRGB, clip: rect_like = None, alpha: bool = False, annots: bool = True)
        width = pixmap.width
        height = pixmap.height
        print(f"get page {pno}: {width} x {height}")
        bytes = pixmap.tobytes()
        enc = base64.b64encode(bytes)
        strEnc = enc.decode("ascii")
        return strEnc

    def changePage(self, down=True):
        if down:
            self.currentPage += 1
        else:
            self.currentPage -= 1
        if self.currentPage < 0:
            self.currentPage = 0
        if self.currentPage >= self.doc.page_count:
            self.currentPage = self.doc.page_count - 1

        return self.currentPage

    def rotate(self):
        current_rotation = self.doc[self.currentPage].rotation
        new_rotation = (current_rotation + 180) % 360
        self.doc[self.currentPage].set_rotation(new_rotation)

    # def saveWithBackup(self):
    #     fpath = pathlib.Path(self.doc.name)
    #     newstem = fpath.stem + "-"
    #     newname = fpath.with_stem(newstem)

    #     self.doc.save(
    #         newname, incremental=False, encryption=fitz.PDF_ENCRYPT_KEEP
    #     )  # update the file - a sub-second matter

    # def saveIncremental(self):
    #     self.doc.save(
    #         pathlib.Path(self.doc.name),
    #         incremental=True,
    #         encryption=fitz.PDF_ENCRYPT_KEEP,
    #     )  # update the file - a sub-second matter

    def save(self):
        # fpath = pathlib.Path(self.name)
        self.backup.keep = True
        self.doc.save(self.name)
