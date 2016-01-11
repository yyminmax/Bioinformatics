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
 
    def save_page(self):
        #print finished
        if True:
            print(u"开始截图！")
            size = self.webpage.mainFrame().contentsSize()
            print(u"页面宽：%d，页面高：%d" % (size.width(),size.height()))
            self.webpage.setViewportSize(QtCore.QSize(size.width()+16,size.height()))
            img = QtGui.QImage(size, QtGui.QImage.Format_ARGB32)
            painter = QtGui.QPainter(img)
            self.webpage.mainFrame().render(painter)
            painter.end()
            filename= self.filename;
            if img.save(filename):
                filepath = os.path.join(os.path.dirname(__file__), filename)
                print(u"截图完毕：%s" % filepath)
            else:
                print(u"截图失败");
        else:
            print(u"网页加载失败")
        self.close()
        
def Move_to_Next_Page(start_url, cnt):
    #r = requests.get(start_url)
    x = '1372-1373-0-0-0-'
    y = '-1-0-0-1-%E5%85%A8%E9%83%A8-%E5%85%A8%E9%83%A8-%E5%85%A8%E9%83%A8' 
    url = start_url + x + str(cnt) + y
    return url

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    url = 'http://t.zmlearn.com'
    cnt = 2
    while(cnt < 8443):
        name = 'Ques' + str(cnt) + '.png'
        shotter = PageShotter(url, name)
        print name
        shotter.shot()
        
        url = Move_to_Next_Page(url, cnt)
        cnt += 1
    sys.exit(app.exec_())
