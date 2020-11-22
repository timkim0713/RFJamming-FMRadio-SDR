#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Fmradio
# Generated: Sun Nov 22 16:29:04 2020
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

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class FMRadio(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Fmradio")
        _icon_path = "C:\Program Files\GNURadio-3.7\share\icons\hicolor\scalable/apps\gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 5e6
        self.channel_width = channel_width = 200e3
        self.channel_freq2 = channel_freq2 = 89.1e6
        self.channel_freq1 = channel_freq1 = 98.1e6
        self.center_freq = center_freq = 97.9e6
        self.audio_gain2 = audio_gain2 = 0
        self.audio_gain1 = audio_gain1 = 1

        ##################################################
        # Blocks
        ##################################################
        _channel_freq2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._channel_freq2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_channel_freq2_sizer,
        	value=self.channel_freq2,
        	callback=self.set_channel_freq2,
        	label='channel_freq2',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._channel_freq2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_channel_freq2_sizer,
        	value=self.channel_freq2,
        	callback=self.set_channel_freq2,
        	minimum=87.9e6,
        	maximum=107.9e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_channel_freq2_sizer)
        _channel_freq1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._channel_freq1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_channel_freq1_sizer,
        	value=self.channel_freq1,
        	callback=self.set_channel_freq1,
        	label='channel_freq1',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._channel_freq1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_channel_freq1_sizer,
        	value=self.channel_freq1,
        	callback=self.set_channel_freq1,
        	minimum=87.9e6,
        	maximum=107.9e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_channel_freq1_sizer)
        _audio_gain2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._audio_gain2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_audio_gain2_sizer,
        	value=self.audio_gain2,
        	callback=self.set_audio_gain2,
        	label='audio_gain2',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._audio_gain2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_audio_gain2_sizer,
        	value=self.audio_gain2,
        	callback=self.set_audio_gain2,
        	minimum=0,
        	maximum=10,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_audio_gain2_sizer)
        _audio_gain1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._audio_gain1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_audio_gain1_sizer,
        	value=self.audio_gain1,
        	callback=self.set_audio_gain1,
        	label='audio_gain1',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._audio_gain1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_audio_gain1_sizer,
        	value=self.audio_gain1,
        	callback=self.set_audio_gain1,
        	minimum=0,
        	maximum=10,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_audio_gain1_sizer)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=center_freq,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=True,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=12,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=12,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(center_freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(0, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.low_pass_filter_0_0 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((audio_gain2, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((audio_gain1, ))
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_wfm_rcv_0_0 = analog.wfm_rcv(
        	quad_rate=480e3,
        	audio_decimation=10,
        )
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=480e3,
        	audio_decimation=10,
        )
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - channel_freq2, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - channel_freq1, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_wfm_rcv_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.analog_wfm_rcv_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.analog_wfm_rcv_0_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_channel_width(self):
        return self.channel_width

    def set_channel_width(self, channel_width):
        self.channel_width = channel_width

    def get_channel_freq2(self):
        return self.channel_freq2

    def set_channel_freq2(self, channel_freq2):
        self.channel_freq2 = channel_freq2
        self._channel_freq2_slider.set_value(self.channel_freq2)
        self._channel_freq2_text_box.set_value(self.channel_freq2)
        self.analog_sig_source_x_0_0.set_frequency(self.center_freq - self.channel_freq2)

    def get_channel_freq1(self):
        return self.channel_freq1

    def set_channel_freq1(self, channel_freq1):
        self.channel_freq1 = channel_freq1
        self._channel_freq1_slider.set_value(self.channel_freq1)
        self._channel_freq1_text_box.set_value(self.channel_freq1)
        self.analog_sig_source_x_0.set_frequency(self.center_freq - self.channel_freq1)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.wxgui_fftsink2_0.set_baseband_freq(self.center_freq)
        self.osmosdr_source_0.set_center_freq(self.center_freq, 0)
        self.analog_sig_source_x_0_0.set_frequency(self.center_freq - self.channel_freq2)
        self.analog_sig_source_x_0.set_frequency(self.center_freq - self.channel_freq1)

    def get_audio_gain2(self):
        return self.audio_gain2

    def set_audio_gain2(self, audio_gain2):
        self.audio_gain2 = audio_gain2
        self._audio_gain2_slider.set_value(self.audio_gain2)
        self._audio_gain2_text_box.set_value(self.audio_gain2)
        self.blocks_multiply_const_vxx_0_0.set_k((self.audio_gain2, ))

    def get_audio_gain1(self):
        return self.audio_gain1

    def set_audio_gain1(self, audio_gain1):
        self.audio_gain1 = audio_gain1
        self._audio_gain1_slider.set_value(self.audio_gain1)
        self._audio_gain1_text_box.set_value(self.audio_gain1)
        self.blocks_multiply_const_vxx_0.set_k((self.audio_gain1, ))


def main(top_block_cls=FMRadio, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
