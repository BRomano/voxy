import pytest
from string import ascii_lowercase


@pytest.mark.parametrize("sentence, word_count, success", [
    ('ahushua auha as uha sad djiasd as d asd asd asdwnwnwnw www', 12, True),
    ('qwe qwe qwe qweqwsdd asd asdasd asd asddds a asas aaaaa .', 11, True),
    ('aisjdijasd asidjaisjdia, asdijaisd, wqoqoqoq , qwwww ... wqqweqwe : ?', 7, True),
    ('fijfqw ,qwe ijqe l,qwq qqq /', 5, True),
    (', . ; / : ´ - +', 0, False),
    ('', 0, False),
])
def test_word_counter(client, sentence, word_count, success):
    payload = {
        'sentence': sentence
    }
    res = client.post('/api/wordcounting/wordCount', json=payload)
    assert res.status_code == 200
    json_data = res.get_json()
    assert json_data.get('count') == word_count


@pytest.mark.parametrize("sentence, word_count, success", [
    ('ahushua auha as uha sad djiasd as d asd asd asdwnwnwnw www', 12, True),
    ('qwe qwe qwe qweqwsdd asd asdasd asd asddds a asas aaaaa .', 11, True),
    ('aisjdijasd asidjaisjdia, asdijaisd, wqoqoqoq , qwwww ... wqqweqwe : ?', 7, True),
    ('fijfqw ,qwe ijqe l,qwq qqq /', 5, True),
    (', . ; / : ´ - +', 0, False),
    ('', 0, False),
])
def test_character_counter(client, sentence, word_count, success):
    payload = {'sentence': sentence}
    res = client.post('/api/wordcounting/wordCount', json=payload)
    assert res.status_code == 200
    json_data = res.get_json()

    characters = {c.lower(): 0 for c in sentence if c in ascii_lowercase}
    for c in sentence:
        if c in ascii_lowercase:
            characters[c.lower()] += 1

    assert json_data.get('count') == word_count
    for _char_obj in json_data.get('characters'):
        if _char_obj.get('count') > 0:
            assert int(_char_obj.get('count')) == characters[_char_obj.get('character')]
