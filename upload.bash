#!/bin/bash
rm -rf dist build bvodola_recipe_scrapers.egg-info
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/* -u bvodola -p 1379BomberMan@!