from pydub import AudioSegment
import os


class AudioClass:
    def __init__(self, audio_list):
        self.audio_list = audio_list

    def create_wav(self):
        print("Converting to wav...")
        # cbn.convert(samplerate=16000, n_channels=1)
        for a in self.audio_list:
            split1 = a.split("/")
            name = split1[-1].split(".")[0] + ".wav"
            output = "/".join(split1[:-2]) + "/wav/" + name
            if os.path.exists(output):
                continue
            print(output)
            sound = AudioSegment.from_file(a, format='m4a')
            sound.export(output,
                         parameters=['-ar', '16000', '-ac', '1', '-ab', '128'],
                         format='wav')
