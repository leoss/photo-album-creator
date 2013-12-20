import os
import codecs
import xml.etree.ElementTree as ET

fileout = '''
<html><head>
<meta name="robots" content="noindex,nofollow">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.js"></script>
<script src="galleria/galleria-1.2.8.min.js"></script>
<style>
    #galleria{ width: 1200px; height: 800px; background: #000 }
</style>
</head><body bgcolor="black">
'''
fileout += '<div id="galleria">\n'


tree = ET.parse('data.xml')
root = tree.getroot()

for pic in root:
    filename = str(pic.find('filename').text)
    title = pic.find('title').text
    if title == None:
        title = "-"
    description = pic.find('description').text
    if description == None:
        description = "-"
    print("working on "+filename)
    fileout += '<a href="images_large/'+filename+'"><img src="images_thumb/'+filename+'" data-title="'+title+'" data-description="'+description+'"></a>\n'

fileout +="\</div>\n\
<script>\n\
    Galleria.loadTheme('galleria/themes/classic/galleria.classic.min.js');\n\
    Galleria.run('#galleria', {_toggleInfo: false});\n\
</script>\n\n\
</body></html>"

print(fileout)

fout = codecs.open("index.html","w","utf-8") #use utf8
fout.write(fileout)
fout.close()

print("write index.html")
