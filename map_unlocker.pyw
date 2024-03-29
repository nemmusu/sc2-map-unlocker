import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox, QFileDialog
from PyQt5 import QtCore
import zipfile
import re

class StrongholdCrusaderEditorUnlocker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stronghold Crusader 2 Editor Unlocker")
        self.setGeometry(100, 100, 300, 150)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.info_label = QLabel("Questo programma sblocca le mappe originali di Stronghold Crusader 2 in modo che possano essere modificate dal map editor")
        self.info_label.setStyleSheet("font-size: 10px; border: 1px solid gray;")
        self.info_label.setWordWrap(True)
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.info_label)

        self.unlock_button = QPushButton("Sblocca Mappe")
        self.unlock_button.setFixedSize(100, 30)
        self.unlock_button.clicked.connect(self.unlock_maps)
        self.layout.addWidget(self.unlock_button)

        self.central_widget.setLayout(self.layout)

    def unlock_maps(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Seleziona il file .shmap", "", "File .shmap (*.shmap)")

        if file_name:
            save_path, _ = QFileDialog.getSaveFileName(self, "Salva come", "mappa-unlocked.shmap", "File .shmap (*.shmap)")

            if save_path:
                with zipfile.ZipFile(save_path, 'w', compression=zipfile.ZIP_DEFLATED) as modified_archive:
                    with zipfile.ZipFile(file_name, 'r') as original_archive:
                        for file_name in original_archive.namelist():
                            with original_archive.open(file_name) as original_file:
                                content = original_file.read().decode('latin-1')

                                if 'editor.ed' in file_name.lower():
                                    modified_content = content.replace("<MapLocked>true</MapLocked>", "<MapLocked>false</MapLocked>")
                                elif 'briefing_text.dat' in file_name.lower():
                                    regex_pattern = r'\$[\w\s]+'
                                    modified_content = re.sub(regex_pattern, '', content)
                                else:
                                    modified_content = content

                                modified_archive.writestr(file_name, modified_content.encode('latin-1'))

                QMessageBox.information(self, "Operazione completata", "Sblocco riuscito! Il file modificato è stato salvato.")

def run_gui():
    app = QApplication(sys.argv)
    window = StrongholdCrusaderEditorUnlocker()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_gui()
