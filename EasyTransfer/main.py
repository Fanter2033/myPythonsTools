from easy_transfer import scan_dir
import argparse
import data_preprocessing as dp
import util
import os

def find_camera():
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="cp files matching time span. \n\
Legal time format: YYYY-MM-DD / YYYY-MM / YYYY / today(t).", \
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    
    parser.add_argument("src",  metavar="src",  type=str, help="source path")
    parser.add_argument("dst",  metavar="dst",  type=str, help="destination path")
    parser.add_argument("start",metavar="start",type=str, help="starting date")
    parser.add_argument("end",  metavar="end",  type=str, help="ending date")
    parser.add_argument("-r","--recursive", help="recursive mode", action="store_true")

    args = parser.parse_args()
    
    if not (os.path.exists(args.src) and os.path.exists(args.dst)):
        exit("Source or destination does not exists")
    
    p_date = ( dp.parse_input(args.start), dp.parse_input(args.end) ) 

    util.hi()
    nFile, nDir = scan_dir(args.src, args.dst, p_date[util.START], p_date[util.END], 
                           dp.parse_options(args))
    if nFile == 0:
        print("Nothing to copy")
    else:
         print("Finish! \n" + "File copied: " + str(nFile) + 
               "\nDirectory created: " + str(nDir))
    