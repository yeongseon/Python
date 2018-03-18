import pytest

@pytest.fixture
def smtp():
    import smtplib
    return smtplib.SMTP("smtp.gamil.com", 587, timeout=5)

def test_ehlo(smtp):
    response, msg = smtp.ehlo()
    assert response == 250
    assert 0 # for demo purpose
