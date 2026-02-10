# Função central de avaliação de caso
# Versão inicial com regras básicas separadas + códigos estruturados via catálogo

from .codigos import (
    IDADE_OBRIGATORIA_AUSENTE,
    IDADE_TIPO_INVALIDO,
    IDADE_FORA_FAIXA,
    IDADE_MENOR_18,
    IDADE_ACIMA_60,
)

def validar_idade_obrigatoria(dados_avaliacao, resultado):
    if "idade" not in dados_avaliacao:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append("Campo obrigatório 'idade' não informado.")
        resultado["codigos"].append(IDADE_OBRIGATORIA_AUSENTE)
        return False
    return True


def validar_tipo_idade(dados_avaliacao, resultado):
    idade = dados_avaliacao.get("idade")
    if not isinstance(idade, (int, float)):
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append("Campo 'idade' deve ser numérico.")
        resultado["codigos"].append(IDADE_TIPO_INVALIDO)
        return False
    return True


def validar_faixa_idade(dados_avaliacao, resultado):
    idade = dados_avaliacao.get("idade")
    if idade < 0 or idade > 120:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append("Campo 'idade' fora da faixa válida (0 a 120).")
        resultado["codigos"].append(IDADE_FORA_FAIXA)
        return False
    return True


def aplicar_exclusao_idade_minima(dados_avaliacao, resultado):
    if dados_avaliacao.get("idade") < 18:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append("Idade menor que 18 anos não permitida.")
        resultado["codigos"].append(IDADE_MENOR_18)
        return False
    return True


def aplicar_alerta_idade_alta(dados_avaliacao, resultado):
    if dados_avaliacao.get("idade") > 60:
        resultado["alertas"].append(
            "Paciente com idade acima de 60 anos. Avaliar com cautela."
        )
        resultado["codigos_alerta"].append(IDADE_ACIMA_60)


def avaliar_caso(dados_avaliacao):
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
    if resultado["alertas"]:
        resultado["texto_base"] = (
            "Avaliação concluída com alertas. Verifique os pontos de atenção."

            # =========================
# Códigos do core de avaliação
# =========================

# --- Idade ---
IDADE_OBRIGATORIA_AUSENTE = "IDADE_OBRIGATORIA_AUSENTE"
IDADE_TIPO_INVALIDO = "IDADE_TIPO_INVALIDO"
IDADE_FORA_FAIXA = "IDADE_FORA_FAIXA"
IDADE_MENOR_18 = "IDADE_MENOR_18"
IDADE_ACIMA_60 = "IDADE_ACIMA_60"

# --- Sexo ---
SEXO_OBRIGATORIO_AUSENTE = "SEXO_OBRIGATORIO_AUSENTE"
SEXO_TIPO_INVALIDO = "SEXO_TIPO_INVALIDO"
SEXO_VALOR_INVALIDO = "SEXO_VALOR_INVALIDO"
SEXO_GESTANTE_INCONSISTENTE = "SEXO_GESTANTE_INCONSISTENTE"

# --- Gestante ---
GESTANTE_TIPO_INVALIDO = "GESTANTE_TIPO_INVALIDO"
GESTANTE_INCONSISTENTE_COM_SEXO = "GESTANTE_INCONSISTENTE_COM_SEXO"
GESTANTE_RISCO_ATIVO = "GESTANTE_RISCO_ATIVO"

# --- Comorbidades ---
COMORBIDADES_TIPO_INVALIDO = "COMORBIDADES_TIPO_INVALIDO"
COMORBIDADES_ITEM_TIPO_INVALIDO = "COMORBIDADES_ITEM_TIPO_INVALIDO"
COMORBIDADES_RISCO_PRESENTE = "COMORBIDADES_RISCO_PRESENTE"

# --- Medicações ---
MEDICACOES_TIPO_INVALIDO = "MEDICACOES_TIPO_INVALIDO"
MEDICACOES_ITEM_TIPO_INVALIDO = "MEDICACOES_ITEM_TIPO_INVALIDO"
MEDICACOES_INTERACAO_RISCO = "MEDICACOES_INTERACAO_RISCO"

# --- Fototipo ---
FOTOTIPO_OBRIGATORIO_AUSENTE = "FOTOTIPO_OBRIGATORIO_AUSENTE"
FOTOTIPO_TIPO_INVALIDO = "FOTOTIPO_TIPO_INVALIDO"
FOTOTIPO_VALOR_INVALIDO = "FOTOTIPO_VALOR_INVALIDO"
FOTOTIPO_RISCO_ELEVADO = "FOTOTIPO_RISCO_ELEVADO"

# --- Data de nascimento ---
DATA_NASCIMENTO_OBRIGATORIA_AUSENTE = "DATA_NASCIMENTO_OBRIGATORIA_AUSENTE"
DATA_NASCIMENTO_TIPO_INVALIDO = "DATA_NASCIMENTO_TIPO_INVALIDO"
DATA_NASCIMENTO_VALOR_INVALIDO = "DATA_NASCIMENTO_VALOR_INVALIDO"
DATA_NASCIMENTO_INCONSISTENTE_COM_IDADE = "DATA_NASCIMENTO_INCONSISTENTE_COM_IDADE"

        )
    else:
        resultado["texto_base"] = "Avaliação concluída sem alertas."

    return resultado
