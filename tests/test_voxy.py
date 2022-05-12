import os
from werkzeug.datastructures import FileStorage
import pytest
from string import ascii_lowercase


@pytest.mark.parametrize("sentence, word_count, status_code", [
    ('ahushua auha as uha sad djiasd as d asd asd asdwnwnwnw www', 12, 200),
    ('qwe qwe qwe qweqwsdd asd asdasd asd asddds a asas aaaaa .', 11, 200),
    ('aisjdijasd asidjaisjdia, asdijaisd, wqoqoqoq , qwwww ... wqqweqwe : ?', 7, 200),
    ('fijfqw ,qwe ijqe l,qwq qqq /', 5, 200),
    (', . ; / : ´ - +', 0, 400),
    ('', 0, 400),
])
def test_word_counter(client, sentence, word_count, status_code):
    payload = {
        'sentence': sentence
    }
    res = client.post('/api/wordcounting/wordCount', json=payload)
    assert res.status_code == status_code
    if status_code == 200:
        json_data = res.get_json()
        assert json_data.get('count') == word_count


@pytest.mark.parametrize("sentence, word_count, status_code", [
    ('ahushua auha as uha sad djiasd as d asd asd asdwnwnwnw www', 12, 200),
    ('qwe qwe qwe qweqwsdd asd asdasd asd asddds a asas aaaaa .', 11, 200),
    ('aisjdijasd asidjaisjdia, asdijaisd, wqoqoqoq , qwwww ... wqqweqwe : ?', 7, 200),
    ('fijfqw ,qwe ijqe l,qwq qqq /', 5, 200),
    (', . ; / : ´ - +', 0, 400),
    ('', 0, 400),
])
def test_character_counter(client, sentence, word_count, status_code):
    payload = {'sentence': sentence}
    res = client.post('/api/wordcounting/wordCount', json=payload)
    assert res.status_code == status_code
    json_data = res.get_json()
    if status_code == 200:
        characters = {c.lower(): 0 for c in sentence if c in ascii_lowercase}
        for c in sentence:
            if c in ascii_lowercase:
                characters[c.lower()] += 1

        assert json_data.get('count') == word_count
        for _char_obj in json_data.get('characters'):
            if _char_obj.get('count') > 0:
                assert int(_char_obj.get('count')) == characters[_char_obj.get('character')]
    else:
        assert 'message' in json_data


@pytest.mark.parametrize("filename, word_count, status_code", [
    ('tests/file1.txt', 14, 200),
    ('tests/file2.txt', 231, 200),
    ('tests/file3.txt', 2377, 200),
    ('', 0, 400),
])
def test_upload_file(client, filename, word_count, status_code):
    file = os.path.join(filename)
    data = {
        'file': FileStorage(
            stream=open(file, "rb"),
            filename=filename,
            content_type="text/plain",
        )
    } if len(filename) else {}

    res = client.post(f'/api/wordcounting/wordCountFile',
                      data=data, content_type="multipart/form-data")

    json_data = res.get_json()
    assert res.status_code == status_code
    if status_code == 200:
        my_file = FileStorage(
            stream=open(file, "rb"),
            filename=filename,
            content_type="text/plain",
        )
        sentence = my_file.read()
        try:
            sentence = sentence.decode('utf-8')
        except UnicodeError:
            sentence = sentence.decode('utf-16')
        characters = {c.lower(): 0 for c in sentence if c in ascii_lowercase}
        for c in sentence:
            if c in ascii_lowercase:
                characters[c.lower()] += 1

        assert json_data.get('count') == word_count
        for _char_obj in json_data.get('characters'):
            if _char_obj.get('count') > 0:
                assert int(_char_obj.get('count')) == characters[_char_obj.get('character')]
    else:
        assert 'message' in json_data
