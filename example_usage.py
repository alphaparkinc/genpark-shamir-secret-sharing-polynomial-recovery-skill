from client import ShamirSecretSharing

sss = ShamirSecretSharing(threshold=3, total_shares=5)
secret = 123456789012345
shares = sss.split_secret(secret)
print(f"Generated {len(shares)} shares:")
for s in shares:
    print(" ", s)

reconstructed = sss.recover_secret(shares[:3])
print("Reconstructed secret:", reconstructed)
