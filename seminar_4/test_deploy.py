from sshcheckers import ssh_checkout, upload_files
import yaml

with open ('config.yaml') as f:
    my_dict = yaml.safe_load(f)

class TestDeployPositive:

    def test_step1_deploy(self):
        res = []
        upload_files(my_dict['address'], 'user2', my_dict['passwordssh'], my_dict['username1'], my_dict['username2'])
        res.append(ssh_checkout(my_dict['address'], 'user2', my_dict['passwordssh'], f"echo '{my_dict['passwordssh']}' | sudo -S dpkg -i my_dict['username2']", 
                                'Настраивается пакет'))
        res.append(ssh_checkout(my_dict['address'], 'user2', my_dict['passwordssh'], f"echo' {my_dict['passwordssh']}' | sudo -S dpkg -s p7zip-full", 
                                'Status: install ok installed'))
        assert all(res)




    # if deploy():
    #     print('Деплой успешен')
    # else:
    #     print('Ошибка деплоя')
        