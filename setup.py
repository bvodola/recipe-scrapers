import os
from setuptools import setup, find_packages

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(
    os.path.join(here, "bvodola_recipe_scrapers", "__version__.py"), "r", encoding="utf-8"
) as f:
    exec(f.read(), about)

README = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="bvodola_recipe_scrapers",
    url="https://github.com/bvodola/recipe-scrapers/",
    version=about["__version__"],
    author="Brunno Vodola",
    author_email="bvodola@gmail.com",
    description="Python package, scraping recipes from all over the internet",
    keywords="python recipes scraper harvest recipe-scraper recipe-scrapers",
    long_description=README,
    install_requires=[
        "beautifulsoup4>=4.6.0",
        "extruct>=0.8.0",
        "language-tags>=1.0.0",
        "requests>=2.19.1",
        "tldextract==2.2.2",
    ],
    packages=find_packages(),
    package_data={"": ["LICENSE"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.6",
)
