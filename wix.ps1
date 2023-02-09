$env:Path = 'C:\Program Files (x86)\WiX Toolset v3.11\bin;' + $env:Path

heat dir dist -srd -dr INSTALLFOLDER -cg PDFrotate -gg -out pdfrotate.wxs

candle pdfrotate.wxs  pdfrotate_heat.wxs


light -out foobar .\pdfrotate.wixobj .\pdfrotate_heat.wixobj

