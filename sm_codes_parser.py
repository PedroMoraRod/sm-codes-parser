import sys, getopt

CLI_ERROR_CODE = 2
QUOTES = 34 #double quotes ASCII code

def get_args(argv : list) -> tuple:
    """
    Returns command-line arguments with options:
        -i,--ifile : input file name
        -o,--ofile : output file name
    """
    input_file = ''
    output_file = ''
    try:
        opts, _ = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('Command line argument syntax error.\nCorrect command format is:\n\tsm_codes_parser.py -i <inputfile> -o <outputfile>')
        sys.exit(CLI_ERROR_CODE)
    for opt, arg in opts:
        if opt == '-h':
            print('sm_codes_parser.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
    return input_file, output_file

def get_sm_codes(input_file: str) -> list:
    """
    Reads given input file which is exptected to be a .txt with the following format:
    
    item0 code0
    item1 code1

    Returns a list of every line separated in a list of item and code
    """
    lines = []
    with open(input_file, 'r') as codes:
        for line in codes:
            line = line.strip() #remove white spaces at the beggining/end and newlines
            line = line.rsplit("\t", 1) #split by last ocurrence of tab space
            lines.append(line)
    return lines

def write_codes_json(codes: list, output_file : str):
    content = '{\n'
    for code in codes:
        content += f'\t{chr(QUOTES)}{code[0]}{chr(QUOTES)}: {chr(QUOTES)}{code[1]}{chr(QUOTES)},\n'
    content = content[:-2:]
    content += '\n}'
    
    with open(output_file, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    try:
        input_file, output_file = get_args(sys.argv[1:])
        if input_file == '' or output_file == '':
            raise Exception("Missing argument(s).\nCorrect command format is:\n\tsm_codes_parser.py -i <inputfile> -o <outputfile>")
        else:
            sm_codes = get_sm_codes(input_file)
            write_codes_json(sm_codes, output_file)
    except Exception as e:
        print(e)
    
