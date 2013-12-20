# -*- coding: utf-8 -*-

import os

filelist = os.listdir("./images_orig/")
fileout = '<?xml version="1.0" encoding="UTF-8"?>\n<!-- Please insert UTF8 Text -->\n<list>\n'

for file in filelist:
    print("working on "+file)
    fileout += ' <picture>\n'
    fileout += '  <filename>'+file+'</filename>\n'
    fileout += '  <title></title>\n'
    fileout += '  <description></description>\n'
    fileout += ' </picture>\n'

fileout +="</list>"

print(fileout)

#TODO ask if file should be overwritten
fout = open("data.xml","w")
fout.write(fileout)
fout.close()

print("write data.xml")
