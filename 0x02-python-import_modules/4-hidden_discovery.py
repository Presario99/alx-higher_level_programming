#!/usr/bin/python3

import dis
import marshal

def get_names_from_pyc(pyc_file):
    with open(pyc_file, 'rb') as f:
        magic = f.read(4)
        timestamp = f.read(4)
        code = marshal.load(f)

        names = set()
        for instr in code.co_code:
            if isinstance(instr, tuple) and instr[0] == dis.opmap['STORE_NAME']:
                name_index = instr[1]
                name = code.co_names[name_index]
                if not name.startswith('__'):
                    names.add(name)

    return sorted(names)

if __name__ == "__main__":
    pyc_file = 'hidden_4.pyc'  # Replace with the actual path to your hidden_4.pyc file
    names = get_names_from_pyc(pyc_file)

    for name in names:
        print(name)
