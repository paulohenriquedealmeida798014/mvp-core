# Função central de avaliação de caso
# Versão inicial com primeira regra simples

def avaliar_caso(dados_avaliacao):
    resultado = {
        "status": "ok",
        "alertas": [],
        "bloqueios": [],
        "texto_base": ""
    }

    # Regra 1: campo obrigatório "idade"
    if "idade" not in dados_avaliacao:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append("Campo obrigatório 'idade' não informado.")
        return resultado

        # Regra 2: critério de exclusão simples - menor de 18 anos
    if dados_avaliacao.get("idade") < 18:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append("Idade menor que 18 anos não permitida.")
        return resultado


    # TODO: outras validações obrigatórias
    # TODO: critérios de exclusão
    # TODO: gerar alertas
    # TODO: montar texto base

    resultado["texto_base"] = "Avaliação básica concluída com sucesso."

    return resultado
