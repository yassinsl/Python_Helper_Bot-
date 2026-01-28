from typing import Dict, Any
import time
import requests

ttl_seconds = 600
cache: Dict[str, Dict[str, Any]] = {}

Methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "CONNECT", "TRACE"]


def handle_get(cache_key: str, endpoint: str, params: Dict[str, str]) -> None:
    now = time.time()

    # 1) Cache HIT (fresh)
    if cache_key in cache:
        entry = cache[cache_key]
        if now < entry["expires_at"]:
            print("CACHE HIT")
            print(entry["data"])
            return

    # 2) Cache MISS or STALE => request
    response = requests.get(endpoint, params=params, timeout=15)

    if not response.ok:
        raise ValueError(f"HTTP {response.status_code} {response.reason}")

    data = response.json()

    # 3) Store in cache
    saved_at = time.time()
    cache[cache_key] = {
        "data": data,
        "saved_at": saved_at,
        "expires_at": saved_at + ttl_seconds,
    }

    print("CACHE MISS (fetched)")
    print(data)


def handel_post(cache_key: str, endpoint: str, params: Dict[str, str]) -> None:
    raise ValueError("POST not implemented yet")


def handel_put(cache_key: str, endpoint: str, params: Dict[str, str]) -> None:
    raise ValueError("PUT not implemented yet")


def handel_delete(cache_key: str, endpoint: str, params: Dict[str, str]) -> None:
    raise ValueError("DELETE not implemented yet")


def handel_head(cache_key: str, endpoint: str, params: Dict[str, str]) -> None:
    pass
def handel_options(cache_key: str, endpoint: str, params: Dict[str, str]) -> None:
    pass
def handel_connect(cache_key: str, endpoint: str, params: Dict[str, str]) -> None:
    pass
def handel_trace(cache_key: str, endpoint: str, params: Dict[str, str]) -> None:
    pass
METHODS_DISPATCH = {
    "GET": handle_get,
    "POST": handel_post,
    "PUT": handel_put,
    "DELETE": handel_delete,
    "HEAD": handel_head,
    "OPTIONS": handel_options,
    "CONNECT": handel_connect,
    "TRACE": handel_trace,
}

def handel_and_display_data(cache_key: str, method: str, endpoint: str, params: Dict[str, str]) -> None:
    handler = METHODS_DISPATCH.get(method)
    if not handler:
        raise ValueError(f"Unsupported method: {method}")
    handler(cache_key, endpoint, params)
def Build_key_request(method: str, endpoint: str, params: Dict[str, str]) -> str:
    parts = []
    for k in sorted(params.keys()):
        parts.append(f"{k}={params[k]}")
    normalize_params = "&".join(parts)
    return f"{method} | {endpoint} | {normalize_params}"
def parse_endpoint(endpoint: str) -> str:
    endpoint = endpoint.strip()
    if not endpoint:
        raise ValueError("Empty endpoint")
    return endpoint
def parse_method(method: str) -> str:
    method = method.strip().upper()
    if not method:
        raise ValueError("Empty method")
    if method not in Methods:
        raise ValueError(f"Invalid method: {method}. Allowed: {Methods}")
    return method
def main() -> None:
    params: Dict[str, str] = {}
    method = input("Give me a method name want to use: ")
    endpoint = input("Give me a endpoint need it: ")

    while True:
        key = input("please the param key: ").strip()
        value = input("please the param value: ").strip()
        if not key or not value:
            break
        params[key] = value

        stop = input("if want stop just enter 1: ").strip()
        if stop == "1":
            break
    try:
        method = parse_method(method)
        endpoint = parse_endpoint(endpoint)

        cache_key = Build_key_request(method, endpoint, params)
        handel_and_display_data(cache_key, method, endpoint, params)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
