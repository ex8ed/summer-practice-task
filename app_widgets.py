# -*- coding: UTF-8 -*-
"""Contains widgets for main GUI file"""


from PySide6.QtWidgets import (QLabel,
                               QComboBox,
                               QLineEdit,
                               QWidget,
                               QMessageBox,
                               QGridLayout)

from app_core import Simulator


class Uocns(QWidget):
    def __init__(self):
        super().__init__(None)
        self.name = "uocns"
        layout = QGridLayout(self)
        row = 0

        layout.addWidget(QLabel(f'<h2> Specify parameters for {self.name}:</h2>', self),
                         row, 0, 1, 2)

        row += 1
        layout.addWidget(QLabel('Topology:', self), row, 0)
        self.topology = QComboBox(self)
        self.topology.addItems(['Mesh', 'Circulant', 'Torus', 'CirculantOpt'])
        layout.addWidget(self.topology)

        row += 1
        layout.addWidget(QLabel('FIFO size, flits', self), row, 0)
        self.fifo_size = QLineEdit(self)
        layout.addWidget(self.fifo_size, row, 1)

        row += 1
        layout.addWidget(QLabel('FIFO count', self), row, 0)
        self.fifo_count = QLineEdit(self)
        layout.addWidget(self.fifo_count)

        row += 1
        layout.addWidget(QLabel('Flit size, bits', self), row, 0)
        self.flit_size = QLineEdit(self)
        layout.addWidget(self.flit_size)

        # TODO needs an extra check for every field
        row += 1
        layout.addWidget(QLabel('Topology args', self), row, 0)
        self.topology_args = QLineEdit(self)
        layout.addWidget(self.topology_args)

        # TODO need to be checked with docs for args format
        row += 1
        layout.addWidget(QLabel('Algorithm args', self), row, 0)
        self.algorithm_args = QLineEdit(self)
        layout.addWidget(self.algorithm_args)

        row += 1
        layout.addWidget(QLabel('Algorithm', self), row, 0)
        self.algorithm = QComboBox(self)
        self.algorithm.addItems(['Dijkstra', 'PO', 'POU'])
        layout.addWidget(self.algorithm)

        row += 1
        layout.addWidget(QLabel('Count run', self), row, 0)
        self.count_run = QLineEdit(self)
        layout.addWidget(self.count_run)

        row += 1
        layout.addWidget(QLabel('Count packet rx', self), row, 0)
        self.count_packet_rx = QLineEdit(self)
        layout.addWidget(self.count_packet_rx)

        row += 1
        layout.addWidget(QLabel('Packet size avg, flits', self), row, 0)
        self.packet_size_avg = QLineEdit(self)
        layout.addWidget(self.packet_size_avg)

        # TODO must be a bool
        row += 1
        layout.addWidget(QLabel('Packet size is fixed', self), row, 0)
        self.packet_size_is_fixed = QComboBox(self)
        self.packet_size_is_fixed.addItems(['True', 'False'])
        layout.addWidget(self.packet_size_is_fixed)

        row += 1
        layout.addWidget(QLabel('Is mode GALS', self), row, 0)
        self.is_mode_gals = QComboBox(self)
        self.is_mode_gals.addItems(['True', 'False'])
        layout.addWidget(self.is_mode_gals)

        row += 1
        layout.addWidget(QLabel('Count packet rx warm up', self), row, 0)
        self.count_packet_rx_warm_up = QLineEdit(self)
        layout.addWidget(self.count_packet_rx_warm_up)

    def read_fields(self):
        s = Simulator(self.name, 0)

        topology = self.topology.currentIndex()
        fifo_size = self.fifo_size.text()
        fifo_count = self.fifo_count.text()
        flit_size = self.flit_size.text()
        topology_args = self.topology_args.text().split()
        algorithm_args = self.algorithm_args.text().split()
        algorithm = self.algorithm.currentIndex()
        count_run = self.count_run.text()
        count_packet_rx = self.count_packet_rx.text()
        packet_size_avg = self.packet_size_avg.text()
        packet_size_is_fixed = self.packet_size_is_fixed.currentIndex()
        is_mode_gals = self.is_mode_gals.currentIndex()
        count_packet_rx_warm_up = self.count_packet_rx_warm_up.text()

        if not fifo_size.isdigit():
            QMessageBox.warning(self, "Ошибка!", 'Необходимо числовое значение в поле "FIFO size"')
            return None
        elif int(fifo_size) < 1 or int(fifo_size) > 128:
            QMessageBox.warning(self,
                                "Ошибка!",
                                'Поле "FIFO size" должно принимать значение от 1 до 128')
            return None

        if not fifo_count.isdigit():
            QMessageBox.warning(self, "Ошибка!", 'Необходимо числовое значение в поле "FIFO count"')
            return None
        elif int(fifo_count) < 1 or int(fifo_count) > 10:
            QMessageBox.warning(self,
                                "Ошибка!",
                                'Поле "FIFO count" должно принимать значение от 1 до 10')
            return None

        if not flit_size.isdigit():
            QMessageBox.warning(self, "Ошибка!", 'Необходимо числовое значение в поле "Flit size"')
            return None
        elif int(flit_size) < 1 or int(flit_size) > 128:
            QMessageBox.warning(self,
                                "Ошибка!",
                                'Поле "Flit size" должно принимать значение от 1 до 128')
            return None

        for arg in topology_args:
            if not arg.isdigit():
                QMessageBox.warning(self,
                                    "Ошибка!",
                                    'Необходимы числовые значения в поле Topology args!\
                                    \nПомните, они должны быть корректными по документации')
                return None

        if not count_run.isdigit():
            QMessageBox.warning(self, "Ошибка!", 'Необходимо числовое значение в поле "Count run"')
            return None
        elif int(count_run) != 1:
            QMessageBox.warning(self, "Ошибка!", 'Значение в поле "Count run" должно принимать значение 1')
            return None

        if not count_packet_rx.isdigit():
            QMessageBox.warning(self, "Ошибка!", 'Необходимо числовое значение в поле "Count packet rx"')
            return None
        elif int(count_packet_rx) < 100 or int(count_packet_rx) > 10000:
            QMessageBox.warning(self,
                                "Ошибка!",
                                'Поле "Count packet rx" должно принимать значение от 100 до 10000')
            return None

        if not packet_size_avg.isdigit():
            QMessageBox.warning(self, "Ошибка!", 'Необходимо числовое значение в поле "Packet size avg"')
            return None
        elif int(packet_size_avg) < 1 or int(packet_size_avg) > 100:
            QMessageBox.warning(self,
                                "Ошибка!",
                                'Поле "Packet size avg" должно принимать значение от 1 до 100')
            return None

        if not count_packet_rx_warm_up.isdigit():
            QMessageBox.warning(self, "Ошибка!", 'Необходимо числовое значение в поле "Packet size avg"')
            return None
        elif int(count_packet_rx_warm_up) < 0 or int(count_packet_rx_warm_up) > 1000:
            QMessageBox.warning(self,
                                "Ошибка!",
                                'Поле "Count packet rx warm up" должно принимать значение от 0 до 1000')
            return None

        s.set_parameter('Topology', topology)
        s.set_parameter('TopologyArguments', topology_args)
        s.set_parameter('Algorithm', algorithm)
        s.set_parameter('AlgorithmArguments', algorithm_args)
        s.set_parameter('FifoSize', fifo_size)
        s.set_parameter('FlitSize', flit_size)
        s.set_parameter('PacketSizeAvg', packet_size_avg)
        s.set_parameter('PacketSizeIsFixed', packet_size_is_fixed == 0)
        s.set_parameter('PacketPeriodAvg', list(range(5, 100, 10)))  # TODO Make calculation for period avg ?
        s.set_parameter('CountRun', count_run)
        s.set_parameter('CountPacketRx', count_packet_rx)
        s.set_parameter('CountPacketRxWarmUp', count_packet_rx_warm_up)
        s.set_parameter('IsModeGALS', is_mode_gals)

        return s


class Booksim(QWidget):
    def __init__(self):
        super().__init__()

    def read_fields(self):
        ...


class Newxim(QWidget):
    def __init__(self):
        super().__init__()

    def read_fields(self):
        ...


class Topaz(QWidget):
    def __init__(self):
        super().__init__()

    def read_fields(self):
        ...


class Dec9(QWidget):
    def __init__(self):
        super().__init__()

    def read_fields(self):
        ...


class GpNocSim(QWidget):
    def __init__(self):
        super().__init__()

    def read_fields(self):
        ...
