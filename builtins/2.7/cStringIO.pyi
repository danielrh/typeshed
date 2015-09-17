# Stubs for cStringIO (Python 2.7)
# See https://docs.python.org/2/library/stringio.html

from typing import IO, List, Iterable, Iterator, Any, Union

class StringIO(IO[str]):
    softspace = ... # type: int

    def __init__(self, s: str = None) -> None: ...
    def getvalue(self) -> str: ...
    def close(self) -> None: ...
    @property
    def closed(self) -> bool: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def read(self, size: int = -1) -> str: ...
    def readable(self) -> bool: ...
    def readline(self, size: int = -1) -> str: ...
    def readlines(self, hint: int = -1) -> List[str]: ...
    def seek(self, offset: int, whence: int = ...) -> None: ...
    def seekable(self) -> bool: ...
    def tell(self) -> int: ...
    def truncate(self, size: int = None) -> int:
        raise IOError()
    def writable(self) -> bool: ...
    def writelines(self, lines: Iterable[str]) -> None: ...
    def next(self) -> str: ...
    def __iter__(self) -> "InputType": ...
    def __enter__(self) -> Any: ...
    def __exit__(self, exc_type: type, exc_val: Any, exc_tb: Any) -> Any: ...
    # only StringO:
    def reset() -> None: ...
    def write(self, b: Union[str, unicode]) -> None: ...
    def writelines(self, lines: Iterable[Union[str, unicode]]) -> None: ...

InputType = StringIO
OutputType = StringIO
