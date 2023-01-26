import json
import os
from pathlib import Path


class JSONFSDAO:

    def __init__(self, repo_path):
        if not isinstance(repo_path, Path):
            repo_path = Path(repo_path)
        self.repo_path = repo_path

    def save(self, name, obj):
        path = self.repo_path / name
        with open(path, 'w') as f:
            json.dump(obj, f)

    def all(self):
        return [el.name for el in self.repo_path.glob('*')]

    def get_by_id(self, name):
        path = self.repo_path / name
        with open(path, 'r') as f:
            obj = json.load(f)
        return obj

    def remove(self, name):
        path = self.repo_path / name
        os.remove(path)

if __name__ == '__main__':

    from prova1.config.AppConfig import REPOPATH

    dao = JSONFSDAO(REPOPATH)

    obj = {'a': 1, 'b': 2, 'c': 3, 'e':4, 'f':1}

    name = 'quarto'

    dao.save(name=name, obj=obj)
    print(dao.get_by_id('quarto'))

    dao.remove('blablabla_new')
    #print(dao.get_by_id('primo'))
    #print(dao.get_by_id('secondo'))

    print(dao.all())