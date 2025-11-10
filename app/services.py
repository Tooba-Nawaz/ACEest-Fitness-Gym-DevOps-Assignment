# Simple in-memory store for demo/testing purposes.
from .models import make_entry, Entry
from typing import List, Dict

_store: Dict[str, Entry] = {}

def add_entry(user, activity, duration_minutes, category='general'):
    e = make_entry(user, activity, duration_minutes, category)
    _store[e.id] = e
    return e

def get_entry(entry_id):
    return _store.get(entry_id)

def list_entries():
    return list(_store.values())

def delete_entry(entry_id):
    return _store.pop(entry_id, None)

def clear_store():
    _store.clear()
