#!/usr/bin/env python

import wget
from xml.etree import ElementTree as et

"""
<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
 <Name>contagiomobile.deependresearch.org</Name>
 <Prefix/>
 <Marker/>
 <MaxKeys>1000</MaxKeys>
 <IsTruncated>false</IsTruncated>
 <Contents>
	<Key>
	ackposts_5622aac15cbc2f04cbf843b6b36864d2_android_samp.zip
	</Key>
	<LastModified>2018-03-28T05:23:53.000Z</LastModified>
	<ETag>"eee2d9a7becf12b0442ee8dab72b2a68"</ETag>
	<Size>60842</Size>
	<StorageClass>STANDARD</StorageClass>
 </Contents>
 <Contents>
	<Key>
	Airpush_2EED7318CA564A909E75AD616CAD5CDF-airpush.zip
	</Key>
	<LastModified>2018-03-28T03:09:12.000Z</LastModified>
	<ETag>"4d7e506a6b991a01aab367846dfbe1d6"</ETag>
	<Size>5589261</Size>
	<StorageClass>STANDARD</StorageClass>
 </Contents>
</ListBucketResult>
"""

tree = et.parse('index.html')
root = tree.getroot()

#for child in root:
#    print child.tag, child.attrib, child.text

#for key in root.iter():
#	print key

for key in root.iter('{http://s3.amazonaws.com/doc/2006-03-01/}Key'):
	print key.text
	url = "http://contagiomobile.deependresearch.org/" + key.text
	wget.download(url)
	print "\n"
	
