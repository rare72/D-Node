# tools/check_node.py

import argparse
import paramiko
import sys
import socket

def check_ssh_connection(target_host, user='root', port=22, timeout=5):
    """
    Attempts to establish an SSH connection to the target host.
    This verifies network connectivity and that the SSH daemon is running.
    """
    print(f"--- 🚀 D-Node Pre-Flight Check ---")
    print(f"[INFO] Attempting to connect to {target_host} on port {port}...")

    client = paramiko.SSHClient()
    # Automatically add the server's host key (less secure, but fine for a check)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # We don't need to provide a password for a simple connection test.
        # This just checks if the port is open and the SSH service is responding.
        client.connect(target_host, port=port, username=user, password='', timeout=timeout)
        print(f"✅ [SUCCESS] SSH connection to {target_host} was successful.")
        print(f"[INFO] Node is online and ready for hardening.")
        return True

    except paramiko.AuthenticationException:
        # This is also a success for our check, as it means the host is up
        # and the SSH service is running, it just didn't accept our blank password.
        print(f"✅ [SUCCESS] SSH service on {target_host} is active (Authentication failed as expected).")
        print(f"[INFO] Node is online and ready for hardening.")
        return True

    except (socket.timeout, paramiko.ssh_exception.NoValidConnectionsError) as e:
        print(f"❌ [FAILURE] Could not connect to {target_host}. Error: {e}", file=sys.stderr)
        print(f"[INFO] Please check the IP address, network connectivity, and ensure the node is running.", file=sys.stderr)
        return False

    except Exception as e:
        print(f"❌ [FAILURE] An unexpected error occurred: {e}", file=sys.stderr)
        return False

    finally:
        client.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="D-Node Pre-Flight Check: Verify node connectivity via SSH.")
    parser.add_argument('--target', required=True, help='The IP address or hostname of the target node.')

    args = parser.parse_args()

    if not check_ssh_connection(args.target):
        sys.exit(1) # Exit with a non-zero status code to indicate failure