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
        
        with open("my_blast.xml", "w") as out_handle:
            out_handle.write(result_handle.read())

        e_value_thresh = 0.004
        common_proteins = ["heat protein", "hemoglobin", "collagen", "actin", "myosin", "keratin", "insulin", 
                           "albumin", "fibrinogen", "immunoglobulin", "enzyme", "ferritin", "tubulin", "fibronectin", 
                           "thrombin", "histone", "elastin", "transthyretin", "cytokeratin", "casein", "globulin", 
                           "myoglobin", "erythropoietin", "prothrombin", "collagenase", "nicotinamide", "lysine", 
                           "cytochrome"]
        
        with open("my_blast.xml") as result_handle:
            blast_records = NCBIXML.parse(result_handle)

            titles = set()

            for blast_record in blast_records:
                for alignment in blast_record.alignments:
                    for hsp in alignment.hsps:
                        if len(titles) < 3 and hsp.expect < e_value_thresh:
                            if alignment.title not in titles:
                                title = alignment.title.split()[1].lower().rstrip(",")
                                if (title.startswith(("heat", "hsp", "hcg")) or title in common_proteins):
                                    titles.add(title)
                        else:
                            break

        print( titles)

temp = DNAtoProtein2()
temp.convert("1 caaggtcaaa taccaagatt ttttcttctt tgtcagtctt gtccaaacca taagcaagag"+
     "  61 ctgctgcagt tggttcgtta acaatacgtt ctacttcaag accagcaatt ttaccagcgt"+
     " 121 cttttgttgc ttgacgttga gcgtcgttga agtaagccgg aactgtgata acagctttgg"+
     " 181 ttactttctc accaaggtag tcttcagcgt agcctttcaa gtattgaagg atcatagctg"+
     " 241 agatttcttg tggagtgtat tctttccatt tgcagaaact ttttcagaag ttcccatctt")