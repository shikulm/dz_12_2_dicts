import pytest
from utils.dicts import get_val

# @pytest.mark.parametrize('collection, key, default, expected', [
#     ()
# ])
@pytest.fixture()
def data():
    return {"vcs": "mercurial"}

def test_get_val(data):
    assert get_val(data, "vcs") == 'mercurial'
    assert get_val(data, "vss") == 'git'
    assert get_val(data, "vcs", "git") == 'mercurial'
    assert get_val(data, "vss", "bazaar") == 'bazaar'
    assert get_val({}, "vcs", "git") == 'git'
    assert get_val({}, "vcs", "bazaar") == 'bazaar'
