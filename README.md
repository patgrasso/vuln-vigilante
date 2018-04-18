# Vuln Vigilante

This is a project for CS 576 - Systems Security at Stevens Institute of
Technology.

The project consists of two components:
- A static analysis tool for finding vulnerabilities.
- A bot that crawls public code repositories and pulls specific ones for
  automatic analysis. This bot also reports significant vulnerabilities to the
  project maintainers.

## Installation

```sh
git clone https://github.com/patgrasso/vuln-vigilante.git
git submodule init
(cd third_party/pycparser && python3 setup.py build)
```

## Usage

```sh
python3 . <c file>
```
