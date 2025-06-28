#!/bin/bash
table_annovar.pl exemplo.vcf humandb/ \
  -buildver hg38 \
  -out saida \
  -remove \
  -protocol refGene,clinvar_20220320 \
  -operation g,f \
  -nastring . \
  -vcfinput
