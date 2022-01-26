<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html> 
    <head>
       <meta name="Erscheinungsjahr" content="{//Erscheinungsjahr}"/>
    </head>
    <body>
        <h2><xsl:value-of select="//Autor"/></h2>
        <h4><xsl:value-of select="//Titel"/></h4>
        <xsl:for-each select="//Strophe">
           <p>
           <xsl:for-each select="Vers">
              <xsl:value-of select="."/><br/>
           </xsl:for-each>
           </p>
        </xsl:for-each>
    </body>
</html>
</xsl:template>
</xsl:stylesheet>