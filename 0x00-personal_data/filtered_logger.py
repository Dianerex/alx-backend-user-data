#!/usr/bin/env python3

""" Module to obfuscate sensitive fields in log messages """

import re
from typing import List

class RedactingFormatter:
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        """ Initializes the RedactingFormatter """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record) -> str:
        """ Returns filtered values from log records """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


PII_FIELDS = ("name", "email", "password", "ssn", "phone")

def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Returns regex obfuscated log messages """
    for field in fields:
        message = re.sub(rf'{field}=(.*?){separator}',
                         rf'{field}={redaction}{separator}', message)
    return message
