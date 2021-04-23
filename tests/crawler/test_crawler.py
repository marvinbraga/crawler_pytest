# coding=utf-8
"""
Teste de Crawler
"""
import pytest
from unittest import mock

from core.utils import load_mockup
from proj.crawler import Crawler


@pytest.fixture
def resume_html():
    """ Utiliza o Moc com o resume.html """
    return load_mockup('resume.html')


@mock.patch('downloader.Downloader')
def test_search_character(downloader_mock, snapshot, resume_html):
    """ Teste de busca """
    url = 'https://www.tibia.com/'
    character = 'Bobeek'
    downloader = downloader_mock.return_value
    downloader.post.return_value = mock.Mock(text=resume_html)
    crawler = Crawler(url, character, downloader)
    snapshot.assert_match(crawler.get_url_information(character).__dict__)
