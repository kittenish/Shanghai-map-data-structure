#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
from time import *
import evaluate_xml
import evaluate_taxi


node,way,relation,node1,graph,idx,lonlatid=evaluate_xml.evaluatexml()

class Map(QtGui.QWidget):

    def __init__(self):
        super(Map, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 700, 700)
        self.setWindowTitle('Shanghai_map')
        self.i = 0
        self.point = {}
        self.b=30.2
        self.t=32.1
        self.r=122
        self.l=120.5
        self.maxt=1.9
        self.fx=0
        self.fy=0
        self.time=time()
        self.show()


    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        #self.drawPoints(qp)
        self.drawLines(qp)
        time1 = time()
        print "Enddrwaing : %f" % (time1-self.time)
        self.time=time1
        qp.end()

    def mousePressEvent(self, event):
        #print self.pos()
        size = self.size()
        pointX = event.globalX()
        pointY = event.globalY()-45
        print pointX,pointY
        lat = float(size.height()-self.fy-pointY)*self.maxt/size.height()+self.b
        lon = float(pointX-self.fx)*self.maxt/size.width()+self.l
        self.point[self.i] = lon
        self.i = self.i+1
        self.point[self.i] = lat
        self.i=self.i+1
        print lat,lon
        if self.i%4 == 0:
            self.b=self.point.get(self.i-3)
            self.t=self.point.get(self.i-1)
            self.r=self.point.get(self.i-2)
            self.l=self.point.get(self.i-4)
            print self.point.get(self.i-3), self.point.get(self.i-4), self.point.get(self.i-1), self.point.get(self.i-2)
            if self.r-self.l >self.t - self.b :
                self.maxt=self.r - self.l
                self.fx=0
                self.fy=(self.height()-((self.t-self.b)/self.maxt*self.height()))/2
                #print self.fy
            else :
                self.maxt=self.t-self.b
                self.fy=0
                self.fx=(self.width()-((self.r-self.l)/self.maxt*self.width()))/2
            #self.l=30.2
            #self.r=35
            #self.t=125
            #self.b=120.5


    #def drawPoints(self, qp):
        #qp.setPen(QtCore.Qt.darkGreen)
        #size = self.size()
        #nodetemp = idx.intersection((self.b,self.l ,self.t,self.r ), objects=True)

        #for i in nodetemp:
            #120.5 30.2
            #y = size.height()-(i.bbox[0]-self.b)/self.maxt*size.height() - self.fy
            #x = (i.bbox[1]-self.l)/self.maxt*size.width() + self.fx
            #print x,y
            #qp.drawPoint(x,y)
        #qp.setPen(QtCore.Qt.gray)


    def drawLines(self,qp):
        pen1 = QtGui.QPen(QtCore.Qt.darkCyan,0.5,QtCore.Qt.SolidLine)
        pen2 = QtGui.QPen(QtCore.Qt.magenta,0.3,QtCore.Qt.SolidLine)
        pen3 = QtGui.QPen(QtCore.Qt.blue,3,QtCore.Qt.SolidLine)
        pen4 = QtGui.QPen(QtCore.Qt.darkMagenta,1,QtCore.Qt.SolidLine)
        pen5 = QtGui.QPen(QtCore.Qt.blue,1,QtCore.Qt.SolidLine)
        pen6 = QtGui.QPen(QtCore.Qt.magenta,1.5,QtCore.Qt.SolidLine)
        qp.setPen(pen1)
        size = self.size()
        for i in way :
            flag = 0
            qp.setPen(pen1)
            if i.tags.has_key("highway"):
                if ((self.r - self.l)<0.25 or (self.t - self.b)<0.25) :
                    qp.setPen(pen6)
                else :
                    qp.setPen(pen2)
                flag = 1
            if i.tags.has_key("waterway") :
                if ((self.r - self.l)<0.25 or (self.t - self.b)<0.25) :
                    qp.setPen(pen3)
                else :
                    qp.setPen(pen5)
                flag = 1
            if i.tags.has_key("aeroway") :
                qp.setPen(pen4)
                flag = 1
            des = len(i.ref)
            if ((self.r-self.l)<0.05 or (self.t - self.b)<0.05 or flag ==1) :
                for j in xrange(0 , des-1) :
                    #if node[node1.get(i.ref[j])].lon < self.r and node[node1.get(i.ref[j])].lon >self.l and node[node1.get(i.ref[j])].lat < self.t and node[node1.get(i.ref[j])].lat > self.b :
                    lon1=(node[node1.get(i.ref[j])].lon-self.l)/self.maxt*size.height() + self.fx
                    lon2=(node[node1.get(i.ref[j+1])].lon-self.l)/self.maxt*size.height() + self.fx
                    lat1=self.height()-(node[node1.get(i.ref[j])].lat-self.b)/self.maxt*size.height() - self.fy
                    lat2=self.height()-(node[node1.get(i.ref[j+1])].lat-self.b)/self.maxt*size.height() - self.fy
                    qp.drawLines(QtCore.QPoint(lon1,lat1),QtCore.QPoint(lon2,lat2))


def main():
    print "Start drawing ..."
    app = QtGui.QApplication(sys.argv)
    ex = Map()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()