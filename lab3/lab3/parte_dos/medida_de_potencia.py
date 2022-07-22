# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: medida_de_potencia
# Author: Camilo y Pedreros
# GNU Radio version: 3.10.1.1

from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio import Modulos_D1A
from gnuradio import blocks
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal







class medida_de_potencia(gr.hier_block2, Qt.QWidget):
    def __init__(self, l_vect=1024):
        gr.hier_block2.__init__(
            self, "medida_de_potencia",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(0, 0, 0),
        )

        Qt.QWidget.__init__(self)
        self.top_layout = Qt.QVBoxLayout()
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)
        self.setLayout(self.top_layout)

        ##################################################
        # Parameters
        ##################################################
        self.l_vect = l_vect

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.potencia_Lineal_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.potencia_Lineal_1.set_update_time(0.10)
        self.potencia_Lineal_1.set_title('potencia Logarítmica [dBm]')

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.potencia_Lineal_1.set_min(i, -1)
            self.potencia_Lineal_1.set_max(i, 1)
            self.potencia_Lineal_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.potencia_Lineal_1.set_label(i, "Data {0}".format(i))
            else:
                self.potencia_Lineal_1.set_label(i, labels[i])
            self.potencia_Lineal_1.set_unit(i, units[i])
            self.potencia_Lineal_1.set_factor(i, factor[i])

        self.potencia_Lineal_1.enable_autoscale(True)
        self._potencia_Lineal_1_win = sip.wrapinstance(self.potencia_Lineal_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._potencia_Lineal_1_win)
        self.potencia_Lineal_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.potencia_Lineal_0.set_update_time(0.10)
        self.potencia_Lineal_0.set_title('potencia Logarítmica [dBW]')

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.potencia_Lineal_0.set_min(i, -1)
            self.potencia_Lineal_0.set_max(i, 1)
            self.potencia_Lineal_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.potencia_Lineal_0.set_label(i, "Data {0}".format(i))
            else:
                self.potencia_Lineal_0.set_label(i, labels[i])
            self.potencia_Lineal_0.set_unit(i, units[i])
            self.potencia_Lineal_0.set_factor(i, factor[i])

        self.potencia_Lineal_0.enable_autoscale(True)
        self._potencia_Lineal_0_win = sip.wrapinstance(self.potencia_Lineal_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._potencia_Lineal_0_win)
        self.potencia_Lineal = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.potencia_Lineal.set_update_time(0.10)
        self.potencia_Lineal.set_title('potencia_Lineal_[W]')

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.potencia_Lineal.set_min(i, -1)
            self.potencia_Lineal.set_max(i, 1)
            self.potencia_Lineal.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.potencia_Lineal.set_label(i, "Data {0}".format(i))
            else:
                self.potencia_Lineal.set_label(i, labels[i])
            self.potencia_Lineal.set_unit(i, units[i])
            self.potencia_Lineal.set_factor(i, factor[i])

        self.potencia_Lineal.enable_autoscale(True)
        self._potencia_Lineal_win = sip.wrapinstance(self.potencia_Lineal.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._potencia_Lineal_win)
        self.fft_vxx_0 = fft.fft_vfc(l_vect, True, window.blackmanharris(1024), True, 1)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, l_vect)
        self.blocks_nlog10_ff_1 = blocks.nlog10_ff(1, 1, 0)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(1, 1, 30)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(3.70053e-6)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(l_vect)
        self.Modulos_D1A_suma_componentes_camilo_pedreros_0 = Modulos_D1A.suma_componentes_camilo_pedreros(l_vect)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.Modulos_D1A_suma_componentes_camilo_pedreros_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.Modulos_D1A_suma_componentes_camilo_pedreros_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_nlog10_ff_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.potencia_Lineal, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.potencia_Lineal_1, 0))
        self.connect((self.blocks_nlog10_ff_1, 0), (self.potencia_Lineal_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self, 0), (self.blocks_stream_to_vector_0, 0))


    def get_l_vect(self):
        return self.l_vect

    def set_l_vect(self, l_vect):
        self.l_vect = l_vect

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

