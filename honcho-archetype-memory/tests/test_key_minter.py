import subprocess
import pytest
from harness.key_minter import mint_peer_token, MintError

class _Result:
    def __init__(self, rc, out="", err=""):
        self.returncode, self.stdout, self.stderr = rc, out, err

def test_builds_correct_command_and_returns_token():
    captured = {}
    def fake_run(cmd, cwd, capture_output, text):
        captured["cmd"], captured["cwd"] = cmd, cwd
        return _Result(0, out="  the.jwt.token  \n")
    token = mint_peer_token("/repos/honcho", "paths-of-reverence", "the-tower", runner=fake_run)
    assert token == "the.jwt.token"
    assert captured["cwd"] == "/repos/honcho"
    assert captured["cmd"][1].endswith("generate_jwt.py")
    assert "--peer" in captured["cmd"] and "the-tower" in captured["cmd"]
    assert "--workspace" in captured["cmd"] and "paths-of-reverence" in captured["cmd"]
    assert "--expires" not in captured["cmd"]   # non-expiring

def test_raises_on_nonzero_exit():
    def fake_run(cmd, cwd, capture_output, text):
        return _Result(1, err="bad secret")
    with pytest.raises(MintError) as exc:
        mint_peer_token("/repos/honcho", "ws", "p", runner=fake_run)
    assert "bad secret" in str(exc.value)
