# TrendNews

- download news from ria.ru
- visualize trends (Python generate html+javascript canvas)
- viewing result html files


# Install and run from sources (on Windows)

- Download sources
- Install python 3.8 (tested only this version)
- Create virtual env, run command "python.exe -m venv venv"
- Activate venv, run command "venv/Scripts/activate.bat"
- Upgrade pip, run command "python.exe -m pip install -upgrade pip"
- Install requirements, run command "pip install -r requirements.txt"
- Create folder src/ria/data
- Run src/ria/riadownload.py
- Waiting finished
- Run src/riacalculate.py
- Waiting finished
- Open /src/*.html files with news trends
