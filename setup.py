from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="calculadora_simples",
    version="0.0.1",
    author="Allan",
    author_email="allanmellom@gmail.com",
    description="Pacote criado para o desafio da Geração Tech Unimed BH - Ciência de Dados, na plataforma DIO.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/allanmellom/Projeto_Criacao_de_Pacotes-calculadora_Geracao_Tech_Unimed-BH-Ciencia_de_Dados-DIO",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)