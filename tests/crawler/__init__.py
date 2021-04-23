# coding=utf-8
""" Init """
from downloader import Downloader
from proj.crawler import Crawler


class Character(Crawler):
    url = 'https://www.tibia.com/'

    def __init__(self, character):
        super().__init__(self.url, character, Downloader())
