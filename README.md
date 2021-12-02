# COVID19-variation
###  Refer to the public article method (https://www.nature.com/articles/s41586-021-03807-6 [PMID: 34261126](https://pubmed.ncbi.nlm.nih.gov/34261126/))

Variation of each mutation position was calculation by RBD region (Sarbecovirus/SARS-CoV-2)

The static logo plots were created by **dmslogo** (https://jbloomlab.github.io/dmslogo/) version 0.6.2; The color of the mutations indicates the expression of RBDs derived from published data (PMID: 32841599).  
**Sarbecovirus variation** of each mutation position was calculation by Sarbecovirus RBD region, which were downloaded from published data (PMID: 34261126;
https://github.com/jbloomlab/SARSr-CoV_RBD_MAP/blob/main/data/RBD_aa_aligned.fasta). Color from light blue to black represents an increase in the mutation frequency.  
**SARS-CoV-2 variation** were calculated using spike sequences from GISAID database (PMID: 31565258). All spike sequences were aligned using MAFFT (version 7, PMID: 31062021) with “--6merpair”parament and Wuhan-Hu-1 as the reference sequence. In the RBD region, sequences with gaps, ambiguous amino acid or more than eight amino acid differences from the Wuhan-Hu-1 were removed leaving 3,722,275 sequences for calculating variation. 

Acknowledging GISAID data contributors  
https://www.gisaid.org/help/publish-with-data-from-gisaid/


### target
**use "COVID19_variation_search_GUI.py" to search "1_variation_COVID19_Sarbecovirus.csv" table**

~~This was mistaken text~~  
## ~~need to do~~
 - 计算所有位点的突变结果  
 - 可视化（Rmarkdown，R-DT）
 - RBD表达热图
 - 所有R脚本、linux脚本写在markdown中
 - python脚本 static logo~~
