#!/usr/bin/env python
# encoding: utf-8

class colorprint(object):

    RED = '\033[31m'       # 红色
    GREEN = '\033[32m'     # 绿色
    YELLOW = '\033[33m'    # 黄色
    BLUE = '\033[34m'      # 蓝色
    FUCHSIA = '\033[35m'   # 紫红色
    CYAN = '\033[36m'      # 青蓝色
    WHITE = '\033[37m'     # 白色

#: no color
    RESET = '\033[0m'      # 终端默认颜色

    def color_str(self, color, s):
        return '{}{}{}'.format(
            getattr(self, color),
            s,
            self.RESET
        )

    def red(self, s):
        return self.color_str('RED', s)

    def green(self, s):
        return self.color_str('GREEN', s)

    def yellow(self, s):
        return self.color_str('YELLOW', s)

    def blue(self, s):
        return self.color_str('BLUE', s)

    def fuchsia(self, s):
        return self.color_str('FUCHSIA', s)

    def cyan(self, s):
        return self.color_str('CYAN', s)

    def white(self, s):
        return self.color_str('WHITE', s)


import os
import time
clr = colorprint()
class python:
    def __init__(self):
        self.pip_pkg = [
        'pyflakes',
        'pylint',
        'pep8',
        'pyserial',
        'matplotlib',
        'PyQt5',
        ]

    def pip_install(self):
        os.system('rm log')
        for pkg in self.pip_pkg:
            str_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            cmd = ('pip3 install %s'%pkg)
            print(clr.green('pip3 install %s'%pkg))
            result = os.popen('pip3 install %s'%pkg).read()
            print(result)
            with open('log','a') as f:
                f.write('%s : %s \n'%(str_time,cmd))
                f.write(result)
                f.write('\n\n\n')


if __name__ == "__main__":
   p = python()
   p.pip_install()




