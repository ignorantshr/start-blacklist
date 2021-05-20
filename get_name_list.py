import getopt
import sys
from typing import List

def read_name(file_path: str) -> List[str]:
    lines = list()
    with open(file_path, 'r') as f:
        f.reconfigure(encoding='utf8')
        lines = f.readlines()
    for i, v in enumerate(lines):
        lines[i] = str.strip(v).strip('\n').strip('\r')
    return lines

if __name__ == '__main__':
    flag = None
    file_path = None
    help_msg = '''
Usage: python get_name_list.py [options]
Options:
    -f      The path to the file that contains the name(or everything you want), default 'starts.txt'
    -F      The separator between the output names, default '\r\n'
    -h      Print this and exit
    '''

    try:
        opts, _ = getopt.getopt(sys.argv[1:], 'hF:f:')
        for o, v in opts:
            if o == '-h':
                print(help_msg)
                exit(0)
            if o == '-F':
                flag = eval(repr(v).replace('\\\\', '\\'))
            elif o == '-f':
                file_path = v
    except getopt.GetoptError as e:
        print(e)
        print(help_msg)
        exit(1)

    if flag is None:
        flag = '\r\n'
    if file_path is None:
        file_path = 'starts.txt'

    names = read_name(file_path)
    print(flag.join(names))
