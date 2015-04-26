#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program demonstrates exception class hierarchy."""


class BaseError(Exception):
    """This is the exception superclass, subclassed to Exception.

    Args:
        None
    """
    pass


class StringError(BaseError, TypeError):
    """This is a subclass of the BaseError and TypeError.

    Args:
        None
    """
    pass


class NumberError(BaseError, TypeError):
    """This is a subclass of the BaseError and TypeError.

    Args:
        None
    """
    pass


class NonZeroError(NumberError):
    """This is a subclass of the BaseError and TypeError.

    Args:
        None
    """
    pass
