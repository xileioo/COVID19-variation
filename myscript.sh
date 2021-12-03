# https://mafft.cbrc.jp/alignment/software/
# https://mafft.cbrc.jp/alignment/software/closelyrelatedviralgenomes.html

awk 'BEGIN {RS = ">" ; ORS = ""} length($NF) >= 500 {print ">"$0}' spikeprot1105.fasta > spikeprot1105_filter_less500.fasta

awk 'BEGIN {RS = ">" ; ORS = ""} $NF !~ /XXXXXXXXXXXXXXXXXXXXXXXXq/ {print ">"$0}' spikeprot1105_filter_less500.fasta > spikeprot1105_filter_less500_more50X.fasta


mafft --anysymbol --6merpair --thread -8 --keeplength --addfragments spikeprot1105_filter_less500_more50X.fasta ref_wuhan_RBD.fa > output.fa

