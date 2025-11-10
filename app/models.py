from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import uuid

@dataclass
class Entry:
    id: str
    user: str
    activity: str
    duration_minutes: int
    category: str = 'general'
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())

def make_entry(user, activity, duration_minutes, category='general'):
    return Entry(id=str(uuid.uuid4()), user=user, activity=activity, duration_minutes=int(duration_minutes), category=category)
