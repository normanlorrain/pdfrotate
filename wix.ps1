$env:Path = 'C:\Program Files (x86)\WiX Toolset v3.11\bin;' + $env:Path

# heat command from wix toolset. Scans a source for "harvesting".  Arguments:
#    dir dist                 == specify we want to harvest a directory ("dir {source}"), source = PyInstaller's "dist" output
#    -srd                     == suppress harvesting the root directory as an element NOT SURE IF NEEDED
#    -cg <ComponentGroupName> 
#    -gg                      == Generate GUIDS
#    -out dist.wxs            == output 
heat dir dist -srd -cg PDFrotate -gg -out dist.wxs

# "Compile" the XML
candle pdfrotate.wxs  dist.wxs

# "Link" the XML
light -out foobar .\pdfrotate.wixobj .\dist.wixobj

