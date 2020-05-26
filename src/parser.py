import re
import os

# const
dirname = os.path.dirname(__file__)
dialect_file = os.path.join(dirname, 'dialects/default')
print(dialect_file)
# ----- extra keyword section -----
# 🔑 defines new variable
# todo: move to dialect file and implement
# variable_definition = '🔑'
# ----- extra keyword section -----

# transpiling map emojpy to python
parser_map = {}
with open(dialect_file, 'r', encoding='utf-8') as f:
    parser_map = {v:k for (k, v) in [x.strip().split(':') for x in f.readlines()]}

# transpiling map python to emojpy
inverse_parser_map = {}
with open(dialect_file, 'r', encoding='utf-8') as f:
    inverse_parser_map = {k:v for (k, v) in [x.strip().split(':') for x in f.readlines()]} 

def write(fp, content):
    '''Writes content to filepath fp'''
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)

def read(fp):
    '''Reads filepath fp'''
    with open(fp, 'r', encoding='utf-8') as f:
        return f.read()

def to_python(file):
    for k, v in parser_map.items():
        file = re.sub(k, v, file)
    return file

def to_emojpy(file):
    for k, v in inverse_parser_map.items():
        file = re.sub(r'\b{}\b'.format(k), v, file)
    return file
    
def parse_file(fp, inverse=False):
    '''Method to parse file in both direction. Default direction is from emojpy to python.'''
   
    file = read(fp)
    file = to_python(file) if not inverse else to_emojpy(file)
        
    return file
    
if __name__ == "__main__":
    # argument parse only if used as script
    import argparse
    parser = argparse.ArgumentParser(description='''transpiler from and to emojpy V1.0 | usage:
    python parser.py filepath or 
    python parser.py --inverse True filepath
    ''')
    parser.add_argument('fp', help='filepath to emojpy/python file')
    parser.add_argument('--inverse', help='transpile to emojpy', default=False)          
    args = parser.parse_args()
    
    # parse file and output it
    print(parse_file(args.fp, args.inverse))
    
    