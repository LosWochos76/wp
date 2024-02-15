#!/bin/sh

pytest --cov=test_project .
pylint . --disable=C0111
