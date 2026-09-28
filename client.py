"""Shamir's (k, n) Threshold Secret Sharing Engine.
100% Python Standard Library.
"""

import secrets

class ShamirSecretSharing:
    """Shamir's (k, n) threshold secret sharing over prime field."""
    PRIME = 2**127 - 1

    def __init__(self, threshold=3, total_shares=5):
        self.k = threshold
        self.n = total_shares

    def split_secret(self, secret):
        coeffs = [secret] + [secrets.randbelow(self.PRIME - 1) + 1 for _ in range(self.k - 1)]
        shares = []
        for x in range(1, self.n + 1):
            y = 0
            for power, c in enumerate(coeffs):
                y = (y + c * pow(x, power, self.PRIME)) % self.PRIME
            shares.append((x, y))
        return shares

    def recover_secret(self, shares):
        secret = 0
        for i, (xi, yi) in enumerate(shares):
            num = 1
            den = 1
            for j, (xj, _) in enumerate(shares):
                if i != j:
                    num = (num * (-xj)) % self.PRIME
                    den = (den * (xi - xj)) % self.PRIME
            den_inv = pow(den, self.PRIME - 2, self.PRIME)
            li = (num * den_inv) % self.PRIME
            secret = (secret + yi * li) % self.PRIME
        return secret
