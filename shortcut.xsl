<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet
  version="1.0"
  xmlns="http://schemas.microsoft.com/wix/2006/wi"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:wix="http://schemas.microsoft.com/wix/2006/wi"
  xmlns:str="http://xsltsl.org/string"
  exclude-result-prefixes="wix str"  
  >

  <xsl:output
    encoding="utf-8"
    method="xml"
    version="1.0"
    indent="yes"    
    />
	
  <!-- Force all components to be Win64="yes" as pyside2 etc. are 32 bit -->
  <xsl:template match='wix:Component'>
    <xsl:copy>
	  <xsl:attribute name="Win64">yes</xsl:attribute>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>
	
  
  <xsl:template match='wix:Component[contains(wix:File/@Source, "SourceDir\PDFrotate.exe")]'> 
    <!-- assumes there is only one Prog.exe -->
    <xsl:copy>
	  <xsl:attribute name="Win64">yes</xsl:attribute>
      <xsl:apply-templates select="@*|node()"/>
      <xsl:comment> added shortcut under Component with File that has Source with PDFrotate.exe</xsl:comment>
      <Shortcut 
        Id="ProgExeShortcut" 
        Name="PDF Rotate" 
		Icon="pdf.ico"
        Directory="ProgramMenuFolder" 
        Advertise="yes">
        <xsl:attribute name="WorkingDirectory"><xsl:value-of select="@Directory"/></xsl:attribute>
      </Shortcut>
    </xsl:copy>
  </xsl:template>

    <!-- identity template -->
  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>

  <xsl:template match='/'>
    <xsl:comment>*** DO NOT EDIT: Generated by heat.exe; transformed by shortcut.xsl</xsl:comment>
    <xsl:apply-templates select="@*|node()"/>
  </xsl:template>

</xsl:stylesheet>