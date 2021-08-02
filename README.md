# UFCPY

![Discord](https://img.shields.io/discord/797127174141378571?label=SERVER&logo=discord&style=for-the-badge) ![PyPI - Downloads](https://img.shields.io/pypi/dw/ufcpy?logo=pypi&style=for-the-badge) ![GitHub forks](https://img.shields.io/github/forks/YoungTrep/ufcpy?color=green&logo=github&style=for-the-badge) ![GitHub Repo stars](https://img.shields.io/github/stars/YoungTrep/ufcpy?color=lime%20green&label=STARS&logo=github&style=for-the-badge)

UFCpy is a Python wrapper to get access to the UFC fighter roster. 

## Installation

Use the package manager [pip](https://pypi.org) to install ufcpy.

```bash
pip install ufcpy
```

## Usage

```python
from ufcpy import Fighter

f = Fighter()
f.get_fighter('jon jones')

# returns 'Bones'
f.nickname

# returns 'Rochester, United States'
f.hometown
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

