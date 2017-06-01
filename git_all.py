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


clr = colorprint()
import os
import time
import sys, getopt
class git:
    github_py_pkg = [
        'picture',
        'qtawesome',
            ]
    github_username = 'RedFalsh'

    coding_py_pkg = [
        'PyQt5_stylesheets',
        'qtawesome',
        'nt2000_in',
        'PersonalDose',
    ]
    py_install_pkg = [
        'PyQt5_stylesheets',
        'qtawesome',
    ]
    coding_username = 'xiongbigboss'

    def __init__(self):
        self.username = os.popen("who | awk '{print $1}'").readlines()[0].replace('\n','')
        self.git_dir = ('/home/%s/git'%self.username)

    def mkdir(self):
        if not os.path.exists(self.git_dir):
            os.system('sudo mkdir -p %s'%self.git_dir)

    def rmkdir(self):
        for dir in self.coding_py_pkg:
            print('%s/%s'%(self.git_dir,dir))
            os.system('sudo rm -r %s/%s'%(self.git_dir,dir))


    def git_github(self):
        for py in self.github_py_pkg:
            print(clr.green('git clone git@github.com:%s/%s.git %s/%s'%(self.github_username,py,self.git_dir,py)))
            os.system('git clone git@github.com:%s/%s.git %s/%s'%(self.github_username,py,self.git_dir,py))
            time.sleep(0.5)

    def git_coding(self):
        for py in self.coding_py_pkg:
            print(clr.green('git clone git@git.coding.net:%s/%s.git %s/%s'%(self.coding_username,py,self.git_dir,py)))
            os.system('git clone git@git.coding.net:%s/%s.git %s/%s'%(self.coding_username,py,self.git_dir,py))
            time.sleep(0.5)

    def install(self):
        for setup in self.py_install_pkg:
            os.chdir('%s/%s'%(self.git_dir,setup))
            print(clr.green(os.getcwd()))
            os.system('sudo python setup.py install')

    def help(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:], "hrmgci", ["help", "remove","mkdir","github","coding","install"])
        except getopt.GetoptError:
            print('error')
        for o, a in opts:
            if o in ("-h", "--help"):
                print('\t%-20s%s'%('-h or --help','show the help information'))
                print('\t%-20s%s'%('-r or --remove','remove all dir'))
                print('\t%-20s%s'%('-m or --mkdir','mkdir /home/username/git'))
                print('\t%-20s%s'%('-g or --github','git from github'))
                print('\t%-20s%s'%('-c or --coding','git from coding'))
                print('\t%-20s%s'%('-i or --install','install python package'))
                sys.exit()
            if o in ("-r", "--remove"):
                self.rmkdir()
            if o in ("-m", "--mkdir"):
                self.mkdir()
            if o in ("-g", "--github"):
                self.mkdir()
                self.git_github()
            if o in ("-c", "--coding"):
                self.mkdir()
                self.git_coding()
            if o in ("-i", "--install"):
                self.install()

if __name__ == "__main__":
    g = git()
    g.help()
