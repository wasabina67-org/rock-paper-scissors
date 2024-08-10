#!/bin/bash

isort src/run.py src/utils.py
black src/run.py src/utils.py
flake8 src/run.py src/utils.py
mypy src/run.py src/utils.py
