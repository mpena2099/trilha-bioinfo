# Plano de Estudos: Bioinformática Clínica, Genética e IA (4 Meses)

## Visão Geral

Duração: 16 semanas\
Carga: 8–10h semanais\
Objetivo: Capacitação prática e teórica para aplicações clínicas em bioinformática e IA em genômica.

---

## Módulo 1 (Semanas 1–4): Fundamentos de Genética e Genética Populacional

**Objetivos:**

- Compreender a base genética, SNPs e herança genética.
- Estudar genética de populações.

**Cursos:**

- [Genética Populacional – Online Cursos Gratuitos](https://onlinecursosgratuitos.com.br/curso/ciencias-humanas-e-sociais/genetica-populacional?utm_source=chatgpt.com)
- [Genética Humana – Pleno Cursos](https://www.plenocursos.com.br/curso/curso-gratuito-de-basico-em-genetica-humana?utm_source=chatgpt.com)

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

**Cursos:**

- [Curso ML para a Saúde – Coursera](https://guide.courseeye.com/curso-recomendado-fundamentos-de-machine-learning-para-a-saude/?utm_source=chatgpt.com)
- [Data Science Academy – ML Biomédico](https://www.datascienceacademy.com.br/course/machine-learning-para-aplicacoes-biomedicas?utm_source=chatgpt.com)

**Entrega esperada:** Notebook com modelo preditivo

---

## Módulo 4 (Semanas 13–16): IA Generativa, XAI e Deploy

**Objetivos:**

- Usar IA generativa (LLMs) para saúde.
- Aplicar SHAP, LIME, FastAPI, Gradio.

**Cursos:**

- [Generative AI for Healthcare – Coursera](https://www.coursera.org/learn/generative-ai-for-healthcare?utm_source=chatgpt.com)

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

## Repositório Git sugerido

**Estrutura ideal:**

```
trilha-bioinfo/
├── modulo1_genetica/
├── modulo2_vcf/
├── modulo3_ml_saude/
├── modulo4_ia_xai/
└── README.md
```

Cada pasta conterá Jupyter Notebooks, PDFs, comandos, datasets e scripts de pré-processamento.

---

## Próximos Passos

1. Acompanhar trilha semanalmente com este documento no celular.
2. Clonar repositório Git com exercícios (fornecido na próxima resposta).
3. Completar os checkpoints a cada 4 semanas.
