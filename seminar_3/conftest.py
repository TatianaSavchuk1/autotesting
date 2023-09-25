from Seminars.seminar_3.checks import checkout
import pytest
import yaml
from datetime import time
import subprocess


with open ('config.yaml') as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def make_folders():
    return checkout (f'mkdir -p {data["folderin"]} {data["folderout"]} {data["folderext"]}', '')


@pytest.fixture()
def make_files():
    return checkout (f'cd {data["folderin"]}; touch file1 file2', '')

# Дополнить проект фикстурой, которая после каждого шага теста дописывает в заранее созданный файл stat.txt строку вида:
# время, кол-во файлов из конфига, размер файла из конфига, статистика загрузки процессора из файла /proc/loadavg (можно писать просто всё содержимое этого файла).

@pytest.fixture()
def make_log():
    return checkout (f'echo {time} stat.txt; cat /proc/loadavg stat.txt', '' )