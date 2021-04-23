# coding=utf-8
"""
Module Test Parser
"""
import pytest

from core.utils import load_mockup
from proj.parser import Parser
from bs4 import BeautifulSoup


@pytest.fixture
def resume_html():
    """ Retorna o Mock com dados. """
    return load_mockup('resume.html')


@pytest.fixture
def not_found_html():
    """ Retorna o Mock sem dados. """
    return load_mockup('not_found.html')


def test_extract_name(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, 'html.parser')
    text = Parser().extract_value(parsed, 'Name:')
    snapshot.assert_match(text)


def test_extract_former_name(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, 'html.parser')
    text = Parser().extract_value(parsed, 'Former Names:')
    snapshot.assert_match(text)


def test_extract_sex(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, 'html.parser')
    text = Parser().extract_value(parsed, 'Sex:')
    snapshot.assert_match(text)


def test_extract_vocation(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, 'html.parser')
    text = Parser().extract_value(parsed, 'Vocation:')
    snapshot.assert_match(text)


def test_extract_level(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, 'html.parser')
    text = Parser().extract_value(parsed, 'Level:')
    snapshot.assert_match(text)


def test_extract_achievement(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, 'html.parser')
    text = Parser().extract_value(parsed, 'Achievement Points:')
    snapshot.assert_match(text)


def test_extract_world(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, 'html.parser')
    text = Parser().extract_value(parsed, 'World:')
    snapshot.assert_match(text)


def test_extract_residence(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, 'html.parser')
    text = Parser().extract_value(parsed, 'Residence:')
    snapshot.assert_match(text)


def test_extract_last_login(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, 'html.parser')
    # Usou método específico.
    text = Parser().extract_last_login(parsed, 'Last Login:')
    snapshot.assert_match(text)


def test_extract_account_status(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, 'html.parser')
    text = Parser().extract_value(parsed, 'Account Status:')
    snapshot.assert_match(text)


def test_extract_deaths(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, 'html.parser')
    deaths = Parser().extract_deaths(parsed)
    for death in deaths:
        snapshot.assert_match(death)


def test_not_found(snapshot, not_found_html):
    confirmation = Parser().character_not_found(not_found_html)
    assert not confirmation
