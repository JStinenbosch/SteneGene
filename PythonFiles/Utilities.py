import shutil

def handle_input_files(files):
    concat_files(files)

# Concatenates the input files chosen using the filechooser into a single query
def concat_files(files):
    with open('ProteinQuery.fa', 'wb') as wfd:
        for f in files:
            with open(f, 'rb') as fd:
                shutil.copyfileobj(fd, wfd, 1024 * 1024 * 10)