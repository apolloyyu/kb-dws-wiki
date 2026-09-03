# dws auth exchange

kind: command
completeness: full
description: Exchange an authorization code for credentials
source: internal/app/auth_command.go:957
visible_flags: 8

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
- dws auth login
- dws auth logout
- dws auth migrate-keychain
- dws auth reset
- dws auth status
