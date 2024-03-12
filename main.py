from dataclasses import dataclass, field, is_dataclass, asdict
from typing import List, Optional
import json

class DataclassJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if is_dataclass(o):
            return asdict(o)
        return super().default(o)

@dataclass
class Color:
    value: str  # Expected in hex format, e.g. "#FFFFFF"

@dataclass
class Node:
    id: str
    type: str
    x: int
    y: int
    width: int
    height: int

@dataclass
class TextNode(Node):
    text: str
    color: Optional[Color] = None

@dataclass
class FileNode(Node):
    file: str
    subpath: Optional[str] = None
    color: Optional[Color] = None

@dataclass
class LinkNode(Node):
    url: str
    color: Optional[Color] = None

@dataclass
class GroupNode(Node):
    label: Optional[str] = None
    background: Optional[str] = None
    backgroundStyle: Optional[str] = None
    color: Optional[Color] = None

@dataclass
class Edge:
    id: str
    fromNode: str
    toNode: str
    fromSide: Optional[str] = None
    fromEnd: Optional[str] = None
    toSide: Optional[str] = None
    toEnd: Optional[str] = None
    color: Optional[Color] = None
    label: Optional[str] = None

@dataclass
class Canvas:
    nodes: Optional[List[Node]] = field(default_factory=list)
    edges: Optional[List[Edge]] = field(default_factory=list)

# Example usage:
color_red = Color("#FF0000")
text_node = TextNode(text="Hello", id="1", type="text", x=10, y=20, width=100, height=50, color=color_red)

# Similarly, create instances of other nodes and edges as needed...

canvas_data = Canvas(nodes=[text_node], edges=[])  # Add other nodes and edges accordingly

import json

with open("canvas_data.json", "w") as f:
    json.dump(canvas_data, f, cls=DataclassJSONEncoder) 