import istools.ipsec_secrets

import hmac
import os
import sys

def read_auth_user_pass_verify():
    """
    Reads credentials passed to OpenVPN auth-user-pass-verify script
    as a (username, password) tuple. You will need the following lines
    in your OpenVPN server config:

    auth-user-pass-verify <path-to-script> via-file
    script-security 2

    See OpenVPN manual: https://openvpn.net/man.html
    """
    with open(sys.argv[1], "r") as f:
        [username, password] = [l.rstrip() for l in f.readlines()]
    return (username, password)

def main():
    """
    Authorizes OpenVPN users against ipsec.secrets(5) file.
    """
    try:
        (username, password) = read_auth_user_pass_verify()
    except:
        print("This tool is only for OpenVPN auth-user-pass-verify-script"
              " in via-file mode.", file=sys.stderr)
        exit(2)

    with open(os.getenv("ISTOOLS_IPSEC_SECRETS_PATH"), "r") as f:
        access = {secret["left"]: secret["right"]
                  for secret in map(ipsec_secrets.read_line, f.readlines())
                  if ipsec_secrets.is_password(secret)}

    sys.exit(int(not hmac.compare_digest(access[username], password)))

if __name__ == '__main__':
    main()
