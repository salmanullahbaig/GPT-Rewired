from setuptools import find_packages, setup

setup(
    name="re_gpt",
    version="2.9.7",
    author="baig",
    description="Unofficial reverse-engineered ChatGPT API in Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/salmanullahbaig/GPT-Rewired.git",
    project_urls={
        "Bug Tracker": "https://github.com/salmanullahbaig/GPT-Rewired.git/issues",
    },
    packages=find_packages(),
    install_requires=["curl_cffi==0.5.9"],
)
