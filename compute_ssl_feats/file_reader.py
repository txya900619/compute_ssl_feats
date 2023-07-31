import soundfile
import kaldiio

class FileReader:
    def __init__(self, rspecifier):
        if ":" not in rspecifier:
            raise ValueError(
                'Give "rspecifier" such as "scp:some.scp: {}"'.format(rspecifier)
            )
        self.rspecifier = rspecifier
        self.ark_or_scp, self.filepath = rspecifier.split(":", 1)
        if not self.ark_or_scp in ["scp", "ark"]:
            raise ValueError(
                'Only supporting "scp" and "ark" for sound file: {}'.format(self.ark_or_scp)
            )

    def __iter__(self):
        if self.ark_or_scp == "scp":
            with open(self.filepath, "r", encoding="utf-8") as f:
                for line in f:
                    key, sound_file_path = line.rstrip().split(None, 1)
                    # Assume PCM16
                    array, rate = soundfile.read(sound_file_path, dtype="int16")
                    # Change Tuple[ndarray, int] -> Tuple[int, ndarray]
                    # (soundfile style -> scipy style)
                    yield key, (rate, array)
        else:
            with kaldiio.ReadHelper(self.rspecifier) as reader:
                for key, array in reader:
                    yield key, array

