#!/System/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python

from instapy.color2gray import grayscale_image
from instapy.color2sepia import sepia_image
from argparse import ArgumentParser

parser = ArgumentParser()

required = parser.add_mutually_exclusive_group(required=True)
parser.add_argument("-f", "--file", required=True, help="The /path to apply filter to.")
required.add_argument('-se', '--sepia', action="store_true", help="Select sepia filter.")
required.add_argument('-g', '--gray', action="store_true", help="Select gray filter.")
parser.add_argument('-sc', '--scale', type=int, default=100, help="Scale factor to resize image in percent of original size")
parser.add_argument('-i', '--implement', metavar='{python, numba, numpy}', help="Choose the implementation")
parser.add_argument('-o', '--out', type=str, help='The output filename', default=None)

args = parser.parse_args()



if __name__ == '__main__':
    if args.sepia:
        sepia_image(args.file, args.out, args.implement, args.scale)
    elif args.gray:
        grayscale_image(args.file, args.out, args.implement, args.scale)