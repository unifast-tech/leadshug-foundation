# cp64 remaining preparation v4

Created a new activation helper without editing the v3 helper. V4 fixes the owner-label lookup to `com.leadshug.channels.owner`, uses a byte scanner for target-key uniqueness rather than decoding every private line, explicitly fails terminally if the private-file write cannot be restored and verified, sets the origin-changed flag before ACL postchecks, requires actual preservation postconditions before declaring rollback verified, and retains original Docker exit/HTTP status before rollback diagnostics.

Validation passed in Windows PowerShell. Public synthetic tests used a temporary file created under the task's T directory, an exclusive `FileStream`, and `Get-Acl` SDDL observations during and after interrupted-write, interrupted-flush, and successful replacement transactions. Both failure controls restored the exact synthetic original; the success control verified exact replacement bytes; ACL SDDL was unchanged throughout; the temporary file was deleted. Alternate declaration duplicates were rejected. No private configuration file was opened.

A separate read-only probe extracted v4's actual selective Docker inspect functions and inspected only the known API container ID. It confirmed image, running/healthy state, the exact owner key `com.leadshug.channels.owner`, project, and service without requesting `Config.Env`.

V4 helper SHA-256: `fe057917b9a8fe0dbf378c2714d378b83973c9a80919a18684e9af9c6604a6be`. Dummy probe SHA-256: `939935002fc0d72772bc9089f1f9aa241feb0c4b1324f26cd9803d458fe12720`. Owner probe SHA-256: `f1ee7fde42f3d6104bf80fe41c7f105b19b8a52fe5cfaacbbc4b8abc8da4431d`.

The new transport is independently accepted by root in the separate immutable `cp64-transport-proof.root-accepted.json` receipt. This preparation does not retire the old child or authorize private-origin access/edit, API/Web recreation, or gateway action. Stop for fresh v4 review and root's separate phase-2 GO.
