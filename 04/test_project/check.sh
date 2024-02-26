#!/bin/sh

pylint . --disable=C0111
pytest --cov=test_project --cov-fail-under=90 --cov-branch .

