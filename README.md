photo-album-creator
===================

These scripts take photos and create a photo album. It is possible to annotate photos.
The aim is to make the annotation process as simple as possible.

As a result a web photo album is created.

Steps:
- copy your images into directory "images_orig"
- resize you images yourself
-- copy resized images (800x600) format into folder "images_large"
-- copy resized images (200x...) format into folder "images_thumb"
- start create_data_listing.py
  data.xml is created
- edit data.xml and insert title and descriptions. Use UTF8!
- start create_photo_album_from_xmldata.py
- copy whole directory into web folder
Now users can start looking at photo album by accessing index.html
