import kaldiio 

class FileWriter:
    def __init__(
        self, wspecifier, compress=False, compression_method=2
    ):
        if compress:
            self.writer = kaldiio.WriteHelper(
                wspecifier, compression_method=compression_method
            )
        else:
            self.writer = kaldiio.WriteHelper(wspecifier)
        self.writer_scp = None

    def __setitem__(self, key, value):
        self.writer[key] = value

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        try:
            self.writer.close()
        except Exception:
            pass

        if self.writer_scp is not None:
            try:
                self.writer_scp.close()
            except Exception:
                pass

