# -*- coding: UTF-8 -*-
"""Contains widgets for main GUI file"""

from random import randint
from PySide6.QtWidgets import (QLabel,
                               QComboBox,
                               QLineEdit,
                               QWidget,
                               QMessageBox,
                               QGridLayout)

from config.style_settings import (DEC_9_WIDGET_COMBO_BOX_WIDTH,
                                   DEC_9_WIDGET_LINE_EDIT_WIDTH)

from app.app_core import Simulator


def isfloat(float_num_str):
    try:
        float(float_num_str)
    except ValueError:
        return False
    else:
        return True


class Uocns(QWidget):
    def __init__(self):
        super().__init__(None)
        self.name = "uocns"
        layout = QGridLayout(self)
        row = 0

        layout.addWidget(QLabel(f'<h3> Specify parameters for {self.name}:</h3>', self),
                         row, 0, 1, 2)

        row += 1
        layout.addWidget(QLabel('Topology', self), row, 0)
        self.topology = QComboBox(self)
        self.topology.addItems(['Mesh', 'Circulant', 'Torus', 'CirculantOpt'])
        self.topology.setCurrentIndex(-1)
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

        row += 1
        layout.addWidget(QLabel('Topology args', self), row, 0)
        self.topology_args = QLineEdit(self)
        layout.addWidget(self.topology_args)

        row += 1
        layout.addWidget(QLabel('Algorithm args', self), row, 0)
        self.algorithm_args = QLineEdit(self)
        layout.addWidget(self.algorithm_args)

        row += 1
        layout.addWidget(QLabel('Algorithm', self), row, 0)
        self.algorithm = QComboBox(self)
        self.algorithm.addItems(['Dijkstra', 'PO', 'POU'])
        self.algorithm.setCurrentIndex(-1)
        layout.addWidget(self.algorithm)

        row = 1
        layout.addWidget(QLabel('Count run', self), row, 2)
        self.count_run = QLineEdit(self)
        layout.addWidget(self.count_run, row, 3)

        row += 1
        layout.addWidget(QLabel('Count packet rx', self), row, 2)
        self.count_packet_rx = QLineEdit(self)
        layout.addWidget(self.count_packet_rx, row, 3)

        row += 1
        layout.addWidget(QLabel('Packet size avg, flits', self), row, 2)
        self.packet_size_avg = QLineEdit(self)
        layout.addWidget(self.packet_size_avg, row, 3)

        row += 1
        layout.addWidget(QLabel('Packet size is fixed', self), row, 2)
        self.packet_size_is_fixed = QComboBox(self)
        self.packet_size_is_fixed.addItems(['True', 'False'])
        self.packet_size_is_fixed.setCurrentIndex(-1)
        layout.addWidget(self.packet_size_is_fixed, row, 3)

        row += 1
        layout.addWidget(QLabel('Is mode GALS', self), row, 2)
        self.is_mode_gals = QComboBox(self)
        self.is_mode_gals.addItems(['True', 'False'])
        self.is_mode_gals.setCurrentIndex(-1)
        layout.addWidget(self.is_mode_gals, row, 3)

        row += 1
        layout.addWidget(QLabel('Count packet rx warm up', self), row, 2)
        self.count_packet_rx_warm_up = QLineEdit(self)
        layout.addWidget(self.count_packet_rx_warm_up, row, 3)

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
            QMessageBox.warning(self, "Ошибка!", 'Необходимо числовое значение в поле "Count packet rx warm up"')
            return None
        elif int(count_packet_rx_warm_up) < 0 or int(count_packet_rx_warm_up) > 1000:
            QMessageBox.warning(self,
                                "Ошибка!",
                                'Поле "Count packet rx warm up" должно принимать значение от 0 до 1000')
            return None

        s.set_parameter('Topology', topology)
        s.set_parameter('TopologyArguments', list(map(int, topology_args)))
        s.set_parameter('Algorithm', algorithm)
        s.set_parameter('AlgorithmArguments', algorithm_args)
        s.set_parameter('FifoSize', int(fifo_size))
        s.set_parameter('FifoCount', int(fifo_count))
        s.set_parameter('FlitSize', int(flit_size))
        s.set_parameter('PacketSizeAvg', int(packet_size_avg))
        s.set_parameter('PacketSizeIsFixed', packet_size_is_fixed == 0)
        s.set_parameter('PacketPeriodAvg', list(range(5, 100, 10)))  # default value that could be changed in UHLNoCS
        s.set_parameter('CountRun', int(count_run))
        s.set_parameter('CountPacketRx', int(count_packet_rx))
        s.set_parameter('CountPacketRxWarmUp', int(count_packet_rx_warm_up))
        s.set_parameter('IsModeGALS', is_mode_gals == 0)

        return s


class Booksim(QWidget):
    def __init__(self):
        super().__init__()
        self.name = 'booksim'
        layout = QGridLayout(self)
        row = 0

        layout.addWidget(QLabel(f'<h3> Specify parameters for {self.name}:</h3>', self),
                         row, 0, 1, 2)

        row += 1
        layout.addWidget(QLabel('Topology', self), row, 0)
        self.topology = QComboBox(self)
        self.topology.addItems(['Mesh', 'Torus'])
        self.topology.setCurrentIndex(-1)
        layout.addWidget(self.topology, row, 1)

        row += 1
        layout.addWidget(QLabel('Virtual channels number', self), row, 0)
        self.virtual_channels_number = QLineEdit(self)
        layout.addWidget(self.virtual_channels_number)

        row += 1
        layout.addWidget(QLabel('Traffic distribution', self), row, 0)
        self.traffic_distribution = QComboBox(self)
        self.traffic_distribution.addItems(['Uniform',
                                            'BitComp',
                                            'BitRev',
                                            'Shuffle',
                                            'Transpose',
                                            'Tomado',
                                            'Neighbor'])
        self.traffic_distribution.setCurrentIndex(-1)
        layout.addWidget(self.traffic_distribution)

        row += 1
        layout.addWidget(QLabel('Sample period, cycles', self), row, 0)
        self.sample_period = QLineEdit(self)
        layout.addWidget(self.sample_period)

        row += 1
        layout.addWidget(QLabel('Topology args', self), row, 0)
        self.topology_args = QLineEdit(self)
        layout.addWidget(self.topology_args)

        row += 1
        layout.addWidget(QLabel('Virtual channel buf size, flits', self), row, 0)
        self.virtual_channel_buffer = QLineEdit(self)
        layout.addWidget(self.virtual_channel_buffer)

        row = 1
        layout.addWidget(QLabel('Packet size, bits', self), row, 2)
        self.packet_size = QLineEdit(self)
        layout.addWidget(self.packet_size, row, 3)

        row += 1
        layout.addWidget(QLabel('Warm up periods, cycles', self), row, 2)
        self.warm_up_periods = QLineEdit(self)
        layout.addWidget(self.warm_up_periods, row, 3)

        row += 1
        layout.addWidget(QLabel('Routing function', self), row, 2)
        self.routing_function = QComboBox(self)
        self.routing_function.addItems(['DimOrder',
                                        'DOR',
                                        'DOR No Express',
                                        'Min',
                                        'RanMin'])
        self.routing_function.setCurrentIndex(-1)
        layout.addWidget(self.routing_function, row, 3)

        row += 1
        layout.addWidget(QLabel('Simulation type', self), row, 2)
        self.simulation_type = QComboBox(self)
        self.simulation_type.addItems(['Latency',
                                       'Throughput'])
        self.simulation_type.setCurrentIndex(-1)
        layout.addWidget(self.simulation_type, row, 3)

        row += 1
        layout.addWidget(QLabel('Max samples, cycles', self), row, 2)
        self.max_samples = QLineEdit(self)
        layout.addWidget(self.max_samples, row, 3)

    def read_fields(self):
        s = Simulator(self.name, 1)

        topology = self.topology.currentIndex()
        virtual_channels_number = self.virtual_channels_number.text()
        traffic_distribution = self.traffic_distribution.currentIndex()
        sample_period = self.sample_period.text()
        topology_args = self.topology_args.text().split()
        virtual_channels_buffer = self.virtual_channel_buffer.text()
        packet_size = self.packet_size.text()
        warm_up_periods = self.warm_up_periods.text()
        routing_function = self.routing_function.currentIndex()
        simulation_type = self.simulation_type.currentIndex()
        max_samples = self.max_samples.text()

        if not virtual_channels_number.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Virtual channels number"')
            return None
        elif int(virtual_channels_number) < 1 or int(virtual_channels_number) > 10:
            QMessageBox.warning(self,
                                "Ошибка!",
                                'Поле "Virtual channels number" должно принимать значение от 1 до 10')
            return None

        if not sample_period.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Sample period, cycles"')
            return None
        elif int(sample_period) < 5000 or int(sample_period) > 100000:
            QMessageBox.warning(self,
                                "Ошибка!",
                                'Поле "Sample period, cycles" должно принимать значение от 5000 до 100000')
            return None

        for arg in topology_args:
            if not arg.isdigit():
                QMessageBox.warning(self,
                                    "Ошибка!",
                                    'Необходимы числовые значения в поле Topology args\
                                    \nПомните, они должны быть корректными по документации')
                return None

        if not virtual_channels_buffer.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Virtual channels buffer size"')
            return None
        elif int(virtual_channels_buffer) < 1 or int(virtual_channels_buffer) > 128:
            QMessageBox.warning(self,
                                "Ошибка!",
                                'Поле "Virtual channels buffer size" должно принимать значение от 1 до 128')
            return None

        if not packet_size.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Packet size, flits"')
            return None
        elif int(packet_size) < 1 or int(packet_size) > 100:
            QMessageBox.warning(self,
                                "Ошибка!",
                                'Поле "Packet size, flits" должно принимать значение от 1 до 100')
            return None

        if not warm_up_periods.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Warm up periods, cycles"')
            return None
        elif int(warm_up_periods) < 0 or int(warm_up_periods) > 10:
            QMessageBox.warning(self,
                                "Ошибка!",
                                'Поле "Warm up periods, cycles" должно принимать значение от 0 до 10')
            return None

        if not max_samples.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Max samples, cycles"')
            return None
        elif int(max_samples) < 1 or int(max_samples) > 10:
            QMessageBox.warning(self,
                                "Ошибка!",
                                'Поле "Max samples, cycles" должно принимать значение от 1 до 10')
            return None

        s.set_parameter('Topology', topology)
        s.set_parameter('TopologyArgs', list(map(int, topology_args)))
        s.set_parameter('RoutingFunction', routing_function)
        s.set_parameter('VirtualChannelsNum', int(virtual_channels_number))
        s.set_parameter('VirtualChannelBufSize', int(virtual_channels_buffer))
        s.set_parameter('TrafficDistribution', traffic_distribution)
        s.set_parameter('PacketSize', int(packet_size))
        s.set_parameter('SimType', simulation_type)
        # default value that could be changed in UHLNoCS
        s.set_parameter('InjectionRate', [i / 100 for i in range(5, 100, 10)])
        s.set_parameter('SamplePeriod', int(sample_period))
        s.set_parameter('WarmUpPeriods', int(warm_up_periods))
        s.set_parameter('MaxSamples', int(max_samples))

        return s


class Newxim(QWidget):
    def __init__(self):
        super().__init__()
        self.name = 'newxim'

        layout = QGridLayout(self)

        row = 0
        layout.addWidget(QLabel(f'<h3> Specify parameters for {self.name}:</h3>', self),
                         row, 0, 1, 2)

        row += 1
        layout.addWidget(QLabel('Topology', self), row, 0)
        self.topology = QComboBox(self)
        self.topology.addItems(['Mesh',
                                'Torus',
                                'Tree',
                                'Circulant'])
        self.topology.setCurrentIndex(-1)
        layout.addWidget(self.topology)

        row += 1
        layout.addWidget(QLabel('Topology channels', self), row, 0)
        self.topology_channels = QLineEdit(self)
        layout.addWidget(self.topology_channels)

        row += 1
        layout.addWidget(QLabel('Selection strategy', self), row, 0)
        self.selection_strategy = QComboBox(self)
        self.selection_strategy.addItems(['Random',
                                          'Buffer level',
                                          'Keep space',
                                          'Random keep space'])
        self.selection_strategy.setCurrentIndex(-1)
        layout.addWidget(self.selection_strategy)

        row += 1
        layout.addWidget(QLabel('Simulation time, cycles', self), row, 0)
        self.simulation_time = QLineEdit(self)
        layout.addWidget(self.simulation_time)

        row += 1
        layout.addWidget(QLabel('Topology args', self), row, 0)
        self.topology_args = QLineEdit(self)
        layout.addWidget(self.topology_args)

        row += 1
        layout.addWidget(QLabel('Virtual channels', self), row, 0)
        self.virtual_channels = QLineEdit(self)
        layout.addWidget(self.virtual_channels)

        row = 1
        layout.addWidget(QLabel('Min packet size, bits', self), row, 2)
        self.min_packet_size = QLineEdit(self)
        layout.addWidget(self.min_packet_size, row, 3)

        row += 1
        layout.addWidget(QLabel('Warm up time, cycles', self), row, 2)
        self.warm_up_time = QLineEdit(self)
        layout.addWidget(self.warm_up_time, row, 3)

        row += 1
        layout.addWidget(QLabel('Routing algorithm', self), row, 2)
        self.routing_algorithm = QComboBox(self)
        self.routing_algorithm.addItems(['Dijkstra',
                                         'Up Down',
                                         'Mesh XY',
                                         'Circulant Pair Exchange',
                                         'Greedy Promotion',
                                         'Circulant Multiplicative',
                                         'Circulant Clockwise',
                                         'Circulant Adaptive'])
        self.routing_algorithm.setCurrentIndex(-1)
        layout.addWidget(self.routing_algorithm, row, 3)

        row += 1
        layout.addWidget(QLabel('Buffer depth', self), row, 2)
        self.buffer_depth = QLineEdit(self)
        layout.addWidget(self.buffer_depth, row, 3)

        row += 1
        layout.addWidget(QLabel('Max packet size, flits', self), row, 2)
        self.max_packet_size = QLineEdit(self)
        layout.addWidget(self.max_packet_size, row, 3)

    def read_fields(self):
        s = Simulator(self.name, 2)

        topology = self.topology.currentIndex()
        topology_channels = self.topology_channels.text()
        selection_strategy = self.selection_strategy.currentIndex()
        simulation_time = self.simulation_time.text()
        topology_args = self.topology_args.text().split()
        virtual_channels = self.virtual_channels.text()
        min_packet_size = self.min_packet_size.text()
        warm_up_time = self.warm_up_time.text()
        routing_algorithm = self.routing_algorithm.currentIndex()
        buffer_depth = self.buffer_depth.text()
        max_packet_size = self.max_packet_size.text()

        if not topology_channels.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Topology channels"')
            return None
        elif int(topology_channels) != 1:
            QMessageBox.warning(self, "Ошибка!",
                                'Значение в поле "Topology channels" должно принимать значение 1')
            return None

        if not simulation_time.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Simulation time"')
            return None
        elif int(simulation_time) < 5000 or int(simulation_time) > 100000:
            QMessageBox.warning(self, "Ошибка!",
                                'Значение в поле "Simulation time" должно принимать значение от 5000 до 100000')
            return None

        for arg in topology_args:
            if not arg.isdigit():
                QMessageBox.warning(self,
                                    "Ошибка!",
                                    'Необходимы числовые значения в поле Topology args\
                                    \nПомните, они должны быть корректными по документации')
                return None

        if not virtual_channels.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Virtual channels"')
            return None
        elif int(virtual_channels) < 1 or int(virtual_channels) > 10:
            QMessageBox.warning(self, "Ошибка!",
                                'Значение в поле "Virtual channels" должно принимать значение от 1 до 10')
            return None

        if not min_packet_size.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Min packet size, flits"')
            return None
        elif int(min_packet_size) < 1 or int(min_packet_size) > 100:
            QMessageBox.warning(self, "Ошибка!",
                                'Значение в поле "Min packet size, flits" должно принимать значение от 1 до 100')
            return None

        if not warm_up_time.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Warm up time, cycles"')
            return None
        elif int(warm_up_time) < 0 or int(warm_up_time) > 10:
            QMessageBox.warning(self, "Ошибка!",
                                'Значение в поле "Warm up time, cycles" должно принимать значение от 1 до 10')
            return None

        if not buffer_depth.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Buffer depth, flits"')
            return None
        elif int(buffer_depth) < 1 or int(buffer_depth) > 128:
            QMessageBox.warning(self, "Ошибка!",
                                'Значение в поле "Buffer depth, flits" должно принимать значение от 1 до 128')
            return None

        if not max_packet_size.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Max packet size, flits"')
            return None
        elif int(max_packet_size) < 1 or int(max_packet_size) > 100:
            QMessageBox.warning(self, "Ошибка!",
                                'Значение в поле "Max packet size, flits" должно принимать значение от 1 до 100')
            return None

        s.set_parameter('Topology', topology)
        s.set_parameter('TopologyArgs', list(map(int, topology_args)))
        s.set_parameter('RoutingAlgorithm', routing_algorithm)
        s.set_parameter('SelectionStrategy', int(selection_strategy))
        s.set_parameter('TopologyChannels', int(topology_channels))
        s.set_parameter('VirtualChannels', int(virtual_channels))
        s.set_parameter('BufferDepth', int(buffer_depth))
        s.set_parameter('MinPacketSize', int(min_packet_size))
        s.set_parameter('MaxPacketSize', int(max_packet_size))
        # default value that could be changed in UHLNoCS
        s.set_parameter('PacketInjectionRate', [i / 100 for i in range(5, 100, 10)])
        s.set_parameter('SimulationTime', int(simulation_time))
        s.set_parameter('WarmUpTime', int(warm_up_time))

        return s


class Topaz(QWidget):
    def __init__(self):
        super().__init__()

        self.name = 'topaz'

        layout = QGridLayout(self)

        row = 0
        layout.addWidget(QLabel(f'<h3> Specify parameters for {self.name}:</h3>', self),
                         row, 0, 1, 2)

        row += 1
        layout.addWidget(QLabel('Router', self), row, 0)
        self.router = QComboBox(self)
        self.router.addItems(['Ligero',
                              'Ligero MCAST',
                              'Mesh CT NOC',
                              'Mesh WH NOC',
                              'Mesh DAMQ NOC',
                              'Mesh CT FAST NOC',
                              'Torus CT NOC',
                              'Torus Bless'])
        self.router.setCurrentIndex(-1)
        layout.addWidget(self.router)

        row += 1
        layout.addWidget(QLabel('Traffic pattern', self), row, 0)
        self.traffic_pattern = QComboBox(self)
        self.traffic_pattern.addItems(['Modal', 'Reactive'])
        self.traffic_pattern.setCurrentIndex(-1)
        layout.addWidget(self.traffic_pattern)

        row += 1
        layout.addWidget(QLabel('Message length, packets', self), row, 0)
        self.message_length = QLineEdit(self)
        layout.addWidget(self.message_length)

        row += 1
        layout.addWidget(QLabel('Flit size, bits', self), row, 0)
        self.flit_size = QLineEdit(self)
        layout.addWidget(self.flit_size)

        row += 1
        layout.addWidget(QLabel('Network Arguments'), row, 0)
        self.network_arguments = QLineEdit(self)
        layout.addWidget(self.network_arguments)

        row += 1
        layout.addWidget(QLabel('Traffic pattern type', self), row, 0)
        self.traffic_pattern_type = QComboBox(self)
        self.traffic_pattern_type.addItems(['Random',
                                            'Bit reversal',
                                            'Perfect shuffle',
                                            'Permutation',
                                            'Tornado',
                                            'Local'])
        self.traffic_pattern_type.setCurrentIndex(-1)
        layout.addWidget(self.traffic_pattern_type)

        row = 1
        layout.addWidget((QLabel('Packet length, flits', self)), row, 2)
        self.packet_length = QLineEdit(self)
        layout.addWidget(self.packet_length, row, 3)

        row += 1
        layout.addWidget(QLabel('Simulation cycles', self), row, 2)
        self.simulation_cycles = QLineEdit(self)
        layout.addWidget(self.simulation_cycles, row, 3)

        row += 1
        layout.addWidget(QLabel('Model name', self), row, 2)
        self.model_name = QLineEdit(self)
        layout.addWidget(self.model_name, row, 3)

    def read_fields(self):
        s = Simulator(self.name, 3)

        router = self.router.currentIndex()
        traffic_pattern = self.traffic_pattern.currentIndex()
        message_length = self.message_length.text()
        flit_size = self.flit_size.text()
        network_arguments = self.network_arguments.text().split()
        traffic_pattern_type = self.traffic_pattern_type.currentIndex()
        packet_length = self.packet_length.text()
        simulation_cycles = self.simulation_cycles.text()
        model_name = self.model_name.text()  # must be a str

        if not message_length.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Message length, packets"')
            return None
        elif int(message_length) != 1:
            QMessageBox.warning(self, "Ошибка!",
                                'Значение в поле "Message length, packets" должно принимать значение 1')
            return None

        if not flit_size.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Flit size, bits"')
            return None
        elif int(flit_size) < 1 or int(flit_size) > 256:
            QMessageBox.warning(self, "Ошибка!",
                                'Значение в поле "Flit size, bits" должно принимать значение от 1 до 256')
            return None

        for arg in network_arguments:
            if not arg.isdigit():
                QMessageBox.warning(self, "Ошибка!",
                                    'Необходимы числовые значения в поле "Network arguments"\
                                    \nПомните, они должны быть корректными по документации!')
                return None

        if not packet_length.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Packet length, flits"')
            return None
        elif int(packet_length) < 1 or int(packet_length) > 100:
            QMessageBox.warning(self, "Ошибка!",
                                'Значение в поле "Packet length, flits" должно принимать значение от 1 до 256')
            return None

        if not simulation_cycles.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Simulation cycles"')
            return None
        elif int(simulation_cycles) < 5000 or int(simulation_cycles) > 100000:
            QMessageBox.warning(self, "Ошибка!",
                                'Значение в поле "Simulation cycles" должно принимать значение от 1 до 256')
            return None

        s.set_parameter('Simulation', model_name)  # must be a str
        s.set_parameter('TopologyArgs', list(map(int, network_arguments)))
        s.set_parameter('SimulationCycles', int(simulation_cycles))
        s.set_parameter('Router', router)
        s.set_parameter('TrafficPatternId', traffic_pattern)
        s.set_parameter('TopazTrafficPatternTypes', traffic_pattern_type)
        s.set_parameter('Seed', randint(1000, 9999))
        s.set_parameter('Load', [i / 10 for i in range(1, 11)])
        s.set_parameter('MessageLength', int(message_length))
        s.set_parameter('PacketLength', int(packet_length))
        s.set_parameter('FlitSize', int(flit_size))

        return s


class Dec9(QWidget):
    def __init__(self):
        super().__init__()
        self.name = 'dec9'

        layout = QGridLayout(self)

        row = 0
        layout.addWidget(QLabel(f'<h3> Specify parameters for {self.name}:</h3>', self),
                         row, 0, 1, 2)

        row += 1
        layout.addWidget(QLabel('Topology', self), row, 0)
        self.topology = QComboBox(self)
        self.topology.addItems(['Mesh', 'Circulant'])
        self.topology.setCurrentIndex(-1)
        self.topology.setFixedWidth(DEC_9_WIDGET_COMBO_BOX_WIDTH)
        layout.addWidget(self.topology)

        row += 1
        layout.addWidget(QLabel('Cycle count', self), row, 0)
        self.cycle_count = QLineEdit(self)
        self.cycle_count.setFixedWidth(DEC_9_WIDGET_LINE_EDIT_WIDTH)
        layout.addWidget(self.cycle_count)

        row += 1
        layout.addWidget(QLabel('Topology args', self), row, 0)
        self.topology_args = QLineEdit(self)
        self.topology_args.setFixedWidth(DEC_9_WIDGET_LINE_EDIT_WIDTH)
        layout.addWidget(self.topology_args)

        row += 1
        layout.addWidget(QLabel('Message length', self), row, 0)
        self.message_length = QLineEdit(self)
        self.message_length.setFixedWidth(DEC_9_WIDGET_LINE_EDIT_WIDTH)
        layout.addWidget(self.message_length)

    def read_fields(self):
        s = Simulator(self.name, 4)

        topology = self.topology.currentIndex()
        topology_args = self.topology_args.text().split()
        cycle_count = self.cycle_count.text()
        message_length = self.message_length.text()

        for arg in topology_args:
            if not arg.isdigit():
                QMessageBox.warning(self,
                                    "Ошибка!",
                                    'Необходимы числовые значения в поле Topology args\
                                    \nПомните, они должны быть корректными по документации')
                return None

        if not cycle_count.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Cycle count"')
            return None
        elif int(cycle_count) < 500 or int(cycle_count) > 100000:
            QMessageBox.warning(self, "Ошибка!",
                                'Значение в поле "Cycle count" должно принимать значение от 500 до 100000')
            return None

        if not message_length.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Message length"')
            return None
        elif int(message_length) < 1 or int(message_length) > 100:
            QMessageBox.warning(self, "Ошибка!",
                                'Значение в поле "Message length" должно принимать значение от 1 до 100')
            return None

        s.set_parameter('Topology', topology)
        s.set_parameter('TopologyArgs', list(map(int, topology_args)))
        s.set_parameter('CycleCount', int(cycle_count))
        s.set_parameter('MessageLength', int(message_length))
        s.set_parameter('InjectionRate', [i / 100 for i in range(5, 100, 10)])

        return s


class GpNocSim(QWidget):
    def __init__(self):
        super().__init__()

        self.name = 'gpNocSim'

        layout = QGridLayout(self)

        row = 0
        layout.addWidget(QLabel(f'<h3> Specify parameters for {self.name}:</h3>', self),
                         row, 0, 1, 2)

        row += 1
        layout.addWidget(QLabel('Topology', self), row, 0)
        self.topology = QComboBox(self)
        self.topology.addItems(['Mesh',
                                'Torus',
                                'Tree',
                                'Circulant'])
        self.topology.setCurrentIndex(-1)
        layout.addWidget(self.topology)

        row += 1
        layout.addWidget(QLabel('Average message length', self), row, 0)
        self.avg_message_length = QLineEdit(self)
        layout.addWidget(self.avg_message_length)

        row += 1
        layout.addWidget(QLabel('Flit length', self), row, 0)
        self.flit_length = QLineEdit(self)
        layout.addWidget(self.flit_length)

        row += 1
        layout.addWidget(QLabel('Number of nodes', self), row, 0)
        self.number_of_nodes = QLineEdit(self)
        layout.addWidget(self.number_of_nodes)

        row += 1
        layout.addWidget(QLabel('Virtual channels number', self), row, 0)
        self.virtual_channels_num = QLineEdit(self)
        layout.addWidget(self.virtual_channels_num)

        row += 1
        layout.addWidget(QLabel('Number of flits per buf', self), row, 0)
        self.number_of_flits = QLineEdit(self)
        layout.addWidget(self.number_of_flits)

        row = 1
        layout.addWidget(QLabel('Number of cycles', self), row, 2)
        self.number_of_cycles = QLineEdit(self)
        layout.addWidget(self.number_of_cycles, row, 3)

        row += 1
        layout.addWidget(QLabel('Number of runs', self), row, 2)
        self.number_of_runs = QLineEdit(self)
        layout.addWidget(self.number_of_runs, row, 3)

        row += 1
        layout.addWidget(QLabel('Warm up cycles', self), row, 2)
        self.warm_up_cycles = QLineEdit(self)
        layout.addWidget(self.warm_up_cycles, row, 3)

        row += 1
        layout.addWidget(QLabel('Traffic type', self), row, 2)
        self.traffic_type = QComboBox(self)
        self.traffic_type.addItems(['Uniform', 'Local'])
        self.traffic_type.setCurrentIndex(-1)
        layout.addWidget(self.traffic_type, row, 3)

    def read_fields(self):
        s = Simulator(self.name, 5)

        topology = self.topology.currentIndex()
        avg_message_len = self.avg_message_length.text()
        flit_length = self.flit_length.text()
        number_of_nodes = self.number_of_nodes.text()
        virtual_channels_count = self.virtual_channels_num.text()
        number_of_flits = self.number_of_flits.text()
        number_of_cycles = self.number_of_cycles.text()
        number_of_runs = self.number_of_runs.text()
        warm_up_cycle = self.warm_up_cycles.text()
        traffic_type = self.traffic_type.currentIndex()

        if not avg_message_len.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Average message length"')
            return None
        elif int(avg_message_len) < -2147483648 or int(avg_message_len) > 2147483647:
            QMessageBox.warning(self, "Ошибка!",
                                'Значение в поле "Average message length" должно принимать значение от -2147483648 до '
                                '2147483647')
            return None

        if not flit_length.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Flit length"')
            return None
        elif int(flit_length) < -2147483648 or int(flit_length) > 2147483647:
            QMessageBox.warning(self, "Ошибка!",
                                'Значение в поле "Flit length" должно принимать значение от -2147483648 до '
                                '2147483647')
            return None

        if not number_of_nodes.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Number of nodes"')
            return None
        elif int(number_of_nodes) < -2147483648 or int(number_of_nodes) > 2147483647:
            QMessageBox.warning(self, "Ошибка!",
                                'Значение в поле "Number of nodes" должно принимать значение от -2147483648 до '
                                '2147483647')
            return None

        if not virtual_channels_count.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Virtual channels count"')
            return None
        elif int(virtual_channels_count) < -2147483648 or int(virtual_channels_count) > 2147483647:
            QMessageBox.warning(self, "Ошибка!",
                                'Значение в поле "Virtual channels count" должно принимать значение от -2147483648 до '
                                '2147483647')
            return None

        if not number_of_flits.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Number of flits"')
            return None
        elif int(number_of_flits) < -2147483648 or int(number_of_flits) > 2147483647:
            QMessageBox.warning(self, "Ошибка!",
                                'Значение в поле "Number of flits" должно принимать значение от -2147483648 до '
                                '2147483647')
            return None

        if not number_of_cycles.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Number of cycles"')
            return None
        elif int(number_of_cycles) < -2147483648 or int(number_of_cycles) > 2147483647:
            QMessageBox.warning(self, "Ошибка!",
                                'Значение в поле "Number of cycles" должно принимать значение от -2147483648 до '
                                '2147483647')
            return None

        if not number_of_runs.isdigit():
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Number of runs"')
            return None
        elif int(number_of_runs) < -2147483648 or int(number_of_runs) > 2147483647:
            QMessageBox.warning(self, "Ошибка!",
                                'Значение в поле "Number of runs" должно принимать значение от -2147483648 до '
                                '2147483647')
            return None

        if not isfloat(warm_up_cycle):
            QMessageBox.warning(self, "Ошибка!",
                                'Необходимо числовое значение в поле "Warm Up Cycle"')
            return None

        s.set_parameter('CurrentNet', topology)
        s.set_parameter('AvgInterArrival', [i * 10 for i in range(5, 15)])
        s.set_parameter('AvgMessageLength', int(avg_message_len))
        s.set_parameter('FlitLength', int(flit_length))
        s.set_parameter('NumOfIpNode', int(number_of_nodes))
        s.set_parameter('CurrentVcCount', int(virtual_channels_count))
        s.set_parameter('NumFlitPerBuffer', int(number_of_flits))
        s.set_parameter('NumCycle', int(number_of_cycles))
        s.set_parameter('NumRun', int(number_of_cycles))
        s.set_parameter('TrafficType', traffic_type)
        s.set_parameter('WarmUpCycle', float(warm_up_cycle))

        return s
