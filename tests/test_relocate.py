def test_elements_are_refreshed(bing_page):
    first = bing_page.search_button
    second = bing_page.search_button
    assert id(first) != id(second)
