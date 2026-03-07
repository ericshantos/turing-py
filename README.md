[🇧🇷] [Lê em português](README.pt.md)

# Turing-py

A simple and extensible **Turing Machine simulator written in Python**, designed for learning, experimentation, and educational purposes.

[![PyPI](https://img.shields.io/pypi/v/turing-py)](https://pypi.org/project/turing-py/)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Install directly from the **Python Package Index (PyPI)**:

```bash
pip install turing-py
````
---

## 📚 About

A **Turing Machine** is an abstract computational model introduced by **Alan Turing** in 1936. It is widely used in computer science to study the limits of computation and algorithm design.

**turing-py** provides a Python implementation that enables:

* Simulation of Turing Machines
* Creation of custom transition rules
* Step-by-step computation
* Experimentation with theoretical algorithms

This project is intended for:

* Computer Science students
* Theory of Computation courses
* Developers interested in computational models
* Educational demonstrations

---

## 📦 Installation

Install using **pip**:

```bash
pip install turing-py
```

Or install from source:

```bash
git clone https://github.com/ericshantos/turing-py.git
cd turing-py
pip install .
```

---

## ✨ Features

* Deterministic Turing Machine simulation
* Customizable tape input
* Configurable states and transitions
* Step-by-step execution
* Simple and modular Python architecture
* Easy to extend and modify
* CLI-ready structure

---

## 📂 Project Structure

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

## 🧪 Example Turing Machines

Examples you can implement using **turing-py**:

* Binary increment machine
* Palindrome checker
* Unary addition
* Even/Odd binary checker
* String copying machine

---

## 🧩 How It Works

A Turing Machine consists of:

* **Tape** – infinite memory divided into cells
* **Head** – reads and writes symbols on the tape
* **States** – machine configuration states
* **Transition Function** – rules that determine the next action

Each step follows this rule:

```
(Current State, Read Symbol) → (Next State, Write Symbol, Move Direction)
```

Where direction can be:

* `L` → Move left
* `R` → Move right

---

## 🤝 Contributing

Contributions are welcome!

To contribute:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/my-feature
```

3. Make your changes
4. Commit your work

```bash
git commit -m "Add new feature"
```

5. Push to your fork

```bash
git push origin feature/my-feature
```

6. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

Developed by **Eric Santos**.
