import os
import shutil
from util import is_in_timeline, ts_to_str, REC
from tqdm import tqdm



def scan_dir(dirPathSrc, dirPathDst, dateBegin, dateEnd, mode):

    abs_dest = os.path.abspath(dirPathDst)
    abs_src = os.path.abspath(dirPathSrc)
    counter = 0
    nDir = 0

    try:
        photos = list(os.scandir(dirPathSrc))
    except Exception as e:
        raise OSError(f"Error accessing directory '{dirPathSrc}': {e}")
    
    for p in tqdm(photos, desc="Processing files", unit=" file"):
        if p.is_file: 
            if is_in_timeline(dateBegin, dateEnd, p):
                full_dst = os.path.join(abs_dest, ts_to_str(p.stat().st_mtime))
                if not os.path.exists(full_dst):
                    os.mkdir(full_dst)
                    nDir += 1
                if not os.path.exists(os.path.join(full_dst, p.name)):
                    counter += 1
                    shutil.copy2(os.path.join(abs_src, p.name), full_dst)
        if os.path.isdir(os.path.join(abs_src, p.name)) and int(mode[REC]):
            sub_counter, sub_nDir = scan_dir(os.path.join(abs_src, p.name), os.path.join(abs_dest, p.name), dateBegin, dateEnd, mode)
            counter, nDir = tuple(x + y for x, y in zip((counter, nDir), (sub_counter, sub_nDir)))

    return counter, nDir


