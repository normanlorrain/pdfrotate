$env:Path = 'C:\Program Files (x86)\WiX Toolset v3.11\bin;' + $env:Path

# heat command from wix toolset. Scans a source for "harvesting".  Arguments:
#    dir dist                 == specify we want to harvest a directory ("dir {source}"), source = PyInstaller's "dist" output
#    -srd                     == suppress harvesting the root directory as an element NOT SURE IF NEEDED
#    -cg <ComponentGroupName> 
#    -gg                      == Generate GUIDS
#    -out dist.wxs            == output 

# Arguments stolen from DCSPresetManager
# os.path.join(wix_bin, 'heat.exe'), 'dir', r'dist\DCSPresetManager',
# '-ke', '-srd', '-v', '-ag',
# '-cg', 'RootDataGroup',
# '-dr', 'RootData',
# '-t', r'wix\appShortcut.xsl',
# '-out', r'build\wix\src.wix'

heat dir dist\PDFrotate -sw5150 -ke -srd -v -ag -cg RootDataGroup -dr RootData  -out dist.wxs

# "Compile" the XML
candle pdfrotate.wxs  dist.wxs

# "Link" the XML
light -out foobar -b dist\PDFrotate  .\pdfrotate.wixobj .\dist.wixobj

