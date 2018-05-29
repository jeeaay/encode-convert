#!python
# -*- coding: UTF-8 -*-

'''
/*
 * @Author: jeay 
 * @Date: 2018-05-29 16:11:38 
 * @Last Modified by: jeay
 * @Last Modified time: 2018-05-29 17:33:37
 */
'''

import sys
import chardet


def convert(filename, out_enc = "UTF8"):
    try:
        #print("convert" , filename)
        fp = open(filename, 'rb')
        content = fp.read()
        fp.close()
        result = chardet.detect(content)
        coding = result.get('encoding')
        coding = coding.replace('-','').upper()

        if coding != out_enc:
            fp = open(filename, 'r', encoding=coding)
            content = fp.read()
            fp.close()
            try:
                new_content = content.encode(out_enc)
            except: 
                return filename + " error"
            fp = open(filename, 'wb')
            fp.write(new_content)
            fp.close()
            return filename + " done"
            #pass
            #print(" done")
        else:
            return filename + " already "+coding
            #pass
            #print(coding)
    except IOError:
        return filename + " error "
        #pass
        #print(" error")