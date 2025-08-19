from setuptools import setup, find_packages

with open("requirements.txt", 'r', encoding="utf-16") as _f:
    requirements = _f.read().splitlines()

print(requirements)
setup(
    name="summarizer",
    version="0.0.1",
    author="Your Name",
    entry_points="""
    [console_scripts]
    summarizer=main:main""",
    description="Azure Machine Learning with Hugging Face",
    packages=find_packages(),
    install_requires=requirements,
    url=""
)
