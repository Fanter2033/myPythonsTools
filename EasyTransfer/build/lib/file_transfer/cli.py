from .easy_transfer import scan_dir
import argparse
from  . import data_preprocessing as dp
from .util import * 
import os

def main():
        parser = argparse.ArgumentParser(description="Copy files matching time span.\n"
                                                     "Legal time format: YYYY-MM-DD / YYYY-MM / YYYY / today(t).",
                                         formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument("src", metavar="src", type=str, nargs="?", help="Source path (ignored in automatic mode)")
        parser.add_argument("dst", metavar="dst", type=str, nargs="?", help="Destination path (ignored in automatic mode)")
        parser.add_argument("start", metavar="start", type=str, nargs="?", help="Starting date (ignored in automatic mode)")
        parser.add_argument("end", metavar="end", type=str, nargs="?", help="Ending date (ignored in automatic mode)")
        parser.add_argument("-r", "--recursive", help="Recursive mode", action="store_true")
        parser.add_argument("-a", "--auto", help="Automatic mode using configuration file", action="store_true")
        args = parser.parse_args()

        if args.auto:  
            config = load_config()
            src_path = config["src"]
            dst_path = config["dst"]
            date_start = dp.parse_input(config["start_date"])
            date_end = dp.parse_input(config["end_date"])
        else:  
            if not args.src or not args.dst or not args.start or not args.end:
                parser.error("In parameterized mode, src, dst, start, and end are required.")

            if not os.path.exists(args.src):
                exit("Error: Source path does not exist.")
            if not os.path.exists(args.dst):
                exit("Error: Destination path does not exist.")

            src_path = args.src
            dst_path = args.dst
            date_start = dp.parse_input(args.start)
            date_end = dp.parse_input(args.end)

        options = dp.parse_options(args)

        nFile, nDir = scan_dir(src_path, dst_path, date_start, date_end, options)
        if nFile == 0:
            print("Nothing to copy.")
        else:
            print(f"Finish!\nFiles copied: {nFile}\nDirectories created: {nDir}")

if __name__ == "__main__":
    main()