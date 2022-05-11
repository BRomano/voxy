from flask import request, jsonify, current_app as app
from voxy.wordcounting import wordcounting_bp as bp

from string import ascii_lowercase, punctuation

EXTRA_VALUES = '´'


def _count_word(sentence: str) -> int:
    """
    This function will receive a sentece as a parameter and return how many words it has

    :param sentence: Sentence
    :return: how many words sentence has
    """
    words = sentence.split(' ')
    words = [word for word in words if word not in punctuation and word not in EXTRA_VALUES]
    return len(words)


def _count_characters(sentence: str) -> [dict]:
    """
    This function will receive a sentece as a parameter and return a dict with ascii counter by characters

    :param sentence: Sentence
    :return: a dict ascii_lowercase with how many characters this string has
    """

    characters = {c.lower(): 0 for c in ascii_lowercase}
    for c in sentence:
        if c in ascii_lowercase:
            characters[c.lower()] += 1

    characters = [{'character': c, 'count': characters[c]} for c in characters]
    return characters


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
        size = _count_word(sentence)
        characters = _count_characters(sentence)
        return jsonify({
            'count': size,
            'characters': characters
        }), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400
