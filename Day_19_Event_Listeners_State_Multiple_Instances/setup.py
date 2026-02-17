from setuptools import setup

APP = ["main.py"]

OPTHIONS = {
    'argv_emulation': True
}

setup(
    app= APP,
    opthions={'py2app':OPTHIONS},
    setup_requires= ['py2app']
)
