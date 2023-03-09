import shutil
import datetime
import os
import pathlib


class BackupFile:
    def __init__(self, name) -> None:
        self.keep = False  # if we exit without changes, don't save the backup.
        name = pathlib.Path(name)
        timestamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
        self.temporaryBackup = name.with_stem(f"~{name.stem}")
        self.permanentBackup = name.with_stem(f"{name.stem} (pdfrotate {timestamp})")

        shutil.copyfile(name, self.temporaryBackup)
        print("Backup file created")

    def __del__(self):
        if self.keep:
            os.rename(self.temporaryBackup, self.permanentBackup)
            print("Kept backup file")
        else:
            os.remove(self.temporaryBackup)
            print("Removed backup file")
