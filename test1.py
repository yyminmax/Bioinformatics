#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
import sys
import os.path
from PyQt4 import QtGui,QtCore,QtWebKit
 
class PageShotter(QtGui.QWidget):
    def __init__(self,url,filename,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.url = url
        self.filename = filename
        self.webpage = None
 
    def shot(self):
        webview = QtWebKit.QWebView(self)
        webview.load(QtCore.QUrl(self.url))
        self.webpage = webview.page()
        self.connect(webview,QtCore.SIGNAL("loadFinished(bool)"),self.save_page)
 
    def save_page(self,finished):
        #print finished
        if finished:
            print u"开始截图！"
            size = self.webpage.mainFrame().contentsSize()
            print u"页面宽：%d，页面高：%d" % (size.width(),size.height())
            self.webpage.setViewportSize(QtCore.QSize(size.width()+16,size.height()))
            img = QtGui.QImage(size, QtGui.QImage.Format_ARGB32)
            painter = QtGui.QPainter(img)
            self.webpage.mainFrame().render(painter)
            painter.end()
            filename= self.filename;
            if img.save(filename):
                filepath = os.path.join(os.path.dirname(__file__), filename)
                print u"截图完毕：%s" % filepath
            else:
                print u"截图失败";
        else:
            print u"网页加载失败！"
        self.close()
 
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    #shotter = PageShotter("http://www.adssfwewfdsfdsf.com")
    shotter = PageShotter("http://www.youku.com/", 'shot.png')
    shotter.shot()
    sys.exit(app.exec_())
