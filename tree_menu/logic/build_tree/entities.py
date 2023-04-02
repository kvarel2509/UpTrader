from __future__ import annotations
from typing import Optional, Sequence


class MenuItem:
    def __init__(
            self,
            title: str,
            link: Optional[str]=None,
            visible: bool=False,
            active: bool=False,
            parent: Optional[MenuItem]=None,
            children: Sequence[MenuItem]=None
        ) -> None:
        self.title = title
        self.link = link
        self.visible = visible
        self.active = active
        self.parent = parent

        if children is None:
            children = []

        self.children = children

    
    def add_child(self, child: MenuItem):
        self.children.append(child)
