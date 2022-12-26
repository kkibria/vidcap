import os
import argparse
import time
import pickle

# CAPTION_TEXT_FILE = r'C:\Users\Khan\Documents\python\youtube-api\caption.txt'

def fn_spilt(fn):
    dirname = os.path.dirname(fn)
    fname = os.path.basename(fn)
    file, ext = os.path.splitext(fname)
    return dirname, file, ext

def parse_time(t):
    s = t.split(':')
    return int(s[0])*60+float(s[1])

def capture(fn):
    start_time = None
    end_time = None
    tsorigin = None

    with open(fn, encoding="utf-8-sig") as f:
        lines = f.readlines()

    # for line in lines:
    #     print(line.strip())
    # exit()

    newcontent = []
    for line in lines:
        if not line.strip():
            continue  
        if not start_time:
            x = line.split()
            start_time = parse_time(x[0])
            end_time = parse_time(x[1])
            continue

        parts = line.split('|')
        if len(parts) < 2:
            parts.append(parts[0])
            parts[0] = parts[0][0:15] 

        print(parts[0])
        input(">")
        ts = time.time()
        if not tsorigin:
            tsorigin = ts
        timestamp = start_time + ts - tsorigin
        newcontent.append([timestamp, parts[1].strip()])

    newcontent.append([end_time, "end_time"])
    return newcontent


def save_pickle(fn, newcontent):
    with open(fn, 'wb') as f:
        print('Saving timestamps...')
        pickle.dump(newcontent, f)

def load_pickle(fn):
    newcontent = None
    with open(fn, 'rb') as f:
        newcontent = pickle.load(f)
    return newcontent


def tsformat(sec):
    m = int(sec/60)
    s = sec%60
    fs = '{:06.3f}'.format(s).replace('.', ',')
    return '00:{:02d}:{}'.format(m, fs)

def render(comp, newcontent, lrcfn, srtfn):
    with open(lrcfn, "w", encoding="utf-8") as f:
        for i in range(len(newcontent)-1):
            t = newcontent[i][0]+comp
            m = int(t/60)
            s = t%60
            print('[{:02d}:{:05.2f}]{}'.format(m, s, newcontent[i][1]), file=f)

    with open(srtfn, "w", encoding="utf-8") as f:
        for i in range(len(newcontent)-1):
            bgn = tsformat(newcontent[i][0]+comp)
            end = tsformat(newcontent[i+1][0]+comp)

            print(i+1, file=f)
            print('{} --> {}'.format(bgn, end), file=f)
            print(newcontent[i][1], file=f)
            print(file=f)


def run(opt):
    d, f, e = fn_spilt(opt.file)
    nc = None
    if e == '.txt':
        nc = capture(opt.file)
        save_pickle(os.path.join(d, f + '.pkl'), nc)

    elif e == '.pkl':
        nc = load_pickle(opt.file)

    else:
        print(".txt or .pkl file only. could not generate close caption files.") 
        return

    if not nc:
        return

    # print(nc)

    lrcfn = os.path.join(d, f + '.lrc')
    srtfn = os.path.join(d, f + '.srt')

    render(int(opt.comp), nc, lrcfn, srtfn)

# COMP = 0


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(
                    prog = 'ProgramName',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')

    argparser.add_argument("--file", required=True,
                           help="text file or pickle")
    argparser.add_argument("--comp", help="Video title", default="0")
    args = argparser.parse_args()

    if not os.path.exists(args.file):
        exit("Please specify a valid file using the --file= parameter.")

    run(args)
