from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='1uwqA', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='1uwqA', atom_files='1uwqA.pdb')
aln.append(file='ancestro.fasta.txt', align_codes='Ancestro', alignment_format='FASTA')
aln.align2d()
aln.write(file='aligned.fasta', alignment_format='FASTA')
aln.write(file='aligned.ali', alignment_format='PIR')
aln.write(file='aligned.pap', alignment_format='PAP')