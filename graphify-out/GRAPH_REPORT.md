# Graph Report - Alfred-Mark-IV  (2026-09-27)

## Corpus Check
- 96 files · ~194,096 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 14 file(s) not represented in the graph (top: .ico 7, (none) 3, .obj 2)

## Summary
- 2485 nodes · 4873 edges · 141 communities (113 shown, 28 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 199 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d67306e2`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- game_updater.py
- file_controller.py
- clipboard_manager.py
- file_processor.py
- web_search.py
- code_helper.py
- TelemetryHUD
- doc_rag.py
- system_monitor.py
- JarvisUI
- protocol_engine.py
- computer_settings.py
- MainWindow
- dev_agent.py
- sys
- TestCentralizedCache
- tts.py
- EchoGuard
- desktop.py
- update_daily_briefing.py
- qcol
- JarvisLive
- config_manager.py
- Detailed Step-by-Step Guide: How to Switch to a Local API
- load_api_keys
- plugin_loader.py
- _tlog
- computer_control.py
- llm_client.py
- .run
- RemoteKeyOverlay
- TronScoreBackgroundPlayer
- _BrowserSession
- _RootShim
- time
- main.py
- audio_devices.py
- GraphManager
- datetime
- CentralizedCache
- crypto-js.min.js
- screen_find.py
- action_loader.py
- .__init__
- TacticalAudioPlayerWidget
- VisemeStream
- screen_processor.py
- _DropCanvas
- ui.py
- spotify_control.py
- server.py
- CustomizeOverlay
- computer_settings
- echo.py
- .__init__
- ._receive_audio
- ._build_app
- background_monitor.py
- find_element
- PushToTalk
- setter
- TestBackgroundWorkerPool
- ScreenCapturePayload
- numpy
- NotesTerminalWidget
- save_app_icon
- ._build_right_panel
- ALFRED — MARK-IV (Wayne Protocol Edition)
- _SysMetrics
- format_memory_for_prompt
- mono_font
- ._apply_name_update
- WakeWordDetector
- get_active_window_info
- daily_brief.py
- get_push_to_talk_enabled
- PluginManagerOverlay
- confirm.py
- ._aes_key
- LogWidget
- TestScreenProcessorWindowContext
- DashboardServer
- MemoryOverlay
- SetupOverlay
- TestAudioDucker
- ._build_jarvis_icon
- test_cache.py
- json
- setup.py
- is_heavenly_restricted
- ._toggle_sentry_mode
- SubjectDossierCard
- _detect_action
- test_screen_processor.py
- _gemini_grounding
- ._apply_ptt_shortcut
- CapabilitiesOverlay
- .clear_chat
- ClipboardPanel
- Daily Brief Protocol
- Email Handling Rules
- Executive Assistant Persona & Behavioral Standards
- 🎙️ 3. Master Tactical Voice Command Codex & Operational Handbook
- /email-triage Workflow
- _template.py
- 6. Spotify AI Agent: Dual-Tier Web API & Native Playback Architecture
- _get_base_dir
- pathlib
- Graphify + Antigravity Project Workflow & Setup Guide
- _get_macos_wifi_interface
- ._decrypt
- _ensure_network_access
- rules/graphify.md
- workflows/graphify.md
- chromadb
- chromadb_config
- format_visual_payload
- fastembed
- sentence_transformers
- ._build_system_instruction
- watchdog_events
- watchdog_observers
- format_window_context
- _news
- ._play_audio
- load_memory
- 15. Bug Fixes & Stability Updates
- audio_core
- Step 2: Configure ALFRED's Target Backend in `config/api_keys.json`
- /deep-work Workflow
- .test_error_isolation_in_concurrent_tasks
- _QuotaCooldown
- 17. Quick Start & Installation
- _gemini_headlines
- _get_base_dir

## God Nodes (most connected - your core abstractions)
1. `MainWindow` - 99 edges
2. `JarvisLive` - 65 edges
3. `JarvisUI` - 45 edges
4. `mono_font()` - 36 edges
5. `tech_font()` - 35 edges
6. `_BrowserSession` - 32 edges
7. `TronScoreBackgroundPlayer` - 32 edges
8. `computer_control()` - 26 edges
9. `is_heavenly_restricted()` - 26 edges
10. `DashboardServer` - 26 edges

## Surprising Connections (you probably didn't know these)
- `3. Dedicated Intel & Notes Terminal (`intel_notes`)` --references--> `intel_notes()`  [INFERRED]
  .agents/rules/file_exploration.md → actions/intel_notes.py
- `High-Performance Client & Anti-Feedback Architecture` --references--> `SpotifyClient`  [INFERRED]
  readme.md → actions/spotify_control.py
- `5. Dual-Mode Tactical Audio Matrix & Background Sound Engine` --references--> `audio_core()`  [INFERRED]
  readme.md → actions/audio_core.py
- `Steps` --references--> `computer_control()`  [INFERRED]
  .agents/workflows/deep_work.md → actions/computer_control.py
- `2. Security, Privacy & Defensive Architecture` --references--> `computer_control()`  [INFERRED]
  readme.md → actions/computer_control.py

## Import Cycles
- None detected.

## Communities (141 total, 28 thin omitted)

### Community 0 - "game_updater.py"
Cohesion: 0.06
Nodes (81): _build_google_flights_url(), flight_finder(), _format_spoken(), _format_text_report(), _get_base_dir(), _parse_date(), _parse_flights_with_gemini(), Path (+73 more)

### Community 1 - "file_controller.py"
Cohesion: 0.07
Nodes (63): copy_file(), create_file(), create_folder(), delete_file(), explore_folder(), file_controller(), find_files(), _format_size() (+55 more)

### Community 2 - "clipboard_manager.py"
Cohesion: 0.05
Nodes (40): add_clipboard_item(), classify_content_type(), clipboard_manager_action(), ClipboardManager, cosine_similarity(), _get_active_window_info(), get_recent_clipboards(), is_sensitive_content() (+32 more)

### Community 3 - "file_processor.py"
Cohesion: 0.08
Nodes (45): _detect_type(), file_processor(), _file_size_str(), _gemini_client(), _output_path(), _process_archive(), _process_audio(), _process_code() (+37 more)

### Community 4 - "web_search.py"
Cohesion: 0.22
Nodes (18): _compare(), _fetch_item(), _ddg_search(), _format_ddg(), _gemini_available(), _gemini_search(), _log_gemini_failure(), _note_gemini_error() (+10 more)

### Community 5 - "code_helper.py"
Cohesion: 0.08
Nodes (48): _build(), _clean_code(), code_helper(), _detect_intent(), _edit_action(), _explain_action(), _fix_code(), _get_gemini() (+40 more)

### Community 6 - "TelemetryHUD"
Cohesion: 0.13
Nodes (11): main(), QWidget, Set up the update timer., Set up system tray icon for control., Handle mouse press for dragging., Handle mouse move for dragging., Update all telemetry displays., Main entry point for the HUD widget. (+3 more)

### Community 7 - "doc_rag.py"
Cohesion: 0.09
Nodes (35): _ChangeHandler, _chunk_text(), crawl_and_index(), _delete_file_chunks(), _detokenize_tokens(), _extract_text_from_file(), _get_chroma_collection(), _get_embedding_model() (+27 more)

### Community 8 - "system_monitor.py"
Cohesion: 0.07
Nodes (38): _get_cpu_temp(), _get_gpu_usage(), get_system_status(), _is_private_or_loopback(), is_protected_process(), _nvml_gpu(), Any, actions/system_monitor.py — System Metric Checks, Process Tree Watchdog &… (+30 more)

### Community 9 - "JarvisUI"
Cohesion: 0.06
Nodes (15): JarvisUI, Thread-safe: raise the irreversible-action gate. Called from action handlers…, Thread-safe: take the gate down., Thread-safe: feed a 0.0–1.0 live audio level to the HUD waveform. Called from…, Ask the avatar to look somewhere for a moment (see HoloAvatar.glance)., Thread-safe: post a schedule of (level, openness, width) mouth frames for…, Thread-safe: wipe the on-screen conversation chat feed., Thread-safe: post special note, research link, or structured data to the… (+7 more)

### Community 10 - "protocol_engine.py"
Cohesion: 0.07
Nodes (39): create_protocol(), _do_save(), execute_protocol(), _execute_tool(), get_action_registry(), get_protocols_file(), interpolate_variables(), _is_failure() (+31 more)

### Community 12 - "MainWindow"
Cohesion: 0.05
Nodes (11): QMainWindow, MainWindow, Slot — display camera preview overlay (main thread)., Slot — runs on Qt main thread. Updates and shows the content panel., Slot — Qt main thread. Lays a document review into the content panel., Slot — Qt main thread. Puts a fresh quiz on the board., Place a floating overlay in the middle of the HUD and show it., Update bottom-left tactical audio player to display and control Spotify… (+3 more)

### Community 13 - "dev_agent.py"
Cohesion: 0.15
Nodes (23): _build_project(), _classify_error(), _extract_culprit_script(), _fix_files(), _get_model(), _has_error(), _install_dependencies(), _is_rate_limit() (+15 more)

### Community 14 - "sys"
Cohesion: 0.15
Nodes (16): _available(), install_for_config(), _pip(), MARK XL — Dependency auto-installer. Called automatically on first launch and…, Return True if the module can be imported (no actual import)., Install all missing packages required by *config*. Blocking — always call from…, install_and_download(), is_installed() (+8 more)

### Community 15 - "TestCentralizedCache"
Cohesion: 0.12
Nodes (8): Verifies that cache errors do not crash callers., Verifies that key generation is deterministic across varying argument orders., Tests basic cache-aside hit and miss lifecycle., Verifies that entries expire after their TTL has elapsed., Tests prefix-based bulk invalidation for mutation hooks., Verifies that exceeding max_entries triggers eviction without unbounded growth., Tests @cached decorator with automatic cache-aside resolution., TestCentralizedCache

### Community 16 - "tts.py"
Cohesion: 0.07
Nodes (25): _compress_silence(), create_tts_player(), EdgeTTSEngine, ElevenLabsTTSEngine, _import_kokoro_pipeline(), KokoroTTSEngine, _synth(), _play_audio_bytes() (+17 more)

### Community 17 - "EchoGuard"
Cohesion: 0.08
Nodes (14): band_energies(), EchoGuard, ndarray, Classifies microphone blocks while the assistant is speaking. Usage:…, True once the estimate rests on enough real echo to be trusted., Residual left by this room's own echo. Higher = harder to separate., False when the acoustics are too poor to judge on content alone. Speakers…, The residual a block must clear right now to count as a voice. (+6 more)

### Community 18 - "desktop.py"
Cohesion: 0.12
Nodes (36): _ask_gemini_for_desktop_action(), _build_sandbox(), clean_desktop(), desktop_control(), _execute_generated_code(), _get_api_key(), _get_base_dir(), get_current_wallpaper() (+28 more)

### Community 19 - "update_daily_briefing.py"
Cohesion: 0.29
Nodes (7): Update Daily Briefing Preferences Action for ALFRED Mark-LIV. Permanently…, Permanently saves daily briefing preferences into long-term memory., update_daily_briefing(), _recursive_update(), remember(), _truncate_value(), update_memory()

### Community 20 - "qcol"
Cohesion: 0.08
Nodes (19): QColor, QPainter, QPixmap, HudCanvas, qcol(), Ask the avatar to look somewhere for a moment (see HoloAvatar.glance)., Thread-safe: hand over a schedule of (level, openness, width) frames. The…, Thread-safe entry point for the audio threads. Stores the louder of the… (+11 more)

### Community 21 - "JarvisLive"
Cohesion: 0.09
Nodes (11): JarvisLive, Chord pressed or released — may arrive on the hotkey thread., Load the detector once (model loads on first start). Idempotent., Called from the detector thread when 'Hey Jarvis' is heard., Auto-sleep after the configured silence window (wake-word mode only)., Enable/disable wake word from the settings UI. Returns a status token:…, Manual sleep/wake button in the UI., Download openwakeword + the model (runs in a UI worker thread). (+3 more)

### Community 22 - "config_manager.py"
Cohesion: 0.13
Nodes (24): ensure_config_dir(), get_base_dir(), _patch_config(), Path, Persist the chosen Live voice. Unknown names collapse to the default so a bad…, Read-modify-write one key without disturbing the rest of the config., Read-modify-write one or more keys in api_keys.json. Every setter in this file…, Merge `values` into a namespace's stored config (read-modify-write, like every… (+16 more)

### Community 23 - "Detailed Step-by-Step Guide: How to Switch to a Local API"
Cohesion: 0.22
Nodes (9): 1. 100% Local & Air-Gapped Offline Execution: Switching from Gemini to Local API, Detailed Step-by-Step Guide: How to Switch to a Local API, Gemini Live API vs. Local Offline API Comparison, Option A: Ollama (Recommended — Simplest Setup), Option B: LM Studio (Recommended for GUI Users), Option C: vLLM or llama.cpp (High-Throughput / Linux Servers), Step 1: Install & Set Up Your Preferred Local LLM Server, Step 3: Launch ALFRED & Verify Connection (+1 more)

### Community 24 - "load_api_keys"
Cohesion: 0.11
Nodes (20): LiveConnectConfig, The optional knobs, kept apart so one bad field can be dropped wholesale. Every…, get_app_icon(), get_gemini_key(), get_llm_provider(), get_media_resolution(), get_openrouter_key(), get_openrouter_model() (+12 more)

### Community 25 - "plugin_loader.py"
Cohesion: 0.10
Nodes (22): _call_run(), discover_plugins(), _load_error(), _opt_upper(), PluginRecord, PluginRegistry, Exception, Path (+14 more)

### Community 26 - "_tlog"
Cohesion: 0.14
Nodes (11): broadcast_progress(), _deliver_news(), main(), runner(), Queue a background task and return task metadata immediately., Announce background completion ensuring ALFRED does not talk over active speech., Execute a single background job, streaming [control] [background XX%] progress., Worker loop consuming background jobs from background_task_queue. (+3 more)

### Community 27 - "computer_control.py"
Cohesion: 0.15
Nodes (29): _base_dir(), _clear_field(), _click(), _clipboard_get(), _clipboard_paste(), computer_control(), _drag(), _focus_window() (+21 more)

### Community 28 - "llm_client.py"
Cohesion: 0.15
Nodes (25): call_llm(), call_llm_stream(), call_llm_text(), _chat_endpoint(), check_model_available(), ensure_ollama_running(), get_base_dir(), _get_headers() (+17 more)

### Community 29 - ".run"
Cohesion: 0.12
Nodes (11): BaseException, _get_api_key(), _is_reconnect_signal(), _keep_context_of(), Background task: voice alerts when metrics exceed thresholds., Check user-configured topics once per day; speak alerts when new headlines…, Background task: periodically checks if the user has been silent long enough,…, Forward phone mic PCM chunks from dashboard queue into the Gemini Live session. (+3 more)

### Community 30 - "RemoteKeyOverlay"
Cohesion: 0.27
Nodes (4): Floating overlay — QR code for instant phone pairing + manual key fallback., Call from any thread when a phone successfully connects., RemoteKeyOverlay, _lbl()

### Community 31 - "TronScoreBackgroundPlayer"
Cohesion: 0.08
Nodes (12): control_playback(), QObject, _base_dir(), Path, Background music audio engine. Plays background score continuously on loop…, Set base normal volume (0.0 to 1.0). Speech ducking scales to 50% of base., Duck to 50% of base volume when speaking, restore to base volume when…, Called when Spotify plays a track. Pauses Tron background music, sets Spotify… (+4 more)

### Community 32 - "_BrowserSession"
Cohesion: 0.05
Nodes (23): browser_control(), _BrowserSession, _detect_default_browser(), _find_exe_windows(), _find_opera_windows(), _firefox_profile_dir(), _log(), _normalize_url() (+15 more)

### Community 34 - "time"
Cohesion: 0.16
Nodes (10): _parse_traceback(), asyncio, Performance Benchmark: dev_agent._parse_traceback Tests O(1) hash map lookups…, Measures lookup time across 50,000 mock project files and 500 stack frames., TestTracebackBenchmark, Verify that a batch of tasks run with a concurrency limit of 5 scales sub-…, TestConcurrencyLimiter, time (+2 more)

### Community 35 - "main.py"
Cohesion: 0.11
Nodes (12): ProactiveEngine, ProactiveEngine 2.0 — context-aware, time-aware, non-repetitive background…, Decides when ALFRED should speak unprompted and builds a context-rich prompt.…, google, google_genai, _Popen, Exception, Raised inside the session TaskGroup to force a clean, voluntary reconnect (e.g.… (+4 more)

### Community 36 - "audio_devices.py"
Cohesion: 0.12
Nodes (18): configure(), _display_name(), _is_pseudo(), prefetch(), _work(), _query(), _collect(), core/audio_devices.py — pick which microphone and which speakers ALFRED uses.… (+10 more)

### Community 37 - "GraphManager"
Cohesion: 0.11
Nodes (14): GraphManager, Any, Path, Save the graph data to the JSON file atomically., Add an entity node to the graph. Returns True if successful., Add a relationship (edge) between two nodes. Returns True if successful., Apply exponential decay to all temporary nodes. Returns the number of nodes…, Query the knowledge graph for a concept and return connected subgraph up to… (+6 more)

### Community 38 - "datetime"
Cohesion: 0.06
Nodes (43): _clean_header_str(), _extract_body_snippet(), gmail_manager(), _load_gmail_creds(), Any, Gmail Manager Action for ALFRED Mark-LIV. Provides full Gmail connectivity: -…, Send an email using Gmail SMTP SSL., Action entry point for Gmail interaction. (+35 more)

### Community 39 - "CentralizedCache"
Cohesion: 0.12
Nodes (14): CentralizedCache, _canonicalize(), decorator(), wrapper(), Any, Stores value in cache with TTL. Fails open gracefully if storage fails., Deletes a key from cache. Fails open gracefully., Invalidates all keys starting with prefix. Useful for mutation hooks. (+6 more)

### Community 41 - "screen_find.py"
Cohesion: 0.15
Nodes (18): _calculate_similarity(), _get_frame_key(), get_onnx_session(), get_rapid_ocr(), _ocr_grounding(), Any, ndarray, actions/screen_find.py — Local Hybrid Element Grounding for ALFRED. Performs… (+10 more)

### Community 42 - "action_loader.py"
Cohesion: 0.12
Nodes (15): ActionRecord, ActionRegistry, _call_handler(), discover_actions(), _is_heavenly_restricted_params(), _opt_upper(), Path, Action discovery, validation, and dispatch — the built-in twin of… (+7 more)

### Community 43 - ".__init__"
Cohesion: 0.08
Nodes (10): BiometricFingerprintWidget, CRTReconWidget, _EqualizerBarsWidget, MetricBar, QWidget, Halftone / CRT Dithered Optical Recon Scanner Widget (Screenshot 1: Top-Left…, Biometric Fingerprint Scanner Widget (Screenshot 1: Middle-Left Biometric Box).…, Tactical Wireframe Humanoid Telemetry Widget (Screenshot 1: Lower-Left… (+2 more)

### Community 44 - "TacticalAudioPlayerWidget"
Cohesion: 0.14
Nodes (5): QFrame, Sleek tactical cyber popup for adjusting master background music volume.…, Bottom-Left Cyber Tactical Audio Player Widget. Styled matching the HUD /…, TacticalAudioPlayerWidget, _VolumeSliderPopup

### Community 45 - "VisemeStream"
Cohesion: 0.13
Nodes (12): collections, coverage(), Text → mouth shape, fused with the audio the avatar is actually speaking. Why…, Reduce any character to a bare Latin letter, or "" if it has none. This is what…, Fraction of the letters in `text` we can reduce to a Latin sound., Split a line of speech into (viseme, duration-weight) pairs. Returns [] for…, Fuses the transcript's shape sequence onto the audio's timing. Thread note:…, Blend audio frames [(level, openness, width)] with the text queue. (+4 more)

### Community 46 - "screen_processor.py"
Cohesion: 0.15
Nodes (19): _base_dir(), _capture_camera(), _cv2_backend(), _detect_camera_index(), _get_camera_index(), _get_os(), _load_config(), _probe_camera() (+11 more)

### Community 47 - "_DropCanvas"
Cohesion: 0.29
Nodes (3): _DropCanvas, _file_category(), _fmt_size()

### Community 48 - "ui.py"
Cohesion: 0.10
Nodes (21): list_devices(), Device names for 'input' or 'output'. Falls back to a synchronous query if the…, core_avatar, get_brief_enabled(), get_hud_style(), get_input_device(), get_output_device(), Which centrepiece the HUD draws: the animated head, or the reactor core. Taste,… (+13 more)

### Community 49 - "spotify_control.py"
Cohesion: 0.05
Nodes (42): authorize_user(), _get_base_dir(), get_devices(), get_spotify_client(), manage_queue(), _OAuthCallbackHandler, Any, Path (+34 more)

### Community 50 - "server.py"
Cohesion: 0.11
Nodes (16): index(), _ensure_certs(), _local_ip(), _make_uploads_dir(), Path, dashboard/server.py — ALFRED Local HTTP Dashboard Plain HTTP on port 8000 (no…, Return the best LAN-facing IPv4 address, no internet required., Make sure config/certs holds a TLS key pair, generating a self-signed one the… (+8 more)

### Community 51 - "CustomizeOverlay"
Cohesion: 0.05
Nodes (14): QDragEnterEvent, QDropEvent, QPointF, QRectF, CustomizeOverlay, _lbl(), CyberGraphicLineButton, FileDropZone (+6 more)

### Community 52 - "computer_settings"
Cohesion: 0.12
Nodes (16): brightness_get(), brightness_set(), computer_settings(), dark_mode(), paste(), press_key(), Current brightness 0-100, or None where it cannot be read., Set brightness to an absolute percentage. Only used to restore a value captured… (+8 more)

### Community 53 - "echo.py"
Cohesion: 0.10
Nodes (14): _duck_linux(), duck_media_apps(), _worker(), _duck_windows(), is_ducked(), Execute ducking on Linux via pulsectl., Lower external media application volume (by default to 30%, i.e. ducking by…, Restore ducked media applications to their exact original volume levels. :param… (+6 more)

### Community 54 - ".__init__"
Cohesion: 0.11
Nodes (5): _fl(), Floating overlay panel shown when the ⚙ header button is toggled., Returns True if auto-start is currently registered on this OS., Open the API key and neural backend configuration overlay from settings., Update application and window icon in realtime.

### Community 55 - "._receive_audio"
Cohesion: 0.20
Nodes (6): FunctionResponse, _clean_transcript(), _is_repeat_chunk(), _run_tool_bounded(), Send a captured frame immediately after its tool response. The frame is already…, True if this transcript chunk has already been seen this turn. Guards against…

### Community 56 - "._build_app"
Cohesion: 0.15
Nodes (14): action_ep(), audio_ws(), _auth(), clear_chat_ep(), command(), download_file(), list_files(), phone_audio_ws() (+6 more)

### Community 57 - "background_monitor.py"
Cohesion: 0.26
Nodes (13): add_monitor(), check_all(), _is_blocked(), list_monitors(), _load(), BackgroundMonitor — user-configured topic watching. Checks DDG news once per…, Run all pending topic checks (once per day per topic). Returns a list of…, remove_monitor() (+5 more)

### Community 58 - "find_element"
Cohesion: 0.14
Nodes (12): find_element(), is_icon_query(), Determine if target query is specifically targeting an icon/non-text element., Main entry point for local hybrid UI element grounding. 1. Executes RapidOCR on…, Action handler called by ALFRED action dispatcher., screen_find(), 8. Full Desktop Control & Operating System Automation, Verification Requirement: Call find_element('Save') on a text editor window.… (+4 more)

### Community 59 - "PushToTalk"
Cohesion: 0.17
Nodes (6): PushToTalk, Begin watching. Returns the scope actually achieved., Feed a press/release from a Qt shortcut (non-Windows, or no hook)., Calls `on_change(held: bool)` whenever the chord is pressed or released. Start…, global' once a system-wide hook is running, else 'window'., Turn hold-to-talk on or off. Returns the scope actually achieved.

### Community 60 - "setter"
Cohesion: 0.11
Nodes (3): setter, _work(), Combined state for the two wake-word buttons. Readiness is a cheap,…

### Community 61 - "TestBackgroundWorkerPool"
Cohesion: 0.12
Nodes (7): Verify that calling interrupt() sets halt event, immediately stops active…, Verify that _safe_background_announce waits until ALFRED finishes speaking…, Verify DashboardServer tracks background tasks and exposes them via endpoint., Verify queue_background_task is registered in TOOL_DECLARATIONS., Verify that queue_background_task returns immediately (sub-millisecond), and…, Dispatch a mock task and verify voice PTT interaction continues with sub-second…, TestBackgroundWorkerPool

### Community 62 - "ScreenCapturePayload"
Cohesion: 0.20
Nodes (4): Hybrid return payload for screen captures. - Behaves as a 3-tuple `(img_bytes,…, ScreenCapturePayload, _do_stream(), tuple

### Community 63 - "numpy"
Cohesion: 0.14
Nodes (9): ndarray, Speech-to-Text engines for MARK XL. Whisper – offline transcription via faster-…, Offline transcription using faster-whisper., Transcribe a float32 mono 16 kHz numpy array. Returns transcript string., Streaming transcription using Vosk., Feed raw int16 LE PCM bytes. Returns (text, is_final)., VoskSTT, WhisperSTT (+1 more)

### Community 65 - "save_app_icon"
Cohesion: 0.20
Nodes (10): Update App Icon Action for ALFRED Mark-LIV. Switches the application window,…, Updates the main application icon and taskbar badge in realtime., update_app_icon(), Save the chosen app icon setting to config., save_app_icon(), format_icon_display_name(), get_available_app_icons(), Format an icon file name into an authentic, sleek tactical insignia title. (+2 more)

### Community 66 - "._build_right_panel"
Cohesion: 0.18
Nodes (3): QHBoxLayout, Read api_keys.json config dict. Returns {} on any error., _read_full_config()

### Community 67 - "ALFRED — MARK-IV (Wayne Protocol Edition)"
Cohesion: 0.13
Nodes (14): 10. Real-Time Insignia & Chassis Hot-Swapper, 11. Protocol Engine & Multi-Step Macro Playbooks (`config/protocols.yaml`), 12. Local Hybrid Visual Grounding (RapidOCR + ONNX + Gemini Fallback), 13. Process-Level Audio Ducking & Background Concurrency, 16. System Architecture & File Structure, 18. Configuration Reference (`config/api_keys.json`), 19. Knowledge Graph (`graphify`), 20. Author & Credits (+6 more)

### Community 68 - "_SysMetrics"
Cohesion: 0.13
Nodes (7): Thread-safe speech channel for plugins: lets a plugin ask JARVIS to say…, Thread-safe: ask the run loop to tear down and rebuild the Live session. Called…, Voice picker applied. The voice is baked into the session at connect time, so a…, Microphone or speaker changed. Both streams are opened inside the session…, _nvml_gpu_windows(), Return NVIDIA GPU utilisation % using nvml.dll directly — zero subprocess., _SysMetrics

### Community 69 - "format_memory_for_prompt"
Cohesion: 0.22
Nodes (10): Build a context snapshot for Gemini. Rotates through three focus areas so…, _entry_value(), format_memory_for_prompt(), _pretty(), Accept both the {'value': ..., 'updated': ...} shape and a bare string, because…, Build the memory block that goes into the system prompt. This used to dump…, Cheap lexical relevance. No embeddings, no network, no model call - this runs…, Find stored facts matching `query`. Backs the recall_memory tool. An empty… (+2 more)

### Community 70 - "mono_font"
Cohesion: 0.14
Nodes (10): QFont, QVBoxLayout, _CameraPreview, mono_font(), PluginSettingsOverlay, Floating overlay that briefly shows what the camera captured., Floating overlay — renders per-plugin settings forms. Fully generic: it…, Collapsible panel below the HUD — shows search results, news, briefings. Hidden… (+2 more)

### Community 71 - "._apply_name_update"
Cohesion: 0.20
Nodes (8): apply_ui_accent(), current_palette(), Applies DOSSIER CRT [A-34] (#8e9bff), VECTOR CRT [WAKU] (#a8ff3e), or BATMAN…, A snapshot of the accent-linked colours currently on class C., LIVE full theme change. Replaces the old palette colours with the new ones in…, Live preview — paints the whole interface the new colour (does NOT write to…, Update all name/theme-dependent UI elements and persist to config., retheme_all_widgets()

### Community 72 - "WakeWordDetector"
Cohesion: 0.20
Nodes (4): Runs the wake model in a dedicated thread. The mic thread calls feed() with raw…, Load the model and spawn the inference thread. Returns True on success. Safe to…, Called from the mic callback (real-time thread). Must stay cheap and never…, WakeWordDetector

### Community 73 - "get_active_window_info"
Cohesion: 0.20
Nodes (10): get_active_window_context(), get_active_window_info(), _get_linux_window_info(), _get_macos_window_info(), _get_windows_window_info(), Query foreground window handle, title, and process name on Windows., Query active frontmost window on macOS via Quartz or AppleScript fallback., Query active window on Linux via xdotool or wmctrl. (+2 more)

### Community 74 - "daily_brief.py"
Cohesion: 0.13
Nodes (20): daily_brief(), _get_gmail_brief(), _get_greeting(), _get_live_weather(), _get_reminders_brief(), _get_system_vitals(), Daily Brief Action for ALFRED Mark-LIV. Provides the ultimate morning and daily…, Fetch unread emails summary via gmail_manager. (+12 more)

### Community 75 - "get_push_to_talk_enabled"
Cohesion: 0.29
Nodes (5): chord_label(), Human-readable name of the chord, for the UI and the logs., get_push_to_talk_enabled(), Hold-a-key-to-speak. When on, the mic is closed unless the chord is held., Repaint the push-to-talk row from the saved setting.

### Community 76 - "PluginManagerOverlay"
Cohesion: 0.31
Nodes (3): QPushButton, PluginManagerOverlay, Floating overlay — lists discovered plugins with per-plugin ON/OFF toggles.

### Community 77 - "confirm.py"
Cohesion: 0.21
Nodes (12): bind(), _log(), _Pending, pending_title(), core/confirm.py — a confirmation the model cannot forge. THE PROBLEM WITH THE…, Called by the UI when the user presses CONFIRM or CANCEL. Runs the stored…, when nothing is waiting. Lets an action avoid stacking two banners., Wire this module to the HUD. Called once from main.py at startup. (+4 more)

### Community 78 - "._aes_key"
Cohesion: 0.31
Nodes (5): auto_login(), device_login_ep(), login(), _derive_key(), SHA-256(sessionKey‖salt) → 32-byte AES-256 key (microseconds, no PBKDF2 needed).

### Community 79 - "LogWidget"
Cohesion: 0.25
Nodes (3): QTextEdit, LogWidget, Cancel any in-flight typing animation, drain the queue, and clear the display.

### Community 80 - "TestScreenProcessorWindowContext"
Cohesion: 0.22
Nodes (5): Verifies system falls back to 'App: Unknown' without raising exceptions., Verification Requirement: Verify [WINDOW_CONTEXT] header contains VS Code and…, Verifies that active window query resolves in < 15ms and adheres to schema., Verifies capture_screen() returns valid compressed image and window context., TestScreenProcessorWindowContext

### Community 82 - "MemoryOverlay"
Cohesion: 0.17
Nodes (8): ConfirmBanner, _HudOverlay, MemoryOverlay, Base for the floating panels placed by hand over the HUD. They are children of…, The gate in front of an action that cannot be taken back. The old confirmation…, Everything ALFRED has stored about you, and when it learned it. Memory used to…, Take every item out of the layout and detach it from the widget tree in this…, Size the panel to its content, re-centre it, and repaint what the old size…

### Community 84 - "TestAudioDucker"
Cohesion: 0.29
Nodes (4): patch, Verify that duck_media_apps lowers target media processes by 70% (0.3 factor),…, Verify Linux pulsectl ducking fallback logic., TestAudioDucker

### Community 85 - "._build_jarvis_icon"
Cohesion: 0.22
Nodes (4): Render an ALFRED tactical icon at 4× resolution and downsample for crisp…, Create a Windows .lnk shortcut WITHOUT launching PowerShell or cmd. Tries…, Resolve the user's REAL desktop directory instead of assuming ~/Desktop, which…, Create a desktop shortcut on Windows / macOS / Linux. Never opens a terminal,…

### Community 86 - "test_cache.py"
Cohesion: 0.25
Nodes (6): get_cache(), Returns the centralized cache client singleton., patch, tests/test_cache.py — Comprehensive Test Suite for CentralizedCache. Tests: -…, Tests that weather queries are cached and subsequently invalidated by…, TestCacheIntegrationHooks

### Community 87 - "json"
Cohesion: 0.13
Nodes (16): json, _all_entries(), forget(), get_base_dir(), pop_last_session(), Path, Return AND remove the most recent session entry. Calling this consumes the…, Register a callable(str) that surfaces trims to the user. (+8 more)

### Community 88 - "setup.py"
Cohesion: 0.36
Nodes (7): _check_assets(), _check_python(), main(), MARK LIV — one-time setup. Installs the Python dependencies for THIS operating…, Fail immediately and clearly rather than deep inside a pip resolver. A wrong…, The avatar's face is a shipped file; a truncated clone should say so., _run()

### Community 89 - "is_heavenly_restricted"
Cohesion: 0.10
Nodes (27): apply_heal_patch(), dev_agent(), _diagnose_trace(), heal_execution_error(), _heuristic_repair(), Parses stderr and stack traces to isolate error category, line number, and…, Attempts fast, deterministic rule-based fixes for standard syntax and import…, r""" Automated diagnostic and self-repair engine for tool and script execution… (+19 more)

### Community 90 - "._toggle_sentry_mode"
Cohesion: 0.33
Nodes (3): Toggle continuous visual context (camera stream) monitoring., Thread-safe: start live camera feed in the full HUD area., Thread-safe: stop the live camera feed.

### Community 92 - "_detect_action"
Cohesion: 0.40
Nodes (5): _detect_action(), _normalise(), Resolve a free-text description to an action name, locally. Returns {"action":…, What to tell the model when nothing matched. Names real actions so its retry…, _suggest()

### Community 93 - "test_screen_processor.py"
Cohesion: 0.29
Nodes (7): capture_screen(), _capture_screen(), _compress(), Captures primary or specified monitor, queries active OS window context,…, Default entry point used by main.py., base64, Unit and integration tests for screen_processor.py window context grounding.…

### Community 94 - "_gemini_grounding"
Cohesion: 0.22
Nodes (9): _capture_screen_image(), _gemini_grounding(), _get_api_key(), _onnx_element_grounding(), Capture current screen into a PIL Image., Run local ONNX element detector (OmniParser-v2 / Florence-2). Returns:…, Fallback visual grounding via Gemini Live / Flash API., Retrieve Gemini API key from api_keys.json or environment. (+1 more)

### Community 95 - "._apply_ptt_shortcut"
Cohesion: 0.29
Nodes (5): qt_sequence(), The same chord as a QKeySequence string., _press(), Bind the chord inside the window when no global hook is available. On macOS and…, Report a windowed press/release to whoever owns the microphone.

### Community 99 - "Daily Brief Protocol"
Cohesion: 0.50
Nodes (3): Daily Brief Protocol, Purpose, Rules

### Community 100 - "Email Handling Rules"
Cohesion: 0.50
Nodes (3): Email Handling Rules, Purpose, Rules

### Community 101 - "Executive Assistant Persona & Behavioral Standards"
Cohesion: 0.50
Nodes (3): Core Operational Rules, Executive Assistant Persona & Behavioral Standards, Persona & Demeanor

### Community 102 - "🎙️ 3. Master Tactical Voice Command Codex & Operational Handbook"
Cohesion: 0.22
Nodes (9): 🎵 1. Tactical Audio Core (TRON Background Engine), 🎧 2. Spotify AI Agent & Music Streaming, 👁️ 3. Desktop Automation, Screen & Multimodal Vision, 🎙️ 3. Master Tactical Voice Command Codex & Operational Handbook, ⚙️ 4. Operating System, Hardware Settings & Applications, ⚡ 5. Compound Protocols & Workflow Macros, 📰 6. Intelligence, Briefings, News & Weather, 🧠 7. Memory, History & Universal Reversibility (+1 more)

### Community 103 - "/email-triage Workflow"
Cohesion: 0.50
Nodes (3): /email-triage Workflow, Objective, Steps

### Community 104 - "_template.py"
Cohesion: 0.50
Nodes (3): Drop-in ALFRED plugin template. Copy this file, rename it (no leading…, parameters: dict of the args Gemini extracted, matching PLUGIN['parameters'].…, run()

### Community 105 - "6. Spotify AI Agent: Dual-Tier Web API & Native Playback Architecture"
Cohesion: 0.22
Nodes (9): 6. Spotify AI Agent: Dual-Tier Web API & Native Playback Architecture, Dual-Tier Control Architecture, Elimination of the Toggle Inversion Bug, High-Performance Client & Anti-Feedback Architecture, Key Capabilities & Default Music Routing, Spotify API & OAuth 2.0 Setup Guide, Step 1: Create a Spotify Developer Application, Step 2: Add Credentials to `config/api_keys.json` (+1 more)

### Community 106 - "_get_base_dir"
Cohesion: 0.67
Nodes (3): _get_api_key(), _get_base_dir(), Path

### Community 107 - "pathlib"
Cohesion: 0.08
Nodes (28): Tactical Audio Core Control Action for ALFRED. Controls the tactical HUD's…, _auto_detect_type(), _config_dir(), intel_notes(), _load_notes(), Path, actions/intel_notes.py — Dedicated Intel & Notes Terminal Action. Provides a…, Action handler called by Gemini / action_loader. (+20 more)

### Community 110 - "._decrypt"
Cohesion: 0.50
Nodes (3): ws_ep(), _decrypt_cbc(), Decrypt base64(IV[16] ‖ ciphertext) with AES-256-CBC + PKCS7.

### Community 111 - "_ensure_network_access"
Cohesion: 0.25
Nodes (3): _ensure_network_access(), Cross-platform, best-effort: open port in the OS firewall for LAN access. Runs…, Second HTTPS server on PORT+1 sharing the same app and in-memory state. Chrome…

### Community 116 - "format_visual_payload"
Cohesion: 0.40
Nodes (3): format_visual_payload(), Prepares the visual frame payload dictionary for the Gemini Live API…, Verifies metadata block is prepended directly to the visual frame payload.

### Community 124 - "._build_system_instruction"
Cohesion: 0.25
Nodes (7): _describe_limits(), _describe_tools(), _load_system_prompt(), One line per capability, straight from the live tool declarations. Derived…, The other half of self-knowledge: what is out of reach, and why. Derived from…, Fill {tokens} in the prompt template. A plain replace rather than str.format:…, _render_prompt()

### Community 127 - "format_window_context"
Cohesion: 0.50
Nodes (3): format_window_context(), Format the standard metadata block: [WINDOW_CONTEXT] App: <Name> | Title:…, Verifies exact string formatting requirements.

### Community 128 - "_news"
Cohesion: 0.18
Nodes (11): _ddg_news(), _format_news(), _get_ddgs(), _news(), _ddg_attempt(), Returns the DDGS class. The package was renamed duckduckgo-search -> ddgs; the…, DDG news search — returns actual articles, not website homepages., DDG first, Gemini as backup, with 15-minute caching to protect quota. (+3 more)

### Community 129 - "._play_audio"
Cohesion: 0.20
Nodes (7): callback(), _open_mic(), _pcm_level(), _pcm_visemes(), Map a block of int16 PCM samples to a 0.0–1.0 loudness level for the HUD…, Slice a PCM block into (level, openness, width) frames, one per 20 ms. Returns…, True while the speakers may still be finishing our last sentence.

### Community 130 - "load_memory"
Cohesion: 0.25
Nodes (8): _do_shutdown(), Summarise the current session in 1-2 sentences and save to long_term.json., all_entries_for_ui(), _empty_memory(), load_memory(), Flat list for the memory panel: what ALFRED knows, and when it learned it.…, Append a 1-2 sentence session summary to long_term.json['sessions']., save_session_summary()

### Community 131 - "15. Bug Fixes & Stability Updates"
Cohesion: 0.40
Nodes (3): 15. Bug Fixes & Stability Updates, Pause the Audio Core (TRON background music engine)., Resume or play the Audio Core (TRON background music engine).

### Community 132 - "audio_core"
Cohesion: 0.50
Nodes (4): audio_core(), Any, Main handler for the Audio Core control action., 5. Dual-Mode Tactical Audio Matrix & Background Sound Engine

### Community 133 - "Step 2: Configure ALFRED's Target Backend in `config/api_keys.json`"
Cohesion: 0.50
Nodes (4): Configuration Template for LM Studio / vLLM (OpenAI-Compatible):, Configuration Template for Ollama:, Configuration Template for OpenRouter API (Frontier Multi-Model Gateway):, Step 2: Configure ALFRED's Target Backend in `config/api_keys.json`

### Community 134 - "/deep-work Workflow"
Cohesion: 0.50
Nodes (3): /deep-work Workflow, Objective, Steps

### Community 135 - ".test_error_isolation_in_concurrent_tasks"
Cohesion: 0.67
Nodes (3): Verify that an exception in one concurrent task does not break or cancel…, execute_task(), safe_run()

### Community 136 - "_QuotaCooldown"
Cohesion: 0.67
Nodes (3): _QuotaCooldown, Raised instead of calling Gemini while the quota breaker is open., RuntimeError

### Community 137 - "17. Quick Start & Installation"
Cohesion: 0.67
Nodes (3): 17. Quick Start & Installation, 1. Prerequisites, 2. Setup & Execution

## Knowledge Gaps
- **52 isolated node(s):** `C`, `Purpose`, `Rules`, `Purpose`, `Rules` (+47 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1024 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **28 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MainWindow` connect `MainWindow` to `CapabilitiesOverlay`, `.clear_chat`, `._build_right_panel`, `15. Bug Fixes & Stability Updates`, `save_app_icon`, `mono_font`, `._apply_name_update`, `.__init__`, `PluginManagerOverlay`, `get_push_to_talk_enabled`, `.closeEvent`, `_DropCanvas`, `ui.py`, `._build_jarvis_icon`, `.__init__`, `._toggle_sentry_mode`, `setter`, `._apply_ptt_shortcut`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Why does `JarvisLive` connect `JarvisLive` to `._play_audio`, `load_memory`, `system_monitor.py`, `JarvisUI`, `EchoGuard`, `load_api_keys`, `_tlog`, `llm_client.py`, `.run`, `time`, `main.py`, `VisemeStream`, `echo.py`, `._receive_audio`, `background_monitor.py`, `PushToTalk`, `TestBackgroundWorkerPool`, `_SysMetrics`, `WakeWordDetector`, `DashboardServer`, `._build_system_instruction`?**
  _High betweenness centrality (0.046) - this node is a cross-community bridge._
- **Why does `ALFRED — MARK-IV (Wayne Protocol Edition)` connect `ALFRED — MARK-IV (Wayne Protocol Edition)` to `15. Bug Fixes & Stability Updates`, `audio_core`, `🎙️ 3. Master Tactical Voice Command Codex & Operational Handbook`, `system_monitor.py`, `17. Quick Start & Installation`, `6. Spotify AI Agent: Dual-Tier Web API & Native Playback Architecture`, `Detailed Step-by-Step Guide: How to Switch to a Local API`, `is_heavenly_restricted`, `find_element`?**
  _High betweenness centrality (0.036) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `JarvisLive` (e.g. with `ProactiveEngine` and `SystemMonitor`) actually correct?**
  _`JarvisLive` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `C`, `Purpose`, `Rules` to the rest of the system?**
  _52 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `game_updater.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05616605616605617 - nodes in this community are weakly interconnected._
- **Should `file_controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06690140845070422 - nodes in this community are weakly interconnected._