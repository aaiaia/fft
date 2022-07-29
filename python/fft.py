# System libarary
import sys
# Math library
import numpy as np

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

if __name__ == '__main__':
    main(sys.argv)
