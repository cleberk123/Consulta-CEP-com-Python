import tkinter as tk
from tkinter import font
import requests
from DB.db import DbCep
from re import sub

class ConsultaCep:

    def __init__(self):
        self.__db = DbCep()
        
    def consulta_cep(self, cep: tk.StringVar, result: tk.Label) -> bool:
        try:
            cep = cep.get()
            cep = self.retira_caractere_invalido(cep)
            cep = self.verifica_tamanho(cep, result)
            cep_formatado = self.formata_cep(cep)
        except Exception as e:
            result.configure(text=f"Erro: {e}")
            return False

        address = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        address_result = address.json()
            
        try:
            cep_verify = self.__db.query_unique_cep(address_result['cep'])
            
            if cep_verify != None:
                    result.configure(text=f"CEP: {cep_verify['cep']}\nLogradouro: {cep_verify['logradouro']}\nBairro: {cep_verify['bairro']}\nLocalidade: {cep_verify['localidade']}\nEstado: {cep_verify['uf']}")
                    return True

            if cep_verify == None:
                if 'erro' not in address_result.keys():
                    result.configure(text=f"CEP: {address_result['cep']}\nLogradouro: {address_result['logradouro']}\nBairro: {address_result['bairro']}\nLocalidade: {address_result['localidade']}\nEstado: {address_result['uf']}")

                    self.__db.insert_cep(address_result) #Retorna mensagem de sucesso
                    return True
                else:
                    result.configure(text=f"Erro: cep inválido")
                    return False
        except Exception as e:
            result.configure(text=f"Erro: {e} inválido")
            return False

    def formata_cep(self, cep: str) -> str:
        cep = f"{cep[0:5]}-{cep[5:8]}"
        return cep

    def retira_caractere_invalido(self, cep: str) -> str:
        cep = sub(r'\D', '', cep) #retira tudo o que não for número
        return cep

    def verifica_tamanho(self, cep: str, result: tk.Label):
        if len(cep) != 8:
            result.configure(text="CEP difere de 8 dígitos. Tente novamente!")
            return
        else:
            return cep