import setuptools

LONG_DESCRIPTION = "test"

with open("docs/source/requirements.txt", "r") as f:
    REQUIREMENTS = f.read().splitlines()

setuptools.setup(
    name="ciberedev.py",
    author="cibere",
    author_email="cibere.dev@gmail.com",
    url="https://github.com/cibere/cibere-dev.py",
    project_urls={
        "Code": "https://github.com/cibere/ciberedev.py",
        "Issue tracker": "https://github.com/cibere/ciberedev.py/issues",
        "Discord/Support Server": "https://discord.gg/2MRrJvP42N",
    },
    version="0.1.10124",
    python_requires=">=3.8",
    install_requires=REQUIREMENTS,
    packages=["ciberedev"],
    description="its a desc",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="MIT",
)
