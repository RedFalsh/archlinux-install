#!/usr/bin/env python
# encoding: utf-8

import os
# from colorprint import colorprint
# clr = colorprint()
# print(clr.red('ddw'))

class samba:
    def __init__(self):
        self.pkg = 'samba'
        self.user= 'john'

    def install(self):
        print('pacman -S samba')
        os.system('pacman -S samba')

    def user_share(self):
        os.system('mkdir -p /var/lib/samba/usershare')
        print('建立sambashare群组:\ngroupadd sambashare')
        os.system('groupadd sambashare')
        print('修改文件夹权限，拥有者更改为root，群组更改为sambashare:\nchown root:sambashare /var/lib/samba/usershare')
        os.system('chown root:sambashare /var/lib/samba/usershare')
        print('sambashare 群组中的用户拥有读取，写入和执行此文件夹中内容的权限：\n chmod 1770 /var/lib/samba/usershare')
        os.system('chmod 1770 /var/lib/samba/usershare')
        print('复制smb.conf配置文件：\ncp smb.conf /etc/samba/smb.conf')
        os.system('cp smb.conf /etc/samba/smb.conf')
        print('将用户添加到群组 sambashare 中:\nusermod -a -G sambashare %s'%self.user)
        os.system('usermod -a -G sambashare %s'%self.user)

    def start_service(self):
        print('开机启动服务smbd.service和nmbd.service服务')
        os.system('systemctl enable smbd.service')
        os.system('systemctl enable nmbd.service')
        print('开启smbd.service和nmbd.service服务')
        os.system('systemctl start smbd.service')
        os.system('systemctl start nmbd.service')

    def add_user(self):
        print('smbpasswd -a %s'%self.user)
        os.system('smbpasswd -a %s'%self.user)
    def change_passwd(self):
        print('smbpasswd %s'%self.user)
        os.system('smbpasswd %s'%self.user)

if __name__ == "__main__":
    s = samba()
    s.install()
    s.user_share()
    s.start_service()
    s.add_user()


