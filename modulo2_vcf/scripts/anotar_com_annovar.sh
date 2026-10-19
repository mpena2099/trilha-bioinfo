#!/bin/bash
# Uso: ./anotar_com_annovar.sh <entrada.vcf> <pasta_humandb> [prefixo_saida]
# Requer table_annovar.pl no PATH e os bancos refGene e clinvar_20220320 (hg38) em <pasta_humandb>.
set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "Uso: $0 <entrada.vcf> <pasta_humandb> [prefixo_saida]" >&2
  exit 1
fi

entrada="$1"
humandb="$2"
saida="${3:-saida}"

table_annovar.pl "$entrada" "$humandb" \
  -buildver hg38 \
  -out "$saida" \
  -remove \
  -protocol refGene,clinvar_20220320 \
  -operation g,f \
  -nastring . \
  -vcfinput
