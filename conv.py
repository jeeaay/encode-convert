#!python
# -*- coding: UTF-8 -*-

'''
/*
 * @Author: jeay 
 * @Date: 2018-05-28 09:03:01 
 * @Last Modified by: jeay
 * @Last Modified time: 2018-05-28 17:45:10
 */
'''

import os,sys
import chardet
import wx
import gui
import time

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
            new_content = content.encode(out_enc)
            fp = open(filename, 'wb')
            fp.write(new_content)
            fp.close()
            return filename + " done"
            pass
            #print(" done")
        else:
            return filename + " already "+coding
            pass
            #print(coding)
    except IOError:
        return filename + " error "
        pass
        #print(" error")

class MianWindow(gui.ConvFrame):
    def init_main_window(self):  
        self.dirPicker.SetPath(os.getcwd())
        self.extlist = ['.txt','.php','.html','.htm','.css','.js','.sass']
    def OnChangeCheckBox( self, event ):
        cb = event.GetEventObject()
        if(cb.GetValue()):
            self.extlist.append(cb.GetLabel())
        else:
            self.extlist.remove(cb.GetLabel())
		#event.Skip()
    def StartConvert( self, event ):
        for (root, dirs, files) in os.walk(self.dirPicker.GetPath()):
            for filename in files:
                fpath = os.path.join(root,filename)
                if fpath.endswith(tuple(self.extlist)):
                    res = convert(os.path.join(root,filename),self.m_choice.GetStringSelection())
                    time.sleep(0.1)
                    self.listBoxLog.Append( res )
                else:
                    pass
                    # self.listBoxLog.Append( res )
                time.sleep(0.1)
        self.listBoxLog.Append(u'All files done')

if __name__ == '__main__':  
    app = wx.App()  
    
    main_win = MianWindow(None)  
    main_win.init_main_window()  
    main_win.Show()  
    app.MainLoop() 



