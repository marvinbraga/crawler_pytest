# coding=utf-8
"""
Utils
"""
import unicodedata


def load_mockup(mockup_name, encoding='utf-8'):
    """ Carrega o arquivo de testes informado. """
    with open(f'tests/mockup/{mockup_name}', encoding=encoding, mode='r') as f:
        return f.read()


def normalize_text(text: str) -> str:
    """ Normaliza o texto de ASCII para UTF-8 """
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
