# Shamir's (k, n) Secret Sharing Skill

High-efficiency, zero-dependency Python implementation of **Shamir's (k, n) Threshold Secret Sharing**.

## Features
- **Information-Theoretic Security**: Any \(k - 1\) shares reveal zero information regarding the underlying secret.
- **Lagrange Interpolation**: Reconstructs secret in \(O(k^2)\) modular operations over Mersenne prime \(2^{127} - 1\).
- **Zero External Dependencies**: Pure Python standard library (`secrets`).
- **Native MCP Protocol**: JSON-RPC 2.0 stdio server compatible with Claude Desktop, Cursor, and Windsurf.

## Architecture
```mermaid
graph TD
    Secret["Master Secret S"] --> Poly["Random Polynomial f(x) = S + a1*x + ... + ak-1*x^(k-1)"]
    Poly --> S1["Share (1, f(1))"]
    Poly --> S2["Share (2, f(2))"]
    Poly --> S3["Share (3, f(3))"]
    S1 & S2 & S3 --> Interp["Lagrange Interpolation at x=0"]
    Interp --> Secret
```
