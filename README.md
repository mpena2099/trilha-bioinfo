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
└── requirements.txt
```

## Como usar

```bash
pip install -r requirements.txt

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

## Licença

[MIT](LICENSE)

---

## Visão Geral

Duração: 16 semanas\
Carga: 8–10h semanais\
Objetivo: Capacitação prática e teórica para aplicações clínicas em bioinformática e IA em genômica.

---

## Módulo 1 (Semanas 1–4): Fundamentos de Genética e Genética Populacional

**Objetivos:**

- Compreender a base genética, SNPs e herança genética.
- Estudar genética de populações.

**Cursos recomendados:**

- [Introduction to Genetics and Evolution – Duke University (Coursera)](https://www.coursera.org/learn/genetics-evolution)
- [Genetics: Analysis and Applications – MIT via edX](https://www.edx.org/search?q=genetics)

**Entrega esperada:** Mapa mental + quiz de fixação

---

## Módulo 2 (Semanas 5–8): Bioinformática Clínica – VCF, dbSNP, Anotação

**Objetivos:**

- Analisar VCFs, buscar variantes em bancos públicos.
- Utilizar ANNOVAR e VEP para anotação funcional.

### Semana a Semana

**Semana 5:** Estrutura do VCF e ferramentas de linha de comando

- `bcftools`, `vcftools`, `IGV`
- [Tutorial oficial VCFtools](https://vcftools.github.io/index.html)

**Semana 6:** Bancos públicos de variantes

- [dbSNP](https://www.ncbi.nlm.nih.gov/snp/), [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/), [gnomAD](https://gnomad.broadinstitute.org)

**Semana 7:** Anotação com [ANNOVAR](https://annovar.openbioinformatics.org) e [VEP](https://www.ensembl.org/info/docs/tools/vep/index.html)

**Semana 8:** Interpretação clínica (guidelines ACMG)

- Produzir laudo genético básico a partir de uma variante real.

**Entrega esperada:** Minirrelatório VCF + laudo clínico básico

---

## Módulo 3 (Semanas 9–12): Machine Learning em Saúde e Genômica

**Objetivos:**

- Construir modelos preditivos usando dados genéticos.
- Trabalhar com XGBoost, Random Forest e validação.

**Cursos recomendados:**

- [Fundamentals of Machine Learning for Healthcare – Stanford University (Coursera)](https://www.coursera.org/learn/fundamental-machine-learning-healthcare)
- [AI for Medicine Specialization – Stanford University (Coursera)](https://www.coursera.org/specializations/ai-for-medicine)

**Entrega esperada:** Notebook com modelo preditivo

---

## Módulo 4 (Semanas 13–16): IA Generativa, XAI e Deploy

**Objetivos:**

- Usar IA generativa (LLMs) para saúde.
- Aplicar SHAP, LIME, FastAPI, Gradio.

**Cursos recomendados:**

- [Generative AI for Healthcare – Google Cloud (Coursera)](https://www.coursera.org/learn/generative-ai-for-healthcare)
- [Generative AI for Healthcare Students and Professionals – University of Glasgow (Coursera)](https://www.coursera.org/learn/generative-ai-for-healthcare-students-and-professionals)

**Entrega esperada:** Protótipo de app com explicabilidade (XAI)

---

## Checkpoints

- Semana 4: Mapa mental e quiz de genética
- Semana 8: Relatório e anotação de variantes
- Semana 12: Modelo de ML com dados genômicos
- Semana 16: App com IA explicável

---

## Recursos Extras

- IGV: [https://software.broadinstitute.org/software/igv/](https://software.broadinstitute.org/software/igv/)
- FTP 1000 Genomes: [ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/](ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/)

---
