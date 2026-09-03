# dws auth exchange

kind: command
completeness: partial
usage: dws auth exchange
description: Exchange an authorization code for credentials
source: internal/app/auth_command.go:957
visible_flags: 8
partial_reason: unverified_flags

## Flags
- --code <String>: Authorization code
- --uid <String>: Optional user identifier for compatibility
- --client-id <String>: Compatibility flag
- --authorize-url <String>: Compatibility flag
- --token-url <String>: Compatibility flag
- --refresh-url <String>: Compatibility flag
- --redirect-url <String>: Compatibility flag
- --scopes <String>: Compatibility flag

## Related
- dws auth export
- dws auth import
- dws auth login
- dws auth logout
- dws auth migrate-keychain
- dws auth reset
