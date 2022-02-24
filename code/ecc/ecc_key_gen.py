from tinyec import registry
import secrets
from util import *

def generate_key_low_level():
    curve = registry.get_curve('secp256r1')

    privKey = secrets.randbelow(curve.field.n)
    pubKey = privKey * curve.g

    print(f"\U0001F449 Curve: {curve}\n")
    print(f"\U0001F449 n: {yellow}{curve.field.n}{default}")
    print(f"\U0001F449 Generator point: ({green}{curve.g.x}, {purple}{curve.g.y}{default})")
    print(f"\U0001F449 private key: {blue}{privKey}{default}")
    print(f"\U0001F449 public key: ({green}{pubKey.x}, {purple}{pubKey.y}{default})")


if __name__ == '__main__':
    generate_key_low_level()