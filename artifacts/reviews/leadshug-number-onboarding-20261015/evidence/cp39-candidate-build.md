# cp39 isolated API candidate build

Built `leadshug-channels-api-candidate:cp36e-ea3080d36a43` from `api-app/Dockerfile` and the `api-app` context using the Windows Docker CLI. The tag was absent before the build. The cp36e nine-entry source manifest matched before the build and after the probe; its SHA-256 is `ea3080d36a4389466a2f59afeab5dc8c1d0a239b8f000d9e16a65ff292e6d3df`. The Docker context transferred 86,530 bytes, with the API `.dockerignore` excluding dotenv files and `.local-files`. No private build arguments or environment values were supplied.

The build succeeded with image ID `sha256:c1b5769ff0a7e58772eb6a1b0c0a120c94ad3aa943119408cc8d1d0df115d136` (`linux/amd64`). An ephemeral probe used `--network none`, `--read-only`, no ports/volumes/environment arguments, and a replacement Node entrypoint, so it did not start the API or migrations. It confirmed Node `v22.23.3`, Alpine `3.24.2`, OpenSSL `3.5.8`, generated Prisma client presence, and the compiled Meta client and convergence-helper exports. The probe container was removed.

After the build, all seven operator container IDs/images remained identical to cp38 and running; the five operator volume identities remained unchanged. The candidate is not served. No compose action, migration, database/provider action, tag replacement, or runtime mutation occurred. Candidate activation remains gated on fresh TQA, separate final review, and source checkpoint acceptance.

The public-source build log is `cp39-candidate-build.log` (SHA-256 `b665ef23efcc8b882b1c416b4be098f50535289aebe8166bad4706e66e418d7e`).
