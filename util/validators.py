import re
from datetime import date
from typing import Any, Optional


def is_in_range(
    field_value: int | float,
    field_label: str,
    low: int | float,
    high: int | float
) -> str:
    field_value = float(field_value)
    if low <= field_value <= high:
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> deve estar entre {low} e {high}."


def is_not_none(field_value: Any, field_label: str) -> str:
    if field_value is not None:
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> não pode ser nulo."


def is_not_empty(field_value: str, field_label: str) -> str:
    if field_value.strip() != "":
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> não pode ser vazio."


def is_integer(field_value: str, field_label: str) -> str:
    try:
        int(field_value)
        return ""
    except ValueError:
        return f"O valor do campo <b>{field_label}</b> deve ser um número inteiro."


def is_float(field_value: str, field_label: str) -> str:
    try:
        float(field_value)
        return ""
    except ValueError:
        return f"O valor do campo <b>{field_label}</b> deve ser um número decimal válido."


def is_size_between(
    field_value: str,
    field_label: str,
    min_size: int,
    max_size: int
) -> str:
    if min_size <= len(field_value) <= max_size:
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> deve ter entre {min_size} e {max_size} caracteres."


def is_max_size(
    field_value: str, field_label: str, max_size: int) -> str:
    if len(field_value) <= max_size:
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> deve ter no máximo {max_size} caracteres."


def is_min_size(
    field_value: str, field_label: str, min_size: int) -> str:
    if len(field_value) >= min_size:
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> deve ter no mínimo {min_size} caracteres."


def is_matching_regex(
    field_value: str, field_label: str, regex: str) -> str:
    if re.match(regex, field_value) is not None:
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> está com o formato incorreto."


def is_email(field_value: str, field_label: str) -> str:
    if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", field_value) is not None:
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> deve ser um e-mail com formato válido."


def is_cpf(field_value: str, field_label: str) -> str:
    if re.match(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", field_value) is not None:
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> deve ser um CPF válido."


def is_cnpj(field_value: str, field_label: str) -> str:
    if re.match(r"^\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}$", field_value) is not None:
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> deve ser um CNPJ válido."


def is_phone_number(
    field_value: str, field_label: str) -> str:
    if re.match(r"^\(\d{2}\) \d{5}-\d{4}$", field_value) is not None:
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> deve ser um telefone no formato (99) 99999-9999."


def is_cep(field_value: str, field_label: str) -> str:
    if re.match(r"^\d{5}-\d{3}$", field_value) is not None:
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> deve ser um CEP válido."


def is_person_name(
    field_value: str, field_label: str) -> str:
    if re.match(r"^[a-zA-ZÀ-ú']{2,40}$", field_value) is not None:
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> deve ser um nome válido."


def is_person_fullname(
    field_value: str, field_label: str) -> str:
    if (
        re.match(r"^[a-zA-ZÀ-ú']{2,40}(?:\s[a-zA-ZÀ-ú']{2,40})+$", field_value)
        is not None
    ):
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> deve ser um nome completo válido."


def is_project_name(
    field_value: str, field_label: str) -> str:
    if re.match(r"^[\w]+(\s[\w]+)*$", field_value) is not None:
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> deve ser um nome válido."


def is_password(
    field_value: str, field_label: str) -> str:
    """
    Tenha pelo menos um caractere minúsculo.
    Tenha pelo menos um caractere maiúsculo.
    Tenha pelo menos um dígito.
    Tenha pelo menos um caractere especial dentre os especificados (@$!%*?&).
    Tenha um comprimento de pelo menos 4 e no máximo 64 caracteres.
    """
    if (
        re.match(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$!%*?&])[A-Za-z\d@#$!%*?&]{4,64}$",
            field_value,
        )
        is not None
    ):
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> deve ser uma senha válida entre 4 e 64 caracteres, contendo pelo menos um caractere minúsculo, um maiúsculo, um dígito e um caractere especial."        


def is_matching_fields(
    field_value: str,
    field_label: str,
    matching_field_value: str,
    matching_field_label: str
) -> str:
    if field_value.strip() == matching_field_value.strip():
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> deve ser igual ao do campo {matching_field_label}."


def is_selected_id_valid(
    field_value: int, field_label: str) -> str:
    if field_value > 0:
        return ""
    else:
        return f"Selecione uma opção para o campo <b>{field_label}</b>."
    

def is_greater_than(
    field_value: int | float,
    field_label: str,
    min_value: int | float
) -> str:
    if field_value > min_value:
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> deve ser maior que {min_value}."


def is_less_than(
    field_value: int | float,
    field_label: str,
    max_value: int | float
) -> str:
    if field_value < max_value:
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> deve ser menor que {max_value}."


def is_greater_than_or_equal(
    field_value: int | float,
    field_label: str,
    min_value: int | float
) -> str:
    if field_value >= min_value:
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> deve ser maior ou igual a {min_value}."


def is_less_than_or_equal(
    field_value: int | float,
    field_label: str,
    max_value: int | float
) -> str:
    if field_value <= max_value:
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> deve ser menor ou igual a {max_value}."


def is_date_valid(
    field_value: str,
    field_label: str
) -> str:
    try:
        date.fromisoformat(field_value)
        return ""
    except ValueError:
        return f"O valor do campo <b>{field_label}</b> deve ser uma data válida no formato YYYY-MM-DD."


def is_date_between(
    field_value: date,
    field_label: str,
    min_date: date,
    max_date: date
) -> str:
    if min_date <= field_value <= max_date:
        return ""
    else:
        return f"O valor do campo <b>{field_label}</b> deve estar entre {min_date.strftime('%d/%m/%Y')} e {max_date.strftime('%d/%m/%Y')}."