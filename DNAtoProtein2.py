import os
from Bio.Seq import Seq, transcribe
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
NCBIWWW.email = "booey475@gmail.com"

class DNAtoProtein2:
    def convert(self, dnaString):
        dnaString = "x"
        dna_seq = Seq("caaggtcaaa taccaagatt ttttcttctt tgtcagtctt gtccaaacca taagcaagag" +
    "   61 ctgctgcagt tggttcgtta acaatacgtt ctacttcaag accagcaatt ttaccagcgt" +
    "  121 cttttgttgc ttgacgttga gcgtcgttga agtaagccgg aactgtgata acagctttgg" +
    "  181 ttactttctc accaaggtag tcttcagcgt agcctttcaa gtattgaagg atcatagctg" +
    "  241 agatttcttg tggagtgtat tctttccatt tgcagaaact ttttcagaag ttcccatctt" +
    "  301 agatttgata gagataactg tatctgggtt tgtaactgct tgacgttttg cagcatcacc" +
    "  361 acgatgattt ctccgttttt gaatgagact acagatggag ttgtgcggtt tccttctggg" +
    "  421 tttgcgatga ttttgctttc agttccttca agaactgcaa ctgctgagtt tgttgtacct" +
    "  481 aagtcaatac cgataatttt agacatgtgt ttttctcctt gttagttaat tttctatttt" +
    "  541 tctttttgat actcttctta agtggcgaca gtggcgacgc cgtcagagct tgacttcgtc" +
    "  601 aatctctttg actaaacttt gagcctaagg tctcaaaatt tgcgcaaata gcgccacggc" +
    "  661 gaagagtatc gtgtttggtt cgcttcgctc actattacaa agccaaacat attttatctt" +
    "  721 tcttcatagt ttattgtcgt ttcggacaag ttttcttatg taaattgcga cacgaggagt" +
    "  781 cgaaatcgat tttatttcga cgacgagtta gtaaggaagc taggcaaacg ccatagcgat")
        rna_seq = Seq(transcribe(dna_seq))
        result_handle = (NCBIWWW.qblast("blastx", "nr", rna_seq,
                               entrez_query="primate[ORGN]",
                               format_type="Text"))
        with open("my_blast.xml", "w") as out_handle:
            out_handle.write(result_handle.read())
        result_handle.close()
        result_handle = open("my_blast.xml")
        blast_record = NCBIXML.read(result_handle)
        E_VALUE_THRESH = 0.04
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                if hsp.expect < E_VALUE_THRESH:
                    title = (alignment.title)
        return title
        
temp = DNAtoProtein2()
temp.convert("x")
# print(temp)