# Função central de avaliação de caso
# Versão inicial com regras básicas separadas

def validar_idade_obrigatoria(dados_avaliacao, resultado):
    if "idade" not in dados_avaliacao:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append("Campo obrigatório 'idade' não informado.")
        return False
    return True


def aplicar_exclusao_idade_minima(dados_avaliacao, resultado):
    if dados_avaliacao.get("idade") < 18:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append("Idade menor que 18 anos não permitida.")
        return False
    return True


def avaliar_caso(dados_avaliacao):
    resultado = {
        "status": "ok",
        "alertas": [],
        "bloqueios": [],
        "texto_base": ""
    }

    # Validação obrigatória
    if not validar_idade_obrigatoria(dados_avaliacao, resultado):
        return resultado

    # Regra de exclusão
    if not aplicar_exclusao_idade_minima(dados_avaliacao, resultado):
        return resultado

    # Regra 3: alerta simples - idade maior que 60 anos
    if dados_avaliacao.get("idade") > 60:
        resultado["alertas"].append("Paciente com idade acima de 60 anos. Avaliar com cautela.")

    # Texto final baseado em alertas
    if len(resultado["alertas"]) > 0:
        resultado["texto_base"] = "Avaliação concluída com alertas. Verifique os pontos de atenção."
    else:
        resultado["texto_base"] = "Avaliação concluída sem alertas."

    return resultado
