from dataclasses import dataclass
from typing import List, Optional, Dict

@dataclass
class HolderChange:
    name: str
    position: Optional[str] = None
    change_pct: Optional[str] = None
    filing_date: Optional[str] = None
    meta: Optional[Dict] = None

@dataclass
class InstitutionalData:
    top_holders: List[HolderChange]
    hedge_fund_activity: List[HolderChange]
