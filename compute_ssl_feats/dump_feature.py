import kaldiio
import soundfile
import numpy as np
from transformers import AutoModel, AutoFeatureExtractor
import torch

from compute_ssl_feats.file_reader import FileReader
from compute_ssl_feats.file_writer import FileWriter
from compute_ssl_feats.utils import is_scipy_wav_style

def dump_feature(
    model_name, rspecifier, wspecifier, device="cuda", layer=None, sampling_rate=16_000
):
    feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    model = model.to(device)
    model.eval()

    with FileWriter(wspecifier) as writer:
        for utt, mat in FileReader(rspecifier):
            if is_scipy_wav_style(mat):
                # If data is sound file, then got as Tuple[int, ndarray]
                rate, mat = mat
                mat = mat.astype(np.float64, order="C") / 32768.0
            nsample = len(mat)

            input_values = feature_extractor(mat, return_tensors="pt", sampling_rate=sampling_rate).input_values
            input_values = input_values.to(device)

            with torch.no_grad():
                outputs = model(input_values, output_hidden_states=True)
                if layer is None: 
                    feat = outputs.last_hidden_state
                else:
                    feat = outputs.hidden_states[layer]
            writer[utt] = feat[0].cpu().numpy()
