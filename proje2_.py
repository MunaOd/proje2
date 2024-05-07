import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox, QLineEdit, QTableWidget, QTableWidgetItem, QCalendarWidget, QStackedWidget, QHeaderView, QMessageBox

class Doktor:
    def __init__(self, isim, uzmanlik_alani):
        self.isim = isim
        self.uzmanlik_alani = uzmanlik_alani
        self.randevular = []

    def randevu_ayarla(self, randevu):
        self.randevular.append(randevu)

    def randevu_iptal(self, randevu):
        self.randevular.remove(randevu)

class Hasta:
    def __init__(self, adi, soyadi, dogum_tarihi, telefon_numarasi, sigorta_numarasi):
        self.adi = adi
        self.soyadi = soyadi
        self.dogum_tarihi = dogum_tarihi
        self.telefon_numarasi = telefon_numarasi
        self.sigorta_numarasi = sigorta_numarasi
        self.randevu_gecmisi = []

    def randevu_ekle(self, randevu):
        self.randevu_gecmisi.append(randevu)

class Randevu:
    def __init__(self, tarih, doktor, hasta):
        self.tarih = tarih
        self.doktor = doktor
        self.hasta = hasta

class RandevuSistemi(QWidget):
    def __init__(self):
        super().__init__()
        self.doktorlar = [Doktor("Ahmet Yılmaz", "Kardiyoloji"), Doktor("Elif Kaya", "Nöroloji"), Doktor("Mehmet Ali", "Dahiliye")]
        self.randevular = []
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        # Hasta bilgileri
        self.adiLabel = QLabel("Adı:")
        self.layout.addWidget(self.adiLabel)

        self.adiLineEdit = QLineEdit()
        self.layout.addWidget(self.adiLineEdit)

        self.soyadiLabel = QLabel("Soyadı:")
        self.layout.addWidget(self.soyadiLabel)

        self.soyadiLineEdit = QLineEdit()
        self.layout.addWidget(self.soyadiLineEdit)

        self.dogumTarihiLabel = QLabel("Doğum Tarihi (GG/AA/YYYY):")
        self.layout.addWidget(self.dogumTarihiLabel)

        self.dogumTarihiLineEdit = QLineEdit()
        self.layout.addWidget(self.dogumTarihiLineEdit)
        
        self.telefonNumarasiLabel = QLabel("Telefon Numarası:")
        self.layout.addWidget(self.telefonNumarasiLabel)

        self.telefonNumarasiLineEdit = QLineEdit()
        self.layout.addWidget(self.telefonNumarasiLineEdit)

        self.sigortaNumarasiLabel = QLabel("Sigorta Numarası:")
        self.layout.addWidget(self.sigortaNumarasiLabel)

        self.sigortaNumarasiLineEdit = QLineEdit()
        self.layout.addWidget(self.sigortaNumarasiLineEdit)

        # Doktor seçimi
        self.doktorSecimLabel = QLabel("Doktor Seçiniz:")
        self.layout.addWidget(self.doktorSecimLabel)

        self.doktorSecimComboBox = QComboBox()
        for doktor in self.doktorlar:
            self.doktorSecimComboBox.addItem(doktor.isim + " - " + doktor.uzmanlik_alani)
        self.layout.addWidget(self.doktorSecimComboBox)

        # Takvim widget'ı
        self.takvimLabel = QLabel("Randevu Tarihi:")
        self.layout.addWidget(self.takvimLabel)

        self.takvimWidget = QCalendarWidget()
        self.layout.addWidget(self.takvimWidget)

        # Randevu butonları
        self.randevuAlButton = QPushButton("Randevu Al")
        self.randevuAlButton.clicked.connect(self.randevuAl)
        self.layout.addWidget(self.randevuAlButton)

        self.randevuIptalButton = QPushButton("Randevu İptal")
        self.randevuIptalButton.clicked.connect(self.randevuIptal)
        self.layout.addWidget(self.randevuIptalButton)

        # Stacked widget for tables
        self.stackedWidget = QStackedWidget()
        self.layout.addWidget(self.stackedWidget)

        # Hasta Randevuları Table
        self.hastaRandevuTable = QTableWidget()
        self.hastaRandevuTable.setColumnCount(3)
        self.hastaRandevuTable.setHorizontalHeaderLabels(["Hasta Adı", "Doktor", "Randevu Tarihi"])

        # Başlık stilini güncelle
        header = self.hastaRandevuTable.horizontalHeader()
        header.setStyleSheet("QHeaderView::section { background-color: #3498db; color: white; border: 1px solid gray; }")

        # Satırlar arası boşlukları azalt
        self.hastaRandevuTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # Satır renklerini sırayla değiştir
        self.hastaRandevuTable.setStyleSheet("alternate-background-color: #f0f0f0; background-color: #ffffff;")

        self.stackedWidget.addWidget(self.hastaRandevuTable)

        # Randevu Ekleme Formu
        self.randevuEklemeFormu = QWidget()
        self.randevuEklemeLayout = QVBoxLayout()
        self.randevuEklemeFormu.setLayout(self.randevuEklemeLayout)

        self.randevuEklemeLayout.addWidget(QLabel("Yeni Randevu Ekleme Formu"))
        # Burada yeni randevu eklemek için gerekli alanları oluşturabilirsiniz.

        self.stackedWidget.addWidget(self.randevuEklemeFormu)

        self.setLayout(self.layout)
        self.setWindowTitle('Randevu Sistemi')
        self.show()

    def randevuAl(self):
        # Yeni randevu ekranını göster
        self.stackedWidget.setCurrentIndex(1)

    def randevuIptal(self):
        # Seçili randevunun indeksini al
        selected_row = self.hastaRandevuTable.currentRow()
        
        if selected_row >= 0:
            # Hasta bilgilerini al
            hasta_adi_soyadi = self.hastaRandevuTable.item(selected_row, 0).text()
            doktor_adi = self.hastaRandevuTable.item(selected_row, 1).text()
            randevu_tarihi = self.hastaRandevuTable.item(selected_row, 2).text()
            
            # Hasta ve doktor nesnelerini bul
            hasta_adi, hasta_soyadi = hasta_adi_soyadi.split()
            for doktor in self.doktorlar:
                if doktor.isim == doktor_adi:
                    for randevu in doktor.randevular:
                        if randevu.hasta.adi == hasta_adi and randevu.hasta.soyadi == hasta_soyadi and randevu.tarih == randevu_tarihi:
                            # Randevuyu hem hasta nesnesinden hem de doktor nesnesinden kaldır
                            doktor.randevu_iptal(randevu)
                            randevu.hasta.randevu_gecmisi.remove(randevu)
                            break
                    
            # Seçili randevuyu tablodan kaldır
            self.hastaRandevuTable.removeRow(selected_row)

    def updateDoktorTables(self):
        self.doktorRandevuTable.setRowCount(len(self.doktorlar))
        self.table_widget.setRowCount(len(self.doktorlar))
        for idx, doktor in enumerate(self.doktorlar):
            self.doktorRandevuTable.setItem(idx, 0, QTableWidgetItem(doktor.isim))
            self.doktorRandevuTable.setItem(idx, 1, QTableWidgetItem(str(len(doktor.randevular))))
            total_appointments = sum(len(d.randevular) for d in self.doktorlar)
            self.table_widget.setItem(idx, 0, QTableWidgetItem(doktor.isim))
            self.table_widget.setItem(idx, 1, QTableWidgetItem(str(total_appointments)))
        
        # StackedWidget'ı güncelle
        self.stackedWidget.setCurrentIndex(0)  # İlk indeksteki widget'ı göster
        
        # Altta bulunan tabloyu tıkladığınızda görünecek şekilde ayarla
        self.hastaRandevuTable.doubleClicked.connect(self.showPatientDetails)

    def showPatientDetails(self, index):
        # Seçili satırın verilerini al
        selected_row = index.row()
        hasta_adi_soyadi = self.hastaRandevuTable.item(selected_row, 0).text()
        doktor_adi = self.hastaRandevuTable.item(selected_row, 1).text()
        randevu_tarihi = self.hastaRandevuTable.item(selected_row, 2).text()

        # Hasta adı ve soyadını ayrı ayrı al
        hasta_adi, hasta_soyadi = hasta_adi_soyadi.split()

        # Hasta ve doktor nesnelerini bul
        for doktor in self.doktorlar:
            if doktor.isim == doktor_adi:
                for randevu in doktor.randevular:
                    if randevu.hasta.adi == hasta_adi and randevu.hasta.soyadi == hasta_soyadi and randevu.tarih == randevu_tarihi:
                        # Hasta detaylarını ekranda göster
                        message = f"Hasta Adı: {hasta_adi}\nSoyadı: {hasta_soyadi}\nDoğum Tarihi: {randevu.hasta.dogum_tarihi}\nTelefon Numarası: {randevu.hasta.telefon_numarasi}\nSigorta Numarası: {randevu.hasta.sigorta_numarasi}\nDoktor: {doktor.isim}\nRandevu Tarihi: {randevu.tarih}"
                        QMessageBox.information(self, "Hasta Detayları", message)
                        break

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandevuSistemi()
    sys.exit(app.exec_())



