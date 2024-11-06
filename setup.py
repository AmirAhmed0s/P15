from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# Import version from your app's __init__.py file
try:
    from dox_theme import __version__ as version
except ImportError:
    version = "0.0.1"  # Fallback version if __version__ is not found

setup(
    name="dox_theme",
    version=version,
    description="Dox Theme compatible with ERPNext v14 and v15",
    author="Nesscale",
    author_email="info@nesscale.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
    classifiers=[
        "Framework :: Frappe",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
