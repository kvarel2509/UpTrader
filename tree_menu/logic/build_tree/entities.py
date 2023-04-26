from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class MenuItem:
    title: str
    link: Optional[str] = None
    visible: bool = False
    active: bool = False
    parent: Optional[MenuItem] = None
    children: List[MenuItem] = field(default_factory=list)

    def add_child(self, child: MenuItem):
        self.children.append(child)
