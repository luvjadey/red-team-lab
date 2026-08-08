# Contributing Guide

Jade's personal code review checklist for the red-team-lab project. Every pull request should pass these checks before merging.

## Security
- [ ] No hardcoded secrets (API keys, passwords, tokens)
- [ ] Input from external sources is validated
- [ ] Dependencies checked for known vulnerabilities
- [ ] Logs don't leak sensitive info (credentials, pii)

## Code Quality
- [ ] Functions have clear names and docstrings
- [ ] Code handles edge cases (empty input, bad data)
- [ ] No leftover debug prints or commented-out code
- [ ] Follows consistent style

## Testing
- [ ] New code has at least one test
- [ ] All existing tests still pass
- [ ] Tested against realistic sample data

## Documentation
- [ ] README updated if behavior changed
- [ ] PR description explains What / Why / Testing

## Branch Workflow
- [ ] Work done on a feature branch (not dev or main directly)
- [ ] Branch deleted after merge