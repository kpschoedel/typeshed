import socket
from _socket import _Address, _RetAddress
from _typeshed import Incomplete, ReadableBuffer
from collections.abc import Callable, MutableSequence, Sequence
from typing import Any, TypeVar

from OpenSSL.crypto import X509, PKey, X509Name

OPENSSL_VERSION_NUMBER: int
SSLEAY_VERSION: int
SSLEAY_CFLAGS: int
SSLEAY_PLATFORM: int
SSLEAY_DIR: int
SSLEAY_BUILT_ON: int

SENT_SHUTDOWN: int
RECEIVED_SHUTDOWN: int

SSLv23_METHOD: int
TLSv1_METHOD: int
TLSv1_1_METHOD: int
TLSv1_2_METHOD: int

TLS_METHOD: int
TLS_SERVER_METHOD: int
TLS_CLIENT_METHOD: int

SSL3_VERSION: int
TLS1_VERSION: int
TLS1_1_VERSION: int
TLS1_2_VERSION: int
TLS1_3_VERSION: int

OP_NO_SSLv2: int
OP_NO_SSLv3: int
OP_NO_TLSv1: int
OP_NO_TLSv1_1: int
OP_NO_TLSv1_2: int
OP_NO_TLSv1_3: int

MODE_RELEASE_BUFFERS: int

OP_SINGLE_DH_USE: int
OP_SINGLE_ECDH_USE: int
OP_EPHEMERAL_RSA: int
OP_MICROSOFT_SESS_ID_BUG: int
OP_NETSCAPE_CHALLENGE_BUG: int
OP_NETSCAPE_REUSE_CIPHER_CHANGE_BUG: int

OP_SSLREF2_REUSE_CERT_TYPE_BUG: int
OP_MICROSOFT_BIG_SSLV3_BUFFER: int
OP_MSIE_SSLV2_RSA_PADDING: int
OP_SSLEAY_080_CLIENT_DH_BUG: int
OP_TLS_D5_BUG: int
OP_TLS_BLOCK_PADDING_BUG: int
OP_DONT_INSERT_EMPTY_FRAGMENTS: int
OP_CIPHER_SERVER_PREFERENCE: int
OP_TLS_ROLLBACK_BUG: int
OP_PKCS1_CHECK_1: int
OP_PKCS1_CHECK_2: int
OP_NETSCAPE_CA_DN_BUG: int
OP_NETSCAPE_DEMO_CIPHER_CHANGE_BUG: int

OP_NO_COMPRESSION: int

OP_NO_QUERY_MTU: int
OP_COOKIE_EXCHANGE: int
OP_NO_TICKET: int

OP_ALL: int

VERIFY_PEER: int
VERIFY_FAIL_IF_NO_PEER_CERT: int
VERIFY_CLIENT_ONCE: int
VERIFY_NONE: int

SESS_CACHE_OFF: int
SESS_CACHE_CLIENT: int
SESS_CACHE_SERVER: int
SESS_CACHE_BOTH: int
SESS_CACHE_NO_AUTO_CLEAR: int
SESS_CACHE_NO_INTERNAL_LOOKUP: int
SESS_CACHE_NO_INTERNAL_STORE: int
SESS_CACHE_NO_INTERNAL: int

SSL_ST_CONNECT: int
SSL_ST_ACCEPT: int
SSL_ST_MASK: int

SSL_CB_LOOP: int
SSL_CB_EXIT: int
SSL_CB_READ: int
SSL_CB_WRITE: int
SSL_CB_ALERT: int
SSL_CB_READ_ALERT: int
SSL_CB_WRITE_ALERT: int
SSL_CB_ACCEPT_LOOP: int
SSL_CB_ACCEPT_EXIT: int
SSL_CB_CONNECT_LOOP: int
SSL_CB_CONNECT_EXIT: int
SSL_CB_HANDSHAKE_START: int
SSL_CB_HANDSHAKE_DONE: int

NO_OVERLAPPING_PROTOCOLS: object

class Error(Exception): ...
class WantReadError(Error): ...
class WantWriteError(Error): ...
class WantX509LookupError(Error): ...
class ZeroReturnError(Error): ...
class SysCallError(Error): ...

def SSLeay_version(type: int) -> str: ...

class Session: ...

class Connection:
    def __getattr__(self, name: str) -> Any: ...  # takes attributes from `self._socket`
    def __init__(self, context: Context, socket: socket.socket | None = ...) -> None: ...
    def get_context(self) -> Context: ...
    def set_context(self, context: Context) -> None: ...
    def get_servername(self) -> bytes | None: ...
    def set_tlsext_host_name(self, name: bytes) -> None: ...
    def pending(self) -> int: ...
    def send(self, buf: ReadableBuffer | str, flags: int = ...) -> int: ...
    write = send
    def sendall(self, buf: ReadableBuffer | str, flags: int = ...) -> int: ...
    def recv(self, bufsiz: int, flags: int | None = ...) -> bytes: ...
    read = recv
    def recv_into(self, buffer: MutableSequence[int], nbytes: int | None = ..., flags: int | None = ...) -> int: ...
    def connect(self, addr: str | bytes | Sequence[str | int]) -> None: ...
    def connect_ex(self, addr: _Address | bytes) -> int: ...
    def accept(self) -> tuple[Connection, _RetAddress]: ...
    def DTLSv1_listen(self) -> None: ...
    def DTLSv1_get_timeout(self) -> float | None: ...
    def DTLSv1_handle_timeout(self) -> bool: ...
    def shutdown(self) -> bool: ...
    def do_handshake(self) -> None: ...
    def get_certificate(self) -> X509 | None: ...
    def get_peer_certificate(self) -> X509 | None: ...
    def get_peer_cert_chain(self) -> list[X509] | None: ...
    def get_verified_chain(self) -> list[X509] | None: ...
    def bio_read(self, bufsiz: int) -> bytes: ...
    def bio_write(self, buf: bytes) -> int: ...
    def bio_shutdown(self) -> None: ...
    def renegotiate(self) -> bool: ...
    def renegotiate_pending(self) -> bool: ...
    def total_renegotiations(self) -> int: ...
    def set_accept_state(self) -> None: ...
    def set_connect_state(self) -> None: ...
    def get_client_ca_list(self) -> list[X509Name]: ...
    def get_cipher_list(self) -> list[str]: ...
    def get_cipher_name(self) -> str | None: ...
    def get_cipher_bits(self) -> int | None: ...
    def get_cipher_version(self) -> str | None: ...
    def get_protocol_version_name(self) -> str: ...
    def get_protocol_version(self) -> int: ...
    def get_shutdown(self) -> int: ...
    def set_shutdown(self, state: int) -> None: ...
    def get_state_string(self) -> bytes: ...
    def server_random(self) -> bytes | None: ...
    def client_random(self) -> bytes | None: ...
    def master_key(self) -> bytes | None: ...
    def export_keying_material(
        self, label: Incomplete, olen: Incomplete, context: Incomplete = ...
    ) -> Incomplete: ...  # TODO: type, see RFC-5705
    def get_app_data(self) -> Any: ...
    def set_app_data(self, data: Any) -> None: ...
    def sock_shutdown(self, __how: int) -> None: ...  # alias to `_socket.socket.shutdown`
    def want_read(self) -> bool: ...
    def want_write(self) -> bool: ...
    def get_session(self) -> Session | None: ...
    def set_session(self, session: Session) -> None: ...
    def get_finished(self) -> bytes | None: ...
    def get_peer_finished(self) -> bytes | None: ...
    def set_alpn_protos(self, protos: Sequence[bytes]) -> None: ...
    def get_alpn_proto_negotiated(self) -> bytes: ...
    def request_ocsp(self) -> None: ...

_T = TypeVar("_T")

class Context:
    def __getattr__(self, name: str) -> Incomplete: ...
    def __init__(self, method: int) -> None: ...
    def load_verify_locations(self, cafile: str | None, capath: str | None = ...) -> None: ...
    def set_options(self, options: int) -> None: ...
    def set_verify(self, mode: int, callback: Callable[[Connection, X509, int, int, int], bool] | None = ...) -> None: ...
    def set_min_proto_version(self, version: int) -> None: ...
    def set_max_proto_version(self, version: int) -> None: ...
    def use_certificate_chain_file(self, certfile: str | bytes) -> None: ...
    def use_certificate_file(self, certfile: str | bytes, filetype: int = ...) -> None: ...
    def use_certificate(self, cert: X509) -> None: ...
    def use_privatekey_file(self, keyfile: str | bytes, filetype: int | None = ...) -> None: ...
    def use_privatekey(self, pkey: PKey) -> None: ...
    def add_extra_chain_cert(self, certobj: X509) -> None: ...
    def set_cipher_list(self, cipher_list: bytes) -> None: ...
    def set_keylog_callback(self, callback: Callable[[Connection, bytes], object]) -> None: ...
    def set_alpn_protos(self, protos: Sequence[bytes]) -> None: ...
    def set_alpn_select_callback(self, callback: Callable[[Connection, list[bytes]], bytes]) -> None: ...
    def set_ocsp_server_callback(self, callback: Callable[[Connection, _T | None], bytes], data: _T | None = ...) -> None: ...
    def set_ocsp_client_callback(
        self, callback: Callable[[Connection, bytes, _T | None], bool], data: _T | None = ...
    ) -> None: ...
