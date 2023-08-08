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
        with kaldiio.ReadHelper(self.rspecifier) as reader:
            for key, array in reader:
                yield key, array
