# Releasing the ea


```shell
cldfbench makecldf cldfbench_ea.py --with-zenodo --with-cldfreadme --glottolog-version v5.2
pytest
```

```shell
cldfbench cldfviz.map cldf --pacific-centered --format png --width 20 --output map.png --with-ocean
```

```shell
cldferd --format compact.svg cldf > erd.svg
```

```shell
cldfbench readme cldfbench_ea.py
cldfbench zenodo --communities dplace cldfbench_ea.py
dplace check cldfbench_ea.py
```

```shell
git status
git tag
```

Adapt CHANGELOG.md.
Add, commit and push all changes.

```shell
dplace release cldfbench_ea.py vX.Y
```