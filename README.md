![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# 🧾 Escalonador de Processos
Esse projeto simula um escalonador de processos para sistemas operacionais. Implementa diversos algoritmos de escalonamento, permitindo analisar e calcular o turnaround.

## 👨‍💻 Algoritmos Implementados
- SJF (Shortest Job First): executa o processo com menor tempo de execução.
- FIFO (First in - First Out): executa o processo que chegou em primeiro lugar.
- RR (Roundrobin): executa o processo de acordo com um quantum de tempo.

## 📩 Como Executar
1. Clone o repositório:
```bash
git clone https://github.com/khrisla/calculator-timewaiting-and-turnaround

cd calculator-timewaiting-and-turnaround
```

## 💻 Tecnologias Utilizadas
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### 📲 Como instalar 
#### Windows:
1. Acesse o site oficial e baixe o arquivo Python: https://www.python.org/downloads/
2. Execute o arquivo baixado
3. Abra o prompt de comando (CMD) ou PowerShell:
```bash
python --v
```
#### Linux
O python ja vem instalado no próprio sistema, basta executar na linha de comando.
```bash
Python3 main.py
```
### ↘ Exemplo de Entrada
```bash
-------------------------------------------------------------------
🔷 Olá! Bem-vindo ao calculador de tempo de espera e turnaround.🔷 
-------------------------------------------------------------------
💠 Qual o tamanho do 1º processo? 
➡ 10
💠 Qual o tamanho do 2º processo? 
➡ 5
💠 Qual o tamanho do 3º processo? 
➡ 12
💠 Qual o tamanho do 4º processo? 
➡ 3
💠 Qual o tamanho do 5º processo? 
➡ 7
-------------------------
```

### ↙ Exemplo de Saída
```bash
*️⃣  Resultados:
-------------------------------------------------------------------
 Processo  | T. Execução  | T. Espera  |    Turnaround
-------------------------------------------------------------------
    1      |      10      |     0      |        10
    2      |      5       |     10     |        15
    3      |      12      |     15     |        27
    4      |      3       |     27     |        30
    5      |      7       |     30     |        37
-------------------------------------------------------------------
  MÉDIA    |      -       |   16.40    |       23.80
-------------------------------------------------------------------
```
## Licença
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## 👥 Contribuintes

- [@eumarianamota](https://github.com/eumarianamota) 
- [@khrisla](https://github.com/khrisla)
- [@wilkneves](https://github.com/wilkneves)