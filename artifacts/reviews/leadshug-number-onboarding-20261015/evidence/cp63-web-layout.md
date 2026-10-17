# cp63 candidate layout validation

An isolated Playwright `1.62.1` / Chromium `151.0.7922.34` browser visited only the candidate Nginx alias on an internal Docker network. The browser used a new in-memory context; package installation occurred only in its owned temporary container. The exact Playwright image was already present, so no image pull occurred. The two owned containers and the internal network were removed after screenshots were copied.

At 375×812, the measured `innerWidth` was 375, document/body scroll widths were 375, the response was 200 and its 12,865 bytes matched source SHA-256 `d0f72c588f0f014de46a327e34d6b26125ca115bc973b56bbb926cd8519e701d`. At 1280×900, `innerWidth` and document/body scroll widths were 1280, with the same 200 response and source hash. Both screenshots showed ten sections, three mailto links, three external links with `rel=noreferrer`, no horizontal overflow, no console/page errors, and zero page-initiated external requests.

Screenshots: `cp63-web-layout-mobile.png` SHA-256 `004e0d748b801a7b9c50f240f9892ee12ff307c18344c51fd2fc38ea6fa2240c`; `cp63-web-layout-desktop.png` SHA-256 `20820eb2f1cf98d2d467f6138ab5fd4146e838cff0336f526f6a5739ed84913b`. The result record is `cp63-web-layout.json` SHA-256 `51e1761fe9d026b823a0f65f7e5fde4956fbc776549a4435bcc824f6fcf8699b`. This is candidate-only evidence and does not constitute public activation.
