# tdbc / toadback

[![Continuous Integration](https://github.com/cvdg/tdbc/actions/workflows/python-package.yml/badge.svg)](https://github.com/cvdg/tdbc/actions/workflows/python-package.yml)

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm-project.org)

## pdm

```shell
brew install pdm
```

## Project init

```shell
$ mkdir ${PRJ_DIR}
$ cd ${PRJ_DIR}
$ pdm init
$ git init
$ git add -A
$ git commit -m "first commit"
$ git branch -M main
$ git remote add origin git@github.com:cvdg/${PRJ}.git
$ git push -u origin main
```