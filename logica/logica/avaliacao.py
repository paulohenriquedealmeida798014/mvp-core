# Catalog of Status Codes and Messages for Evaluation Core System

## Success Codes
- **200 OK**: The request has succeeded.

## Client Error Codes
- **400 Bad Request**: The server could not understand the request due to invalid syntax.
- **401 Unauthorized**: The client must authenticate itself to get the requested response.
- **403 Forbidden**: The client does not have access rights to the content.
- **404 Not Found**: The server can not find the requested resource.

## Server Error Codes
- **500 Internal Server Error**: The server has encountered a situation it doesn't know how to handle.
- **502 Bad Gateway**: The server was acting as a gateway or proxy and received an invalid response from the upstream server.
- **503 Service Unavailable**: The server is not ready to handle the request due to temporary overloading or maintenance of the server.

## Custom Status Codes
- **1001 Validation Error**: Indicates that the input data failed validation.
- **1002 Processing Error**: Indicates that there was an error during processing the request.

## Informational Codes
- **100 Continue**: The server has received the request headers, and the client should proceed to send the request body.
# Avaliacao.py

from codigos import some_function  # replace 'some_function' with actual functions you need


def evaluate_something():
    # Your evaluation logic goes here
    pass


def evaluate_another_thing():
    # Your evaluation logic goes here
    pass
