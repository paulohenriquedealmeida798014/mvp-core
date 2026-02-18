# Schema declarativo dos campos estruturais do MVP

SCHEMA_CAMPOS = {
    "idade": {
        "obrigatorio": True,
        "tipo": (int, float),
        "min": 0,
        "max": 120,
    },
    "sexo": {
        "obrigatorio": True,
        "tipo": str,
        "valores_permitidos": {"masculino", "feminino", "outro", "desconhecido"},
    },
}
