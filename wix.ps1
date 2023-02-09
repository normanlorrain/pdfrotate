$env:Path = 'C:\Program Files (x86)\WiX Toolset v3.11\bin;' + $env:Path

heat dir dist -srd -dr INSTALLFOLDER -cg PDFrotate -gg -out dist.wxs

candle pdfrotate.wxs  dist.wxs


light -out foobar .\pdfrotate.wixobj .\dist.wixobj

