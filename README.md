# Trilha Bioinfo: Bioinformática Clínica, Genética e IA

Plano de estudos de 16 semanas e código de apoio. Projeto pessoal e educacional.

> **Aviso:** nada aqui serve para diagnóstico ou decisão clínica. Os dados dos exemplos são simulados. Não commite dados genéticos reais de pacientes (o `.gitignore` já ignora `*.vcf`, `*.bam` e `*.gz`).

## Estrutura

```
trilha-bioinfo/
├── CRONOGRAMA.md        # tarefas semana a semana
├── modulo1_genetica/    # leituras, mapas mentais, resumos
├── modulo2_vcf/         # scripts de anotação, datasets, laudos
├── modulo3_ml_saude/    # notebook de ML com SNPs simulados
├── modulo4_ia_xai/      # API FastAPI de demonstração
├── requirements.txt
└── requirements-dev.txt
```

## Como usar

```bash
pip install -r requirements.txt   # use requirements-dev.txt para rodar os testes (pytest)

# Notebook do módulo 3
jupyter notebook modulo3_ml_saude/notebooks/modelo_snp_predicao.ipynb

# API de demonstração (docs em http://127.0.0.1:8000/docs)
uvicorn modulo4_ia_xai.api.app_fastapi:app --reload

# Anotação com ANNOVAR (requer instalação e registro no site do ANNOVAR)
./modulo2_vcf/scripts/anotar_com_annovar.sh entrada.vcf humandb/ saida
```

## Status

| Módulo | Situação |
|---|---|
| 1. Genética | em andamento |
| 2. VCF e anotação | script de exemplo pronto |
| 3. ML em saúde | notebook com dados simulados |
| 4. IA e XAI | API de demonstração, sem modelo real |

## Plano

16 semanas, 8 a 10 horas por semana. As tarefas de cada semana, com links dos cursos, estão no [CRONOGRAMA.md](CRONOGRAMA.md).

| Semanas | Módulo | Entrega |
|---|---|---|
| 1 a 4 | Fundamentos de genética e genética populacional | Mapa mental e quiz |
| 5 a 8 | Bioinformática clínica: VCF, bancos de variantes, anotação, ACMG | Minirrelatório VCF e laudo básico |
| 9 a 12 | Machine learning em saúde e genômica | Notebook com modelo preditivo |
| 13 a 16 | IA generativa, XAI (SHAP, LIME) e deploy | Protótipo de app com explicabilidade |

## Recursos extras

- Bancos de variantes: [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/), [gnomAD](https://gnomad.broadinstitute.org)
- Anotação: [VEP](https://www.ensembl.org/info/docs/tools/vep/index.html)
- Visualização: [IGV](https://software.broadinstitute.org/software/igv/)
- Dados: [FTP 1000 Genomes](https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/)
- Cursos complementares: [AI for Medicine, Stanford (Coursera)](https://www.coursera.org/specializations/ai-for-medicine), [Generative AI for Healthcare Students and Professionals, University of Glasgow (Coursera)](https://www.coursera.org/learn/generative-ai-for-healthcare-students-and-professionals)

## Licença

[MIT](LICENSE)
