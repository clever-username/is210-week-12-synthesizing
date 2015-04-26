#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program demonstrates exception class hierarchy."""


class CustomError(Exception):
    """This is the exception superclass, subclassed to Exception.

    Args:
        None
    """
    def __init__(self, value, cause='default'):
        """This is the CustomError class constructor.

            Args:
                value(mixed): Value passed as parameter.
                cause(str): OPTIONAL value parameter.
            Attribute:
                value(mixed): Value passed as parameter.
                cause(str): OPTIONAL value parameter.
            Returns:
                Returns attribute values.
            Examples:
                >>> myerr = CustomError('Whoah!', cause='Messed up!')
                >>> print myerr.cause
                Messed up!
        """
        Exception.__init__(self, value)
        self.cause = cause
