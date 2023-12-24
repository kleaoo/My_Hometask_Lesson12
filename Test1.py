from functions import salary,hello_who

def test_hello_who_max():
    assert hello_who('Artem') == 'Hello,Artem'
    assert hello_who('Roma') == 'Hello,Roma'
    assert hello_who('Maximka') == 'Hello,Maximka'
    assert hello_who('Dima') == 'Hello,Dima'
    assert hello_who('Nikita') == 'Hello,Nikita'