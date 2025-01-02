import os
import shutil
from util import is_in_timeline, ts_to_str, REC
from tqdm import tqdm


def scan_dir(dirPathSrc, dirPathDst, dateBegin, dateEnd, mode) -> tuple:
    """
    Scans the source directory and copies files to the destination directory based on the specified date range and mode.
    Args:
        dirPathSrc (str): The source directory path.
        dirPathDst (str): The destination directory path.
        dateBegin (datetime): The start date for the date range filter.
        dateEnd (datetime): The end date for the date range filter.
        mode (list): A list containing mode settings, including whether to process directories recursively.
    Returns:
        tuple: A tuple containing two integers:
            - counter (int): The number of files copied.
            - nDir (int): The number of new directories created.
    Notes:
        - Files are copied only if they fall within the specified date range.
        - If the recursive mode is enabled, subdirectories are processed recursively.
        - Permission errors and other exceptions during file processing are caught and logged, and the corresponding files are skipped.
    """
    abs_dest = os.path.abspath(dirPathDst)
    abs_src = os.path.abspath(dirPathSrc)
    counter = 0
    nDir = 0

    try:
        photos = list(os.scandir(dirPathSrc))
    except Exception as e:
        raise OSError(f"Error accessing directory '{dirPathSrc}': {e}")

    for p in tqdm(photos, desc="Processing files", unit=" file"):
        try:
            if p.is_file():
                if is_in_timeline(dateBegin, dateEnd, p):
                    full_dst = os.path.join(abs_dest, ts_to_str(p.stat().st_mtime))
                    if not os.path.exists(full_dst):
                        os.mkdir(full_dst)
                        nDir += 1
                    if not os.path.exists(os.path.join(full_dst, p.name)):
                        counter += 1
                        shutil.copy2(os.path.join(abs_src, p.name), full_dst)
            elif p.is_dir() and int(mode[REC]):  # Process directories only if recursive mode is enabled
                sub_counter, sub_nDir = scan_dir(p.path, os.path.join(abs_dest, p.name), dateBegin, dateEnd, mode)
                counter, nDir = tuple(x + y for x, y in zip((counter, nDir), (sub_counter, sub_nDir)))
        except PermissionError as e:
            print(f"PermissionError: {e}. Skipping '{p.name}'.")
        except Exception as e:
            print(f"Error processing '{p.name}': {e}. Skipping.")

    return counter, nDir