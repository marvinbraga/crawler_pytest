# coding=utf-8
"""
Parser Module
"""
import re

from bs4 import BeautifulSoup

from core.utils import normalize_text
from model import Tibia


class Parser:
    """ Parser de HTML para o site Tibia. """
    ACCOUNT_STATUS_REGEX = r'(Account\sStatus\:)'

    def parse(self, html):
        """ Método de execução do parser. """
        parsed = BeautifulSoup(html, 'html.parser')
        return Tibia(
            name=self.extract_value(parsed, 'Name:'),
            former_name=self.extract_value(parsed, 'Former Names:'),
            sex=self.extract_value(parsed, 'Sex:'),
            vocation=self.extract_value(parsed, 'Vocation:'),
            level=self.extract_value(parsed, 'Level:'),
            achievement=self.extract_value(parsed, 'Achievement Points:'),
            world=self.extract_value(parsed, 'World:'),
            residence=self.extract_value(parsed, 'Residence:'),
            # Usou método específico.
            last_login=self.extract_last_login(parsed, 'Last Login:'),
            # Usou método específico.
            account_status=self.extract_account_status(parsed),
            deaths=self.extract_deaths(parsed),
        )

    @staticmethod
    def character_not_found(html):
        """ Verificar se nã existe informação. """
        parsed = BeautifulSoup(html, 'html.parser')
        result = parsed.find(string=re.compile(r'(does\snot\sexist.)'))
        return not bool(result)

    @staticmethod
    def _get_information(result):
        """ Recupera a informação padrão do HTML. """
        if result:
            return result.find_next('td').text.strip()

    def extract_value(self, html, value):
        """ Recupera o valor do HTML. """
        result = html.find('td', string=value)
        return self._get_information(result)

    def extract_last_login(self, html, value):
        """ Recupera o valor do HTML. """
        result = html.find('td', string=value)
        return normalize_text(self._get_information(result))

    def extract_account_status(self, html):
        """ Recupera o valor do HTML. """
        result = html.find('td', string=re.compile(self.ACCOUNT_STATUS_REGEX))
        return self._get_information(result)

    @staticmethod
    def extract_deaths(html):
        """ Recupera a informação """
        text = html.find('b', string='Character Deaths')
        result = []
        if text:
            rows = text.find_all_next('tr')
            for item in rows:
                if item.text == 'Account Information':
                    break
                # Recupera o 1o. TD dentro da TR
                timestamp = normalize_text(item.select_one('td:nth-of-type(1)').text.strip())
                # Recupera o 2o. TD dentro da TR
                description = normalize_text(item.select_one('td:nth-of-type(2)').text.strip())
                result.append({'timestamp': timestamp, 'description': description})

        return result
