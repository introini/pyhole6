from dataclasses import dataclass
from typing import Optional, Dict, Any, List
from datetime import datetime


@dataclass
class Session(dict):
    valid: bool
    sid: str|None
    validity: int
    totp: bool
    csrf: str|None
    message: Optional[str] = None

@dataclass
class StatsEntry(dict):
    pass

@dataclass
class BlockingStatus:
    enabled: bool
    timer: Optional[int] = None

@dataclass
class HostInfo:
    # Add relevant fields
    pass

@dataclass
class VersionInfo:
    # Add relevant fields
    pass

@dataclass
class HistoryEntry:
    timestamp: datetime
    total: int
    cached: int
    blocked: int
    forwarded: int | None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'HistoryEntry':
        return cls(
            timestamp=datetime.fromtimestamp(data.get('timestamp', 0)),
            total=data.get('total', 0),
            cached=data.get('cached', 0),
            blocked=data.get('blocked', 0),
            forwarded=data.get('forwarded', 0)
        )

@dataclass
class HistoryDBEntry(dict):
    pass
