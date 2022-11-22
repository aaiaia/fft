# System libarary
import sys
import threading
import time
# Path library
from pathlib import Path
# Math library
import numpy as np
# fft library
import librosa
import librosa.display
# plot library
import matplotlib.pyplot as plt 
# for Debugging
import getopt

def main(argv):
    print(argv)
    HELP_MSG = 'python [FILE] --help, --radix_bit=[NUMBER, 2~11], --sampling_rate=[NUMBER], --frame_per_sample=[NUMBER, reserved], --in_file=[PATH, essential], --test'

    _funcName = sys._getframe(0).f_code.co_name

    __in_file = ''

    __radix_bit = 8 
    __sampling_rate = 16000 
    __frame_per_sample = 4000  # 250ms

    try:
        # opts: getopt 옵션에 따라 파싱 ex) [('-i', 'myinstancce1')]
        # etc_args: getopt 옵션 이외에 입력된 일반 Argument
        # argv 첫번째(index:0)는 파일명, 두번째(index:1)부터 Arguments
        opts, etc_args = getopt.getopt(argv[1:], \
            "hb:r:s:i:t:", ["help", "radix_bit=", "sampling_rate=", "frame_per_sample=", "in_file=", "test"])
    except getopt.GetoptError as e: # 옵션지정이 올바르지 않은 경우
        print('exception: ' + str(e))
        print(HELP_MSG)
        sys.exit(2)

    for opt, arg in opts: # 옵션이 파싱된 경우
        if opt in ("-h", "--help"): # HELP 요청인 경우 사용법 출력
            print(HELP_MSG)
            sys.exit(2)
        elif opt in ("-b", "--radix_bit"):
            __radix_bit = int(arg)
            print('set __radix_bit: ' + str(__radix_bit))
        elif opt in ("-r", "--sampling_rate"):
            __sampling_rate = int(arg)
            print('set __sampling_rate: ' + str(__sampling_rate))
        elif opt in ("-s", "--frame_per_sample"):
            __frame_per_sample = int(arg)
            print('set __frame_per_sample: ' + str(__frame_per_sample))
        elif opt in ("-i", "--in_file"):
            __in_file = arg
            print('set __in_file: ' + __in_file)
        elif opt in ("-t", "--test"):
            __test_on = True
            print('set __test_on: ' + str(__test_on))

    if __in_file != '':
        if not Path(__in_file).exists():
            print('file not found: ' + __in_file)
            exit()
    else:
        print('needs input file!')
        exit()

    print('[configured specification]')
    print('__in_file: '             + str(__in_file             ))
    print('__radix_bit: '           + str(__radix_bit           ))
    print('__sampling_rate: '       + str(__sampling_rate       ))
    print('__frame_per_sample: '    + str(__frame_per_sample    ))

    x = librosa.load(__in_file, sr=__sampling_rate)[0]  # x, sr = librosa.load(__in_file) #sr = librosa.load(__in_file)[1] 
    y = librosa.stft(x, n_fft=2**__radix_bit, hop_length=2**(__radix_bit-1), win_length=2**(__radix_bit-1))

    magnitude = np.abs(y)
    log_spectrogram = librosa.amplitude_to_db(magnitude)

    plt.figure(figsize=(10,4))
    librosa.display.specshow(log_spectrogram, sr=__sampling_rate, hop_length=2**(__radix_bit-1))
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.colorbar(format='%+2.0f dB')
    plt.title("Spectrogram (dB)")
    plt.show()

if __name__ == '__main__':
    main(sys.argv)
