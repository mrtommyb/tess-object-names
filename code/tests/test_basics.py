
def test_imports():
    import tessnames
    from tessnames import nameYield

def test_seed():
    from tessnames import nameYield
    t = nameYield(123)
    assert t.phrase()[0] == 'visual'
    assert t.phrase()[2] == 'bug-eyed'
    assert t.phrase()[3] == 'sidewalk'