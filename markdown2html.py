#!/usr/bin/python

import sys
import codecs
import markdown
import os
import stat

mkdfile=sys.argv[1]

filepos = mkdfile.rfind("/")

filenamepos = mkdfile.rfind(".")

filename = mkdfile[filepos+1:filenamepos]

input_file = codecs.open(mkdfile, mode="r", encoding="utf-8")
text = input_file.read()
html = markdown.markdown(text,output_format="html",\
        extensions=['markdown.extensions.tables'])
htmlfinal = "<html>" + "\n" + \
            "    <head>\n" + \
            "    <meta http-equiv=Content-Type  content=\"text/html; charset=utf8\">\n" + \
            "    <link rel=\"stylesheet\" type=\"text/css\" href=\"stylesheets/stylesheet.css\" media=\"screen\">\n" + \
            "    </head>" + \
            "\n\n" + \
            "    <body>" + \
            "\n" + \
            "    " + html + \
            "\n" + \
            "    </body>" + \
            "\n" + \
            "</html>"

output_file = codecs.open(filename + ".html", mode="w", 
        encoding="utf-8",
        errors="xmlcharrefreplace")
output_file.write(htmlfinal)

os.chmod(filename+".html", stat.S_IRUSR+stat.S_IRGRP +stat.S_IWUSR+ stat.S_IROTH)
