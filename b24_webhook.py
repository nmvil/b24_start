import json
from b24_start.color import color as c
import b24_start.rest_decryptor as d
import re
from simple_term_menu import TerminalMenu


def wh_from_json(j):
    webhooks = j['webhook']
    options = list(webhooks)
    menu = TerminalMenu(options, skip_empty_entries=True)
    i = menu.show()
    webhook = webhooks[options[i]]
    mes = re.findall(r'//[-a-z0-9.]+/', webhook)
    print(c.link('{}'.format(mes[0][2:-1])))
    return webhook


def get():
    try:
        config_json = open('bitrix.json', 'rb')
        print(c.success('нашёл bitrix.json'))
        webhook = wh_from_json(json.load(config_json))
        config_json.close()
        return webhook
    except FileNotFoundError:
        print(c.error('bitrix.json не нашел'))
        webhook = wh_from_json(json.loads(d.decrypt()))
        return webhook
