from checks import checkout
import pytest
import yaml


with open ('config.yaml') as f:
    data = yaml.safe_load(f)



class TestPositive:

    def test_step1(self):
        assert checkout(f'cd {data["folderin"]}; 7z a {data["folderout"]}/arch1', 'Everything is OK'), 'test_step1 FAIL'


    # def test_step2(self):
    #     assert checkout(f'cd {data["folderout"]}; 7z d arch1.7z', 'Everything is OK'), 'test_step1 FAIL'


    # def test_step3(self):
    #     assert checkout(f'cd {data["folderext"]}; 7z u {data["folderout"]}/arch1', 'Everything is OK'), 'test_step1 FAIL'


    # def test_step4(self):
    #     assert checkout(f'cd {data["folderout"]}; 7z l arch1.7z', 'Everything is OK'), 'test_step1 FAIL'


    # def test_step5(self):
    #     assert checkout(f'cd {data["folderout"]}; 7z x arch1.7z', 'Everything is OK'), 'test_step1 FAIL'


if __name__ == '__main__':
    pytest.main(['-vv'])