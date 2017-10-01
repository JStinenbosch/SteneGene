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

def add_property_to_string(property: str, arg_dict: dict, result_list: list, default) -> None:
    """ This function is used to construct argument lists in various places. We check whether a certain property is
        defined. If it is, we add its value to the argument list. If it isn't, we use the default.
    """
    if property in arg_dict:
        result_list.append("-" + property + " " + arg_dict[property] + " ")
    else:
        result_list.append("-" + property + " " + default + " ")