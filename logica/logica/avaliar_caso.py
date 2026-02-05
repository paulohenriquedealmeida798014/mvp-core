# Função central de avaliação de caso
# Versão inicial com regras básicas separadas + códigos estruturados via catálogo

from typing import Dict, Any
from .codigos import (
    IDADE_OBRIGATORIA_AUSENTE,
    IDADE_TIPO_INVALIDO,
    IDADE_FORA_FAIXA,
    IDADE_MENOR_18,
    IDADE_ACIMA_60,
)

VERSAO_PROTOCOLO = "1.0.0"

Resultado = Dict[str, Any]
Entrada = Dict[str, Any]


def validar_idade_obrigatoria(dados_avaliacao: Entrada, resultado: Resultado) -> bool:
    """Bloqueia se o campo 'idade' não estiver presente."""
    if "idade" not in dados_avaliacao:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append("Campo obrigatório 'idade' não informado.")
        resultado["codigos"].append(IDADE_OBRIGATORIA_AUSENTE)
        return False
    return True


def validar_tipo_idade(dados_avaliacao: Entrada, resultado: Resultado) -> bool:
    """Bloqueia se 'idade' não for numérico."""
    idade = dados_avaliacao.get("idade")
    if not isinstance(idade, (int, float)):
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append("Campo 'idade' deve ser numérico.")
        resultado["codigos"].append(IDADE_TIPO_INVALIDO)
        return False
    return True


def validar_faixa_idade(dados_avaliacao: Entrada, resultado: Resultado) -> bool:
    """Bloqueia se 'idade' estiver fora da faixa 0–120."""
    idade = dados_avaliacao.get("idade")
    if idade < 0 or idade > 120:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append("Campo 'idade' fora da faixa válida (0 a 120).")
        resultado["codigos"].append(IDADE_FORA_FAIXA)
        return False
    return True


def aplicar_exclusao_idade_minima(dados_avaliacao: Entrada, resultado: Resultado) -> bool:
    """Bloqueia se 'idade' for menor que 18."""
    if dados_avaliacao.get("idade") < 18:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append("Idade menor que 18 anos não permitida.")
        resultado["codigos"].append(IDADE_MENOR_18)
        return False
    return True


def aplicar_alerta_idade_alta(dados_avaliacao: Entrada, resultado: Resultado) -> None:
    """Gera alerta se 'idade' for maior que 60."""
    if dados_avaliacao.get("idade") > 60:
        resultado["alertas"].append(
            "Paciente com idade acima de 60 anos. Avaliar com cautela."
        )
        resultado["codigos_alerta"].append(IDADE_ACIMA_60)


def avaliar_caso(dados_avaliacao: Entrada) -> Resultado:
    """Orquestra a avaliação aplicando validações, exclusões e alertas."""
    resultado: Resultado = {
        "versao_protocolo": VERSAO_PROTOCOLO,
        "status": "ok",
        "alertas": [],
        "bloqueios": [],
        "codigos": [],
        "codigos_alerta": [],
        "texto_base": ""
    }

    # Validação obrigatória
    if not validar_idade_obrigatoria(dados_avaliacao, resultado):
        return resultado

    # Validação de tipo
    if not validar_tipo_idade(dados_avaliacao, resultado):
        return resultado

    # Validação de faixa
    if not validar_faixa_idade(dados_avaliacao, resultado):
        return resultado

    # Regra de exclusão
    if not aplicar_exclusao_idade_minima(dados_avaliacao, resultado):
        return resultado

    # Aplicar alertas
    aplicar_alerta_idade_alta(dados_avaliacao, resultado)

    # Texto final baseado em alertas
    if resultado["alertas"]:
        resultado["texto_base"] = (
            "Avaliação concluída com alertas. Verifique os pontos de atenção."
        )
    else:
        resultado["texto_base"] = "Avaliação concluída sem alertas."

    return resultado
