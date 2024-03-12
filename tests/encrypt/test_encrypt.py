from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(123, 5)

    with pytest.raises(TypeError):
        encrypt_message("teste", "Teste")

    assert encrypt_message("bcapac", 3) == "acb_cap"
    assert encrypt_message("bcapac", 4) == "ca_pacb"
    assert encrypt_message("bcapac", 9) == "capacb"
