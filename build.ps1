if (test-path build) {
    Remove-Item -Force -Recurse build
}
if (test-path dist) {
    Remove-Item -Force -Recurse dist
}
# pyinstaller --onefile --icon pdf.png -n pdfrotate .\main.py
flet pack -i .\wix\pdf.png -n PDFrotate --onedir .\src\main.py