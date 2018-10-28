from modules.site.layout_generator import LayoutGenerator


def test_some_sum():
    assert 2 + 2 == 4


def test_some_sum_2():
    assert LayoutGenerator.gen_header().find("<h1>")
