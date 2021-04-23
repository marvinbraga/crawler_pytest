# coding=utf-8
"""
Model Module
"""
from dataclasses import dataclass


@dataclass
class Tibia:
    """ Classe para recupera informações no Crawler. """
    name: str
    former_name: str
    sex: str
    vocation: str
    level: str
    achievement: str
    world: str
    residence: str
    last_login: str
    account_status: str
    deaths: list
