import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox, QFileDialog, QLineEdit
from PyQt5 import QtCore, QtGui
import zipfile

class StrongholdCrusaderEditorUnlocker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stronghold Crusader 2 Map Unlocker")
        self.setGeometry(100, 100, 300, 150)  # Modifica le dimensioni della finestra

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.info_label = QLabel("Questo programma sblocca le mappe originali di Stronghold Crusader 2 in modo che possano essere modificate dal map editor")
        self.info_label.setStyleSheet("font-size: 10px; border: 1px solid gray;")
        self.info_label.setWordWrap(True)
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.info_label)

        self.name_label = QLabel("Nome della mappa:")
        self.layout.addWidget(self.name_label)

        self.name_input = QLineEdit()
        self.layout.addWidget(self.name_input)

        self.unlock_button = QPushButton("Sblocca Mappe")
        self.unlock_button.setFixedSize(100, 30)
        self.unlock_button.clicked.connect(self.unlock_maps)
        self.layout.addWidget(self.unlock_button)

        self.central_widget.setLayout(self.layout)

    def unlock_maps(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Seleziona il file .shmap", "", "File .shmap (*.shmap)")

        if file_name:
            save_name = self.name_input.text()  # Ottiene il testo dalla casella di testo
            if not save_name:
                QMessageBox.warning(self, "Nome del file mancante", "Inserisci un nome per la mappa.")
                return

            modified_file_name = os.path.join("./", f"{save_name}-unlocked.shmap")  # Utilizza il nome fornito dall'utente

            with zipfile.ZipFile(modified_file_name, 'w', compression=zipfile.ZIP_DEFLATED) as modified_archive:
                with zipfile.ZipFile(file_name, 'r') as original_archive:
                    for file_name in original_archive.namelist():
                        with original_archive.open(file_name) as original_file:
                            if 'editor.ed' in file_name.lower():
                                content = original_file.read().decode('latin-1')
                                modified_content = content.replace("<MapLocked>true</MapLocked>", "<MapLocked>false</MapLocked>")
                                content_name = modified_content.split("""<SceneName id="ref-4">""")[1].split("</")[0]
                                modified_content = modified_content.replace(content_name, save_name)
                                modified_archive.writestr(file_name, modified_content.encode('latin-1'))
                            else:
                                modified_archive.writestr(file_name, original_file.read())

            QMessageBox.information(self, "Operazione completata", "Sblocco riuscito! Il file modificato è stato salvato.")

def run_gui():
    app = QApplication(sys.argv)
    window = StrongholdCrusaderEditorUnlocker()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_gui()
