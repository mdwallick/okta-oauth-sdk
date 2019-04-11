import json
import logging
import os
import sys

from .util.exceptions import *
from .jwt import JwtVerifier

"""
Usage: python3 -m okta-jwt <base64 encoded JWT>
"""
def main():
    jwt = sys.argv[1]

    try:
        oktaJwt = JwtVerifier()
        decoded_jwt = oktaJwt.decode(jwt)
        print("decoded_jwt: {0}".format(json.dumps(decoded_jwt, indent=4, sort_keys=True)))

        if oktaJwt.introspect(jwt):
            print("Issuer reports the token is still valid.")
        else:
            print("Issuer reports the token is no longer valid.")

    except ExpiredTokenError:
        print("JWT signature is valid, but the token has expired!")

    except InvalidSignatureError:
        print("JWT signature validation failed!")

if __name__ == "__main__":
    main()
