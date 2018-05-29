#!python
# -*- coding: UTF-8 -*-

'''
/*
 * @Author: jeay 
 * @Date: 2018-05-28 09:03:01 
 * @Last Modified by: jeay
 * @Last Modified time: 2018-05-29 17:16:32
 */
'''

import os,wx
import gui,conv

from threading import Thread
from wx.lib.pubsub import pub

__author__ = 'jeay'

class MianWindow(gui.ConvFrame):
    def init_main_window(self):
        pub.subscribe(self.updateLogs, "updatelogs")
        self.dirPicker.SetPath(os.getcwd())
        self.extlist = ['.txt','.php','.html','.htm','.css','.js','.sass']
    def OnChangeCheckBox( self, event ):
        cb = event.GetEventObject()
        if(cb.GetValue()):
            self.extlist.append(cb.GetLabel())
        else:
            self.extlist.remove(cb.GetLabel())
    def updateLogs(self,msg):
        self.listBoxLog.Append( msg )
        self.listBoxLog.SetSelection(self.listBoxLog.GetCount()-1)
        pass
		#event.Skip()
    def StartConvert( self, event ):
        srcDir = self.dirPicker.GetPath()
        extTuple = tuple(self.extlist)
        outEncode = self.m_choice.GetStringSelection()
        ConvThread(srcDir,extTuple,outEncode)
        """ for (root, dirs, files) in os.walk(srcDir):
            for filename in files:
                fpath = os.path.join(root,filename)
                if fpath.endswith(extTuple):
                    res = conv.convert(os.path.join(root,filename),outEncode)
                    time.sleep(0.1)
                    self.listBoxLog.Append( res )
                else:
                    pass
                    # self.listBoxLog.Append( res )
                time.sleep(0.1)
        self.listBoxLog.Append(u'All files done') """

class ConvThread(Thread):
    def __init__(self,srcDir,extTuple,outEncode):
        #线程实例化时立即启动
        self.srcDir = srcDir
        self.extTuple = extTuple
        self.outEncode = outEncode
        Thread.__init__(self)
        self.start()
    def run(self):
        #线程执行的代码
        for (root, dirs, files) in os.walk(self.srcDir):
            for filename in files:
                fpath = os.path.join(root,filename)
                if fpath.endswith(self.extTuple):
                    res = conv.convert(os.path.join(root,filename),self.outEncode)
                    wx.CallAfter(pub.sendMessage, "updatelogs", msg=res)
                else:
                    pass
        wx.CallAfter(pub.sendMessage, "updatelogs", msg=u'All files done')
            

if __name__ == '__main__':  
    app = wx.App()  
    
    main_win = MianWindow(None)  
    main_win.init_main_window()  
    main_win.Show()  
    app.MainLoop() 



