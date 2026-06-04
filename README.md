# URLtoApp

Convert any website into a cross-platform desktop app. Enter a URL, and build for Windows, macOS, and Linux — all from a single interface.

## Problem

Web apps are great, but sometimes you need a native desktop experience — a dedicated window, taskbar integration, offline-capable shell, or just a distraction-free environment. Manually wrapping a website into a desktop app for every platform is tedious and time-consuming.

## Solution

URLtoApp is a **Tauri + Svelte** desktop app that takes any URL and builds native desktop applications for all major platforms:

- **Windows** (MSI/NSIS installer)
- **macOS** (DMG)
- **Linux** (AppImage, deb)

## Features

- **URL input** — Paste any website URL, app name is auto-generated
- **Cross-platform builds** — Build for Windows, macOS, and Linux simultaneously
- **Native shell** — Each app is a real Tauri window with full native capabilities
- **Zero configuration** — No need to write any code or config files

## Tech Stack

- **Backend:** Rust + Tauri 2
- **Frontend:** Svelte 5 + TypeScript + Vite

## Build

```bash
# Prerequisites: Rust, Node.js, and Tauri CLI
npm install
npm run tauri build
```

## License

MIT
