# cp63 Web build-base provenance correction

The immutable preparation record contains a malformed `node:22-alpine` local image ID with a 63-character digest suffix. The current local tag resolves to full ID `sha256:7c3b093add7c43400ee83b815ab2cda98794a10045bcf76ce9bb2f89b97cbc5c`; its repository digest matches the digest recorded in preparation: `node@sha256:0a7108bf6c7bf5de370ffb1a3ed6be93d405b43ff159f681a8d18e0c2bc2e402`.

The actual candidate build log names `docker.io/library/node:22-alpine` and the build used no `--pull`; builder working-directory, package copy, and `npm ci` steps were cached. The raw log does not print a resolved immutable digest. This record therefore corrects the malformed baseline ID and reports the matching repository digest, while making no claim of exact pre/post local-ID equality or a log-verified resolved digest. The existing candidate JSON also recorded `sameBeforeAfter: true` for the node base. That boolean overstates what the truncated baseline permits; this diagnostic supersedes it for interpretation. The repoDigest match and cached local-tag build are supported, while exact pre/post local-ID equality is not. Original preparation and candidate artifacts remain unchanged.

Diagnostic record: `cp63-web-build-provenance.json` SHA-256 `79f77613a4f804a0ca25181e614159b771b1a2b3aa0ca98a8d719f03f52f0e1f`.
