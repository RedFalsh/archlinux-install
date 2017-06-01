
fdisk -l

cfdisk /dev/sda
	dos
	/dev/sda1  1G   linux boot
	/dev/sda2  2G   linux swap /solaris
	/dev/sda3  37G  linux
	
fdisk -l

mkfs.ext4 /dev/sda1
mkswap /dev/sda2
swapon /dev/sda2
mkfs.ext4 /dec/sda3

mount /dev/sda3 /mnt

mkdir /mnt/boot /mnt/var mnt/home

mount /dev/sda1 /mnt/boot

nano /etc/pacman.d/mirrorlist
Server = http://mirrors.aliyun.com/archlinux/$repo/os/$arch
Server = http://mirrors.163.com/archlinux/$repo/os/$arch

pacstrap /mnt base base-devel

pacman -Syu

pacstrap /mnt grub-bios

clear 

genfstab -p /mnt >> /mnt/etc/fstab

arch-chroot /mnt
 
hwclock --systohc --utc

mkinitcpio -p linux

passwd root

useradd -m -g users -G wheel -s /bin/bash john

passwd john

grub-install /dev/sda

grub-mkconfig -o /boot/grub/grub.cfg

exit

reboot

root

hostnamectl set-hostname archlinux

ip addr 

systemctl enable dhcpcd

systemctl start dhcpcd

ping www.google.com

nano /etc/sudoers

root ALL=(ALL) ALL
john ALL=(ALL) ALL

pacman -S xorg


pacman -S xterm xorg-xclock xorg-twm xorg-xinit xorg-server-utils

#这里不装也可以，直接startxfce4
pacman -S slin slim-themes archlinux-themes-slim xdg-user-dirs

pacman -S xfce4

pacman -S systemctl enable slim.service

pwd

cp /etc/X11/xinit/xinitrc ~/.xinitrc

nano .xinitrc
#twn &
#...
#...
#..
exec xfce4-session

nano 

current_theme archlinux-soft







pacman -S plasma kdebase


pacman -R plasma-mediacenter

pacman -S ttf-freefont

systemctl enable sddm


reboot



================>>>ifconfig
pacman -S net-tools dnsutils inetutils iproute2

================>>>openssh
sudo pacman -S openssh

systemctl enable sshd

systemctl start sshd

================>>>yaourt
sudo nano /etc/pacman.conf

[archlinuxcn]
SigLevel = Optional TrustedOnly
Server   =  http://repo.archlinuxcn.org/$arch

sudo pacman -Sy yaourt fakeroot


================>>>numix-themes
pacman -S numix-themes

yaourt -S numix-circle

================>>>cairo-dock




	