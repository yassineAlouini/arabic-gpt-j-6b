from setuptools import find_packages, setup

NAME = 'arabic_gpt'
VERSION = '0.0.1'
AUTHOR = ''
DESCRIPTION = """Fine-tuning GPT-J-6B on an Arabic dataset."""
EMAIL = ""
URL = ""

setup(
    name=NAME,
    version=VERSION,
    packages=find_packages(),
    # Some metadata
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    url=URL,
    license="MIT",
    keywords="HuggingFace TPU JAX machine-learning",
)