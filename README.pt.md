[🇬🇧] [Read in English](README.md)

# Turing-py

Um simulador simples e extensível de **Máquina de Turing escrito em Python**, desenvolvido para aprendizado, experimentação e fins educacionais.

[![PyPI](https://img.shields.io/pypi/v/turing-py)](https://pypi.org/project/turing-py/)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Licença: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Instale diretamente a partir do **Python Package Index (PyPI)**:

```bash
pip install turing-py
```

---

## 📚 Sobre

Uma **Máquina de Turing** é um modelo computacional abstrato introduzido por **Alan Turing** em 1936. Ela é amplamente utilizada na ciência da computação para estudar os limites da computação e o projeto de algoritmos.

O **turing-py** fornece uma implementação em Python que permite:

* Simulação de Máquinas de Turing
* Criação de regras de transição personalizadas
* Execução passo a passo
* Experimentação com algoritmos teóricos

Este projeto é destinado a:

* Estudantes de Ciência da Computação
* Disciplinas de Teoria da Computação
* Desenvolvedores interessados em modelos computacionais
* Demonstrações educacionais

---

## 📦 Instalação

Instale usando **pip**:

```bash
pip install turing-py
```

Ou instale a partir do código-fonte:

```bash
git clone https://github.com/ericshantos/turing-py.git
cd turing-py
pip install .
```

---

## ✨ Funcionalidades

* Simulação de Máquina de Turing determinística
* Entrada de fita personalizável
* Estados e transições configuráveis
* Execução passo a passo
* Arquitetura Python simples e modular
* Fácil de estender e modificar
* Estrutura preparada para CLI

---

## 📂 Estrutura do Projeto

```
turing-py/
│
├── pyproject.toml
├── README.md
├── LICENSE
├── .gitignore
│
├── src/
    └── tmpy/
        ├── __init__.py
        │
        ├── machine/
        │   ├── __init__.py
        │   ├── turing_machine.py
        │   ├── tape.py
        │   └── states.py
        │
        ├── alphabet/
        │   ├── __init__.py
        │   ├── symbol.py
        │   ├── alphabet.py
        │   └── tape_alphabet.py
        │
        └─ transition/
            ├── __init__.py
            ├── transition.py
            ├── transition_function.py
            └── direction.py
```

---

## 🧪 Exemplos de Máquinas de Turing

Exemplos que podem ser implementados usando **turing-py**:

* Máquina de incremento binário
* Verificador de palíndromo
* Adição unária
* Verificador de paridade (par/ímpar) em binário
* Máquina de cópia de strings

---

## 🧩 Como Funciona

Uma Máquina de Turing é composta por:

* **Fita (Tape)** – memória infinita dividida em células
* **Cabeçote (Head)** – lê e escreve símbolos na fita
* **Estados (States)** – estados de configuração da máquina
* **Função de Transição (Transition Function)** – regras que determinam a próxima ação

Cada passo segue a seguinte regra:

```
(Estado Atual, Símbolo Lido) → (Próximo Estado, Símbolo Escrito, Direção do Movimento)
```

Onde a direção pode ser:

* `L` → mover para a esquerda
* `R` → mover para a direita

---

## 🤝 Contribuindo

Contribuições são bem-vindas!

Para contribuir:

1. Faça um fork do repositório
2. Crie uma nova branch

```bash
git checkout -b feature/minha-feature
```

3. Faça suas alterações
4. Faça o commit das mudanças

```bash
git commit -m "Adiciona nova funcionalidade"
```

5. Envie para o seu fork

```bash
git push origin feature/minha-feature
```

6. Abra um Pull Request

---

## 📜 Licença

Este projeto está licenciado sob a **Licença MIT**.

---

## 👨‍💻 Autor

Desenvolvido por **Eric Santos**.