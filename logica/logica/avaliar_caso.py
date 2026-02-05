# Função central de avaliação de caso
# Pipeline extensível de regras + códigos e mensagens via catálogo

from typing import Dict, Any, Callable, List
from .codigos import (
    IDADE_OBRIGATORIA_AUSENTE,
    IDADE_TIPO_INVALIDO,
    IDADE_FORA_FAIXA,
    IDADE_MENOR_18,
    IDADE_ACIMA_60,
)
from .mensagens import (
    MSG_IDADE_OBRIGATORIA_AUSENTE,
    MSG_IDADE_TIPO_INVALIDO,
    MSG_IDADE_FORA_FAIXA,
    MSG_IDADE_MENOR_18,
    MSG_ALERTA_IDADE_ACIMA_60,
    MSG_TEXTO_BASE_ALERTAS,
    MSG_TEXTO_BASE_OK,
)

VERSAO_PROTOCOLO = "1.0.0"

Resultado = Dict[str, Any]
Entrada = Dict[str, Any]
Regra = Callable[[Entrada, Resultado], bool]


def validar_idade_obrigatoria(dados_avaliacao: Entrada, resultado: Resultado) -> bool:
    """Bloqueia se o campo 'idade' não estiver presente."""
    if "idade" not in dados_avaliacao:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append(MSG_IDADE_OBRIGATORIA_AUSENTE)
        resultado["codigos"].append(IDADE_OBRIGATORIA_AUSENTE)
        return False
    return True


def validar_tipo_idade(dados_avaliacao: Entrada, resultado: Resultado) -> bool:
    """Bloqueia se 'idade' não for numérico."""
    idade = dados_avaliacao.get("idade")
    if not isinstance(idade, (int, float)):
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append(MSG_IDADE_TIPO_INVALIDO)
        resultado["codigos"].append(IDADE_TIPO_INVALIDO)
        return False
    return True


def validar_faixa_idade(dados_avaliacao: Entrada, resultado: Resultado) -> bool:
    """Bloqueia se 'idade' estiver fora da faixa 0–120."""
    idade = dados_avaliacao.get("idade")
    if idade < 0 or idade > 120:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append(MSG_IDADE_FORA_FAIXA)
        resultado["codigos"].append(IDADE_FORA_FAIXA)
        return False
    return True


def aplicar_exclusao_idade_minima(dados_avaliacao: Entrada, resultado: Resultado) -> bool:
    """Bloqueia se 'idade' for menor que 18."""
    if dados_avaliacao.get("idade") < 18:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append(MSG_IDADE_MENOR_18)
        resultado["codigos"].append(IDADE_MENOR_18)
        return False
    return True


def aplicar_alerta_idade_alta(dados_avaliacao: Entrada, resultado: Resultado) -> bool:
    """Gera alerta se 'idade' for maior que 60."""
    if dados_avaliacao.get("idade") > 60:
        resultado["alertas"].append(MSG_ALERTA_IDADE_ACIMA_60)
        resultado["codigos_alerta"].append(IDADE_ACIMA_60)
    return True


PIPELINE_REGRAS: List[Regra] = [
    validar_idade_obrigatoria,
    validar_tipo_idade,
    validar_faixa_idade,
    aplicar_exclusao_idade_minima,
    aplicar_alerta_idade_alta,
]


def avaliar_caso(dados_avaliacao: Entrada) -> Resultado:
    """Orquestra a avaliação aplicando o pipeline de regras."""
    resultado: Resultado = {
        "versao_protocolo": VERSAO_PROTOCOLO,
        "status": "ok",
        "alertas": [],
        "bloqueios": [],
        "codigos": [],
        "codigos_alerta": [],
        "texto_base": ""
    }

    for regra in PIPELINE_REGRAS:
        ok = regra(dados_avaliacao, resultado)
        if not ok:
            return resultado

    if resultado["alertas"]:
        resultado["texto_base"] = MSG_TEXTO_BASE_ALERTAS
    else:
        resultado["texto_base"] = MSG_TEXTO_BASE_OK

    return resultado
