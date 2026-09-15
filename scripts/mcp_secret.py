#!/usr/bin/env python3
"""Resolve {{kc:<account>}} tokens from the macOS login Keychain (service
"claude-mcp") into MCP server subprocess argv/env, or into HTTP headers for
Claude Code's headersHelper. Never prints a secret value.

Compatible with /usr/bin/python3 (3.9).

Usage:
  mcp_secret.py exec -- <command> <args...>
      Substitute {{kc:<account>}} tokens found in argv and in the current
      process environment's values, then exec <command> with the resolved
      argv/env (os.execvp, so PATH lookup still applies to <command>).
  mcp_secret.py headers <Header>=<account> [<Header>=<account> ...]
      Print a JSON object {header: value}, values pulled from Keychain.
  mcp_secret.py selftest
      Create a throwaway Keychain item, prove token substitution works,
      delete the item.

A missing Keychain item exits non-zero with a stderr message naming only
the account, never a value.
"""
import json
import os
import re
import subprocess
import sys

SERVICE = "claude-mcp"
TOKEN_RE = re.compile(r"\{\{kc:([^}]+)\}\}")


def keychain_get(account):
    result = subprocess.run(
        ["/usr/bin/security", "find-generic-password", "-s", SERVICE, "-a", account, "-w"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        sys.stderr.write("mcp_secret: no Keychain item for account: %s\n" % account)
        sys.exit(1)
    return result.stdout.rstrip("\n")


def substitute(value, cache):
    def repl(m):
        account = m.group(1)
        if account not in cache:
            cache[account] = keychain_get(account)
        return cache[account]
    return TOKEN_RE.sub(repl, value)


def cmd_exec(argv):
    if not argv or argv[0] != "--":
        sys.stderr.write("mcp_secret: exec requires '--' before the command\n")
        sys.exit(2)
    command_argv = argv[1:]
    if not command_argv:
        sys.stderr.write("mcp_secret: exec requires a command after '--'\n")
        sys.exit(2)
    cache = {}
    resolved_argv = [substitute(a, cache) for a in command_argv]
    for key, val in list(os.environ.items()):
        if "{{kc:" in val:
            os.environ[key] = substitute(val, cache)
    os.execvp(resolved_argv[0], resolved_argv)


def cmd_headers(argv):
    cache = {}
    out = {}
    for pair in argv:
        if "=" not in pair:
            sys.stderr.write("mcp_secret: headers expects Header=account, got: %s\n" % pair)
            sys.exit(2)
        header, account = pair.split("=", 1)
        out[header] = keychain_get(account)
    print(json.dumps(out))


def cmd_selftest():
    account = "claude-mcp-selftest"
    value = "selftest-value-123"
    add = subprocess.run(
        ["/usr/bin/security", "add-generic-password", "-U", "-s", SERVICE, "-a", account,
         "-w", value, "-T", "/usr/bin/security"],
        capture_output=True, text=True,
    )
    assert add.returncode == 0, "selftest: could not create throwaway Keychain item: %s" % add.stderr
    try:
        cache = {}
        resolved = substitute("prefix-{{kc:%s}}-suffix" % account, cache)
        assert resolved == "prefix-%s-suffix" % value, "selftest: arg token substitution mismatch"
        os.environ["MCP_SECRET_SELFTEST_ENV"] = "{{kc:%s}}" % account
        for key, val in list(os.environ.items()):
            if "{{kc:" in val:
                os.environ[key] = substitute(val, cache)
        assert os.environ["MCP_SECRET_SELFTEST_ENV"] == value, "selftest: env token substitution mismatch"
        del os.environ["MCP_SECRET_SELFTEST_ENV"]
    finally:
        subprocess.run(["/usr/bin/security", "delete-generic-password", "-s", SERVICE, "-a", account],
                        capture_output=True, text=True)
    print("selftest OK")


def main():
    argv = sys.argv[1:]
    if not argv:
        sys.stderr.write(__doc__)
        sys.exit(2)
    mode, rest = argv[0], argv[1:]
    if mode == "exec":
        cmd_exec(rest)
    elif mode == "headers":
        cmd_headers(rest)
    elif mode == "selftest":
        cmd_selftest()
    else:
        sys.stderr.write("mcp_secret: unknown mode: %s\n" % mode)
        sys.exit(2)


if __name__ == "__main__":
    main()
