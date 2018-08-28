#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
# App: Omnibus - InQuest Labs
# Website: https://www.inquest.net
# Author: Adam M. Swanda
# ---
# Purpose: ASCII art banners
##

import random


banners = ["""
                     The OSINT Omnibus
o               .        ___---___                    .                   
       .              .--\        --.     .     .         .
                    ./.;_.\     __/~ \.     
                   /;  / `-'  __\    . \                            
 .        .       / ,--'     / .   .;   \        |
                 | .|       /       __   |      -O-       .
                |__/    __ |  . ;   \ | . |      |
                |      /  \\_    . ;| \___|    
   .    o       |      \  .~\\___,--'     |           .
                 |     | . ; ~~~~\_    __|
    |             \    \   .  .  ; \  /_/   .
   -O-        .    \   /         . |  ~/                  .
    |    .          ~\ \   .      /  /~          o
  .                   ~--___ ; ___--~       
                 .          ---         .              
             https://github.com/InQuest/omnibus""", """

 ██████╗ ███╗   ███╗███╗   ██╗██╗██████╗ ██╗   ██╗███████╗
██╔═══██╗████╗ ████║████╗  ██║██║██╔══██╗██║   ██║██╔════╝
██║   ██║██╔████╔██║██╔██╗ ██║██║██████╔╝██║   ██║███████╗
██║   ██║██║╚██╔╝██║██║╚██╗██║██║██╔══██╗██║   ██║╚════██║
╚██████╔╝██║ ╚═╝ ██║██║ ╚████║██║██████╔╝╚██████╔╝███████║
 ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝╚═════╝  ╚═════╝ ╚══════╝
             https://github.com/InQuest/omnibus""" , """

▒█████   ███▄ ▄███▓ ███▄    █  ██▓ ▄▄▄▄    █    ██   ██████ 
▒██▒  ██▒▓██▒▀█▀ ██▒ ██ ▀█   █ ▓██▒▓█████▄  ██  ▓██▒▒██    ▒ 
▒██░  ██▒▓██    ▓██░▓██  ▀█ ██▒▒██▒▒██▒ ▄██▓██  ▒██░░ ▓██▄   
▒██   ██░▒██    ▒██ ▓██▒  ▐▌██▒░██░▒██░█▀  ▓▓█  ░██░  ▒   ██▒
░ ████▓▒░▒██▒   ░██▒▒██░   ▓██░░██░░▓█  ▀█▓▒▒█████▓ ▒██████▒▒
░ ▒░▒░▒░ ░ ▒░   ░  ░░ ▒░   ▒ ▒ ░▓  ░▒▓███▀▒░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░
  ░ ▒ ▒░ ░  ░      ░░ ░░   ░ ▒░ ▒ ░▒░▒   ░ ░░▒░ ░ ░ ░ ░▒  ░ ░
░ ░ ░ ▒  ░      ░      ░   ░ ░  ▒ ░ ░    ░  ░░░ ░ ░ ░  ░  ░  
    ░ ░         ░            ░  ░   ░         ░           ░  
                                         ░
             https://github.com/InQuest/omnibus"""]


def show_banner():
    return random.choice(banners)
