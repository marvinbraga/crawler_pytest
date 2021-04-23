# coding=utf-8
"""
Downloader module
"""
import requests


class Downloader:
    """ Classe para gerenciar o download. """
    def __init__(self):
        self.session = requests.Session()

    def get(self, url, params=None, cookies=None):
        """ Executa o GET de um site. """
        response = self.session.get(url, params=params, verify=False, cookies=cookies)
        response.raise_for_status()
        return response

    def post(self, url, data=None):
        """ Executa o POST de um site. """
        response = self.session.post(url, data=data, verify=False)
        response.raise_for_status()
        return response

    def close(self):
        """ Fecha a seção do request. """
        self.session.close()
