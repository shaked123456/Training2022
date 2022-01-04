import requests
import pathlib

scripts = pathlib.Path


def test_main_method():
    request = requests.get("http://0.0.0.0:2222/")
    assert request.status_code == 200, "Test failed !"
