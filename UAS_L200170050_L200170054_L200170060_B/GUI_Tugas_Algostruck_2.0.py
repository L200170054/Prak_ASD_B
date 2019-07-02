from PyQt5 import QtCore, QtGui, QtWidgets
import re
from data_buku import *
from data_logika import *

class Ui_halaman_utama(object):
    
    def setupUi(self, halaman_utama):
        
        halaman_utama.setObjectName("halaman_utama")
        halaman_utama.resize(795, 590)

        self.centralwidget = QtWidgets.QWidget(halaman_utama)
        self.centralwidget.setObjectName("centralwidget")

        self.frame_data_buku = QtWidgets.QFrame(self.centralwidget)
        self.frame_data_buku.setGeometry(QtCore.QRect(0, 160, 231, 261))
        self.frame_data_buku.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_data_buku.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_data_buku.setObjectName("frame_data_buku")

        self.label_urut = QtWidgets.QLabel(self.frame_data_buku)
        self.label_urut.setGeometry(QtCore.QRect(20, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_urut.setFont(font)
        self.label_urut.setObjectName("label_urut")

#--------------------------------------------------------------------------------
        
        # Tombol Urutkan
        self.tombol_urutkan = QtWidgets.QPushButton(self.frame_data_buku)
        self.tombol_urutkan.setGeometry(QtCore.QRect(20, 210, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tombol_urutkan.setFont(font)
        self.tombol_urutkan.setObjectName("tombol_urutkan")

        self.label_urut_2 = QtWidgets.QLabel(self.frame_data_buku)
        self.label_urut_2.setGeometry(QtCore.QRect(20, 50, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_urut_2.setFont(font)
        self.label_urut_2.setObjectName("label_urut_2")

#--------------------------------------------------------------------------------
        
        # Radio Button Judul Buku
        self.radioButton_judul = QtWidgets.QRadioButton(self.frame_data_buku)
        self.radioButton_judul.setGeometry(QtCore.QRect(20, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.radioButton_judul.setFont(font)
        self.radioButton_judul.setObjectName("radioButton_judul")
        self.radioButton_judul.setChecked(True)

        # Radio Button Nama Penulis
        self.radioButton_penulis = QtWidgets.QRadioButton(self.frame_data_buku)
        self.radioButton_penulis.setGeometry(QtCore.QRect(20, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.radioButton_penulis.setFont(font)
        self.radioButton_penulis.setObjectName("radioButton_penulis")

        # Radio Button Tanggal Terbit Buku
        self.radioButton_tanggal = QtWidgets.QRadioButton(self.frame_data_buku)
        self.radioButton_tanggal.setGeometry(QtCore.QRect(20, 170, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.radioButton_tanggal.setFont(font)
        self.radioButton_tanggal.setObjectName("radioButton_tanggal")

        self.frame_table = QtWidgets.QFrame(self.centralwidget)
        self.frame_table.setGeometry(QtCore.QRect(239, 9, 551, 531))
        self.frame_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_table.setObjectName("frame_table")

#--------------------------------------------------------------------------------
        
        # Table Data Buku
        self.table_data = QtWidgets.QTableWidget(self.frame_table)
        self.table_data.setGeometry(QtCore.QRect(0, 0, 551, 531))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.table_data.setFont(font)
        self.table_data.setObjectName("table_data")
        self.table_data.setColumnCount(3)
        self.table_data.setRowCount(0)

        # Data Buku Pada Table :

        # Header
        header = ['Judul Buku', 'Penulis', 'Tahun Terbit']
        self.table_data.setHorizontalHeaderLabels(header)

        for i in range(len(data_final)):
            row_kosong = self.table_data.rowCount()

            self.table_data.insertRow(row_kosong)
            self.table_data.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(data_final[i][0]))
            self.table_data.setItem(row_kosong, 1, QtWidgets.QTableWidgetItem(data_final[i][1]))
            self.table_data.setItem(row_kosong, 2, QtWidgets.QTableWidgetItem(data_final[i][2]))


#--------------------------------------------------------------------------------
        
        self.frame_cari = QtWidgets.QFrame(self.centralwidget)
        self.frame_cari.setGeometry(QtCore.QRect(-1, 9, 231, 141))
        self.frame_cari.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cari.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cari.setObjectName("frame_cari")

        self.label_cari = QtWidgets.QLabel(self.frame_cari)
        self.label_cari.setGeometry(QtCore.QRect(20, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_cari.setFont(font)
        self.label_cari.setObjectName("label_cari")

#--------------------------------------------------------------------------------

        # Textbox Pencarian
        self.textBox_cari = QtWidgets.QLineEdit(self.frame_cari)
        self.textBox_cari.setGeometry(QtCore.QRect(20, 50, 181, 31))
        self.textBox_cari.setObjectName("textBox_cari")

        # Tombol Pencarian
        self.tombol_cari = QtWidgets.QPushButton(self.frame_cari)
        self.tombol_cari.setGeometry(QtCore.QRect(20, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tombol_cari.setFont(font)
        self.tombol_cari.setObjectName("tombol_cari")

#--------------------------------------------------------------------------------

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 430, 231, 111))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        halaman_utama.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(halaman_utama)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 21))
        self.menubar.setObjectName("menubar")

        halaman_utama.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(halaman_utama)
        self.statusbar.setObjectName("statusbar")

        halaman_utama.setStatusBar(self.statusbar)

#--------------------------------------------------------------------------------
        
        self.tombol_urutkan.clicked.connect(self.action_pengurutan)
        self.tombol_cari.clicked.connect(self.action_cari)

#--------------------------------------------------------------------------------
        
        self.retranslateUi(halaman_utama)
        QtCore.QMetaObject.connectSlotsByName(halaman_utama)

#--------------------------------------------------------------------------------

    def action_pengurutan(self):

        if self.radioButton_judul.isChecked():
            pengurut_judul(data_final)
        elif self.radioButton_penulis.isChecked():
            pengurut_penulis(data_final)
        elif self.radioButton_tanggal.isChecked():
            pengurut_tanggal(data_final)

        self.table_data.setRowCount(0)
        
        for i in range(len(data_final)):
            row_kosong = self.table_data.rowCount()

            self.table_data.insertRow(row_kosong)
            self.table_data.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(data_final[i][0]))
            self.table_data.setItem(row_kosong, 1, QtWidgets.QTableWidgetItem(data_final[i][1]))
            self.table_data.setItem(row_kosong, 2, QtWidgets.QTableWidgetItem(data_final[i][2]))

#-------------------------------------------------------------------------------#

    def action_cari(self):

        target = self.textBox_cari.text()
        
        alpha = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        numb = "1234567890"
        char = "!@#$%^&*()_+-={}[];':'<>,.?/~`"
        campuran = alpha + numb
        campuran_ulti = campuran + char

        self.table_data.setRowCount(0)
        
        for i in range(len(data_final)):
            if target in data_final[i][0]:
                if data_final[i][0] == self.textBox_cari.text():
                    row_kosong = self.table_data.rowCount()

                    self.table_data.insertRow(row_kosong)
                    self.table_data.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(data_final[i][0]))
                    self.table_data.setItem(row_kosong, 1, QtWidgets.QTableWidgetItem(data_final[i][1]))
                    self.table_data.setItem(row_kosong, 2, QtWidgets.QTableWidgetItem(data_final[i][2]))
                    break
                
            elif target in data_final[i][1]:
                if data_final[i][1] == self.textBox_cari.text():
                    row_kosong = self.table_data.rowCount()

                    self.table_data.insertRow(row_kosong)
                    self.table_data.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(data_final[i][0]))
                    self.table_data.setItem(row_kosong, 1, QtWidgets.QTableWidgetItem(data_final[i][1]))
                    self.table_data.setItem(row_kosong, 2, QtWidgets.QTableWidgetItem(data_final[i][2]))
                    break
                
            elif target in data_final[i][2]:
                if data_final[i][2] == self.textBox_cari.text():
                    row_kosong = self.table_data.rowCount()

                    self.table_data.insertRow(row_kosong)
                    self.table_data.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(data_final[i][0]))
                    self.table_data.setItem(row_kosong, 1, QtWidgets.QTableWidgetItem(data_final[i][1]))
                    self.table_data.setItem(row_kosong, 2, QtWidgets.QTableWidgetItem(data_final[i][2]))
                    break

#-------------------------------------------------------------------------------#

    def retranslateUi(self, halaman_utama):

        _translate = QtCore.QCoreApplication.translate
        halaman_utama.setWindowTitle(_translate("halaman_utama", "MainWindow"))
        self.label_urut.setText(_translate("halaman_utama", "Urutkan Data Buku"))
        self.tombol_urutkan.setText(_translate("halaman_utama", "URUTKAN"))
        self.label_urut_2.setText(_translate("halaman_utama", "Berdasarkan :"))
        self.radioButton_judul.setText(_translate("halaman_utama", "Judul Buku"))
        self.radioButton_penulis.setText(_translate("halaman_utama", "Nama Penulis"))
        self.radioButton_tanggal.setText(_translate("halaman_utama", "Tahun Terbit"))
        self.label_cari.setText(_translate("halaman_utama", "Cari"))
        self.tombol_cari.setText(_translate("halaman_utama", "CARI"))

#-------------------------------------------------------------------------------#

if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)
    halaman_utama = QtWidgets.QMainWindow()
    ui = Ui_halaman_utama()
    ui.setupUi(halaman_utama)
    halaman_utama.show()
    sys.exit(app.exec_())



# Kode Cadangan Untuk Ide Tertentu :

# Menambah table kosong pada table, dan mengisinya dengan apapun

## row_kosong = self.table_data.rowCount()
        
## self.table_data.insertRow(row_kosong)
## self.table_data.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem('dada'))
