#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

class color:
    def link(string):
        return f'\033[0m\033[03;04;38;05;105m{str(string)}\033[0m'

    def success(string):
        return f'\033[0m\033[01;38;05;46m{str(string)}\033[0m'

    def error(string):
        return f'\033[0m\033[38;05;196m{str(string)}\033[0m'

    def attention(string):
        return f'\033[0m\033[01;38;05;229;48;05;196m{str(string)}\033[0m'

    def warning(string):
        return f'\033[0m\033[03;38;05;222m{str(string)}\033[0m'

    def comment(string):
        return f'\033[0m\033[01;03;38;05;68m{str(string)}\033[0m'

    def orange(string):
        return f'\033[0m\033[01;38;05;178m{str(string)}\033[0m'

    def skin(string):
        return f'\033[0m\033[01;38;05;222m{str(string)}\033[0m'

    def green_bg(string):
        return f'\033[0m\033[48;05;22m{str(string)}\033[0m'

    def italic(string):
        return f'\033[0m\033[03m{str(string)}\033[0m'

    def text(string):
        return f'\033[0m\033[03;38;05;213m{str(string)}\033[0m'

    def cyan(string):
        return f'\033[0m\033[38;05;51m{str(string)}\033[0m'

    def green(string):
        return f'\033[0m\033[38;05;46m{str(string)}\033[0m'

    rm_row = '\033[A                                                                                          \033[A'


if __name__ == '__main__':
    for key, value in color.__dict__.items():
        if callable(value):
            print(value(key))
