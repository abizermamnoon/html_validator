#!/bin/python3
import re


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that
    are not meant to be used directly by the user
    are prefixed with an underscore.

    This function returns a list of all the html tags
    contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
   '''
    tags = re.findall(r'<[^>]+>', html)
    return tags


def validate_html(html):
    '''
    This function performs a limited version of html validation
    by checking whether every opening tag has
    a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate a
    # list of html tags without any extra text;
    # then process these html tags using the balanced
    # parentheses algorithm from the class/book
    # the main difference between your code and the code from class will be
    # that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags

    if len(html) == 0:
        return True
    lc = _extract_tags(html)
    stack = []
    if len(lc) == 0:
        return False
    for i, symbol in enumerate(lc):
        if re.match('<([^/][\s\S]*?)>', symbol):
            stack.append(symbol[1:-1].split()[0])
        else:
            if len(stack) == 0:
                return False
            elif stack[-1] == symbol[2:-1]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


print("validate_html('<')=", validate_html('<'))
