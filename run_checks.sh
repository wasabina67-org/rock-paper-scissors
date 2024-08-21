#!/bin/bash

isort src/run.py src/utils.py
black src/run.py src/utils.py
flake8 src/run.py src/utils.py
mypy src/run.py src/utils.py

isort tests/test_utils.py
black tests/test_utils.py
flake8 tests/test_utils.py
mypy tests/test_utils.py
