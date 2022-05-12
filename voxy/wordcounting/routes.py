from flask import request, jsonify
from voxy.wordcounting import wordcounting_bp as bp

from string import ascii_lowercase, punctuation

EXTRA_VALUES = '´'


def _count_word(sentence: str) -> int:
    """
    This function will receive a sentece as a parameter and return how many words it has

    :param sentence: Sentence
    :return: how many words sentence has
    """
    if len(sentence) == 0:
        raise Exception('Text must have at least one word')

    sentence = sentence.replace('\n', ' ')
    words = sentence.split(' ')
    words = [word for word in words if word not in punctuation and word not in EXTRA_VALUES]
    return len(words)


def _count_characters(sentence: str) -> [dict]:
    """
    This function will receive a sentece as a parameter and return a dict with ascii counter by characters

    :param sentence: Sentence
    :return: a dict ascii_lowercase with how many characters this string has
    """
    if len(sentence) == 0:
        raise Exception('Text must have at least one word')

    characters = {c.lower(): 0 for c in ascii_lowercase}
    for c in sentence:
        if c in ascii_lowercase:
            characters[c.lower()] += 1

    characters = [{'character': c, 'count': characters[c]} for c in characters]
    return characters


def do_word_count(sentence: str) -> [int, dict]:
    size = _count_word(sentence)
    if size == 0:
        raise Exception('Text must have at least one word')

    characters = _count_characters(sentence)
    return size, characters


@bp.route('/wordCount', methods=['POST'])
def get_words_count():
    """
    Will count how much words the sentence on post body has
    ---
    description: Will count how much words the sentence on post body has
    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#definitions/RequestWordCounter'

    definitions:
      RequestWordCounter:
        type: object
        properties:
          sentence:
            type: string
            required: true
      ResponseWordCounter:
        type: object
        properties:
          counter:
            type: number
          characters:
            type: array
            items:
              $ref: '#definitions/CharacterCounter'
        example:
          counter: 12
          characters:
            - character: a
              counter: 8
            - character: b
              counter: 10
            - character: t
              counter: 2

      CharacterCounter:
        type: object
        properties:
          character:
            type: string
          count:
            type: number
        example:
          character: a
          counter: 5

      ErrorMessage:
        type: object
        properties:
          message:
            type: string
    responses:
      200:
        description: The object retrieved from thrid party API, or getted from cache. If Attribute cached_data is false, the object was cached
        schema:
          $ref: '#definitions/ResponseWordCounter'

      400:
        description: if any error occur on endpoint
        schema:
          $ref: '#definitions/ErrorMessage'
    """

    try:
        sentence = request.json.get('sentence')
        size, characters = do_word_count(sentence)

        return jsonify({
            'count': size,
            'characters': characters
        }), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@bp.route('/wordCountFile', methods=['POST'])
def get_words_count_file():
    """
    Upload a txt file to count how many words it has
    ---
    description: Will count how many words the txt file has.
    parameters:
      - name: file
        in: formData
        type: file
        required: true
        description: The file to be imported
    responses:
      200:
        description: The object retrieved from thrid party API, or getted from cache. If Attribute cached_data is false, the object was cached
        schema:
          $ref: '#definitions/ResponseWordCounter'

      400:
        description: if any error occur on endpoint
        schema:
          $ref: '#definitions/ErrorMessage'
    """

    try:
        if len(request.files) != 1 or 'file' not in request.files:
            message = 'There is no files on request content'
            if 'file' not in request.files:
                message = 'Wrong post request'
            raise Exception(message)

        file = request.files['file']
        if file.content_type != 'text/plain':
            raise Exception('Incorrect content type, file must be txt')

        contents = file.read()
        try:
            contents = contents.decode('utf-8')
        except UnicodeError:
            contents = contents.decode('utf-16')

        size, characters = do_word_count(contents)
        return jsonify({
            'count': size,
            'characters': characters
        }), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400
