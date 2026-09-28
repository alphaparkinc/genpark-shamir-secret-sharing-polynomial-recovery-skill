import sys
import json
from client import ShamirSecretSharing

sss = ShamirSecretSharing(threshold=3, total_shares=5)

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "shamir_secret_op",
                        "description": "Split secret into (k, n) shares or recover secret from k shares",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "action": {"type": "string", "enum": ["split", "recover"]},
                                "secret": {"type": "integer"},
                                "shares": {
                                    "type": "array",
                                    "items": {"type": "array", "items": {"type": "integer"}}
                                }
                            },
                            "required": ["action"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "shamir_secret_op":
            act = args["action"]
            if act == "split":
                shs = sss.split_secret(int(args["secret"]))
                return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"shares": shs})}]}}
            elif act == "recover":
                shs = [tuple(s) for s in args["shares"]]
                sec = sss.recover_secret(shs)
                return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"recovered_secret": sec})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
