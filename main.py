# coding=utf-8
"""
Módulo de Crawler
"""
import argparse
from importlib import import_module


def main():
    module = _import_module()
    parsed = _get_flag()
    return module.Character(parsed.name)


def _import_module():
    return import_module('proj')


def _get_flag():
    parser = argparse.ArgumentParser(description='Chamando Crawler')
    sub_parser = parser.add_subparsers()
    crawler = sub_parser.add_parser('crawler')
    crawler.add_argument('--name', help='Nome do personagem do Tibia')

    return parser.parse_args()


if __name__ == '__main__':
    main()
