# cp40 isolated API candidate build

Built `leadshug-channels-api-candidate:cp36f-88d419218e08` from the real `api-app/Dockerfile` and `api-app` context using Windows Docker CLI. The new tag was absent beforehand. All nine cp36f source-manifest entries matched both before the build and after the probe; the manifest SHA-256 is `88d419218e080050e2d95724b1ecee19a095c4541e74b6b0f658536336f6859e`. The API `.dockerignore` excludes dotenv files and `.local-files`; no private build arguments or environment values were passed. Docker reported a 43.99 kB context transfer.

The build succeeded with image ID `sha256:8f78e4813da53f29e48dd61e20077f616b4c915d30fe8d7676c102df8b9bd805` (`linux/amd64`) and the requested owner/checkpoint/source-manifest labels. One ephemeral probe used `--network none`, `--read-only`, no environment arguments, ports or volumes, and a replacement Node entrypoint, so it did not start the API or migrations. It confirmed Node `v22.23.3`, Alpine `3.24.2`, OpenSSL `3.5.8`, generated Prisma client presence, and compiled Meta client/convergence helper exports. The probe container was removed.

All seven operator container identities/images and five volume identities remain unchanged from cp38 and cp39; all containers are running, and the cp39 historical candidate tag remains unchanged. No compose action, migration, database/provider action, or runtime mutation occurred. This candidate is not served and cannot be activated until fresh TQA, separate final review and the source checkpoint are accepted.

Optional HTTPS readiness check only: the current hostname failed DNS resolution in WSL (`gaierror`, `EAI_NONAME`) and Windows curl (`exit 6`); root and health were unreachable in both contexts. No tunnel or hostname action was taken. This does not change candidate-build success or prove application/runtime failure.

The public-source build log is `cp40-candidate-build.log` (SHA-256 `71483b6d92e4f4a60be78992956fa32fffac1f77a4ff32727781a54b5db61608`).
