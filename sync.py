#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Syncronizaiton
# Author: Kevin
# Generated: Wed Nov 20 17:20:05 2019
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
import time
from gnuradio import qtgui


class syncronization2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Syncronizaiton")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Syncronizaiton")
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

        self.settings = Qt.QSettings("GNU Radio", "syncronization2")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 3000000
        self.fc = fc = 2.45e9

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source_0.set_center_freq(fc, 0)
        self.uhd_usrp_source_0.set_gain(30, 0)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	fc, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_freq_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "syncronization2")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.fc, self.samp_rate)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.uhd_usrp_source_0.set_center_freq(self.fc, 0)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.fc, self.samp_rate)


    ###################################
    # Timing function added by Kevin. This function allows the user specify the radio start time and resets the pps on the radio for syncronization. 
    # Code based on code from:
    # http://lists.ettus.com/pipermail/usrp-users_lists.ettus.com/attachments/20150115/66ac59c6/attachment-0002.html
    ####################################

    def timing(self):    
        
        # Get user time
        print('Type in desired start time (min only)')
        user_start_time = (int(input()),)

        # Convert local time to sturct_time format
        local_time = time.time()
        user_time = time.localtime(local_time)
        
        # Create future time in struct_time format
        t = user_time[0:4]+user_start_time+(0,)+user_time[6:9]
        
        # Convert future time to seconds
        future_time = time.mktime(t)

        # Set start time delay to time difference between future and local time
        start_time = int(future_time - local_time)
        
        # Set start time, where start_time > 2.0
        self.uhd_usrp_source_0.set_start_time(uhd.time_spec(start_time))
       
        # Set to one radio next pps, initially
        self.uhd_usrp_source_0.set_time_unknown_pps(uhd.time_spec(0.0))
        curr_hw_time = self.uhd_usrp_source_0.get_time_last_pps()
        while curr_hw_time==self.uhd_usrp_source_0.get_time_last_pps():
            pass
        # Sleep for 50ms
        time.sleep(0.05)

        # Synchronize both radios time registers
        self.uhd_usrp_source_0.set_time_next_pps(uhd.time_spec_t(0.0))
   
        # Sleep for a couple seconds to make sure all usrp time registers latched and settled
        time.sleep(2)
   
        # Check the last pps time
        for ii in range(0,5):
            last_pps0 = self.uhd_usrp_source_0.get_time_last_pps()
   
            print("last_pps0 : %6.12f"%uhd.time_spec_t.get_real_secs(last_pps0))
           
            time.sleep(1.0)
        
        # For completion varification
        print('Cute cuddly Kittens') 
        print(time.ctime())


def main(top_block_cls=syncronization2, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.timing()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
