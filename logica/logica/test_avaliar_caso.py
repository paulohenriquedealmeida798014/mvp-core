from .avaliar_caso import avaliar_caso
from .codigos import (
    IDADE_OBRIGATORIA_AUSENTE,
    IDADE_TIPO_INVALIDO,
    IDADE_FORA_FAIXA,
    IDADE_MENOR_18,
    IDADE_ACIMA_60,
)

def test_idade_ausente_bloqueia():
    resultado = avaliar_caso({})
    assert resultado["status"] == "bloqueado"
    assert IDADE_OBRIGATORIA_AUSENTE in resultado["codigos"]

def test_idade_tipo_invalido_bloqueia():
    resultado = avaliar_caso({"idade": "abc"})
    assert resultado["status"] == "bloqueado"
    assert IDADE_TIPO_INVALIDO in resultado["codigos"]

def test_idade_fora_faixa_bloqueia():
    resultado = avaliar_caso({"idade": 200})
    assert resultado["status"] == "bloqueado"
    assert IDADE_FORA_FAIXA in resultado["codigos"]

def test_idade_valida_com_alerta():
    resultado = avaliar_caso({"idade": 65})
    assert resultado["status"] == "ok"
    assert IDADE_ACIMA_60 in resultado["codigos_alerta"]
    assert len(resultado["alertas"]) == 1
