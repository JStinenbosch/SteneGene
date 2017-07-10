from PythonFiles.Utilities import *
from PyqT5
acceptable_extensions = ['.fasta', '.fas', '.fa', '.fsa', '.fna', '.fsa_nt']


def displayFileChoice():


    files = eg.fileopenbox("Please select files", filetypes=['*' + ext for ext in acceptable_extensions], multiple=True)
    while not files.endswith(tuple(acceptable_extensions)):
        eg.msgbox('''Please select a file with one of the following extensions:
                .fasta, .fas, .fa, .seq, .fsa: Generic FASTA
                .fna, .fsa_nt: FASTA nucleic acids\n''')
        files = eg.fileopenbox("Please select files", filetypes=['*' + ext for ext in acceptable_extensions], multiple=True)
    handleInputFiles([files])

def displayHelpMenu():
    eg.msgbox(msg="Authors:\n JBA Stinenbosch\n FG te Nijenhuis", title="Help", ok_button="Return")
    mainGUILoop()


def mainGUILoop():
    mainchoice = eg.indexbox(title="Sequence Analysis v0.1.0", choices=["Specify input files", "Help"],
                             msg="Welcome to Sequence Analysis, what do you want to do?")

    if mainchoice == 0:
        displayFileChoice()
    elif mainchoice == 1:
        displayHelpMenu()
    print(['*' + ext for ext in acceptable_extensions])

mainGUILoop()