#!/usr/bin/env python3
import sys
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtQuick import QQuickView
import beautifulweather
import math
import qtawesome as qta

__author__ = "matthew beerens"
__version__ = "0.1.0"
__license__ = "MIT"

class MyWidget(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()

		#transparent background
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setWindowFlag(QtCore.Qt.Tool)

		#weather data
		self.weather = beautifulweather.get_weather()

		#img for weather description
		img = QtGui.QImage()
		img.loadFromData(self.weather[3].data)
		self.wimg = QtWidgets.QLabel()
		self.wimg.setPixmap(QtGui.QPixmap.fromImage(img))

		#description box
		dbox = QtWidgets.QHBoxLayout()
		dbox.setContentsMargins(10,0,10,10)
		self.desc = QtWidgets.QLabel(str(self.weather[0][0]['main']))
		self.desc.setAlignment(QtCore.Qt.AlignCenter)
		self.desc.setFont(QtGui.QFont('SansSerif', 14))
		self.wimg.setAlignment(QtCore.Qt.AlignCenter)
		dbox.addWidget(self.desc)
		dbox.addWidget(self.wimg)
		
		#temp box
		tbox = QtWidgets.QHBoxLayout()
		tbox.setContentsMargins(10,0,10,10)
		self.temp = QtWidgets.QLabel(str(round(self.weather[1]['temp'] - 273.15))+'°')
		self.temp_icon = qta.IconWidget('fa5s.thermometer-half', color='red')
		self.temp.setAlignment(QtCore.Qt.AlignCenter)
		self.temp.setFont(QtGui.QFont('SansSerif', 14))
		self.temp_icon.resize(30,30)
		tbox.addWidget(self.temp)
		tbox.addWidget(self.temp_icon)
		
		#humidity box
		hbox = QtWidgets.QHBoxLayout()
		hbox.setContentsMargins(10,0,10,10)
		self.humidity = QtWidgets.QLabel(str(self.weather[1]['humidity'])+'%')
		self.humidity_icon = qta.IconWidget('fa5s.tint', color='cyan')
		self.humidity.setAlignment(QtCore.Qt.AlignCenter)
		self.humidity.setFont(QtGui.QFont('SansSerif', 14))
		hbox.addWidget(self.humidity)
		hbox.addWidget(self.humidity_icon)
		
		#wind box
		wbox = QtWidgets.QHBoxLayout()
		wbox.setContentsMargins(10,0,10,10)
		self.wind = QtWidgets.QLabel(str(self.weather[2]['speed']))
		self.wind_icon = qta.IconWidget('fa5s.wind', color='white')
		self.wind.setAlignment(QtCore.Qt.AlignCenter)
		self.wind.setFont(QtGui.QFont('SansSerif',14))
		wbox.addWidget(self.wind)
		wbox.addWidget(self.wind_icon)

		#set layout
		self.layout = QtWidgets.QHBoxLayout()
		self.layout.setAlignment(QtCore.Qt.AlignCenter)
		self.layout.addLayout(tbox)
		self.layout.addLayout(dbox)
		self.layout.addLayout(hbox)
		self.layout.addLayout(wbox)
		self.layout.addStretch(1)

		#finialize layout
		self.setLayout(self.layout)

def main():
	app = QtWidgets.QApplication([])
	widget = MyWidget()
	screen_resolution = app.desktop().screenGeometry()
	widget.setGeometry(screen_resolution.width()-400,-10,400,20)
	widget.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()