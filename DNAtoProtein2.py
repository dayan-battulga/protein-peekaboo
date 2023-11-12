import os
from Bio.Seq import Seq, transcribe
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
NCBIWWW.email = "booey475@gmail.com"

class DNAtoProtein2:
    def convert(self, dnaString):
        dna_seq = Seq(dnaString)
        rna_seq = Seq(transcribe(dna_seq))
        result_handle = (NCBIWWW.qblast("blastx", "nr", rna_seq,
                               entrez_query="primates[ORGN]"))
        out_handle = open("my_blast.xml", "w")
        out_handle.write(result_handle.read())
        result_handle.close()
        out_handle.close()
        result_handle = open("my_blast.xml")
        blast_records = NCBIXML.parse(result_handle)
        E_VALUE_THRESH = 0.0000000001
        count = 0
        titles = []
        for blast_record in blast_records:
            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    if count < 3 and hsp.expect < E_VALUE_THRESH:
                        if alignment.title not in titles:
                            titles.append(alignment.title)
                            count += 1
                    else:
                        break
        return titles 
temp = DNAtoProtein2()
temp.convert("x")