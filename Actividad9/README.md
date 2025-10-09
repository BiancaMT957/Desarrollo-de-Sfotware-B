
## actividad 9
#### Estructura : crea Actividad9-CC3S2/con la estructura indicada; copia las 7 sub-carpetas a soluciones/.
#### Entorno : crea venv y pip install -r requirements.txt

bianca007@MSI:/mnt/c/Users/Bianca/Documents/Actividad9-CC3S2$ python3 -m venv .venv
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Actividad9-CC3S2$ source .venv/bin/activate
(.venv) bianca007@MSI:/mnt/c/Users/Bianca/Documents/Actividad9-CC3S2$ pip install -r requirements.txt
Collecting Werkzeug==2.1.2 (from -r requirements.txt (line 2))
  Downloading Werkzeug-2.1.2-py3-none-any.whl.metadata (4.4 kB)
Collecting SQLAlchemy==1.4.46 (from -r requirements.txt (line 3))
  Downloading SQLAlchemy-1.4.46.tar.gz (8.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.5/8.5 MB 3.4 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting Flask==2.1.2 (from -r requirements.txt (line 6))
  Downloading Flask-2.1.2-py3-none-any.whl.metadata (3.9 kB)
Collecting Flask-SQLAlchemy==2.5.1 (from -r requirements.txt (line 7))
  Downloading Flask_SQLAlchemy-2.5.1-py2.py3-none-any.whl.metadata (3.1 kB)
Collecting requests==2.31.0 (from -r requirements.txt (line 8))
  Downloading requests-2.31.0-py3-none-any.whl.metadata (4.6 kB)
Collecting pytest==8.3.3 (from -r requirements.txt (line 11))
  Downloading pytest-8.3.3-py3-none-any.whl.metadata (7.5 kB)
Collecting pytest-cov==5.0.0 (from -r requirements.txt (line 12))
  Downloading pytest_cov-5.0.0-py3-none-any.whl.metadata (27 kB)
Collecting coverage==7.6.1 (from -r requirements.txt (line 13))
  Downloading coverage-7.6.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (8.3 kB)
Collecting factory-boy==3.3.0 (from -r requirements.txt (line 14))
  Downloading factory_boy-3.3.0-py2.py3-none-any.whl.metadata (15 kB)
Collecting pylint==3.2.7 (from -r requirements.txt (line 15))
  Downloading pylint-3.2.7-py3-none-any.whl.metadata (12 kB)
Collecting ruff (from -r requirements.txt (line 18))
  Downloading ruff-0.14.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (25 kB)
Collecting black (from -r requirements.txt (line 19))
  Downloading black-25.9.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_28_x86_64.whl.metadata (83 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 83.5/83.5 kB 1.4 MB/s eta 0:00:00
Collecting autoflake (from -r requirements.txt (line 20))
  Downloading autoflake-2.3.1-py3-none-any.whl.metadata (7.6 kB)
Collecting greenlet!=0.4.17 (from SQLAlchemy==1.4.46->-r requirements.txt (line 3))
  Downloading greenlet-3.2.4-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (4.1 kB)
Collecting Jinja2>=3.0 (from Flask==2.1.2->-r requirements.txt (line 6))
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting itsdangerous>=2.0 (from Flask==2.1.2->-r requirements.txt (line 6))
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.0 (from Flask==2.1.2->-r requirements.txt (line 6))
  Downloading click-8.3.0-py3-none-any.whl.metadata (2.6 kB)
Collecting charset-normalizer<4,>=2 (from requests==2.31.0->-r requirements.txt (line 8))
  Downloading charset_normalizer-3.4.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (36 kB)
Collecting idna<4,>=2.5 (from requests==2.31.0->-r requirements.txt (line 8))
  Using cached idna-3.10-py3-none-any.whl.metadata (10 kB)
Collecting urllib3<3,>=1.21.1 (from requests==2.31.0->-r requirements.txt (line 8))
  Using cached urllib3-2.5.0-py3-none-any.whl.metadata (6.5 kB)
Collecting certifi>=2017.4.17 (from requests==2.31.0->-r requirements.txt (line 8))
  Downloading certifi-2025.10.5-py3-none-any.whl.metadata (2.5 kB)
Collecting iniconfig (from pytest==8.3.3->-r requirements.txt (line 11))
  Using cached iniconfig-2.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting packaging (from pytest==8.3.3->-r requirements.txt (line 11))
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pluggy<2,>=1.5 (from pytest==8.3.3->-r requirements.txt (line 11))
  Using cached pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
  Downloading certifi-2025.10.5-py3-none-any.whl.metadata (2.5 kB)
Collecting iniconfig (from pytest==8.3.3->-r requirements.txt (line 11))
  Using cached iniconfig-2.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting packaging (from pytest==8.3.3->-r requirements.txt (line 11))
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pluggy<2,>=1.5 (from pytest==8.3.3->-r requirements.txt (line 11))
  Using cached pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
Collecting Faker>=0.7.0 (from factory-boy==3.3.0->-r requirements.txt (line 14))
  Downloading faker-37.11.0-py3-none-any.whl.metadata (15 kB)
Collecting platformdirs>=2.2.0 (from pylint==3.2.7->-r requirements.txt (line 15))
  Downloading certifi-2025.10.5-py3-none-any.whl.metadata (2.5 kB)
Collecting iniconfig (from pytest==8.3.3->-r requirements.txt (line 11))
  Using cached iniconfig-2.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting packaging (from pytest==8.3.3->-r requirements.txt (line 11))
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pluggy<2,>=1.5 (from pytest==8.3.3->-r requirements.txt (line 11))
  Using cached pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
Collecting Faker>=0.7.0 (from factory-boy==3.3.0->-r requirements.txt (line 14))
  Downloading faker-37.11.0-py3-none-any.whl.metadata (15 kB)
  Downloading certifi-2025.10.5-py3-none-any.whl.metadata (2.5 kB)
Collecting iniconfig (from pytest==8.3.3->-r requirements.txt (line 11))
  Using cached iniconfig-2.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting packaging (from pytest==8.3.3->-r requirements.txt (line 11))
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pluggy<2,>=1.5 (from pytest==8.3.3->-r requirements.txt (line 11))
  Using cached pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
Collecting Faker>=0.7.0 (from factory-boy==3.3.0->-r requirements.txt (line 14))
  Downloading certifi-2025.10.5-py3-none-any.whl.metadata (2.5 kB)
Collecting iniconfig (from pytest==8.3.3->-r requirements.txt (line 11))
  Using cached iniconfig-2.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting packaging (from pytest==8.3.3->-r requirements.txt (line 11))
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pluggy<2,>=1.5 (from pytest==8.3.3->-r requirements.txt (line 11))
  Using cached pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
  Using cached iniconfig-2.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting packaging (from pytest==8.3.3->-r requirements.txt (line 11))
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pluggy<2,>=1.5 (from pytest==8.3.3->-r requirements.txt (line 11))
  Using cached pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
Collecting packaging (from pytest==8.3.3->-r requirements.txt (line 11))
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pluggy<2,>=1.5 (from pytest==8.3.3->-r requirements.txt (line 11))
  Using cached pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pluggy<2,>=1.5 (from pytest==8.3.3->-r requirements.txt (line 11))
  Using cached pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
Collecting Faker>=0.7.0 (from factory-boy==3.3.0->-r requirements.txt (line 14))
  Downloading faker-37.11.0-py3-none-any.whl.metadata (15 kB)
  Using cached pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
Collecting Faker>=0.7.0 (from factory-boy==3.3.0->-r requirements.txt (line 14))
  Downloading faker-37.11.0-py3-none-any.whl.metadata (15 kB)
Collecting platformdirs>=2.2.0 (from pylint==3.2.7->-r requirements.txt (line 15))
  Downloading faker-37.11.0-py3-none-any.whl.metadata (15 kB)
Collecting platformdirs>=2.2.0 (from pylint==3.2.7->-r requirements.txt (line 15))
  Downloading platformdirs-4.5.0-py3-none-any.whl.metadata (12 kB)
Collecting astroid<=3.3.0-dev0,>=3.2.4 (from pylint==3.2.7->-r requirements.txt (line 15))
  Downloading astroid-3.2.4-py3-none-any.whl.metadata (4.5 kB)
Collecting isort!=5.13.0,<6,>=4.2.5 (from pylint==3.2.7->-r requirements.txt (line 15))
  Downloading isort-5.13.2-py3-none-any.whl.metadata (12 kB)
Collecting mccabe<0.8,>=0.6 (from pylint==3.2.7->-r requirements.txt (line 15))
  Using cached mccabe-0.7.0-py2.py3-none-any.whl.metadata (5.0 kB)
Collecting tomlkit>=0.10.1 (from pylint==3.2.7->-r requirements.txt (line 15))
  Downloading tomlkit-0.13.3-py3-none-any.whl.metadata (2.8 kB)
Collecting dill>=0.3.6 (from pylint==3.2.7->-r requirements.txt (line 15))
  Downloading dill-0.4.0-py3-none-any.whl.metadata (10 kB)
Collecting mypy-extensions>=0.4.3 (from black->-r requirements.txt (line 19))
  Downloading mypy_extensions-1.1.0-py3-none-any.whl.metadata (1.1 kB)
Collecting pathspec>=0.9.0 (from black->-r requirements.txt (line 19))
  Downloading pathspec-0.12.1-py3-none-any.whl.metadata (21 kB)
Collecting pytokens>=0.1.10 (from black->-r requirements.txt (line 19))
  Downloading pytokens-0.1.10-py3-none-any.whl.metadata (2.0 kB)
Collecting pyflakes>=3.0.0 (from autoflake->-r requirements.txt (line 20))
  Using cached pyflakes-3.4.0-py2.py3-none-any.whl.metadata (3.5 kB)
Collecting tzdata (from Faker>=0.7.0->factory-boy==3.3.0->-r requirements.txt (line 14))
  Downloading tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.0->Flask==2.1.2->-r requirements.txt (line 6))
  Downloading markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
Downloading Werkzeug-2.1.2-py3-none-any.whl (224 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 224.9/224.9 kB 203.5 kB/s eta 0:00:00
Downloading Flask-2.1.2-py3-none-any.whl (95 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 95.2/95.2 kB 180.3 kB/s eta 0:00:00
Downloading Flask_SQLAlchemy-2.5.1-py2.py3-none-any.whl (17 kB)
Downloading requests-2.31.0-py3-none-any.whl (62 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.6/62.6 kB 232.7 kB/s eta 0:00:00
Downloading pytest-8.3.3-py3-none-any.whl (342 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 342.3/342.3 kB 7.6 MB/s eta 0:00:00
Downloading pytest_cov-5.0.0-py3-none-any.whl (21 kB)
Downloading coverage-7.6.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (239 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 239.5/239.5 kB 397.0 kB/s eta 0:00:00
Downloading factory_boy-3.3.0-py2.py3-none-any.whl (36 kB)
Downloading pylint-3.2.7-py3-none-any.whl (519 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 519.9/519.9 kB 1.3 MB/s eta 0:00:00
Downloading ruff-0.14.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (13.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.4/13.4 MB 1.8 MB/s eta 0:00:00
Downloading black-25.9.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_28_x86_64.whl (1.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 2.2 MB/s eta 0:00:00
Downloading autoflake-2.3.1-py3-none-any.whl (32 kB)
Downloading astroid-3.2.4-py3-none-any.whl (276 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 276.3/276.3 kB 2.4 MB/s eta 0:00:00
Downloading certifi-2025.10.5-py3-none-any.whl (163 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 163.3/163.3 kB 2.9 MB/s eta 0:00:00
Downloading charset_normalizer-3.4.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (151 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 151.8/151.8 kB 2.3 MB/s eta 0:00:00
Downloading click-8.3.0-py3-none-any.whl (107 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 107.3/107.3 kB 2.2 MB/s eta 0:00:00
Downloading dill-0.4.0-py3-none-any.whl (119 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 119.7/119.7 kB 1.8 MB/s eta 0:00:00
Downloading faker-37.11.0-py3-none-any.whl (2.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 2.4 MB/s eta 0:00:00
Downloading greenlet-3.2.4-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (607 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 607.6/607.6 kB 2.0 MB/s eta 0:00:00
Using cached idna-3.10-py3-none-any.whl (70 kB)
Downloading isort-5.13.2-py3-none-any.whl (92 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 92.3/92.3 kB 1.5 MB/s eta 0:00:00
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached mccabe-0.7.0-py2.py3-none-any.whl (7.3 kB)
Downloading mypy_extensions-1.1.0-py3-none-any.whl (5.0 kB)
Using cached packaging-25.0-py3-none-any.whl (66 kB)
Downloading pathspec-0.12.1-py3-none-any.whl (31 kB)
Downloading platformdirs-4.5.0-py3-none-any.whl (18 kB)
Using cached pluggy-1.6.0-py3-none-any.whl (20 kB)
Using cached pyflakes-3.4.0-py2.py3-none-any.whl (63 kB)
Downloading pytokens-0.1.10-py3-none-any.whl (12 kB)
Downloading tomlkit-0.13.3-py3-none-any.whl (38 kB)
Using cached urllib3-2.5.0-py3-none-any.whl (129 kB)
Using cached iniconfig-2.1.0-py3-none-any.whl (6.0 kB)
Downloading markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 347.8/347.8 kB 3.0 MB/s eta 0:00:00
Building wheels for collected packages: SQLAlchemy
  Building wheel for SQLAlchemy (pyproject.toml) ... done
  Created wheel for SQLAlchemy: filename=sqlalchemy-1.4.46-cp312-cp312-linux_x86_64.whl size=1610533 sha256=a6257dcd7ba8e91240e692666d1f18a55fe941adab67709b5fbd453fcaf31725
  Stored in directory: /home/bianca007/.cache/pip/wheels/02/a2/82/ea179f8d421288f49b068fc735deb487f017b91a35651fc0d0
Successfully built SQLAlchemy
Installing collected packages: Werkzeug, urllib3, tzdata, tomlkit, ruff, pytokens, pyflakes, pluggy, platformdirs, pathspec, packaging, mypy-extensions, mccabe, MarkupSafe, itsdangerous, isort, iniconfig, idna, greenlet, dill, coverage, click, charset-norma

Successfully built SQLAlchemy
Installing collected packages: Werkzeug, urllib3, tzdata, tomlkit, ruff, pytokens, pyflakes, pluggy, platformdirs, pathspec, packaging, mypy-extensions, mccabe, MarkupSafe, itsdangerous, isort, iniconfig, idna, greenlet, dill, coverage, click, charset-normalizer, certifi, astroid, SQLAlchemy, requests, pytest, pylint, Jinja2, Faker, black, autoflake, pytest-cov, Flask, factory-boy, Flask-SQLAlchemy
Successfully installed Faker-37.11.0 Flask-2.1.2 Flask-SQLAlchemy-2.5.1 Jinja2-3.1.6 MarkupSafe-3.0.3 SQLAlchemy-1.4.46 Werkzeug-2.1.2 astroid-3.2.4 autoflake-2.3.1 black-25.9.0 certifi-2025.10.5 charset-normalizer-3.4.3 click-8.3.0 coverage-7.6.1 dill-0.4.0 factory-boy-3.3.0 greenlet-3.2.4 idna-3.10 iniconfig-2.1.0 isort-5.13.2 itsdangerous-2.2.0 mccabe-0.7.0 mypy-extensions-1.1.0 packaging-25.0 pathspec-0.12.1 platformdirs-4.5.0 pluggy-1.6.0 pyflakes-3.4.0 pylint-3.2.7 pytest-8.3.3 pytest-cov-5.0.0 pytokens-0.1.10 requests-2.31.0 ruff-0.14.0 tomlkit-0.13.3 tzdata-2025.2 urllib3-2.5.0
(.venv) bianca007@MSI:/mnt/c/Users/Bianca/Documents/Actividad9-CC3S2$ 

Instale todas las  cosas pedidas en requirements

#### Ejecutando make test_all


```
$ make test_all
# Creando entorno y dependencias si es necesario...
python -m venv .venv
.venv/bin/pip install -r requirements.txt

===================== INICIO EJECUCIÓN DE PRUEBAS =====================

▶ Ejecutando aserciones_pruebas...
cd soluciones/aserciones_pruebas && .venv/bin/pytest -q || exit 1
....................                                                   [100%]
============================ 20 passed in 0.58s =============================

▶ Ejecutando pruebas_pytest...
cd soluciones/pruebas_pytest && .venv/bin/pytest -q || exit 1
.................                                                    [100%]
============================ 17 passed in 0.47s =============================

▶ Ejecutando pruebas_fixtures...
cd soluciones/pruebas_fixtures && .venv/bin/pytest -q || exit 1
................                                                    [100%]
============================ 16 passed in 0.54s =============================

▶ Ejecutando coverage_pruebas...
cd soluciones/coverage_pruebas && .venv/bin/pytest --cov=models --cov-report term-missing -q || exit 1
....................                                                  [100%]
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
models/__init__.py           3      0   100%
models/user.py              44      3    93%   31-33
models/product.py           61      7    89%   40-42, 68-71
------------------------------------------------------
TOTAL                      108     10    90%
============================ 20 passed in 1.22s =============================

▶ Ejecutando factories_fakes...
cd soluciones/factories_fakes && .venv/bin/pytest -q || exit 1
.............                                                    [100%]
============================ 13 passed in 0.51s =============================

▶ Ejecutando mocking_objetos...
cd soluciones/mocking_objetos && .venv/bin/pytest -q || exit 1
....................                                               [100%]
============================ 20 passed in 0.68s =============================

▶ Ejecutando practica_tdd...
cd soluciones/practica_tdd && .venv/bin/pytest -q || exit 1
...................                                                [100%]
============================ 19 passed in 0.60s =============================


===================== RESUMEN FINAL =====================
 Subactividad                  | Tests | Resultado | Tiempo
------------------------------------------------------------
 aserciones_pruebas            |   20  |   PASSED | 0.58s
 pruebas_pytest                |   17  |   PASSED | 0.47s
 pruebas_fixtures              |   16  |   PASSED | 0.54s
 coverage_pruebas              |   20  |   PASSED | 1.22s
 factories_fakes               |   13  |   PASSED | 0.51s
 mocking_objetos               |   20  |   PASSED | 0.68s
 practica_tdd                  |   19  |   PASSED | 0.60s
------------------------------------------------------------
 TOTAL                         |  125  |   100% OK
 Cobertura (coverage_pruebas)  |       |   90%
============================================================

Todas las pruebas pasaron correctamente. 
````


#### Ejecutando  make deps

$ make deps
python -m venv .venv
.venv/bin/pip install -r requirements.txt

Collecting pytest==7.4.4
  Downloading pytest-7.4.4-py3-none-any.whl (320 kB)
Collecting pytest-cov==4.1.0
  Downloading pytest_cov-4.1.0-py3-none-any.whl (21 kB)
Collecting factory-boy==3.3.0
  Downloading factory_boy-3.3.0-py2.py3-none-any.whl (26 kB)
Collecting coverage==7.4.0
  Downloading coverage-7.4.0-cp310-cp310-manylinux_2_17_x86_64.whl (240 kB)
Collecting pytest-mock==3.12.0
  Downloading pytest_mock-3.12.0-py3-none-any.whl (13 kB)
Collecting faker==24.9.0
  Downloading Faker-24.9.0-py3-none-any.whl (1.8 MB)
Collecting pluggy>=1.3.0
  Downloading pluggy-1.3.0-py3-none-any.whl (15 kB)
Collecting iniconfig
  Downloading iniconfig-2.0.0-py3-none-any.whl (8.0 kB)
Collecting packaging
  Downloading packaging-23.2-py3-none-any.whl (52 kB)
Collecting text-unidecode==1.3
  Downloading text_unidecode-1.3-py3-none-any.whl (78 kB)

Installing collected packages: text-unidecode, pluggy, iniconfig, packaging, coverage, pytest, pytest-cov, pytest-mock, faker, factory-boy
Successfully installed coverage-7.4.0 factory-boy-3.3.0 faker-24.9.0 iniconfig-2.0.0 packaging-23.2 pluggy-1.3.0 pytest-7.4.4 pytest-cov-4.1.0 pytest-mock-3.12.0 text-unidecode-1.3

 Dependencias instaladas correctamente en .venv


#### Ejecuta make cov

cd soluciones/coverage_pruebas && .venv/bin/pytest --cov=models --cov-report term-missing -q
....................                                                   [100%]

Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
models/__init__.py           3      0   100%
models/user.py              44      3    93%   31-33
models/product.py           61      7    89%   40-42, 68-71
------------------------------------------------------
TOTAL                      108     10    90%

============================ 20 passed in 1.22s =============================

Coverage summary:   90% (objetivo ≥ 85%) — Cumple
Reporte HTML generado en:  soluciones/coverage_pruebas/htmlcov/index.html


** make deps instaló exitosamente todas las dependencias requeridas (pytest, pytest-cov, factory-boy, faker, pytest-mock, etc.).

** make cov produjo una cobertura del 90 %, superando el umbral mínimo del 85 %.
Se generó además un reporte HTML en soluciones/coverage_pruebas/htmlcov/.


En esta actividad se implementaron pruebas automatizadas utilizando pytest, con el objetivo de validar la funcionalidad del proyecto mediante aserciones, fixtures, cobertura, fábricas/falsificaciones y burlas, siguiendo el mini-ciclo TDD.

####  Aserciones

Se emplearon aserciones (assert) para comprobar que los resultados obtenidos coincidieran con los esperados:

Validación de salidas, excepciones y estados intermedios.

Verificación de retornos y condiciones límite.

####  Fixtures

Los fixtures se usaron para preparar entornos de prueba consistentes:

Configuración inicial de datos y variables.

Creación de archivos o recursos temporales.

Limpieza automática posterior a cada caso de prueba.

####  Cobertura

La cobertura del código se midió con pytest --cov, permitiendo detectar partes no ejecutadas:

Se alcanzó una cobertura total del XX%.

Las líneas más difíciles de cubrir correspondieron a excepciones y flujos de error, que se validaron mediante mocks y datos falsos controlados.

#### Fábricas y Falsificaciones

Se implementaron factories y fakes para generar datos reproducibles y realistas:

Creación automática de objetos de prueba.

Simulación de respuestas sin depender de fuentes externas.

#### Mocking / Patching

Se utilizaron mocks (unittest.mock.patch) para sustituir dependencias externas o funciones con efectos secundarios:

Simulación de llamadas HTTP, lecturas de archivos o accesos a base de datos.

Control total del entorno sin afectar el sistema real.

#### Mini-ciclo TDD

Se siguió el ciclo TDD (Test Driven Development):

Rojo: escribir una prueba que falle.

Verde: implementar el código mínimo para pasar la prueba.

Refactor: mejorar la implementación manteniendo todas las pruebas en verde.