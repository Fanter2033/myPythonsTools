"""
-- subShifter by Pietro Sami --

I wrote this program quickly because I wanted to watch Anatomy of a Fall (great film, by the way!) 
but the subtitles I found weren't synchronized with the movie.
Hope you find this script useful. "Buona visione!"

"""
import sys
s_to_mill = 1000
m_to_mill = s_to_mill*60
h_to_mill = m_to_mill*60

def rebuildTime(time):
    remTime = time
    h = remTime // (h_to_mill)
    remTime -= h*h_to_mill
    m = remTime // (m_to_mill)
    remTime -= m*m_to_mill
    s = remTime // s_to_mill
    remTime -= s*s_to_mill
    return str(h) + ":" + str(m) + ":" + str(s) + "," + str(remTime)

def changePoints(timeCode):
    t = timeCode.split(":")
    secNmill = t[2].split(",")
    totalMilliseconds = int(t[0])*h_to_mill + int(t[1])*m_to_mill + int(secNmill[0])*s_to_mill + int(secNmill[1])
    totalMilliseconds += timeShift
    if(totalMilliseconds < 0):
        exit("attention: trying to set subtitles before the start")
    return str(rebuildTime(totalMilliseconds))

def shiftTime(line):
    timeCodes = line.split(" --> ")
    timeCodes[1] = timeCodes[1].replace('\n','')
    return (changePoints(timeCodes[0]) + " --> " + changePoints(timeCodes[1])+"\n")

if __name__ == "__main__":
    timeShift = 0
    srtFile = ""
    srtFileShifted = ""
    if(len(sys.argv) == 2 and (sys.argv[1] == "--help" or sys.argv[1] == "-h")):
        exit("usage: \n python subShifter <file> <time> \n - only .srt file are supported \n - the time value must be expressed in milliseconds")
    if(len(sys.argv) != 3):
        exit("wrong arguments")
    if(not(sys.argv[1].endswith(".srt"))):
        exit("attention: only srt files are supported")
    try:
        timeShift = int(sys.argv[2])
    except:
        exit("attention: wrong time format")

    with open(sys.argv[1], "r") as srtFile:
        for line in srtFile:
            if ("-->" in line):
                srtFileShifted += shiftTime(line)
            else:
                srtFileShifted += line
        newName = sys.argv[1] + ".shifted." + str(timeShift) + ".srt"
        newFile = open(newName, "w")
        newFile.write(srtFileShifted)
        newFile.close()
