import argparse

from str2bool import str2bool

from compute_ssl_feats.dump_feature import dump_feature

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write_num_frames", type=str, help="Specify wspecifer for utt2num_frames"
    )
    parser.add_argument(
        "rspecifier", type=str, help="Read specifier for feats. e.g. ark:some.ark"
    )
    parser.add_argument(
        "wspecifier", type=str, help="Write specifier. e.g. ark:some.ark"
    )
    parser.add_argument(
        "--model_name", type=str, help="Hugginface model name or model path"
    )
    parser.add_argument(
        "--layer", type=int, help="Index of feature layer"
    )
    parser.add_argument("--sampling_rate", type=int, default=16_000)

    return parser

def entrypoint():
    parser = get_parser()
    args = parser.parse_args()

    dump_feature(
        args.model_name,
        rspecifier=args.rspecifier,
        wspecifier=args.wspecifier,
        layer=args.layer,
        device="cuda",
        sampling_rate=args.sampling_rate,
        # write_num_frames=args.write_num_frames,
    )

