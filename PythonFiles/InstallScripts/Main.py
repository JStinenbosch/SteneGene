from easygui import *

acceptable_extensions = ['*.fasta', '*.fas', '*.fa', '*.fsa', '*.fna', '*.fsa_nt']

file = fileopenbox("Please select files", filetypes=acceptable_extensions)
while not file.endswith(tuple(acceptable_extensions)) :
    file_extension_box = msgbox('''Please select a file with one of the following extensions:
        .fasta, .fas, .fa, .seq, .fsa: Generic FASTA
        .fna, .fsa_nt: FASTA nucleic acids\n''')
    file = fileopenbox("Please select files", filetypes=acceptable_extensions)

