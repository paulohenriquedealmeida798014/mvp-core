# Função central de avaliação de caso
# Versão inicial com primeira regra simples

def validar_idade_obrigatoria(dados_avaliacao, resultado):

    def aplicar_exclusao_idade_minima(dados_avaliacao, resultado):
    if dados_avaliacao.get("idade") < 18:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append("Idade menor que 18 anos não permitida.")
        return False
    return True

    if "idade" not in dados_avaliacao:
        resultado["status"] = "bloqueado"
        resultado["bloqueios"].append("Campo obrigatório 'idade' não informado.")
        return False
    return True

def avaliar_caso(dados_avaliacao):
    resultado = {
        "status": "ok",
        "alertas": [],
        "bloqueios": [],
        "texto_base": ""
    }

   if not validar_idade_obrigatoria(dados_avaliacao, resultado):
        return resultado

        if not aplicar_exclusao_idade_minima(dados_avaliacao, resultado):
        return resultado


        # Regra 3: alerta simples - idade maior que 60 anos
    if dados_avaliacao.get("idade") > 60:
        resultado["alertas"].append("Paciente com idade acima de 60 anos. Avaliar com cautela.")


       if len(resultado["alertas"]) > 0:
        resultado["texto_base"] = "Avaliação concluída com alertas. Verifique os pontos de atenção."
    else:
        resultado["texto_base"] = "Avaliação concluída sem alertas."

    

    return resultado
