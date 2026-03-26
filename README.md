# Simple TCP Port Scanner

Um verificador de portas TCP (Port Scanner) rápido e multithreaded desenvolvido em Python.

## Sobre o Projeto
Este script realiza um **TCP Connect Scan** para identificar portas abertas em um endereço IP alvo. Ele utiliza a biblioteca nativa `socket` para a conexão de rede e a biblioteca `concurrent.futures` para paralelismo (multithreading), permitindo a varredura de centenas de portas em poucos segundos de forma eficiente.

## Como Executar

1. Certifique-se de ter o Python 3 instalado em sua máquina.
2. Clone este repositório ou faça o download do arquivo `port_scanner.py`.
3. Abra o terminal e execute o script:
   ```bash
   python port_scanner.py
