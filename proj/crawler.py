# coding=utf-8
"""
Crawler Module
"""
import json
from urllib.parse import urljoin

from proj.parser import Parser


class Crawler:
    """ Classe para crawler. """

    def __init__(self, url, character, downloader):
        self.downloader = downloader
        self.url = url
        self.parser = Parser()
        self.get_url_information(character)

    def get_url_information(self, character):
        """ Monta a URL para recuperar as informações.  """
        url = urljoin(self.url, 'community/?subtopic=characters')
        params = self.config_params(character)
        response = self.downloader.post(url, data=params)

        if self.parser.character_not_found(response.text):
            parsed = self.parser.parse(response.text)
            self.save_data(parsed.__dict__)
            return parsed

    @staticmethod
    def config_params(character):
        """ Cria dicionário para guardar informações do submit. """
        return {'name': character, 'x': 0, 'y': 0}

    @staticmethod
    def save_data(data):
        """ Salva informações coletadas em arquivo json. """
        name = data.get('name').lower().replace(' ', '_')
        with open(f'./proj/database/{name}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f)
            print(f'Personagem {name} foi salvo com sucesso!')
