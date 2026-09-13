# SmartIDE-release
This repo is for publishing SmartIDE APKs.

## Download SmartIDE EAP

**Latest: [v12.6](https://github.com/SmartIDE-org/SmartIDE-release/releases/tag/smartide-eap-v12.6)**, published 2026-09-13.

| APK | Size | For |
|---|---|---|
| **[arm64-v8a](https://github.com/SmartIDE-org/SmartIDE-release/releases/download/smartide-eap-v12.6/smartide-eap_v12.6_release_arm64-v8a.apk)** | 94 MB | most phones and tablets — pick this if unsure |
| **[armeabi-v7a](https://github.com/SmartIDE-org/SmartIDE-release/releases/download/smartide-eap-v12.6/smartide-eap_v12.6_release_armeabi-v7a.apk)** | 91 MB | older 32-bit ARM devices |
| **[x86_64](https://github.com/SmartIDE-org/SmartIDE-release/releases/download/smartide-eap-v12.6/smartide-eap_v12.6_release_x86_64.apk)** | 94 MB | Intel/AMD devices and emulators |
| **[x86](https://github.com/SmartIDE-org/SmartIDE-release/releases/download/smartide-eap-v12.6/smartide-eap_v12.6_release_x86.apk)** | 94 MB | older 32-bit Intel devices |
| **[universal](https://github.com/SmartIDE-org/SmartIDE-release/releases/download/smartide-eap-v12.6/smartide-eap_v12.6_release_universal.apk)** | 191 MB | works everywhere, largest download |

SmartIDE EAP (`org.smartide.code.eap`) is the early-access build of SmartIDE. It installs alongside the Play Store app and keeps its own data.

### What's new in v12.6

**VS Code**
- VS Code now runs upstream Code-OSS, and no longer hangs on "Starting VS Code...".
- Laid out for phones: the accessory bar stays on screen and is tappable, and Back closes context menus.
- Setup no longer needs proot-distro, and the server restarts when you open another project.

**AI Coding Agent**
- New providers: OpenAI, DeepSeek, xAI (Grok), Mistral AI, Z.ai (GLM), Moonshot AI (Kimi) and NVIDIA NIM.
- Up-to-date default models for every provider, and thinking works again with the newest Claude models.

**Project View and menus**
- The Project View is IntelliJ's own, and Expand Recursively no longer blanks the tree.
- Menus and popups behave like IntelliJ's: nested submenus open instead of closing the popup.

**Run and terminal**
- Run no longer reinstalls a toolchain that is already installed.
- The terminal's bootstrap is extracted once instead of on every launch.
- The Bazel framework installs from packages.

**Stability**
- Faster startup, and fixes for crashes and freezes in session restore, icon loading, agent tool results, the folder picker and terminal scrolling.

## All recent releases

The latest five releases of every app published here. **SmartIDE EAP** and **SmartIDE Termux** are different apps, not versions of one another.

| App | Version | Published | arm64-v8a | armeabi-v7a | x86_64 | x86 | universal |
|---|---|---|---|---|---|---|---|
| SmartIDE EAP | [v12.6](https://github.com/SmartIDE-org/SmartIDE-release/releases/tag/smartide-eap-v12.6) | 2026-09-13 | [94 MB](https://github.com/SmartIDE-org/SmartIDE-release/releases/download/smartide-eap-v12.6/smartide-eap_v12.6_release_arm64-v8a.apk) | [91 MB](https://github.com/SmartIDE-org/SmartIDE-release/releases/download/smartide-eap-v12.6/smartide-eap_v12.6_release_armeabi-v7a.apk) | [94 MB](https://github.com/SmartIDE-org/SmartIDE-release/releases/download/smartide-eap-v12.6/smartide-eap_v12.6_release_x86_64.apk) | [94 MB](https://github.com/SmartIDE-org/SmartIDE-release/releases/download/smartide-eap-v12.6/smartide-eap_v12.6_release_x86.apk) | [191 MB](https://github.com/SmartIDE-org/SmartIDE-release/releases/download/smartide-eap-v12.6/smartide-eap_v12.6_release_universal.apk) |
| SmartIDE Termux | [v10.0.1](https://github.com/SmartIDE-org/SmartIDE-release/releases/tag/smartide-termux-v10.0.1) | 2026-07-22 | [70 MB](https://github.com/SmartIDE-org/SmartIDE-release/releases/download/smartide-termux-v10.0.1/smartide-termux_v10.0.1_release_arm64-v8a.apk) | [66 MB](https://github.com/SmartIDE-org/SmartIDE-release/releases/download/smartide-termux-v10.0.1/smartide-termux_v10.0.1_release_armeabi-v7a.apk) | [70 MB](https://github.com/SmartIDE-org/SmartIDE-release/releases/download/smartide-termux-v10.0.1/smartide-termux_v10.0.1_release_x86_64.apk) | [69 MB](https://github.com/SmartIDE-org/SmartIDE-release/releases/download/smartide-termux-v10.0.1/smartide-termux_v10.0.1_release_x86.apk) | [160 MB](https://github.com/SmartIDE-org/SmartIDE-release/releases/download/smartide-termux-v10.0.1/smartide-termux_v10.0.1_release_universal.apk) |
| SmartIDE Termux | [v9.1.0](https://github.com/SmartIDE-org/SmartIDE-release/releases/tag/smartide-termux-v9.1.0) | 2026-03-28 | [50 MB](https://github.com/SmartIDE-org/SmartIDE-release/releases/download/smartide-termux-v9.1.0/smartide-termux_v9.1.0_release_arm64-v8a.apk) | [47 MB](https://github.com/SmartIDE-org/SmartIDE-release/releases/download/smartide-termux-v9.1.0/smartide-termux_v9.1.0_release_armeabi-v7a.apk) | [50 MB](https://github.com/SmartIDE-org/SmartIDE-release/releases/download/smartide-termux-v9.1.0/smartide-termux_v9.1.0_release_x86_64.apk) | [49 MB](https://github.com/SmartIDE-org/SmartIDE-release/releases/download/smartide-termux-v9.1.0/smartide-termux_v9.1.0_release_x86.apk) | [141 MB](https://github.com/SmartIDE-org/SmartIDE-release/releases/download/smartide-termux-v9.1.0/smartide-termux_v9.1.0_release_universal.apk) |

See [all releases](https://github.com/SmartIDE-org/SmartIDE-release/releases).
