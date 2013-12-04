#!/usr/bin/python
import os
import sys
import commands
import optparse
import re
from os.path import join, getsize



def get_files(dir, pattern):
    size = 0L
    res = []
    for root,dir,files in os.walk(dir):
        for f in files:
            if f.endswith(pattern):
                res.append(join(root, f))
    return res


htmls = get_files("./", ".html")

def parse_jpg(text):
    pos =0
    end = len(text)
    res = []
    while(pos < end):
        if  text[pos:pos+4] == ".jpg" or text[pos:pos+4] == ".png":
            begin = pos
            while( begin > 0) :
                if text[begin-4:begin] == "http":
                    begin = begin - 4
                    break
                else:
                    begin = begin - 1
            res.append(text[begin:pos+4])
            pos = pos + 4
        else:
            pos = pos + 1
    return res
        
        
def process_one(jpg):
    length = len(jpg)
    first = 0
    while(first<length):
        if(jpg[first]=='/' and jpg[first+1]=='/'):
            first = first+1;
            break
        else:
            first = first+ 1;
    end = length - 1
    while(end > 0):
        if(jpg[end] == '/'):
            break
        else:
            end = end-1
    new_path = jpg[0:first] + "/chenyukang.github.com/images" + jpg[end:]
    return new_path
    
def process(html_file):
    f = open(html_file, "r")
    text = f.read()
    out_text = text
    res = parse_jpg(text)
    new_res = []
    if len(res) != 0:
        for jpg in res:
            new_jpg = process_one(jpg)
            new_res.append(new_jpg)
            out_text = out_text.replace(jpg, new_jpg)
    if(len(new_res) != 0):
        print html_file
        new_file = html_file + ".bak"
        out_html = open(new_file, "w+")
        out_html.write(out_text)
        out_html.close()
        cmd = "mv " + new_file + " " + html_file
        os.system(cmd)
    
for f in htmls:
    process(f)
                   

#pattern = re.compile('http:\/\/.+\.(jpg|png)')
#pattern = re.compile('(https?:)?//?[^\'"<>]+?\.(jpg|jpeg|gif|png)')
#pattern = re.compile('\.png|\.jpg')
#res = pattern.findall("ahttp://c/b/a.jpg:http://c/x.png")
#print res
