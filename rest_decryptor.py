#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import base64
from b24_start.color import color as c
from simple_term_menu import TerminalMenu
import hashlib
from getpass import getpass as gp


def decrypt(p=False):
    res = bytearray()
    if not p:
        p = gp(prompt=c.text('Password: '), stream=None)
        print(c.rm_row)
    key = bytearray(p.encode('ascii'))
    key1 = hashlib.md5(key).digest()
    with open('bitrix.json.enc', 'r') as config_enc:
        encrypted_file = bytearray(base64.standard_b64decode(config_enc.read()))
    while len(encrypted_file) > 0:
        m = encrypted_file[:16]
        encrypted_file = encrypted_file[16:]
        for i in range(len(m)):
            m[i] = m[i] ^ key1[i]
        res.extend(m)
        tempkey = bytearray()
        tempkey.extend(key)
        tempkey.extend(key1)
        tempkey.extend(m)
        key1 = hashlib.md5(tempkey).digest()
    try:
        res = res.decode('utf-8')
        print(c.success('верный пароль!'))
    except UnicodeDecodeError:
        print(c.error('неверный пароль!'))
    return res


def encrypt():
    p = gp(prompt=c.text('Password: '), stream=None)
    print(c.rm_row)
    res = bytearray()
    key = bytearray(p.encode('ascii'))
    key1 = hashlib.md5(key).digest()
    with open('bitrix.json', 'rb') as config_json:
        encrypted_file = bytearray(config_json.read())
    while len(encrypted_file) > 0:
        m = encrypted_file[:16]
        encrypted_file = encrypted_file[16:]
        tempkey = bytearray()
        tempkey.extend(key)
        tempkey.extend(key1)
        tempkey.extend(m)
        for i in range(len(m)):
            m[i] = m[i] ^ key1[i]
        res.extend(m)
        key1 = hashlib.md5(tempkey).digest()
    with open('bitrix.json.enc', 'w') as config_json:
        config_json.write(base64.standard_b64encode(res).decode('ascii'))
    print(c.success('Done!'))


if __name__ == '__main__':
    options = ['encrypt bitrix.json', 'decrypt bitrix.json.enc']
    menu = TerminalMenu(options, skip_empty_entries=True)
    i = menu.show()
    if i == 0:
        encrypt()
    else:
        with open('bitrix.json', 'w') as config_json:
            config_json.write(decrypt())
