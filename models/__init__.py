#!/usr/bin/python3
"""makes the folder into a package"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
