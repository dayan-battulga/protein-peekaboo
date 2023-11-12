import os
from Bio.Seq import Seq, transcribe
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

NCBIWWW.email = "booey475@gmail.com"

class DNAtoProtein2:
    def convert(self, dnaString):
        dna_seq = Seq(dnaString)
        rna_seq = Seq(transcribe(dna_seq))
        result_handle = (NCBIWWW.qblast("blastx", "nr", rna_seq, entrez_query="primates[ORGN]"))
        out_handle = open("my_blast.xml", "w")
        out_handle.write(result_handle.read())
        result_handle.close()
        out_handle.close()
        result_handle = open("my_blast.xml")
        blast_records = NCBIXML.parse(result_handle)
        e_value_thresh = 0.004
        common_proteins = ["heat protein", "hemoglobin", "collagen", "actin", "myosin", "keratin", "insulin", 
                           "albumin", "fibrinogen", "immunoglobulin", "enzyme", "ferritin", "tubulin", "fibronectin", 
                           "thrombin", "histone", "elastin", "transthyretin", "cytokeratin", "casein", "globulin", 
                           "myoglobin", "erythropoietin", "prothrombin", "collagenase", "nicotinamide", "lysine", 
                           "cytochrome"]
        
        titles = []

        for blast_record in blast_records:
            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    if hsp.expect < e_value_thresh:
                        if alignment.title not in titles:
                            title = alignment.title.split()[1].lower().rstrip(",")
                            if (title.startswith(("heat", "hsp", "hcg")) or title in common_proteins):
                                titles.append(title)

        titles = list(set(titles))

        for title in titles:
            print(title)

temp = DNAtoProtein2()
temp.convert("input")