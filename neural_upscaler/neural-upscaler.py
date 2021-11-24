from pathlib import Path
from argparse import ArgumentParser
import upscaler

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-f", "--file",
        dest="input_path", 
        help="Path to the image file", 
        metavar="FILE",
        type=Path
    )

    parser.add_argument(
        "-o", "--output",
        dest="output_path", 
        help="Path to the output file", 
        metavar="FILE",
        type=Path,
        default=None
    )
    args = parser.parse_args()
    upscaler.run(args.input_path, args.output_path)