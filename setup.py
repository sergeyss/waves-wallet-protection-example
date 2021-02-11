import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="waves-wallet-protection",
    version="1.0.0",
    author="Sergey Valiev",
    author_email="123@456.email",
    description="Waves wallet protection by using second signature",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="git@github.com:sergeyss/waves-wallet-protection-example.git",
    packages=setuptools.find_packages(),
    python_requires='>=3.9',
    install_requires=[
        'pywaves>=0.8.38'
    ]
)
