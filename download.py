# -*- coding: utf-8 -*- 
import urllib
import re
import sys
import time

#输出进度条
def dlProgress(count, blockSize, totalSize):
	percent = int(count*blockSize*100/totalSize)
	output ="[%d/%d]%s has downloaded %d%%: %d B/%d B" %(num,file_nums,name_url[0],percent,count*blockSize,totalSize)
	sys.stdout.write(output)
	sys.stdout.write('\b'*len(output))
	sys.stdout.flush()
	if percent >= 100:
		print  '[%d/%d] %s download is complete! %d B/%d B' %(num,file_nums,file_name,count*blockSize,totalSize)  

filepath = "C:\Users\Halouccr\Desktop\ICT2.txt"
txt = open(filepath)
txt_list = txt.readlines()
file_nums = len(txt_list)

#读取txt非空总行数
for x in txt_list:
	if not x.split():
		file_nums-=1

num = 0
for line in txt_list:
	if not line.split():
		#print 'This is a \\n'
		continue
	else:
		num =num+1
		name_url = line.split(' ',1)
		#print name_url[0]
		file_type = (name_url[1])[-5:-1]
		#print file_type
		file_name = name_url[0] + file_type
		#print file_name
		#sys.stdout.write(name_url[0] + '    ')
		targetpath = "C:\\Users\\Halouccr\\Desktop\\ICT2\\material\\" + file_name
		urllib.urlretrieve(name_url[1],targetpath,dlProgress)
txt.close()


