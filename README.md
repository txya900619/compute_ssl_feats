# compute-ssl-feats
A kaldi compute-mfcc-feats replacement with ssl model

## install
```bash
git clone git@github.com:txya900619/compute_ssl_feats.git
cd compute_ssl_feats & pip install -e .
```

## Usage
### options
  - `-h, --help`  show this help message and exit
  - `--model_name MODEL_NAME` Hugginface model name or model path
  - `--layer LAYER`   Index of the layer of the output feature, or the last layer if not specified
  - `--sampling_rate SAMPLING_RATE`

## example
output facebook/wav2vec2-xls-r-300m layer 24 features to test.ark
```bash
compute-ssl-feats --model_name="facebook/wav2vec2-xls-r-300m" --layer=24 "scp:wav.scp" "ark,scp:test.ark,test.scp"
```
