#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Dvbt Tx
# Generated: Sun Nov 22 16:30:13 2020
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import dtv
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import osmosdr
import sip
import sys
import time
from gnuradio import qtgui


class dvbt_tx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Dvbt Tx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Dvbt Tx")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "dvbt_tx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.vga2_gain = vga2_gain = 10
        self.vga1_gain = vga1_gain = -8
        self.tx_gain = tx_gain = 50
        self.samp_rate = samp_rate = (8000000.0 * 8) / 7
        self.center_freq = center_freq = 429e6

        ##################################################
        # Blocks
        ##################################################
        self._vga2_gain_range = Range(0, 25, 1, 10, 200)
        self._vga2_gain_win = RangeWidget(self._vga2_gain_range, self.set_vga2_gain, "vga2_gain", "counter_slider", int)
        self.top_layout.addWidget(self._vga2_gain_win)
        self._vga1_gain_range = Range(-35, -4, 1, -8, 200)
        self._vga1_gain_win = RangeWidget(self._vga1_gain_range, self.set_vga1_gain, "vga1_gain", "counter_slider", int)
        self.top_layout.addWidget(self._vga1_gain_win)
        self._tx_gain_range = Range(0, 89, 1, 50, 200)
        self._tx_gain_win = RangeWidget(self._tx_gain_range, self.set_tx_gain, "tx_gain", "counter_slider", float)
        self.top_layout.addWidget(self._tx_gain_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + 'hackrf=0,buffers=128,buflen=32768' )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(center_freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(vga2_gain, 0)
        self.osmosdr_sink_0.set_if_gain(0, 0)
        self.osmosdr_sink_0.set_bb_gain(vga1_gain, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(8750000, 0)

        self.fft_vxx_0 = fft.fft_vcc(8192, False, (window.rectangular(8192)), True, 1)
        self.dtv_dvbt_symbol_inner_interleaver_0 = dtv.dvbt_symbol_inner_interleaver(6048, dtv.T8k, 1)
        self.dtv_dvbt_reference_signals_0 = dtv.dvbt_reference_signals(gr.sizeof_gr_complex, 6048, 8192, dtv.MOD_64QAM, dtv.NH, dtv.C2_3, dtv.C2_3, dtv.GI_1_32, dtv.T8k, 1, 0)
        self.dtv_dvbt_reed_solomon_enc_0 = dtv.dvbt_reed_solomon_enc(2, 8, 0x11d, 255, 239, 8, 51, 8)
        self.dtv_dvbt_map_0 = dtv.dvbt_map(6048, dtv.MOD_64QAM, dtv.NH, dtv.T8k, 1)
        self.dtv_dvbt_inner_coder_0 = dtv.dvbt_inner_coder(1, 6048, dtv.MOD_64QAM, dtv.NH, dtv.C2_3)
        self.dtv_dvbt_energy_dispersal_0 = dtv.dvbt_energy_dispersal(1)
        self.dtv_dvbt_convolutional_interleaver_0 = dtv.dvbt_convolutional_interleaver(136, 12, 17)
        self.dtv_dvbt_bit_inner_interleaver_0 = dtv.dvbt_bit_inner_interleaver(6048, dtv.MOD_64QAM, dtv.NH, dtv.T8k)
        self.digital_ofdm_cyclic_prefixer_0 = digital.ofdm_cyclic_prefixer(8192, 8192+256, 0, '')
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 8192)
        self.blocks_multiply_const_xx_0 = blocks.multiply_const_cc(0.0022097087)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, 'C:\\Users\\hamin\\Desktop\\Fall2020\\CSE310\\CSE310_FinalProject\\dmb\\honne2.ts', True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.dtv_dvbt_energy_dispersal_0, 0))
        self.connect((self.blocks_multiply_const_xx_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_ofdm_cyclic_prefixer_0, 0), (self.blocks_multiply_const_xx_0, 0))
        self.connect((self.dtv_dvbt_bit_inner_interleaver_0, 0), (self.dtv_dvbt_symbol_inner_interleaver_0, 0))
        self.connect((self.dtv_dvbt_convolutional_interleaver_0, 0), (self.dtv_dvbt_inner_coder_0, 0))
        self.connect((self.dtv_dvbt_energy_dispersal_0, 0), (self.dtv_dvbt_reed_solomon_enc_0, 0))
        self.connect((self.dtv_dvbt_inner_coder_0, 0), (self.dtv_dvbt_bit_inner_interleaver_0, 0))
        self.connect((self.dtv_dvbt_map_0, 0), (self.dtv_dvbt_reference_signals_0, 0))
        self.connect((self.dtv_dvbt_reed_solomon_enc_0, 0), (self.dtv_dvbt_convolutional_interleaver_0, 0))
        self.connect((self.dtv_dvbt_reference_signals_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.dtv_dvbt_reference_signals_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.dtv_dvbt_symbol_inner_interleaver_0, 0), (self.dtv_dvbt_map_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.digital_ofdm_cyclic_prefixer_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "dvbt_tx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_vga2_gain(self):
        return self.vga2_gain

    def set_vga2_gain(self, vga2_gain):
        self.vga2_gain = vga2_gain
        self.osmosdr_sink_0.set_gain(self.vga2_gain, 0)

    def get_vga1_gain(self):
        return self.vga1_gain

    def set_vga1_gain(self, vga1_gain):
        self.vga1_gain = vga1_gain
        self.osmosdr_sink_0.set_bb_gain(self.vga1_gain, 0)

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.osmosdr_sink_0.set_center_freq(self.center_freq, 0)


def main(top_block_cls=dvbt_tx, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
