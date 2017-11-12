from Bio.Blast import NCBIXML
import os.path

expect_value = 0.001




def xml_to_fasta_files(blast_xml, expect_value):
    for blast_xml_files in blast_xml:
        blast_records = NCBIXML.parse(open(blast_xml_files))
        for blast_record in blast_records:
            if hasattr(blast_record, 'alignments'):
                for alignment in blast_record.alignments:
                    first_alignment = alignment.hsps[0]
                    if first_alignment.expect < expect_value:
                        file = open(os.path.splitext(blast_xml_files)[0] + "/" + blast_record.query + ".fa", "w")
                        file.write(">" + alignment.hit_id + " " + blast_record.query + " [" + os.path.splitext(blast_record.database)[0] + "]" +
                                   "\n")
                        new_first_alignment = first_alignment.sbjct.replace("-", "")
                        start = 0
                        while len(new_first_alignment) - start >= 80:
                            file.write(new_first_alignment[start:start+80] + "\n")
                            start += 80
                        file.write(new_first_alignment[start:])
                        file.close()

def add_dir_to_path(blast_xml):
    for blast_xml_files in blast_xml:
        current_directory = os.path.dirname(blast_xml_files)
        final_directory = os.path.join(current_directory, os.path.splitext(os.path.basename(blast_xml_files))[0])
        if not os.path.exists(final_directory):
           os.makedirs(final_directory)


