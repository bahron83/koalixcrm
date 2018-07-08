<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"
        xmlns:fo="http://www.w3.org/1999/XSL/Format">
    <xsl:decimal-format name="european" decimal-separator="," grouping-separator="."/>
    <xsl:template match="django-objects">
        <fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format">
            <!-- defines page layout -->
            <fo:layout-master-set>
                <fo:simple-page-master master-name="simple"
                                       page-height="21cm"
                                       page-width="29.7cm"
                                       margin-top="1.5cm"
                                       margin-bottom="1.0cm"
                                       margin-left="1.5cm"
                                       margin-right="1.5cm">
                    <fo:region-body margin-top="2.5cm" margin-bottom="1.5cm"/>
                    <fo:region-before extent="4.5cm"/>
                    <fo:region-after extent="1.5cm"/>
                </fo:simple-page-master>
            </fo:layout-master-set>
            <fo:page-sequence master-reference="simple">
                <fo:static-content flow-name="xsl-region-before">
                    <fo:table table-layout="fixed" width="100%">
                        <fo:table-column column-width="23.9cm"/>
                        <fo:table-column column-width="2.8cm"/>
                        <fo:table-body font-size="9pt"
                                       font-family="BitstreamVeraSans">
                            <fo:table-row height="2cm" border-bottom-color="black" border-bottom-style="solid"
                                          border-bottom-width="0.5pt">
                                <fo:table-cell padding-bottom="3pt">
                                    <fo:block text-align="left">
                                        <fo:external-graphic content-width="6.0cm">
                                            <xsl:attribute name="src">
                                                file:///<xsl:value-of select="filebrowser_directory"/>/<xsl:value-of
                                                    select="object[@model='djangoUserExtension.documenttemplate']/field[@name='logo']"/>
                                            </xsl:attribute>
                                        </fo:external-graphic>
                                    </fo:block>
                                </fo:table-cell>
                                <fo:table-cell padding-bottom="3pt">
                                    <fo:block font-size="7pt"
                                              font-family="BitstreamVeraSans"
                                              text-align="left"
                                              margin-top="0.15cm">Irgendeine Firma
                                    </fo:block>
                                    <fo:block font-size="7pt"
                                              font-family="BitstreamVeraSans"
                                              text-align="left">Irgendwostrasse 12
                                    </fo:block>
                                    <fo:block font-size="7pt"
                                              font-family="BitstreamVeraSans"
                                              text-align="left">CH-8000 Zürich
                                    </fo:block>
                                    <fo:block font-size="7pt"
                                              font-family="BitstreamVeraSans"
                                              text-align="left">www.koalix.org
                                    </fo:block>
                                    <fo:block font-size="7pt"
                                              font-family="BitstreamVeraSans"
                                              text-align="left">emailaddress@gmail.com
                                    </fo:block>
                                    <fo:block font-size="7pt"
                                              font-family="BitstreamVeraSans"
                                              text-align="left">+41 xx xxx xx xx
                                    </fo:block>
                                </fo:table-cell>
                            </fo:table-row>
                        </fo:table-body>
                    </fo:table>
                </fo:static-content>
                <fo:static-content flow-name="xsl-region-after">
                    <fo:block font-size="8pt"
                              font-family="BitstreamVeraSans"
                              text-align="left">
                        <xsl:text> </xsl:text>
                    </fo:block>
                    <fo:table table-layout="fixed" width="100%">
                        <fo:table-column column-width="5.0cm"/>
                        <fo:table-column column-width="5.0cm"/>
                        <fo:table-column column-width="13.7cm"/>
                        <fo:table-column column-width="3.0cm"/>
                        <fo:table-body>
                            <fo:table-row border-top-color="black" border-top-style="solid" border-top-width="0.5pt"
                                          height="0.1cm">
                                <fo:table-cell number-columns-spanned="4">
                                    <fo:block font-size="5pt"
                                              font-family="BitstreamVeraSans"
                                              text-align="left"
                                              font-weight="bold"
                                    >
                                        <xsl:text> </xsl:text>
                                    </fo:block>
                                </fo:table-cell>
                            </fo:table-row>
                            <fo:table-row>
                                <fo:table-cell>
                                    <fo:block font-size="7pt"
                                              font-family="BitstreamVeraSans"
                                              text-align="start">
                                        <xsl:value-of
                                                select="object[@model='djangoUserExtension.documenttemplate']/field[@name='pagefooterleft']"/>
                                    </fo:block>
                                </fo:table-cell>
                                <fo:table-cell>
                                    <fo:block font-size="7pt"
                                              font-family="BitstreamVeraSans"
                                              text-align="end">
                                        <xsl:value-of
                                                select="object[@model='djangoUserExtension.documenttemplate']/field[@name='pagefootermiddle']"/>
                                    </fo:block>
                                </fo:table-cell>
                                <fo:table-cell>
                                    <fo:block font-size="7pt"
                                              font-family="BitstreamVeraSans"
                                              text-align="end">
                                        <xsl:value-of
                                                select="object[@model='djangoUserExtension.documenttemplate']/field[@name='bankingaccountref']"/>
                                    </fo:block>
                                </fo:table-cell>
                                <fo:table-cell>
                                    <fo:block font-size="7pt"
                                              font-family="BitstreamVeraSans"
                                              text-align="end">Seite<fo:page-number/>/
                                        <fo:page-number-citation ref-id="last-page"/>
                                    </fo:block>
                                </fo:table-cell>
                            </fo:table-row>
                        </fo:table-body>
                    </fo:table>
                </fo:static-content>
                <fo:flow flow-name="xsl-region-body">
                    <xsl:for-each select="object[@model='crm.textparagraphinsalesdocument']">
                        <xsl:choose>
                            <xsl:when test="field[@name='purpose']='BS'">
                                <fo:block font-size="9pt"
                                          font-family="BitstreamVeraSans"
                                          color="black"
                                          text-align="left"
                                          margin-top="2cm"
                                          linefeed-treatment="preserve">
                                    <xsl:value-of select="field[@name='text_paragraph']"/>
                                </fo:block>
                            </xsl:when>
                        </xsl:choose>
                    </xsl:for-each>
                    <fo:block font-size="15pt"
                              font-family="BitstreamVeraSans"
                              color="black"
                              text-align="left"
                              font-weight="bold"
                              margin-top="2cm">
                        Work Report
                    </fo:block>
                    <fo:block font-size="10pt"
                              font-family="BitstreamVeraSans"
                              color="black"
                              text-align="left"
                              font-weight="bold"
                              margin-bottom="1cm">
                        Employee: <xsl:value-of select="object[@model='auth.user']/field[@name='username']"/>
                    </fo:block>
                    <xsl:for-each select="object[@model='crm.textparagraphinsalesdocument']">
                        <xsl:choose>
                            <xsl:when test="field[@name='purpose']='AS'">
                                <fo:block font-size="9pt"
                                          font-family="BitstreamVeraSans"
                                          color="black"
                                          text-align="left"
                                          margin-top="1cm"
                                          linefeed-treatment="preserve"
                                          page-break-after="always">
                                    <xsl:value-of select="field[@name='text_paragraph']"/>
                                </fo:block>
                            </xsl:when>
                        </xsl:choose>
                    </xsl:for-each>
                    <xsl:for-each select="object[@model='djangoUserExtension.userextension']/Month_Work_Hours">
                        <fo:table table-layout="fixed" width="100%">
                            <xsl:for-each select="../../object[@model='djangoUserExtension.userextension']/Day_Work_Hours">
                                <fo:table-column column-width="0.8cm"/>
                            </xsl:for-each>
                            <fo:table-header font-size="8pt" line-height="9pt" font-weight="bold"
                                             font-family="BitstreamVeraSans">
                                <fo:table-row>
                                    <xsl:for-each select="../../object[@model='djangoUserExtension.userextension']/Day_Work_Hours">
                                        <fo:table-cell border-color="black" border-style="solid" border-width="0.5pt"
                                                       padding="2.5pt">
                                            <fo:block text-align="start">
                                                <xsl:value-of select="current()/@day"/>
                                            </fo:block>
                                        </fo:table-cell>
                                    </xsl:for-each>
                                </fo:table-row>
                            </fo:table-header>
                            <fo:table-body font-size="9pt"
                                           font-family="BitstreamVeraSans">
                                <fo:table-row>
                                    <xsl:for-each select="../../object[@model='djangoUserExtension.userextension']/Day_Work_Hours">
                                        <fo:table-cell border-color="black" border-style="solid" border-width="0.5pt"
                                                       padding="2.5pt">
                                            <fo:block text-align="start">
                                                <xsl:value-of select="current()"/>
                                            </fo:block>
                                        </fo:table-cell>
                                    </xsl:for-each>
                                </fo:table-row>
                            </fo:table-body>
                        </fo:table>
                    </xsl:for-each>
                    <fo:block id="last-page"></fo:block>
                </fo:flow>
                <xsl:apply-templates/>
            </fo:page-sequence>
        </fo:root>
    </xsl:template>
</xsl:stylesheet>
