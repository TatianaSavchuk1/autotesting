from Seminars.seminar_4.sshcheckers import ssh_checkout
import pytest
import yaml
from datetime import datetime


with open ('config.yaml') as f:
    my_dict = yaml.safe_load(f)


@pytest.fixture()
def make_log():
    with open ('log.txt') as l:
        l.write(datetime.now().replace(microsecond=0))
    l.close
    return ssh_checkout (my_dict['address'], 'user2', my_dict['passwordssh'], my_dict['username1'], my_dict['username2'], my_dict['port'])