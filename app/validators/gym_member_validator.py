import re
from fastapi import HTTPException, status

class GymMemberValidators:
    @staticmethod
    def validate_name_format(name: str) -> str:
        if not name.replace(" ", "").isalpha():
            raise ValueError("O nome deve conter apenas letras e espaço.")
        return name.title()

    @staticmethod
    def validate_cpf_format(cpf: str) -> str:
        cpf_digits = re.sub(r'\D', '', cpf)
        if len(cpf_digits) != 11:
            raise ValueError("CPF inválido")
        return cpf_digits

    @staticmethod
    def validate_phone_format(phone: str) -> str:
        phone_digits = re.sub(r'\D', '', phone)
        if len(phone_digits) != 11:
            raise ValueError("Celular inválido")
        return phone_digits
