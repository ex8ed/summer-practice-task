# -*- coding: UTF-8 -*-
"""Contains GUI-core and all applied logic. Run this file to start the app."""

import sys
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QVBoxLayout,
                               QLabel,
                               QComboBox,
                               QLineEdit,
                               QPushButton,
                               QHBoxLayout,
                               QWidget,
                               QStackedWidget)

from app_core import Extractor
from app_widgets import Uocns


class SimulatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Goose generator")

        self.setStyleSheet("""
            QMainWindow {
                background-color: #20420e;
            }
        """)

        # main widgets and layouts:
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # combobox with sim types; main chooser:
        self.c_box = QComboBox(self)
        self.c_box.addItems(['uocns',
                             'booksim',
                             'newxim',
                             'topaz',
                             'dec9',
                             'gpNocSim'])

        # instances for sim-params parts:
        self.uocns_UI = Uocns()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.uocns_UI)

        layout.addWidget(QLabel('<h3>Select sim:</h3>', self))
        layout.addWidget(self.c_box)
        layout.addWidget(self.Stack)
        self.c_box.setCurrentIndex(0)
        self.c_box.currentIndexChanged.connect(self.__index_changed)

        self.setLayout(layout)

    def __index_changed(self):
        self.Stack.setCurrentIndex(self.c_box.currentIndex())

    def __choose_directory(self):
        ...

    def __save_info_to_file(self):
        ...


    __sim_types = {0: 'uocns',
                   1: 'booksim',
                   2: 'newxim',
                   3: 'topaz',
                   4: 'dec9',
                   5: 'gpNocSim'}


def main():
    app = QApplication(sys.argv)
    win = SimulatorApp()
    win.show()
    app.exec()


if __name__ == "__main__":
    main()
