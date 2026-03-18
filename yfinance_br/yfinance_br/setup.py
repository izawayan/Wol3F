# Arquivo: setup.py
from setuptools import setup, find_packages

setup(
    name="yfinance-br-quant", # Nome que será usado no pip install
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "yfinance",
        "pandas"
    ],
    author="Seu Nome",
    description="Wrapper robusto do yfinance focado em tratamento de erros, delistings e DY para o mercado brasileiro.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)