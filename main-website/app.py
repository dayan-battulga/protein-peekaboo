# app.py
from flask import Flask, request, jsonify
import os
from Bio.Seq import Seq, transcribe
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from flask_cors import CORS

NCBIWWW.email = "booey475@gmail.com"

app = Flask(__name__)
CORS(app)

class DNAtoProtein:
    def convert(self, dnaString):
        dna_seq = Seq(dnaString)
        rna_seq = Seq(transcribe(dna_seq))

        result_handle = (NCBIWWW.qblast("blastx", "nr", rna_seq, entrez_query="primates[ORGN]"))
        
        with open("my_blast.xml", "w") as out_handle:
            out_handle.write(result_handle.read())
            
        min_evalue = 0.0000001
    
        result_handle = open("my_blast.xml")
        blast_records = NCBIXML.parse(result_handle)

        title_evalues = {}
        titles = []

        for blast_record in blast_records:
            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    if hsp.expect < min_evalue:
                        aligntitle = alignment.title
                        aligntitle = aligntitle.split("|")
                        aligntitle = aligntitle[2].strip()
                        aligntitle = aligntitle.split("]")
                        aligntitle = aligntitle[0].strip() + "]"
                        title_evalues[hsp.expect] = aligntitle


        result_handle.close()

        evalues = sorted(title_evalues.keys())[:3]
        
        for evalue in evalues:
            titles.append(str(title_evalues[evalue]) + " e = " + str(evalue))

        return titles 

temp = DNAtoProtein()

@app.route('/api/content', methods=['POST'])
def content():
    data = request.get_json()
    input_string = data.get('text', '')
    result = temp.convert(input_string)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=4000)

