import listgame2

def test_2():
    assert listgame2.solve(2) == 1

def test_3():
    assert listgame2.solve(3) == 1

def test_4():
    assert listgame2.solve(4) == 1

def test_5():
    assert listgame2.solve(5) == 1

def test_6():
    assert listgame2.solve(6) == 2

def test_7():
    assert listgame2.solve(7) == 1

def test_8():
    assert listgame2.solve(4) == 1

def test_9():
    assert listgame2.solve(4) == 1

def test_10():
    assert listgame2.solve(10) == 2

def test_12():
    assert listgame2.solve(12) == 2

def test_16():
    assert listgame2.solve(16) == 2

def test_32():
    assert listgame2.solve(32) == 2    

def test_36():
    assert listgame2.solve(36) == 3

def test_40():
    assert listgame2.solve(40) == 3

def test_41():
    assert listgame2.solve(41) == 1

def test_42():
    assert listgame2.solve(42) == 3

def test_43():
    assert listgame2.solve(43) == 1

def test_864():
    assert listgame2.solve(864) == 4

def test_10368():
    assert listgame2.solve(10368) == 6

def test_112500():
    assert listgame2.solve(112500) == 6
