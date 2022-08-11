# System libarary
import sys
import threading
import time
# Math library
import numpy as np
# Audio library
from lib.audio.pyaudio.record import pyaudio_recorder

def main(argv):
    print(argv)
    HELP_MSG = 'No help message'

    _funcName = sys._getframe(0).f_code.co_name

    # Variables for fft
    _sample_per_frame = 8000  # number of samples per 250ms
    _range_time_domain = np.arange(_sample_per_frame)  # get number of samples using numpy library
    _sampling_frequency = _sample_per_frame/0.25  # unit time per samples
    _time_per_frame = _sample_per_frame/_sampling_frequency # time
    _range_freq_domain = _range_time_domain/_time_per_frame
    _range_freq_domain = _range_freq_domain[range(int(_sample_per_frame/2))]

    print('_sample_per_frame: ' + str(_sample_per_frame))
    print('_range_time_domain: ' + str(_range_time_domain))
    print('_sampling_frequency: ' + str(_sampling_frequency))
    print('_time_per_frame: ' + str(_time_per_frame))
    print('_range_freq_domain: ' + str(_range_freq_domain))

    _pcm_data_list = []

    _recorder = pyaudio_recorder.PyaudioRecorder(byte=2, channel=1, rate=8000, frame_per_sample=_sample_per_frame)
    _recorder.run_thread()
    while(True):
        _pcm_data_list = _recorder.get_from_queue()
        for _pcm_data in _pcm_data_list:
            _np_data = np.frombuffer(_pcm_data, dtype=np.int16)
            _peak = np.average(np.abs(_np_data))*2
            _bars = "#" * int(50*_peak/2**16)
            print('_peak: %05d, and _bars: %s'%(_peak,_bars))
            _fft_data = np.fft.fft(_np_data)
            print('_fft_data: ', end='')
            print(_fft_data)
        time.sleep(0.01)
    _recorder.stop_thread()

if __name__ == '__main__':
    main(sys.argv)
