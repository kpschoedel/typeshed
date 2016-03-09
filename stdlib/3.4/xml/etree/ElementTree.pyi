# Stubs for xml.etree.ElementTree (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, AnyStr, Union, IO, Callable, Dict, List, Tuple, Sequence, Iterator, TypeVar, Optional, KeysView, ItemsView, Generator
import io

VERSION = ... # type: str

class ParseError(SyntaxError): ...

def iselement(element: 'Element') -> bool: ...

_Ss = TypeVar('_Ss', str, bytes)
_T = TypeVar('_T')
_str_or_bytes = Union[str, bytes]

class Element:
    tag = ... # type: _str_or_bytes
    attrib = ... # type: Dict[_str_or_bytes, _str_or_bytes]
    text = ... # type: Optional[_str_or_bytes]
    tail = ... # type: Optional[_str_or_bytes]
    def __init__(self, tag: Union[AnyStr, Callable[..., 'Element']], attrib: Dict[AnyStr, AnyStr]=..., **extra: Dict[str, AnyStr]) -> None: ...
    def append(self, subelement: 'Element') -> None: ...
    def clear(self) -> None: ...
    def copy(self) -> 'Element': ...
    def extend(self, elements: Sequence['Element']) -> None: ...
    def find(self, path: str, namespaces: Dict[str, str]=...) -> Optional['Element']: ...
    def findall(self, path: str, namespaces: Dict[str, str]=...) -> List['Element']: ...
    def findtext(self, path: str, default: _T=..., namespaces: Dict[str, str]=...) -> Union[_T, str]: ...
    def get(self, key: AnyStr, default: _T=...) -> Union[AnyStr, _T]: ...
    def getchildren(self) -> List['Element']: ...
    def getiterator(self, tag: Union[str, AnyStr]=...) -> List['Element']: ...
    def insert(self, index: int, subelement: 'Element') -> None: ...
    def items(self) -> ItemsView[AnyStr, AnyStr]: ...
    def iter(self, tag: Union[str, AnyStr]=...) -> Generator['Element', None, None]: ...
    def iterfind(self, path: str, namespaces: Dict[str, str]=...) -> List['Element']: ...
    def itertext(self) -> Generator[str, None, None]: ...
    def keys(self) -> KeysView[AnyStr]: ...
    def makeelement(self, tag: _Ss, attrib: Dict[_Ss, _Ss]) -> 'Element': ...
    def remove(self, subelement: 'Element') -> None: ...
    def set(self, key: AnyStr, value: AnyStr) -> None: ...
    def __bool__(self) -> bool: ...
    def __delitem__(self, index: int) -> None: ...
    def __getitem__(self, index) -> 'Element': ...
    def __len__(self) -> int: ...
    def __setitem__(self, index: int, element: 'Element') -> None: ...

def SubElement(parent: Element, tag: AnyStr, attrib: Dict[AnyStr, AnyStr]=..., **extra: Dict[str, AnyStr]) -> Element: ...
def Comment(text: _str_or_bytes=...) -> Element: ...
def ProcessingInstruction(target: str, text: str=...) -> Element: ...

PI = ... # type: Callable[..., Element]

class QName:
    text = ... # type: str
    def __init__(self, text_or_uri: str, tag: str=...) -> None: ...


_file_or_filename = Union[str, bytes, int, IO[Any]]

class ElementTree:
    def __init__(self, element: Element=..., file: _file_or_filename=...) -> None: ...
    def getroot(self) -> Element: ...
    def parse(self, source: _file_or_filename, parser: 'XMLParser'=...) -> Element: ...
    def iter(self, tag: Union[str, AnyStr]=...) -> Generator[Element, None, None]: ...
    def getiterator(self, tag: Union[str, AnyStr]=...) -> List[Element]: ...
    def find(self, path: str, namespaces: Dict[str, str]=...) -> Optional[Element]: ...
    def findtext(self, path: str, default: _T=..., namespaces: Dict[str, str]=...) -> Union[_T, str]: ...
    def findall(self, path: str, namespaces: Dict[str, str]=...) -> List[Element]: ...
    def iterfind(self, path: str, namespaces: Dict[str, str]=...) -> List[Element]: ...
    def write(self, file_or_filename: _file_or_filename, encoding: str=..., xml_declaration: Optional[bool]=..., default_namespace: str=..., method: str=..., *, short_empty_elements: bool=...) -> None: ...
    def write_c14n(self, file: _file_or_filename) -> None: ...

def register_namespace(prefix: str, uri: str) -> None: ...
def tostring(element: Element, encoding: str=..., method: str=..., *, short_empty_elements: bool=...) -> str: ...

class _ListDataStream(io.BufferedIOBase):
    lst = ... # type: List[str]
    def __init__(self, lst) -> None: ...
    def writable(self) -> bool: ...
    def seekable(self) -> bool: ...
    def write(self, b: str) -> None: ...
    def tell(self) -> int: ...

def tostringlist(element: Element, encoding: str=..., method: str=..., *, short_empty_elements: bool=...) -> List[str]: ...
def dump(elem: Element) -> None: ...
def parse(source: _file_or_filename, parser: 'XMLParser'=...) -> ElementTree: ...
def iterparse(source: _file_or_filename, events: Sequence[str]=..., parser: 'XMLParser'=...) -> Iterator[Tuple[str, Element]]: ...

class XMLPullParser:
    def __init__(self, events: Sequence[str]=..., *, _parser: 'XMLParser'=...) -> None: ...
    def feed(self, data: bytes) -> None: ...
    def close(self) -> None: ...
    def read_events(self) -> Iterator[Tuple[str, Element]]: ...

class _IterParseIterator:
    root = ... # type: Any
    def __init__(self, source: _file_or_filename, events: Sequence[str], parser: 'XMLParser', close_source: bool=...) -> None: ...
    def __next__(self) -> Tuple[str, Element]: ...
    def __iter__(self) -> _IterParseIterator: ...

def XML(text: AnyStr, parser: 'XMLParser'=...) -> Element: ...
def XMLID(text: AnyStr, parser: 'XMLParser'=...) -> Tuple[Element, Dict[str, Element]]: ...

# TODO-improve this type
fromstring = ... # type: Callable[..., Element]

def fromstringlist(sequence: Sequence[AnyStr], parser: 'XMLParser'=...) -> Element: ...

class TreeBuilder:
    def __init__(self, element_factory: Callable[[AnyStr, Dict[AnyStr, AnyStr]], Element]=...) -> None: ...
    def close(self) -> Element: ...
    def data(self, data: AnyStr) -> None: ...
    def start(self, tag: AnyStr, attrs: Dict[AnyStr, AnyStr]) -> Element: ...
    def end(self, tag: AnyStr) -> Element: ...

class XMLParser:
    parser = ... # type: Any
    target = ... # type: TreeBuilder
    # TODO-what is entity used for???
    entity = ... # type: Any
    version = ... # type: str
    def __init__(self, html: int=..., target: TreeBuilder=..., encoding: str=...) -> None: ...
    def doctype(self, name: str, pubid: str, system: str) -> None: ...
    def close(self) -> Any: ...  # TODO-most of the time, this will be Element, but it can be anything target.close() returns
    def feed(self, data: AnyStr)-> None: ...
