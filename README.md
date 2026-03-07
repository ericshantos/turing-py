# Turing-py

A simple and extensible **Turing Machine simulator written in Python**, designed for learning, experimentation, and educational purposes.

This project allows users to define **states, transitions, and tapes** to simulate the behavior of a **deterministic Turing Machine**, one of the fundamental models in the theory of computation.

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
    └── pytm/
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

---
