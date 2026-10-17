# cp47 isolated API candidate

Built the single new tag `leadshug-channels-api-candidate:cp36i-af21e98e41ec` from the frozen cp36i nine-file manifest. The build exited 0 and produced image ID `sha256:fe5fb7eaf6a68123f9da6b92a0a69483180d213f556b4bedf313f04a383b4821`. It used the project API Dockerfile and `.dockerignore`; the 56.54 kB build context excluded `.local-files`, dotenv files, and `.git`. Source hashes matched cp36i both before and after.

The effective probe used `--network none --read-only`, no ports or mounts, and an explicit Node entrypoint. It observed Node 22.23.3, Alpine, OpenSSL 3.5.8, Prisma 6.19.3 with a `linux-musl-openssl-3.0.x` query engine artifact, and the expected compiled module exports. Four compiled module hashes are in the JSON receipt. No database connection or API startup ran.

The first stdin-based probe invocation exited with no output because Docker Desktop did not pass the here-document script. A second invocation used a direct `node -e` script and completed the intended checks. Both were ephemeral `--rm` runs, and no probe container remains. This execution detail is recorded for root review.

All seven operator container IDs/images/statuses and five volume identities/owner labels were identical before and after. The operator API remains on its previous image. No source, Git, tunnel, configuration, provider, database, auth, Meta, or private data was changed or read. This candidate has not been activated or served and does not establish Meta acceptance, device recovery, or final delivery acceptance.
