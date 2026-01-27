from typing import List ,Dict, Any
import sys
def Build_key_request(method : str, endpoint: str, params: Dict[Any, Any])->None:
    normalize_params = ""
    for key, value in params.items():
        normalize_params+= (key + "=" + value)
        normalize_params += "&"
    normalize_params = normalize_params.rstrip("&");
    key = method + " | " + endpoint + " | " + normalize_params; 
def parse_endpoint(endpoint :str)-> str:
    endpoint = endpoint.strip();
    if not endpoint:
        raise("Empty endpoint");
    return endpoint;
def parse_method(method: str)->str:
    Methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "CONNECT", "TRACE"]
    method = method.strip();
    if method == "":
        raise ValueError("Empty value !!");
    check = next(check for check in Methods if check == method, None);
    if not check:
        raise ValueError(f"This Method : {method} in {Methods}") 
    return method;
def main():
    #TODO: parse Input;
    params= {}    
    method = input("Give me a method name want to use: ");
    endpoint = input("Give me a enpoint need it");
    while True:
        key = input("please the param need to change or get: ").strip();
        value = input("please the param need to change or get: ").strip();
        if not key or not value: break;
        params[key] = value;
        stop = int(input("if want stop just enter 1: "))
        if not stop or stop == 1:
            break;
    try:
        method = parse_method(method);
        endpoint = parse_endpoint(endpoint)
        Build_key_request(method, endpoint, param);
    except ValueError as e:
        print(f"Error : {e}")
if __name__ == "__main__":
    main()
