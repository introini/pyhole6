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
class Statistic:
    # Add relevant fields based on API response
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
    forwarded: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'HistoryEntry':
        return cls(
            timestamp=datetime.fromtimestamp(data['timestamp']),
            total=data['total'],
            cached=data['cached'],
            blocked=data['blocked'],
            forwarded=data['forwarded']
        )

