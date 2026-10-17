# cp64 Web diagnostic probe v2 supplement

This supplement binds to the immutable preparation JSON SHA-256 `9811ed037176e94e8f49a6e63cbc37735bf720c0d0f0e254d593b1462940c3eb`; that package and its original probes were not edited.

The new WSL v2 source uses single-backslash raw regex word boundaries for both script and form tags. Python AST parsing passed, and a synthetic `<script defer></script><form></form>` sample produced one script and one form. No network or runtime probe ran.

A separate Windows probe copy removes only `AcceptEncoding.ParseAdd('identity')`, allowing later capture in both explicit identity-encoding mode and default HttpClient mode. Neither probe ran. The original probes remain untouched.

- WSL v2 SHA-256: `d1b2ff3cb2ebec09a00946128e476f2f53a0bb5551dfc4a7be7340e0cad06bea`
- Windows default-encoding copy SHA-256: `73bc8a71ad829de25840cd48be78afde033762fb9a5e42d878aac86174194cc4`
- Supplement JSON SHA-256: `681c4d28c38ad8ab09b5d5e260c49a5f3d9b1683c7ba2ba45fad99b266fa1d4d`
