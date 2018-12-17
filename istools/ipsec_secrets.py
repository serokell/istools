def read_line(s):
    """
    Reads one line in ipsec.secrets(5) format and returns a dictionary
    with left, right, and auth-type keys. Caveat: very simplistic, does
    not handle includes, non-quoted passwords, inlined RSA, ... Also
    requires that : between username and auth_type is space-delimeted
    from both sides.
    """
    [username, _, auth_type, password] = s.rstrip().split()
    return {"auth_type": auth_type,
            "username": left,
            "password": right}

def write_line(secret):
    return '{username} : {auth_type} "{password}"'.format(**secret)

password_auth_types = ['EAP', 'PSK']

def is_password(secret):
    """
    ipsec.secrets will also contain path to private key for
    the certificate, so this function filters out secrets that are
    not EAP or PSK plaintext secrets.
    """
    return (secret["auth_type"] in password_auth_types and
            secret["username"] != "" and
            secret["password"] != "")
