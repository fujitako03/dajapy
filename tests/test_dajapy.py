from dajapy import __version__, is_dajare


def test_version():
    assert __version__ == '0.1.0'

def test_is_dajare_true():
    """
    正常テスト（ダジャレ判定）
    """
    sentence = "アルミ缶の上にあるみかん"
    kaburi_count=5

    dajare_flg = is_dajare(
        sentence=sentence,
        kaburi_count=kaburi_count)

    assert dajare_flg == True

def test_is_dajare_false():
    """
    正常テスト（ダジャレじゃない判定）
    """
    sentence = "ハエは速え～"
    kaburi_count=3

    dajare_flg = is_dajare(
        sentence=sentence,
        kaburi_count=kaburi_count)

    assert dajare_flg == False
