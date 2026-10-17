# cp64 v8 read-only resource probe

The exact v8 `Get-ContainerFacts` formatter completed with native exit 0 for all seven known container IDs, including Web and Gateway where the earlier formatter failed because `.State.Health` was absent. Identity, image, owner, project and running-state guards passed; empty health fields are handled safely. The five expected volume names also passed exact inspect.

No container, image, network, volume, private environment, or service was changed or read beyond the selected safe fields.
