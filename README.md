# UFCPY

![Discord](https://img.shields.io/discord/797127174141378571?label=SERVER&logo=discord&logoColor=white&style=for-the-badge)<br>
![GitHub forks](https://img.shields.io/github/forks/YoungTrep/ufcpy?color=color&logo=github&style=for-the-badge)<br>
![GitHub Repo stars](https://img.shields.io/github/stars/YoungTrep/ufcpy?color=lime%20green&logo=github&style=for-the-badge)

UFCpy is a Python wrapper to get access to the UFC fighter roster.

## Installation

Use the package manager [pip](https://pypi.org) to install ufcpy.

```bash
pip install ufcpy
```

## Usage

```python
from ufcpy import find_fighter_by_fullname

fighter = find_fighter_by_fullname('Jon Jones')

# returns 'Bones'
fighter.nickname

# returns 'Rochester, United States'
fighter.hometown
```

```python
from ufcpy import Champion

Champions = Champion()

# returns heavyweight champion
Champions.heavyweight
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
