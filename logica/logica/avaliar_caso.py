# Função central de avaliação de caso
# Versão inicial com regras básicas separadas + códigos estruturados

def validar_idade_obrigatoria(dados_avaliacao, resultado):
    if "idade" not in dados_avaliacao:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append("Campo obrigatório 'idade' não informado.")
        resultado["codigos"].append("IDADE_OBRIGATORIA_AUSENTE")
        return False
    return True


def validar_tipo_idade(dados_avaliacao, resultado):
    idade = dados_avaliacao.get("idade")
    if not isinstance(idade, (int, float)):
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append("Campo 'idade' deve ser numérico.")
        resultado["codigos"].append("IDADE_TIPO_INVALIDO")
        return False
    return True


def validar_faixa_idade(dados_avaliacao, resultado):
    idade = dados_avaliacao.get("idade")
    if idade < 0 or idade > 120:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append("Campo 'idade' fora da faixa válida (0 a 120).")
        resultado["codigos"].append("IDADE_FORA_FAIXA")
        return False
    return True


def aplicar_exclusao_idade_minima(dados_avaliacao, resultado):
    if dados_avaliacao.get("idade") < 18:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append("Idade menor que 18 anos não permitida.")
        resultado["codigos"].append("IDADE_MENOR_18")
        return False
    return True


def aplicar_alerta_idade_alta(dados_avaliacao, resultado):
    if dados_avaliacao.get("idade") > 60:
        resultado["alertas"].append(
            "Paciente com idade acima de 60 anos. Avaliar com cautela."
        )


def avaliar_caso(dados_avaliacao):
    resultado = {
        "status": "ok",
        "alertas": [],
        "bloqueios": [],
        "codigos": [],
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
