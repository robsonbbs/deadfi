# Dead-FI

Ferramenta criada como prova de conceito de vulnerabilidade em roteadores que usam o MAC Adress como senha padrão

## Como executar esse script
  1 - Instale o scapy (apt-get install python-scapy) 
                                                    
  2 - Coloque a interface wifi em modo monitor
      (airmon-ng start nomedainterface)
      
  3 - Dê permissão (chmod +x) para o arquivo deadfi.py
  
  4 - Execute a linha de comando:
     ./deadfi.py interface_criada_pelo_airmon

