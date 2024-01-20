import os
import wave
from vosk import Model, KaldiRecognizer


class RecognizerClass:
    def __init__(self):
        self.model = Model("model")

    def create_map(self, wav):
        split1 = wav.split("/")
        name = split1[-1][:-4] + ".json"
        output = "/".join(split1[:-2]) + "/map/" + name
        if os.path.exists(output):
            print(f"Exists file '{output}'")
            return True
        print(output)
        wf = wave.open(wav, "rb")
        rec = KaldiRecognizer(self.model, wf.getframerate())
        rec.SetWords(True)
        ss = '{\n"fragments": [\n'
        while True:
            dat = wf.readframes(4000)
            if len(dat) == 0:
                break
            if rec.AcceptWaveform(dat):
                sss = rec.Result()
                ss += sss + ",\n"
                print(sss)
        ss += rec.FinalResult() + "]}"
        with open(output, mode="w", encoding="UTF-8") as ff:
            ff.write(ss)
        print(f"Create file '{output}'")
        return True
