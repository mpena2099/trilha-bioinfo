from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Trilha Bioinfo: demo de predição de risco",
    description=(
        "Demonstração educacional. Os valores retornados são fictícios, "
        "não vêm de um modelo treinado e não servem para diagnóstico."
    ),
)


class SNPInput(BaseModel):
    rs123: int = Field(ge=0, le=2, description="Número de alelos alternativos (0, 1 ou 2)")
    rs456: int = Field(ge=0, le=2, description="Número de alelos alternativos (0, 1 ou 2)")


@app.post("/prever")
def prever(input: SNPInput):
    # Regra fixa de exemplo, a ser trocada pelo modelo do módulo 3.
    risco = 0.3 if input.rs123 == 1 else 0.7
    return {
        "risco": risco,
        "aviso": "Valor fictício para demonstração. Não use para decisões clínicas.",
    }
