# -*- coding: UTF-8 -*-
"""Contains GUI-core and all applied logic.
    Run this file to start the app."""

import sys
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QVBoxLayout,
                               QLabel,
                               QComboBox,
                               QWidget,
                               QStackedWidget)

from app.app_widgets import (Uocns,
                             Booksim,
                             Newxim,
                             Topaz,
                             Dec9)

from config.style_settings import (Q_MAIN_WINDOW_STYLE,
                                   Q_SIM_COMBO_BOX_WIDTH)


class SimulatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UHLNoCS config generator")
        self.setStyleSheet(Q_MAIN_WINDOW_STYLE)

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
        self.c_box.setFixedWidth(Q_SIM_COMBO_BOX_WIDTH)

        # instances for sim-params parts:
        self.uocns_UI = Uocns()
        self.booksim_UI = Booksim()
        self.newxim_UI = Newxim()
        self.topaz_UI = Topaz()
        self.dec9_UI = Dec9()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.uocns_UI)
        self.Stack.addWidget(self.booksim_UI)
        self.Stack.addWidget(self.newxim_UI)
        self.Stack.addWidget(self.topaz_UI)
        self.Stack.addWidget(self.dec9_UI)

        layout.addWidget(QLabel('<h2>Select sim:</h2>', self))
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
