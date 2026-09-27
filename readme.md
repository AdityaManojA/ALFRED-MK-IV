#  ALFRED — MARK III (Wayne Protocol Edition)
### Autonomous Multimodal AI Desktop Assistant & Tactical Terminal
**Architect & Lead Creator:** **ADITYA MANOJ**

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![AI Backend](https://img.shields.io/badge/AI-Gemini%203.1%20Flash%20Live%20%7C%20Local%20Ollama-8E75B2.svg?logo=google&logoColor=white)](https://ai.google.dev/)
[![Local LLMs](https://img.shields.io/badge/Local%20LLM-Ollama%20%7C%20LM%20Studio%20%7C%20vLLM-orange.svg)](https://ollama.com)
[![PyQt6](https://img.shields.io/badge/GUI-PyQt6%20Software%20Renderer-41CD52.svg?logo=qt&logoColor=white)](https://riverbankcomputing.com/software/pyqt/)
[![AES-256 Remote](https://img.shields.io/badge/Mobile-Quantum%20Dashboard%20(iOS%2FAndroid)-00f0ff.svg)](https://github.com/AdityaManojA/ALFRED-MK-IV)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

> **ALFRED MARK-IV** is an autonomous, real-time voice, vision, and system-control executive assistant built for complete digital sovereignty and tactical computing. Featuring native bidirectional audio streaming, real-time visual grounding, full desktop automation, high-performance long-term memory, and encrypted mobile remote telemetry.

---

##  1. 100% Local & Air-Gapped Offline Execution: Switching from Gemini to Local API

**ALFRED is architected for dual-backend operation**: you can seamlessly toggle between Google's high-speed **Gemini 3.1 Flash Live API** (cloud multimodal WebSocket) and **100% local, air-gapped open-weight models** (Ollama, LM Studio, vLLM, Jan, LocalAI, or llama.cpp) without changing a single line of application code.

###  Gemini Live API vs. Local Offline API Comparison

| Feature | Gemini 3.1 Flash Live | Local Open-Weight API (Ollama / vLLM / LM Studio) |
|---|---|---|
| **Audio Latency** | Sub-second native bidirectional WebSocket streaming | Local STT/TTS pipeline or text-streaming |
| **Privacy & Security** | Encrypted TLS to Google Cloud | 100% offline, zero network egress, fully air-gapped |
| **Hardware Requirements** | Zero local compute (runs on any CPU) | 8GB–24GB+ VRAM/RAM depending on quantized model size |
| **API Token Cost** | Pay-per-token or free tier quotas | **$0.00 forever** (unlimited free local inference) |
| **Tool / Function Calling** | Native Gemini Automatic Function Calling (AFC) | Tool-calling supported via JSON mode or prompt schema |
| **Offline Operation** | Requires active Internet connection | **Operates entirely without internet connection** |

---

###  Detailed Step-by-Step Guide: How to Switch to a Local API

#### Step 1: Install & Set Up Your Preferred Local LLM Server

Choose any of the following recommended local model engines:

##### Option A: Ollama (Recommended — Simplest Setup)
1. Download and run the installer for Windows, macOS, or Linux from [ollama.com](https://ollama.com/).
2. Open PowerShell or Terminal and pull your model of choice:
   ```powershell
   # Recommended for 8GB VRAM / RAM (Fast & Accurate):
   ollama pull llama3.2:3b-instruct-q4_K_M
   # Or for 16GB VRAM / RAM (High reasoning capacity):
   ollama pull qwen2.5:7b-instruct
   # Or for deep programming & tool execution:
   ollama pull deepseek-coder-v2:16b
   ```
3. Start the Ollama daemon (runs automatically in background at `http://localhost:11434` or verify with `ollama list`).

##### Option B: LM Studio (Recommended for GUI Users)
1. Download [LM Studio](https://lmstudio.ai/) and launch it.
2. Search and download any quantized GGUF model with tool-calling capabilities (e.g., `Qwen2.5-7B-Instruct-GGUF` or `Llama-3.1-8B-Instruct-GGUF`).
3. Click the **Local Server** tab (double-arrow icon `<->` on the left sidebar).
4. Set the port to `1234` (default) and click **Start Server**.
5. Your local OpenAI-compatible endpoint is now live at `http://localhost:1234/v1`.

##### Option C: vLLM or llama.cpp (High-Throughput / Linux Servers)
Run with your OpenAI-compatible API flag:
```bash
python -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2.5-7B-Instruct --port 8000
```

---

#### Step 2: Configure ALFRED's Target Backend in `config/api_keys.json`

Open `config/api_keys.json` in the root folder of ALFRED. Set `llm_provider`, `llm_url`, and `llm_model`:

##### Configuration Template for Ollama:
```json
{
    "llm_provider": "ollama",
    "llm_url": "http://localhost:11434",
    "llm_model": "llama3.2",
    "assistant_name": "ALFRED",
    "user_name": "Master Wayne",
    "ui_color": "#e5a93b",
    "voice_name": "Charon",
    "wake_word_enabled": true,
    "push_to_talk_enabled": true
}
```

##### Configuration Template for LM Studio / vLLM (OpenAI-Compatible):
```json
{
    "llm_provider": "openai",
    "llm_url": "http://localhost:1234/v1",
    "llm_model": "qwen2.5-7b-instruct",
    "assistant_name": "ALFRED",
    "user_name": "Master Wayne",
    "ui_color": "#e5a93b",
    "voice_name": "Charon",
    "wake_word_enabled": true,
    "push_to_talk_enabled": true
}
```

---

#### Step 3: Launch ALFRED & Verify Connection

Start ALFRED in your terminal:
```powershell
python main.py
```
* **Connection Handshake**: `core/llm_client.py` will probe your local endpoint during startup:
  ```text
  [LLM] Connected to local Ollama server at http://localhost:11434 (model: llama3.2)
  [Actions] Action discovery complete: 23 active.
  ```
* **Offline Wake Word**: When offline, ALFRED automatically utilizes `openwakeword` on your local CPU for zero-cloud keyword activation.

---

#### Step 4: How to Switch Back to Gemini Live API Anytime

To return to Gemini Live, either:
1. Re-add your `"gemini_api_key"` in `config/api_keys.json`:
   ```json
   {
       "gemini_api_key": "AIzaSyYourActualKeyHere...",
       "llm_provider": "gemini"
   }
   ```
2. Or set the system environment variable:
   ```powershell
   $env:GEMINI_API_KEY="AIzaSyYourActualKeyHere..."
   ```
ALFRED will automatically prioritize the Gemini Live bidirectional WebSocket when a valid key is detected.

---

##  2. Security, Privacy & Defensive Architecture

ALFRED is designed around uncompromising principles of system integrity, process containment, and self-preservation:

* **The Heavenly Restriction**: ALFRED is strictly and irrevocably forbidden from accessing, opening, reading, listing, modifying, or executing files inside `D:\Projects\Personal-Assistant` and all subpaths (including `Mark-LIV`). If instructed, ALFRED delivers the explicit non-negotiable denial:
  > *"Due to the heavenly restriction placed upon my creator, I cannot."*
* **C: Drive Quarantine**: File manipulation on the `C:` drive is strictly confined to the user's **Desktop** and **Documents** folders. Any attempt to touch system or root directories (`C:\Windows`, `C:\Program Files`, `Downloads`, `AppData`, or `C:\`) is blocked with:
  > *"Access denied: Access to C: drive is restricted to Desktop and Documents only."*
* **Safe Storage Zones (`D:` & `E:` Drives)**: `D:` drive and `E:` drive are designated safe zones for general file operations, development projects, and media (with `D:\Projects\Personal-Assistant` remaining permanently locked).
* **Multi-Layer Hard Enforcement**:
  * **Cognitive Shield**: System prompts and instruction guards enforce baseline refusal.
  * **Global Dispatch Interceptor**: `_execute_tool()` checks all arguments via `core.path_guard` and halts unauthorized paths before action dispatch.
  * **Subsystem Isolation**: `file_controller`, `file_processor`, `open_app`, `action_loader`, and `computer_control` enforce independent path resolution checks.
* **Human Confirmation Gate**: Destructive or irreversible operations (system shutdown, OS reboot, WiFi interface toggles) generate a physical cryptographic confirmation button on screen; ALFRED cannot self-execute them without user approval.
* **Universal Action Undo Stack**: Saying *"undo"*, *"revert that"*, or *"put it back"* rolls back file creations, moves, renames, writes, and system settings modifications.

---

##  3. Real-Time Multimodal Intelligence & Dual Audio Engine

| Subsystem | Architectural Implementation |
|---|---|
| ⚡ **Bidirectional Live Audio** | Native streaming via **Gemini 3.1 Flash Live** (or local Ollama/LM Studio streaming). Real-time natural speech with sub-second response latency. |
| 🌐 **Bidirectional WebAudio Streaming** | Low-latency WebSocket audio interface (`/ws/audio` endpoint) enabling browser-based voice input/output with separate queues for phone mic (`_phone_audio_queue`) and WebSocket audio (`_audio_queue`), featuring connection management, automatic reconnection, and audio activity visualization in the HUD. |
| 👄 **Formant & Viseme Lip-Sync** | ~50 mouth shapes/sec derived from real-time FFT audio formants (F1 openness, F2 spread/round) combined with Unicode articulatory decomposition across 20+ languages. |
| 👁️ **Visual Multimodal Grounding** | On-demand single-frame capture of multi-monitor displays and webcams (`screen_processor.py`). Frame feeds are labelled by origin and injected into conversational context. |
| 🎚️ **Global Push-to-Talk** | Hold `Ctrl+Space` to talk. Hardware mic remains completely shut off when idle. Polled at 30 Hz via Windows raw virtual key polling, window-scoped on macOS/Linux. |
| 🔇 **Calibrated Echo Cancellation** | Output latency-calibrated acoustic echo cancellation (`_out_latency + _TAIL_MARGIN`). Drops ALFRED's own voice tail so the microphone never triggers on self-speech. |

---

##  4. Dynamic Background Audio Matrix & Voice-Ducked Sound System

* **Integrated Ambient Sound Dock**: Dedicated cybernetic background soundtrack player at the bottom-left of the HUD with custom music loading and seamless loop playback.
* **Featured Soundtrack — The Son of Flynn (From TRON: Legacy Score)**:
  > *"It's one of my fav childhood movies, the graphical interface and intelligence development of the tech field reminded me of the movie I watched when I was a kid, so I decided to throw this one in while I work. You guys can swap it out, remove it entirely, or add more to it!"* — **Aditya Manoj**
* **Intelligent Speech Ducking**: Continuously monitors TTS speech output. Background audio plays at a crisp 10% volume normally and dynamically ducks to 5% whenever ALFRED speaks, returning smoothly upon turn completion.
* **Audio-Reactive Waveform Controls**: Replaced generic media playback glyphs with high-tech graphic equalizer lines that animate in sync with active playback.
* **Popup Gain Slider HUD**: Floating real-time volume slider for instantaneous gain adjustments directly on click without opening deep settings menus.
* **Telemetry HUD Overlay** (`ui_overlay.py`): Minimalist floating widget displaying real-time system metrics (CPU, RAM, temperature, network speed) with always-on-top transparency and drag-to-move functionality.

---

##  5. Quantum Mobile Remote & iPhone 16 Dashboard

* **Encrypted Web Remote (AES-256-CBC)**: Scan the on-screen QR code from the desktop terminal or browse locally over WiFi. Session keys and traffic are encrypted locally with zero external server dependencies.
* **iPhone 16 Viewport Architecture**: High-density responsive layout tailored for mobile displays with collapsible telemetry cards and zero button overflow.
* **Dual-Destination Tactical Screenshots**: Asking ALFRED to capture the screen automatically dispatches high-resolution PNG captures to **both**:
  1. **Desktop**: `~/Desktop/alfred_screenshot_<timestamp>.png`
  2. **Phone Feed**: Real-time transmission to the mobile dashboard with an **inline thumbnail preview** and a single-tap **View / Save Image** download link.
* **Emoji-Free ANSI Red Telemetry**: Operational status stream rendered in clean, high-contrast, machine-readable ANSI Red brackets:
  `[phone]`, `[control]`, `[screen]`, `[camera]`, `[out]`, `[warn]`, `[error]`, `[mic]`, `[speaker]`, `[listen]`, `[link]`, `[online]`, `[halt]`, `[brief]`, `[monitor]`, `[proactive]`.

---

##  6. Full Desktop Control & Operating System Automation

* **Deep OS Automation**: Keystrokes, mouse positioning, clicks, drags, window focus management, clipboard read/write, and AI-driven element location (`screen_find`).
* **OS-Native Task Scheduling**: Reminders and recurring tasks scheduled via Windows Task Scheduler (`schtasks`), macOS `launchd`, or Linux `systemd`/`at`.
* **Enterprise Windows Autostart**: Robust registry management querying and maintaining `ALFRED_AI` with backward-compatible legacy key cleanup.
* **Persistent Browser Profile Bridges**: Multi-tier profile automation (`~/.alfred_profiles` with legacy fallback) preventing session and authentication dropouts during web automation.

---

##  7. High-Performance Memory & Conversational Briefing Customizer

* **O(N log N) Pruning Engine**: Memory trimming optimized from $O(N^2)$ to $O(N \log N)$ using single-pass size accumulators and conservative lower-bound estimation. 50,000 records trimmed in **0.33 seconds** without CPU spikes.
* **Tiered Memory Hierarchy (`memory/long_term.json`)**: Core identity facts stay in context; extended history is recalled on demand via sub-millisecond local keyword search (`recall_memory`).
* **Conversational Briefing Directive Customizer (`update_daily_briefing.py`)**: Saying *"update my daily briefing"* opens an interactive alignment protocol where ALFRED captures specific additions, topics, news sources, or location shifts, permanently committing them to memory.

---

##  8. Real-Time Insignia & Chassis Hot-Swapper

* **Multi-Insignia Catalog**: Scans and registers brand assets from `Icons/` (Batman Beyond, Arkham Asylum, Classic Bat, White Bat, Tactical Stealth).
* **Live Runtime Reconfiguration (`update_app_icon.py`)**: Hot-swaps the active application window icon, Windows taskbar insignia, and system tray in real time upon voice request (*"update the app icon to Batman Beyond"*) or via the Customise Assistant drawer.
* **Automatic Shortcut Synchronization**: Dynamically generates and updates `A.L.F.R.E.D.lnk` on the desktop without interrupting the running session.

---

##  9. Protocol Engine & Multi-Step Macro Playbooks (`config/protocols.yaml`)

ALFRED features an autonomous **Protocol Engine** (`actions/protocol_engine.py`) for executing complex, sequential, compound system workflows via simple custom voice triggers:

* **Voice Trigger Activation**: Activate entire multi-app, multi-action workflows using custom trigger words collected during workflow setup.
  * *Example: Saying **"FCC CLAUDE"** immediately opens PowerShell as Administrator, types and launches `fcc-server`, waits for initialization, opens a secondary terminal window, and executes `fcc-claude`.*
* **Interactive Workflow Creation ("LETS CREATE A WORKFLOW")**:
  * Users can state *"Let's create a workflow"* to formulate compound routines interactively.
  * Employs ALFRED's cryptographic **Single-Click Confirmation Gate** (`core/confirm.py`) to display an on-screen HUD banner before committing new playbooks to `config/protocols.yaml`.
* **Dynamic Variable Interpolation**: Steps support runtime substitution for `{timestamp}`, `{date}`, `{time}`, `{user}`, `{workspace}`, and custom voice arguments.
* **Execution Delays & Pacing**: Fine-grained per-step timing control via `sleep_ms` (e.g. allowing server processes to bind ports before launching client terminals).
* **Strict Defensive Path Guarding**: Every step argument is validated through `core.path_guard` prior to dispatch. If any step attempts to access unauthorized paths or fails execution, the engine **immediately aborts** all remaining steps and outputs:
  ```text
  [error] Protocol <Name> halted at Step <X>: <reason>
  ```
* **Red-Tag Operational Telemetry**: Emits high-visibility step telemetry during execution:
  ```text
  [control] Executing Protocol <Name> Step <X>/<Y>: <Tool_Name>
  ```

---

##  10. Local Hybrid Visual Grounding (RapidOCR + ONNX + Gemini Fallback)

Directly streaming full screenshots to cloud APIs for coordinate lookup introduces network latency and high token consumption. ALFRED resolves this via a multi-tiered local hybrid element grounding pipeline (`actions/screen_find.py`):

1. **Local RapidOCR Detection (<150ms)**: Scans screen captures locally using `rapidocr_onnxruntime`. Uses intelligent toolbar strip partitioning and early-termination recognition to identify target buttons and text labels in **~75–95ms** without network calls.
2. **Quantized ONNX Vision Detector**: If the query is an icon or non-text glyph (e.g., search icon, close button), ALFRED runs a locally cached, quantized ONNX model (`omniparser_v2_quant.onnx` / `florence2_quant.onnx`) with zero cold-start latency.
3. **Automatic Delegation Threshold**:
   * **Confidence $\ge 0.80$**: Returns normalized `(x, y)` coordinates to `computer_control.py` immediately without calling external APIs.
   * **Confidence $< 0.80$**: Automatically falls back to Gemini visual grounding and emits red-tag telemetry:
     ```text
     [screen] Local grounding confidence low (<score>) — delegating to Gemini
     ```

---

##  11. Process-Level Audio Ducking & Background Concurrency

* **Process-Level Media Ducking (`core/audio_ducker.py`)**: Interacts directly with OS audio session managers (`pycaw` on Windows, `pulsectl` on Linux) to automatically reduce background media processes (Spotify, Chrome, YouTube, VLC, Edge) by **70%** (factor `0.3`) whenever ALFRED speaks, restoring exact pre-duck volumes when speech completes or is interrupted (`[halt]`).
* **Non-Blocking Background Worker Pool (`main.py`)**: Asynchronous worker queue (`background_task_queue`) executing long-running background tasks (web scraping, video processing, graph indexing) concurrently without blocking primary voice conversation turns, streaming live telemetry updates (`[control] [background XX%]`) to the HUD.
* **Bounded Concurrency Limiter (`core/concurrency.py`)**: Asynchronous worker pools with controlled concurrency limits (default: 5 concurrent workers) preventing socket exhaustion, thread starvation, and rate limits.
* **Centralized TTL & LRU Cache (`core/cache.py`)**: Thread-safe memory cache with deterministic argument hashing, prefix invalidation on mutations, and graceful fail-open resilience.

---

##  12. Active Process Watchdog, Anomaly Detection & Auto-Throttling (`actions/system_monitor.py`)

ALFRED incorporates an OS security and performance watchdog daemon that actively monitors running process trees, flags resource anomalies, inspects outbound network sockets, and executes automated resource throttling:

* **Active Process Tree Monitoring (`watch_process_tree`)**: Continuously monitors the host process hierarchy via `psutil`. Automatically identifies single non-system processes sustaining **>90% CPU utilization for >10 consecutive seconds**.
* **High-Visibility Alert Telemetry**: Real-time anomaly detection emits standard red-tag operational telemetry to the HUD and system logs:
  ```text
  [monitor] Resource anomaly: Process <PID:Name> utilizing <X>% CPU
  ```
* **Suspicious Socket Inspection (`track_suspicious_sockets`)**: Tracks active outbound TCP/UDP network connections querying non-standard remote ports. Filters out RFC private subnets, loopback addresses, and standard service ports (HTTP, HTTPS, SSH, DNS, NTP, etc.), alerting on unexpected remote network egress:
  ```text
  [monitor] Suspicious socket: Process <PID:Name> -> <Remote_IP>:<Port>
  ```
* **Automated Resource Throttling & Suspension (`throttle_process`)**:
  * Automatically lowers target process priority class to `psutil.BELOW_NORMAL_PRIORITY_CLASS` (or nice value 10 on Unix) to prevent system freezing and prioritize interactive tasks.
  * Supports pausing runaway workloads via `process.suspend()`, and restoring normal execution using `resume_process()`.
* **System & IDE Shielding Constraints**:
  * **Core System Binaries Protected**: `csrss.exe`, `explorer.exe`, `lsass.exe`, `services.exe`, `systemd`, `launchd`, and essential OS services are strictly exempted from throttling.
  * **Developer Compilers Protected**: `code.exe`, `cl.exe`, `gcc.exe`, `g++.exe`, `rustc.exe`, `python.exe`, `py.exe` are never throttled during intensive builds or test suites.
  * **ALFRED Hierarchy Protected**: ALFRED's own process (`os.getpid()`) and all child/worker sub-processes are permanently shielded.
* **Confirmation-Gated Termination Gate (`terminate_process`)**:
  * **Strict Safety Mandate**: To prevent accidental data loss or desktop disruption, processes are **never terminated automatically**.
  * Any termination request is intercepted and dispatched through ALFRED's cryptographic **Single-Click UI Confirmation Gate** (`core/confirm.py`) with an on-screen HUD prompt requiring explicit approval.

---

##  13. Bug Fixes & Stability Updates

* **Windows Modern Audio Endpoint Compatibility**: Fixed volume control in `actions/computer_settings.py` to interface with modern `pycaw.EndpointVolume` scalar setters, resolving attribute errors and eliminating PyAutoGUI mouse failsafe triggers.
* **Path Guard Word Filtering**: Refined `core/path_guard.py` to prevent false-positive path resolution on plain single-word tool parameters (such as `"Save"` or `"File"`).
* **HUD Volume Popup Geometry**: Resolved `QPoint` namespace issue during volume popup positioning in `ui.py`.

---

##  14. System Architecture & File Structure

```
ALFRED-MK-II/
├── main.py                     # Main execution loop, Live WebSocket/Local LLM router, audio streams, tool dispatcher
├── ui.py                       # PyQt6 HUD interface, audio visualizer, drawer settings
├── ui_overlay.py               # Minimalist floating HUD widget for telemetry display
├── setup.py                    # OS-aware package and dependency installer
├── core/
│   ├── prompt.txt              # Master persona directives, execution rules & Heavenly Restriction
│   ├── llm_client.py           # Dual-backend local LLM connector (Ollama / OpenAI-compatible / LM Studio)
│   ├── action_loader.py        # Dynamic action discovery, parameter validation & Heavenly Restriction guard
│   ├── plugin_loader.py        # Drop-in plugin discovery, sandboxing & isolation
│   ├── audio_ducker.py         # Process-level audio ducking for Spotify, Chrome, VLC (pycaw/pulsectl)
│   ├── concurrency.py          # Bounded concurrent worker pool & rate-limiting semaphore
│   ├── cache.py                # Centralized thread-safe TTL/LRU cache with prefix invalidation
│   ├── heal_error.py           # Autonomous runtime error diagnosis and recovery
│   ├── viseme.py               # Unicode articulatory transcription to mouth shapes
│   ├── echo.py                 # Device-calibrated acoustic echo cancellation guard
│   ├── hotkey.py               # Global / local Push-to-Talk chord interceptor
│   ├── undo.py                 # Stack-based reversible action journal
│   ├── confirm.py              # Cryptographic UI confirmation gate for destructive actions
│   ├── audio_devices.py        # Measured host API audio device enumeration (MME / DirectSound / WASAPI)
│   ├── path_guard.py           # Path validation, C: drive quarantine, and Heavenly Restriction enforcement
│   └── wake_word.py            # Local offline openwakeword detection thread
├── actions/                    # Self-describing operational tools (TOOL dictionary schema)
│   ├── protocol_engine.py      # Macro playbook engine executing multi-step YAML workflows
│   ├── screen_find.py          # Local hybrid RapidOCR + ONNX element grounding (<150ms)
│   ├── computer_control.py     # OS automation, keyboard/mouse input, dual screenshots
│   ├── screen_processor.py     # Multi-monitor screen & camera capture engine
│   ├── file_controller.py      # File system operations with path restriction checks
│   ├── file_processor.py       # PDF/DOCX/TXT analysis, parsing, and summarization
│   ├── open_app.py             # OS-specific application and executable launcher
│   ├── computer_settings.py    # Volume, brightness, WiFi, power state management
│   ├── web_search.py           # Multi-mode parallel search (news, research, comparison)
│   ├── intel_notes.py          # Tactical mission note logger and scratchpad
│   ├── proactive.py            # Context-aware proactive check-in engine
│   ├── background_monitor.py   # Daily background topic watcher and headline alerts
│   ├── reminder.py             # OS-native task scheduler notifications
│   ├── system_monitor.py       # Process tree watchdog, anomaly alerts, throttling & socket inspection
│   ├── dev_agent.py            # Autonomous code developer agent with O(1) file matching
│   ├── code_helper.py          # Code analysis, debugging, and generation
│   ├── send_message.py         # WhatsApp and Telegram message dispatcher
│   ├── youtube_video.py        # YouTube search and playback control
│   ├── update_app_icon.py      # Real-time window, taskbar & chassis insignia switcher
│   ├── update_daily_briefing.py# Conversational briefing preference and directive customizer
│   ├── game_updater.py         # Steam and Epic Games library updater
│   ├── flight_finder.py        # Commercial flight search and travel assistant
│   ├── gmail_manager.py        # Local Gmail integration and inbox digest
│   └── weather_report.py       # Localized live meteorological reports
├── config/
│   ├── protocols.yaml          # Macro playbook workflows, trigger words, and compound step definitions
│   ├── api_keys.json           # User credentials, model settings, identity & voice preferences
│   └── certs/                  # Local self-signed SSL/TLS certificates for HTTPS/WSS
├── models/                     # Quantized local ONNX vision & element detection models
│   └── omniparser_v2_quant.onnx# Quantized UI element detector for local grounding
├── plugins/                    # User drop-in plugin folder
│   ├── _template.py            # Reference plugin template
│   ├── calendar_sync.py        # Local agenda, appointments, and meeting scheduling
│   └── focus_protocol.py       # Deep work interval and Pomodoro focus sessions
├── dashboard/                  # Quantum Mobile Remote Server
│   ├── server.py               # FastAPI + Uvicorn + WebSocket encrypted daemon
│   ├── static/
│   │   ├── app.html            # iPhone 16 responsive tactical web app & telemetry console
│   │   └── login.html          # Quantum access matrix login gateway
│   └── uploads/                # Transferred files & captured screenshots
├── memory/
│   ├── memory_manager.py       # High-performance O(N log N) memory persistence and indexing
│   ├── config_manager.py       # Settings, voice, theme, and API key management
│   ├── graph_manager.py        # Dynamic knowledge graph mutation and decay for Graphify
│   └── long_term.json          # Local encrypted fact database
├── tests/                      # Unit, integration & benchmark test suites
│   ├── test_protocol_engine.py # Protocol engine & playbook execution tests
│   ├── test_screen_find.py     # Local hybrid grounding & sub-150ms latency tests
│   ├── test_system_monitor.py  # Process tree anomaly, throttling & socket inspection tests
│   ├── test_audio_ducker.py    # Process-level audio ducking tests
│   ├── test_background_worker.py# Background worker non-blocking concurrency tests
│   ├── test_concurrency.py     # Bounded worker scaling tests
│   ├── test_cache.py           # TTL & LRU caching tests
│   ├── test_heal_error.py      # Auto-healing error recovery tests
│   └── benchmarks/             # 50,000-record execution benchmarks
└── graphify-out/               # GraphRAG knowledge graph, community clusters, and analysis
```

---

##  15. Quick Start & Installation

### 1. Prerequisites
* **Operating System**: Windows 10/11, macOS, or Linux.
* **Python**: `3.11`, `3.12`, or `3.13`.
* **Hardware**: Standard microphone and speakers. *(No dedicated GPU required — runs on lightweight software rendering).*
* **Intelligence Backend**: Either a free Gemini API key from [Google AI Studio](https://aistudio.google.com/) **OR** a local Ollama / LM Studio installation.

### 2. Setup & Execution

```powershell
# Clone the repository
git clone https://github.com/AdityaManojA/ALFRED-MK-II.git
cd ALFRED-MK-II

# Run the OS-tailored dependency setup
python setup.py

# Launch ALFRED
python main.py
```

*On the first launch, if using Gemini, enter your free API key in the setup dialog. If running locally with Ollama, simply point `config/api_keys.json` to your local host.*

---

##  16. Configuration Reference (`config/api_keys.json`)

```json
{
    "assistant_name": "ALFRED",
    "user_name": "Master Wayne",
    "ui_color": "#e5a93b",
    "voice_name": "Charon",
    "wake_word_enabled": false,
    "push_to_talk_enabled": true,
    "llm_provider": "ollama",
    "llm_url": "http://localhost:11434",
    "llm_model": "llama3.2",
    "app_icon": "Icons/Classic Bat.png"
}
```

### Hotkey Shortcuts
| Shortcut | Action |
|---|---|
| `Ctrl+Space` (Hold) | Global Push-to-Talk (opens mic, releases on release) |
| `F4` | Instant Microphone Mute / Unmute |
| `F11` | Toggle Fullscreen / Windowed Tactical HUD |
| `Escape` | Interrupt ALFRED mid-speech (drains queue, re-arms mic) |

---

##  17. Knowledge Graph (`graphify`)

This codebase is indexed with a persistent **GraphRAG Knowledge Graph** located in `graphify-out/`:
* **2,150 nodes** & **4,223 relationships** mapped across 123 semantic functional communities.
* Interactive navigable graph visualization: [`graphify-out/graph.html`](file:///d:/Projects/Personal-Assistant/Mark-LIV/graphify-out/graph.html).
* Architectural breakdown: [`graphify-out/GRAPH_REPORT.md`](file:///d:/Projects/Personal-Assistant/Mark-LIV/graphify-out/GRAPH_REPORT.md).
* **Dynamic Knowledge Graph Management**: Real-time graph mutation, entity/relationship addition, exponential decay, and 2-hop querying via `memory/graph_manager.py` for persistent knowledge evolution and context-aware reasoning.

---

##  18. Author & Credits

* **Lead Architect & Creator:** **ADITYA MANOJ**
* **Original Creator & Core Inspiration:** **[FatihMakes](https://github.com/FatihMakes)** — creator of [Mark-LIV](https://github.com/FatihMakes/Mark-LIV)
* **Project:** ALFRED-MK-II (Wayne Protocol Edition)
* **License:** [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)

---

##  Special Thanks & Acknowledgements

> ### 🌟 Big Shoutout & Gratitude to [FatihMakes](https://github.com/FatihMakes)!
> A massive thank you to **FatihMakes** for developing the original **[Mark-LIV](https://github.com/FatihMakes/Mark-LIV)** project! 
> 
> The initial codebase, architecture vision, and creative inspiration for this entire assistant originated from his phenomenal open-source work. Huge respect and credit to him for laying the foundation.
> 
> 👉 **Original Repository:** [https://github.com/FatihMakes/Mark-LIV](https://github.com/FatihMakes/Mark-LIV) ⭐

---
*Built with precision for autonomy, performance, and complete digital sovereignty.*
