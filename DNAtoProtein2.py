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
        commonProteins = ["heat protein", "hemoglobin", "collagen", "actin", "myosin", "keratin", "insulin", "albumin", "fibrinogen", "immunoglobulin", "enzyme", "ferritin", "tubulin", "fibronectin", "thrombin", "histone", "elastin", "transthyretin", "cytokeratin", "casein", "globulin", "myoglobin", "erythropoietin", "prothrombin", "collagenase"]
        titles = []
        for blast_record in blast_records:
            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    if hsp.expect < E_VALUE_THRESH:
                        if alignment.title not in titles:
                            title = alignment.title.split()
                            title = title[1].lower()
                            if (title == "heat" or title[0:3] == "hsp") and title not in titles:
                                titles.append(title)
                            elif title in commonProteins and title not in titles:
                                titles.append(title)
                    else:
                        break
        for i in titles:
            print(i)
temp = DNAtoProtein2()
temp.convert("x")