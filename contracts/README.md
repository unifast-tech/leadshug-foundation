# LeadsHug Contracts

This directory is an index and verification rule, not a second authority for contract behavior or live verification state. The responsible module defines every contract before it is indexed here.

For each indexed contract, link the responsible module and identify its version, authentication surface, tenant/BU scope, request/response shape, errors, verification scope, and evidence. Use the explicit lifecycle verification states `Not-Assessed`, `Documented`, `Verified`, or `Deprecated` only where the responsible record has evidence; never infer coverage from this index.

State definitions and transitions are owned by [the evolution lifecycle](../evolution_lifecycle.md). No current contract inventory is asserted by this README.
