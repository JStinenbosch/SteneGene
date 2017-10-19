import shutil
from Bio.Blast import NCBIXML

acceptable_extensions = ['.fasta', '.fas', '.fa', '.fsa', '.fna', '.fsa_nt']

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

def check_extensions(files):
    wgs_files = list(filter(lambda name: name.endswith(tuple(acceptable_extensions)), files))
    if not wgs_files:
        print("Incorrect extension, we only allow " + str(acceptable_extensions))
        exit(-1)
    return wgs_files

def add_property_to_string(property, arg_dict: dict, result_string: str, default):
    """ This function is used to construct argument strings in various places. We check whether a certain property is
        defined. If it is, we add its value to the argument string. If it isn't, we use the default.
    """
    if property in arg_dict:
        result_string += ("-" + property + " " + arg_dict[property] + " ")
    else:
        result_string += ("-" + property + " " + default + " ")
    return result_string

def parse_blast_out(blast_out_xml):
    result_handle = open(blast_out_xml)
    blast_records = NCBIXML.parse(result_handle)
    blast_records = list(blast_records)