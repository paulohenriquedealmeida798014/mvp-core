# Função central de avaliação de caso
# Versão com regras básicas separadas + códigos estruturados via catálogo

from .codigos import (
    IDADE_OBRIGATORIA_AUSENTE,
    IDADE_TIPO_INVALIDO,
    IDADE_FORA_FAIXA,
    IDADE_MENOR_18,
    IDADE_ACIMA_60,
    MSG_IDADE_OBRIGATORIA_AUSENTE,
    MSG_IDADE_TIPO_INVALIDO,
    MSG_IDADE_FORA_FAIXA,
    MSG_IDADE_MENOR_18,
    MSG_ALERTA_IDADE_ACIMA_60,
    MSG_TEXTO_BASE_ALERTAS,
    MSG_TEXTO_BASE_OK,
)


def validar_idade_obrigatoria(dados_avaliacao, resultado):
    """
    Valida se o campo 'idade' está presente.
    
    Args:
        dados_avaliacao (dict): Dados da avaliação
        resultado (dict): Dicionário de resultado para preenchimento
    
    Returns:
        bool: True se válido, False caso contrário
    """
    if "idade" not in dados_avaliacao:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append(MSG_IDADE_OBRIGATORIA_AUSENTE)
        resultado["codigos"].append(IDADE_OBRIGATORIA_AUSENTE)
        return False
    return True


def validar_tipo_idade(dados_avaliacao, resultado):
    """
    Valida se o campo 'idade' é do tipo numérico.
    
    Args:
        dados_avaliacao (dict): Dados da avaliação
        resultado (dict): Dicionário de resultado para preenchimento
    
    Returns:
        bool: True se válido, False caso contrário
    """
    idade = dados_avaliacao.get("idade")
    if not isinstance(idade, (int, float)):
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append(MSG_IDADE_TIPO_INVALIDO)
        resultado["codigos"].append(IDADE_TIPO_INVALIDO)
        return False
    return True


def validar_faixa_idade(dados_avaliacao, resultado):
    """
    Valida se o campo 'idade' está na faixa válida (0 a 120).
    
    Args:
        dados_avaliacao (dict): Dados da avaliação
        resultado (dict): Dicionário de resultado para preenchimento
    
    Returns:
        bool: True se válido, False caso contrário
    """
    idade = dados_avaliacao.get("idade")
    if idade < 0 or idade > 120:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append(MSG_IDADE_FORA_FAIXA)
        resultado["codigos"].append(IDADE_FORA_FAIXA)
        return False
    return True


def aplicar_exclusao_idade_minima(dados_avaliacao, resultado):
    """
    Aplica regra de exclusão para idade menor que 18 anos.
    
    Args:
        dados_avaliacao (dict): Dados da avaliação
        resultado (dict): Dicionário de resultado para preenchimento
    
    Returns:
        bool: True se válido, False caso contrário
    """
    if dados_avaliacao.get("idade") < 18:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append(MSG_IDADE_MENOR_18)
        resultado["codigos"].append(IDADE_MENOR_18)
        return False
    return True


def aplicar_alerta_idade_alta(dados_avaliacao, resultado):
    """
    Aplica alerta para idade acima de 60 anos.
    
    Args:
        dados_avaliacao (dict): Dados da avaliação
        resultado (dict): Dicionário de resultado para preenchimento
    """
    if dados_avaliacao.get("idade") > 60:
        resultado["alertas"].append(MSG_ALERTA_IDADE_ACIMA_60)
        resultado["codigos_alerta"].append(IDADE_ACIMA_60)


def avaliar_caso(dados_avaliacao):
    """
    Função central de avaliação de caso.
    Executa todas as validações e regras em sequência.
    
    Args:
        dados_avaliacao (dict): Dicionário com os dados a serem avaliados
                               Campos esperados: idade (obrigatório)
    
    Returns:
        dict: Dicionário com resultado da avaliação contendo:
            - status (str): 'ok', 'bloqueado' ou 'alerta'
            - alertas (list): Lista de mensagens de alerta
            - bloqueios (list): Lista de mensagens de bloqueio
            - codigos (list): Lista de códigos de bloqueio
            - codigos_alerta (list): Lista de códigos de alerta
            - texto_base (str): Texto resumido do resultado
    
    Example:
        >>> dados = {"idade": 25}
        >>> resultado = avaliar_caso(dados)
        >>> print(resultado["status"])
        'ok'
    """
    resultado = {
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
    resultado["texto_base"] = (
        MSG_TEXTO_BASE_ALERTAS if resultado["alertas"] else MSG_TEXTO_BASE_OK
    )

    return resultado
