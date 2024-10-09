# -*- coding: utf-8 -*-
# Created by Nicolae Gaidarji at 20.06.2022
import logging
import re
import requests
import sys
from CONSTANT import *


logger = logging.getLogger(__name__)


def format_text_new_line(p_text, p_width=31):
    # v_text = p_text.decode('cp1251', 'replace')
    v_text = p_text.decode()
    v_text = v_text.replace('ii: ', ': \n')

    v_step = 0
    v_counter = 0
    v_text2 = ''
    v_text_temp = ''

    for row in v_text:
        v_step += 1
        v_counter += 1

        v_text_temp = v_text_temp + row
        if len(v_text_temp) == p_width and row == ' ':
            v_step = 0
            v_text2 = v_text2 + v_text_temp + '\n'
            v_text_temp = ''
        if row == '\n':
            v_step = 0
            v_text2 = v_text2 + v_text_temp
            v_text_temp = ''
        if len(v_text_temp) == p_width and row != ' ':
            v_pos_space = v_text_temp.rfind(' ')
            v_text2 = v_text2 + v_text_temp[:v_pos_space] + '\n'
            v_text_temp = v_text_temp[v_pos_space+1:]
            v_step = 0

    return v_text2


def create_nonfiscal_check(p_text):
    v_return = '38\n42,\n42,\n42,'
    p_text = p_text.replace('\n', '\n42,')

    v_return = v_return + p_text + '\n39'
    return v_return


def convert_char_rom(p_text):
    v_result = p_text.replace(b'\xc8\x9a', b'T')
    v_result = v_result.replace(b'\xc3\xa2', b'i')
    v_result = v_result.replace(b'\xc4\x83', b'a')
    v_result = v_result.replace(b'\xc8\x9b', b't')
    v_result = v_result.replace(b'\xc8\x99', b's')
    v_result = v_result.replace(b'\xc3\xae', b'i')
    v_result = v_result.replace(b'\xe2\x80\x9e', b'"')
    v_result = v_result.replace(b'\xe2\x80\x9d', b'"')

    return v_result


class Iqos:
    def __init__(self, p_url):
        logger.info('Init class Iqos')
        self.iqos_url = p_url

    def get_check(self):
        logger.info('get check')
        v_res = requests.get(self.iqos_url)

        v_text = v_res.text.encode('UTF-8')
        v_text = v_text.replace(b'\r', b'')
        v_text = convert_char_rom(v_text)
        v_text = format_text_new_line(v_text)
        v_text = create_nonfiscal_check(v_text)

        logger.info('return: \n{v_text}'.format(v_text=v_text))
        return v_text
