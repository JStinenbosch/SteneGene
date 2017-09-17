import shutil
from Bio.Blast import NCBIXML

def handle_input_files(files, name='GeneQuery.fa'):
    concat_files(files, name)
    return name

# Concatenates the input files chosen using the filechooser into a single query
def concat_files(files, name):
    with open(name , 'wb') as wfd:
        for f in files:
            with open(f, 'rb') as fd:
                shutil.copyfileobj(fd, wfd, 1024 * 1024 * 10)

def extract_sequence(blastout_XML_file):
    with open(blastout_XML_file) as handle:
        return NCBIXML.parse(handle)
