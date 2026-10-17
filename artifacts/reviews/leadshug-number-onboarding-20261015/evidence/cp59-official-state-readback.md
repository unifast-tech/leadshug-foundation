# cp59 official channel state readback

A scoped read of only the known BU’s two channels and current attempts shows the official channel is not promoted. It is `CONECTANDO`, generation 1, with current attempt `ERROR` / `EXPIRED`, safe error `ATTEMPT_EXPIRED`, version 4, and no active lease. No official resource, active channel credential, verified identity, receipt, or connected timestamp is present. This is an expired attempt, not a merely reserved/authorized attempt.

The same BU’s nonofficial channel remains connected with its current receipt-verified attempt v2, generation/pairing/verified epoch 1, active managed identity, and no lease. The user reported the intended official number differs from the nonofficial number. No `PHONE_MISMATCH` runtime error was observed; source guard behavior is not evidence that this code occurred.

Next, use the ordinary official-channel UI for this BU to start a supported fresh registration/re-authorization after selecting the intended official business account and its own test number. No provider or database action was taken here. Terminal STOP for root adjudication.
