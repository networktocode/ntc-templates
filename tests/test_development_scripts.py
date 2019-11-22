import development_scripts as tds


def test_ensure_spacing_for_multiline_comment():
    remark = "comment 11\n#        comment 12\n#comment 13\n"
    remark_formatted = tds.ensure_spacing_for_multiline_comment(remark)
    assert remark_formatted == "comment 11\n# comment 12\n# comment 13"






'''
def ensure_spacing_for_multiline_comment(remark):
    """
    Finds all comments and ensures a single space after "#" symbol.

    Args:
        remark (str): The remark of a comment from a ``ruamel.yaml.token.CommentToken``.

    Returns:
        str: The ``remark`` formatted with a single space after comment start, "#"

    Example:
        >>> remark = "comment 11\n#        comment 12\n#comment 13\n"
        >>> remark_formatted = ensure_spacing_for_multiline_comment(remark)
        >>> # Formatting has normalized each comment to have a single space after the "#"
        >>> remark_formatted
        'comment 11\n# comment 12\n# comment 13'
        >>>
    """
    remarks = re.findall(RE_MULTILINE_REMARK, remark)
    # remarks that don't have a subsequent comment are not captured by regex
    if not remarks:
        remarks = (("", remark),)
    # Example remarks: [('comment \n#', '      comment2 '), ('\n  #', 'comment3 # 9')]
    remark_formatted = "".join([entry[0] + " " + entry[1].strip() for entry in remarks])
    return remark_formatted


def ensure_space_after_octothorpe(comment):
    """
    Ensures a single space is between the "#" and first letter of a comment.

    Args:
        comment (ruamel.yaml.token.CommentToken): The comment to update.

    Returns:
        None: The comment is updated in place.

    Example:
        >>> yml = ruamel.yaml.YAML()
        >>> with open("test.yml", encoding="utf-8") as fh:
        ...     print(fh.read())
        ...     fh.seek(0)
        ...     data = yml.load(fh)
        ...
        ---
        a: 5 # comment 1
        b: 6 #comment 2
        #comment 3
        c:
          - 7 #comment 4
        #comment 5
          - 8
        #comment 6
        d:
          #comment 7
          e: a #comment 8
          f:
            - 9
            #comment 9
            - 10
            - a:
                a: 8
                #comment 10
                b: 1
            - b: 1
            - 9
        #comment 11
        #        comment 12
        #comment 13

        >>> type(data)
        <class 'ruamel.yaml.comments.CommentedMap'>
        >>> comment = data.ca.items["b"][2]
        >>> comment
        CommentToken('#comment 2\n#comment 3\n', line: 2, col: 5)
        >>> ensure_space_after_octothorpe(comment)
        >>> # Both comments within the CommentToken object
        >>> # now have a space between the "#" and the first symbol
        >>> comment
        CommentToken('# comment 2\n# comment 3\n', line: 2, col: 5)
        >>>
    """
    if comment is not None:
        # Comments can start with whitespace,
        # so partition is used to preserve that in the final result
        space, octothorpe, remark = comment.value.partition("#")
        remark_formatted = ensure_spacing_for_multiline_comment(remark)
        comment.value = f"{space}# {remark_formatted.lstrip()}\n"


def ensure_space_comments(comments):
    """
    Ensures there is a space after the "#" in comments.

    Args:
        comments (iter): The comments from ruamel.yaml.YAML() object.

    Returns:
         None: Comments are update in place.

    Example:
        >>> yml = ruamel.yaml.YAML()
        >>> with open("test.yml", encoding="utf-8") as fh:
        ...     print(fh.read())
        ...     fh.seek(0)
        ...     data = yml.load(fh)
        ...
        ---
        a: 5 # comment 1
        b: 6 #comment 2
        #comment 3
        c:
          - 7 #comment 4
        #comment 5
          - 8
        #comment 6
        d:
          #comment 7
          e: a #comment 8
          f:
            - 9
            #comment 9
            - 10
            - a:
                a: 8
                #comment 10
                b: 1
            - b: 1
            - 9
        #comment 11
        #        comment 12
        #comment 13

        >>> type(data)
        <class 'ruamel.yaml.comments.CommentedMap'>
        >>> comments = data.ca.items.values()
        >>> comments
        dict_values([
            [None, None, CommentToken('# comment 1\n', line: 1, col: 5), None],
            [None, None, CommentToken('#comment 2\n#comment 3\n', line: 2, col: 5), None],
            [None, None, None, [CommentToken('#comment 7\n', line: 10, col: 2)]]
        ])
        >>> ensure_space_comments(comments)
        >>> # Every comment now has a space between the "#" and the first symbol
        >>> comments
        dict_values([
            [None, None, CommentToken('# comment 1\n', line: 1, col: 5), None],
            [None, None, CommentToken('# comment 2\n# comment 3\n', line: 2, col: 5), None],
            [None, None, None, [CommentToken('# comment 7\n', line: 10, col: 2)]]
        ])
        >>>
    """
    comment_objects = (comment for comment_list in comments for comment in comment_list)
    for comment in comment_objects:
        # Some comments are nested inside an additional list
        if not isinstance(comment, list):
            ensure_space_after_octothorpe(comment)
        else:
            for cmt in comment:
                ensure_space_after_octothorpe(cmt)


def update_yaml_comments(yaml_object):
    """
    Ensures comments have a space after the "#" on itself and its entries

    Args:
        yaml_object (ruamel.yaml.comments.CommentedMap | ruamel.yaml.comments.CommentedSeq): The list or dict object.

    Returns:
        None: Comments are updated in place.

    Example:
        >>> yml = ruamel.yaml.YAML()
        >>> with open("test.yml", encoding="utf-8") as fh:
        ...     print(fh.read())
        ...     fh.seek(0)
        ...     data = yml.load(fh)
        ...
        ---
        a: 5 # comment 1
        b: 6 #comment 2
        #comment 3
        c:
          - 7 #comment 4
        #comment 5
          - 8
        #comment 6
        d:
          #comment 7
          e: a #comment 8
          f:
            - 9
            #comment 9
            - 10
            - a:
                a: 8
                #comment 10
                b: 1
            - b: 1
            - 9
        #comment 11
        #        comment 12
        #comment 13

        >>> type(data)
        <class 'ruamel.yaml.comments.CommentedMap'>
        >>> update_yaml_comments(data)
        >>> with open("test.yml", "w", encoding="utf-8") as fh
        ...     yml.dump(data, fh)
        ...
        >>>
        # Notice that comments now have a space between the hash and first symbol.
        >>> with open("test.yml", encoding="utf-8") as fh:
        ...     print(fh.read())
        ...
        a: 5 # comment 1
        b: 6 # comment 2
        #comment 3
        c:
        - 7   # comment 4
        #comment 5
        - 8
        # comment 6
        d:
          # comment 7
          e: a # comment 8
          f:
          - 9
            # comment 9
          - 10
          - a:
              a: 8
                # comment 10
              b: 1
          - b: 1
          - 9
        # comment 11
        # comment 12
        # comment 13

        >>>
    """
    comments = yaml_object.ca.items.values()
    ensure_space_comments(comments)
    try:
        yaml_object_values = yaml_object.values()
    except AttributeError:
        yaml_object_values = yaml_object

    for entry in yaml_object_values:
        if isinstance(entry, dict) or isinstance(entry, list):
            update_yaml_comments(entry)

'''
