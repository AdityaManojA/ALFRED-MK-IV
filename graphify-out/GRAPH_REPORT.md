# Graph Report - Alfred-Mark-IV  (2026-09-27)

## Corpus Check
- 96 files · ~188,326 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 16 file(s) not represented in the graph (top: .ico 7, (none) 3, .bak 2)

## Summary
- 2439 nodes · 4776 edges · 134 communities (110 shown, 24 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 189 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `4bc75e02`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- game_updater.py
- file_controller.py
- add_clipboard_item
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
- CentralizedCache
- tts.py
- EchoGuard
- desktop.py
- memory_manager.py
- HudCanvas
- JarvisLive
- config_manager.py
- readme.md
- Any
- get_plugin_enabled
- _tlog
- computer_control.py
- llm_client.py
- load_api_keys
- tech_font
- TronScoreBackgroundPlayer
- _BrowserSession
- .__init__
- .test_error_isolation_in_concurrent_tasks
- main.py
- audio_devices.py
- GraphManager
- gmail_manager.py
- get_input_device
- crypto-js.min.js
- screen_find.py
- action_loader.py
- mono_font
- TacticalAudioPlayerWidget
- VisemeStream
- screen_processor.py
- qcol
- ui.py
- SpotifyClient
- time
- CustomizeOverlay
- computer_settings
- echo.py
- install_and_download
- server.py
- ._build_app
- background_monitor.py
- TestProtocolEngine
- PushToTalk
- spotify_control.py
- TestBackgroundWorkerPool
- ScreenCapturePayload
- stt.py
- NotesTerminalWidget
- save_app_icon
- ._build_right_panel
- .__init__
- _SysMetrics
- ProactiveEngine
- PluginSettingsOverlay
- ._apply_name_update
- WakeWordDetector
- get_active_window_info
- plugin_loader.py
- .__init__
- intel_notes.py
- .add_clipboard_item
- .broadcast
- LogWidget
- TestScreenProcessorWindowContext
- DashboardServer
- MemoryOverlay
- Optimized Approach
- TestAudioDucker
- ._build_jarvis_icon
- ClipboardManager
- .play
- json
- is_heavenly_restricted
- ._toggle_sentry_mode
- SubjectDossierCard
- _detect_action
- capture_screen
- weather_report.py
- ._apply_ptt_shortcut
- installer.py
- .clear_chat
- _VolumeSliderPopup
- Daily Brief Protocol
- Email Handling Rules
- Executive Assistant Persona & Behavioral Standards
- duck_media_apps
- /email-triage Workflow
- _template.py
- .control_playback
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
- _RootShim
- watchdog_events
- watchdog_observers
- ClipboardPanel
- audio_ws
- ._listen_audio
- clipboard_manager_action
- is_sensitive_content
- _make_uploads_dir
- _base_dir

## God Nodes (most connected - your core abstractions)
1. `MainWindow` - 95 edges
2. `JarvisLive` - 64 edges
3. `JarvisUI` - 45 edges
4. `mono_font()` - 36 edges
5. `tech_font()` - 35 edges
6. `_BrowserSession` - 32 edges
7. `TronScoreBackgroundPlayer` - 30 edges
8. `is_heavenly_restricted()` - 26 edges
9. `qcol()` - 25 edges
10. `computer_control()` - 24 edges

## Surprising Connections (you probably didn't know these)
- `3. Dedicated Intel & Notes Terminal (`intel_notes`)` --references--> `intel_notes()`  [INFERRED]
  .agents/rules/file_exploration.md → actions/intel_notes.py
- `Spotify Action (`actions/spotify_control.py`)` --references--> `get_spotify_client()`  [INFERRED]
  pasted-content-id-b6c3-here-is-warm-rainbow.md → actions/spotify_control.py
- `2. Security, Privacy & Defensive Architecture` --references--> `computer_control()`  [INFERRED]
  readme.md → actions/computer_control.py
- `1. File Opening (`open`)` --references--> `file_controller()`  [INFERRED]
  .agents/rules/file_exploration.md → actions/file_controller.py
- `2. Folder Exploration (`explore`)` --references--> `file_controller()`  [INFERRED]
  .agents/rules/file_exploration.md → actions/file_controller.py

## Import Cycles
- None detected.

## Communities (134 total, 24 thin omitted)

### Community 0 - "game_updater.py"
Cohesion: 0.06
Nodes (80): browser_control(), _log(), _build_google_flights_url(), flight_finder(), _format_spoken(), _format_text_report(), _get_base_dir(), _parse_date() (+72 more)

### Community 1 - "file_controller.py"
Cohesion: 0.07
Nodes (62): copy_file(), create_file(), create_folder(), delete_file(), explore_folder(), file_controller(), find_files(), _format_size() (+54 more)

### Community 2 - "add_clipboard_item"
Cohesion: 0.14
Nodes (12): add_clipboard_item(), get_recent_clipboards(), paste_clipboard_item(), Polling loop inspecting OS clipboard., search_clipboard(), start_clipboard_listener(), stop_clipboard_listener(), Verify search_clipboard accurately matches contents by keyword and semantics. (+4 more)

### Community 3 - "file_processor.py"
Cohesion: 0.08
Nodes (45): _detect_type(), file_processor(), _file_size_str(), _gemini_client(), _output_path(), _process_archive(), _process_audio(), _process_code() (+37 more)

### Community 4 - "web_search.py"
Cohesion: 0.07
Nodes (43): _get_live_weather(), Fetch live weather conditions without opening an external browser., _compare(), _fetch_item(), _ddg_news(), _ddg_search(), _format_ddg(), _format_news() (+35 more)

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
Cohesion: 0.05
Nodes (51): _get_cpu_temp(), _get_gpu_usage(), get_system_status(), _is_private_or_loopback(), is_protected_process(), _nvml_gpu(), Any, actions/system_monitor.py — System Metric Checks, Process Tree Watchdog &… (+43 more)

### Community 9 - "JarvisUI"
Cohesion: 0.05
Nodes (16): setter, JarvisUI, Thread-safe: raise the irreversible-action gate. Called from action handlers…, Thread-safe: take the gate down., Thread-safe: feed a 0.0–1.0 live audio level to the HUD waveform. Called from…, Ask the avatar to look somewhere for a moment (see HoloAvatar.glance)., Thread-safe: post a schedule of (level, openness, width) mouth frames for…, Thread-safe: wipe the on-screen conversation chat feed. (+8 more)

### Community 10 - "protocol_engine.py"
Cohesion: 0.12
Nodes (31): create_protocol(), _do_save(), execute_protocol(), _execute_tool(), get_action_registry(), get_protocols_file(), interpolate_variables(), _is_failure() (+23 more)

### Community 12 - "MainWindow"
Cohesion: 0.05
Nodes (9): QMainWindow, MainWindow, Slot — display camera preview overlay (main thread)., Slot — runs on Qt main thread. Updates and shows the content panel., Slot — Qt main thread. Lays a document review into the content panel., Slot — Qt main thread. Puts a fresh quiz on the board., Place a floating overlay in the middle of the HUD and show it., Update bottom-left tactical audio player to display and control Spotify… (+1 more)

### Community 13 - "dev_agent.py"
Cohesion: 0.11
Nodes (31): _build_project(), _classify_error(), dev_agent(), _diagnose_trace(), _extract_culprit_script(), _fix_files(), _get_model(), _has_error() (+23 more)

### Community 14 - "sys"
Cohesion: 0.18
Nodes (11): main(), remove_emojis_from_headings(), re, _check_assets(), _check_python(), main(), MARK LIV — one-time setup. Installs the Python dependencies for THIS operating…, Fail immediately and clearly rather than deep inside a pip resolver. A wrong… (+3 more)

### Community 15 - "CentralizedCache"
Cohesion: 0.06
Nodes (22): CentralizedCache, _canonicalize(), decorator(), wrapper(), Any, Stores value in cache with TTL. Fails open gracefully if storage fails., Deletes a key from cache. Fails open gracefully., Invalidates all keys starting with prefix. Useful for mutation hooks. (+14 more)

### Community 16 - "tts.py"
Cohesion: 0.07
Nodes (25): _compress_silence(), create_tts_player(), EdgeTTSEngine, ElevenLabsTTSEngine, _import_kokoro_pipeline(), KokoroTTSEngine, _synth(), _play_audio_bytes() (+17 more)

### Community 17 - "EchoGuard"
Cohesion: 0.08
Nodes (14): band_energies(), EchoGuard, ndarray, Classifies microphone blocks while the assistant is speaking. Usage:…, True once the estimate rests on enough real echo to be trusted., Residual left by this room's own echo. Higher = harder to separate., False when the acoustics are too poor to judge on content alone. Speakers…, The residual a block must clear right now to count as a voice. (+6 more)

### Community 18 - "desktop.py"
Cohesion: 0.12
Nodes (36): _ask_gemini_for_desktop_action(), _build_sandbox(), clean_desktop(), desktop_control(), _execute_generated_code(), _get_api_key(), _get_base_dir(), get_current_wallpaper() (+28 more)

### Community 19 - "memory_manager.py"
Cohesion: 0.08
Nodes (35): Update Daily Briefing Preferences Action for ALFRED Mark-LIV. Permanently…, Permanently saves daily briefing preferences into long-term memory., update_daily_briefing(), _do_shutdown(), Summarise the current session in 1-2 sentences and save to long_term.json., _all_entries(), all_entries_for_ui(), _empty_memory() (+27 more)

### Community 20 - "HudCanvas"
Cohesion: 0.09
Nodes (15): QPainter, HudCanvas, Ask the avatar to look somewhere for a moment (see HoloAvatar.glance)., Thread-safe: hand over a schedule of (level, openness, width) frames. The…, Thread-safe entry point for the audio threads. Stores the louder of the…, True only when this canvas can actually be seen by the user., Draw the Avengers: Endgame Stark Arc Reactor at (cx, cy) with outer radius r., Draw subtle background CRT coordinate grid with + crosshairs (Screenshot 2). (+7 more)

### Community 21 - "JarvisLive"
Cohesion: 0.06
Nodes (22): Restore ducked media applications to their exact original volume levels. :param…, unduck_media_apps(), JarvisLive, Chord pressed or released — may arrive on the hotkey thread., Stop JARVIS mid-speech: drain queued audio and open mic immediately., Background task: voice alerts when metrics exceed thresholds., Check user-configured topics once per day; speak alerts when new headlines…, Background task: periodically checks if the user has been silent long enough,… (+14 more)

### Community 22 - "config_manager.py"
Cohesion: 0.15
Nodes (20): ensure_config_dir(), get_base_dir(), Path, Persist the chosen Live voice. Unknown names collapse to the default so a bad…, Read-modify-write one key without disturbing the rest of the config., Merge `values` into a namespace's stored config (read-modify-write, like every…, Persist assistant name and user name to config., save_api_keys() (+12 more)

### Community 23 - "readme.md"
Cohesion: 0.06
Nodes (32): 10. Local Hybrid Visual Grounding (RapidOCR + ONNX + Gemini Fallback), 11. Process-Level Audio Ducking & Background Concurrency, 13. Bug Fixes & Stability Updates, 14. System Architecture & File Structure, 15. Quick Start & Installation, 16. Configuration Reference (`config/api_keys.json`), 17. Knowledge Graph (`graphify`), 18. Author & Credits (+24 more)

### Community 24 - "Any"
Cohesion: 0.17
Nodes (8): cosine_similarity(), Any, Compute cosine similarity between two float vectors., Lazily initialize local fastembed model., Compute 384-dimensional vector embedding for text., Return the most recent count items in chronological order (oldest to newest…, Perform semantic and keyword search across clipboard history., Push historical item to system clipboard active paste slot.

### Community 25 - "get_plugin_enabled"
Cohesion: 0.14
Nodes (11): _call_run(), PluginRegistry, One entry per settings SECTION, for enabled plugins that declare a…, Invoke run() passing only the kwargs it actually declares (or all of them if it…, How this plugin's result should re-enter the conversation, if it said., get_plugin_config(), get_plugin_enabled(), get_plugin_setting() (+3 more)

### Community 26 - "_tlog"
Cohesion: 0.08
Nodes (19): FunctionResponse, _clean_transcript(), _is_repeat_chunk(), broadcast_progress(), _run_tool_bounded(), _deliver_news(), main(), runner() (+11 more)

### Community 27 - "computer_control.py"
Cohesion: 0.12
Nodes (32): _base_dir(), _clear_field(), _click(), _clipboard_get(), _clipboard_paste(), computer_control(), _drag(), _focus_window() (+24 more)

### Community 28 - "llm_client.py"
Cohesion: 0.12
Nodes (24): call_llm(), call_llm_stream(), _do_stream(), call_llm_text(), check_model_available(), ensure_ollama_running(), get_base_dir(), get_llm_provider() (+16 more)

### Community 29 - "load_api_keys"
Cohesion: 0.09
Nodes (24): LiveConnectConfig, The optional knobs, kept apart so one bad field can be dropped wholesale. Every…, get_app_icon(), get_assistant_name(), get_gemini_key(), get_hud_style(), get_llm_provider(), get_media_resolution() (+16 more)

### Community 30 - "tech_font"
Cohesion: 0.11
Nodes (9): CapabilitiesOverlay, Floating glassmorphic overlay displaying a categorized directory of everything…, Floating overlay — QR code for instant phone pairing + manual key fallback., Call from any thread when a phone successfully connects., RemoteKeyOverlay, _lbl(), SetupOverlay, _lbl() (+1 more)

### Community 31 - "TronScoreBackgroundPlayer"
Cohesion: 0.09
Nodes (10): control_playback(), QObject, _base_dir(), Path, Background music audio engine. Plays background score continuously on loop…, Set base normal volume (0.0 to 1.0). Speech ducking scales to 50% of base., Duck to 50% of base volume when speaking, restore to base volume when…, Called when Spotify plays a track. Pauses Tron background music, sets Spotify… (+2 more)

### Community 32 - "_BrowserSession"
Cohesion: 0.05
Nodes (19): _BrowserSession, _detect_default_browser(), _find_exe_windows(), _find_opera_windows(), _firefox_profile_dir(), _normalize_url(), _open_native(), Bare words like "instagram" → "https://instagram.com" Domains like… (+11 more)

### Community 33 - ".__init__"
Cohesion: 0.10
Nodes (5): QDragEnterEvent, QDropEvent, CyberGraphicLineButton, FileDropZone, Tactical button rendered strictly with vector graphic lines, sharp 2px border…

### Community 34 - ".test_error_isolation_in_concurrent_tasks"
Cohesion: 0.29
Nodes (5): Verify that an exception in one concurrent task does not break or cancel…, Verify that a batch of tasks run with a concurrency limit of 5 scales sub-…, TestConcurrencyLimiter, execute_task(), safe_run()

### Community 35 - "main.py"
Cohesion: 0.07
Nodes (26): BaseException, google, google_genai, _describe_limits(), _describe_tools(), _get_api_key(), _is_reconnect_signal(), _keep_context_of() (+18 more)

### Community 36 - "audio_devices.py"
Cohesion: 0.12
Nodes (18): configure(), _display_name(), _is_pseudo(), prefetch(), _work(), _query(), _collect(), core/audio_devices.py — pick which microphone and which speakers ALFRED uses.… (+10 more)

### Community 37 - "GraphManager"
Cohesion: 0.11
Nodes (14): GraphManager, Any, Path, Save the graph data to the JSON file atomically., Add an entity node to the graph. Returns True if successful., Add a relationship (edge) between two nodes. Returns True if successful., Apply exponential decay to all temporary nodes. Returns the number of nodes…, Query the knowledge graph for a concept and return connected subgraph up to… (+6 more)

### Community 38 - "gmail_manager.py"
Cohesion: 0.07
Nodes (34): daily_brief(), _get_gmail_brief(), _get_greeting(), _get_reminders_brief(), _get_system_vitals(), Fetch unread emails summary via gmail_manager., Check scheduled reminders in ~/.alfred/reminders or ~/.jarvis/reminders., Inspect core CPU, RAM, and Battery vitals. (+26 more)

### Community 39 - "get_input_device"
Cohesion: 0.16
Nodes (13): list_devices(), Device names for 'input' or 'output'. Falls back to a synchronous query if the…, get_input_device(), get_output_device(), _patch_config(), Read-modify-write one or more keys in api_keys.json. Every setter in this file…, Microphone device name, or '' for the system default., Speaker device name, or '' for the system default. (+5 more)

### Community 41 - "screen_find.py"
Cohesion: 0.07
Nodes (39): _calculate_similarity(), _capture_screen_image(), find_element(), _gemini_grounding(), _get_api_key(), _get_frame_key(), get_onnx_session(), get_rapid_ocr() (+31 more)

### Community 42 - "action_loader.py"
Cohesion: 0.15
Nodes (12): ActionRecord, ActionRegistry, _call_handler(), discover_actions(), _opt_upper(), Path, Action discovery, validation, and dispatch — the built-in twin of…, Invoke the handler passing only the context kwargs it actually declares (or all… (+4 more)

### Community 43 - "mono_font"
Cohesion: 0.08
Nodes (14): QFont, BiometricFingerprintWidget, _CameraPreview, CRTReconWidget, MetricBar, mono_font(), QWidget, Halftone / CRT Dithered Optical Recon Scanner Widget (Screenshot 1: Top-Left… (+6 more)

### Community 44 - "TacticalAudioPlayerWidget"
Cohesion: 0.16
Nodes (4): _EqualizerBarsWidget, Mini animated cyber audio wave visualizer., Bottom-Left Cyber Tactical Audio Player Widget. Styled matching the HUD /…, TacticalAudioPlayerWidget

### Community 45 - "VisemeStream"
Cohesion: 0.13
Nodes (12): collections, coverage(), Text → mouth shape, fused with the audio the avatar is actually speaking. Why…, Reduce any character to a bare Latin letter, or "" if it has none. This is what…, Fraction of the letters in `text` we can reduce to a Latin sound., Split a line of speech into (viseme, duration-weight) pairs. Returns [] for…, Fuses the transcript's shape sequence onto the audio's timing. Thread note:…, Blend audio frames [(level, openness, width)] with the text queue. (+4 more)

### Community 46 - "screen_processor.py"
Cohesion: 0.18
Nodes (17): _capture_camera(), _cv2_backend(), _detect_camera_index(), _get_camera_index(), _get_os(), _load_config(), _probe_camera(), Screen & webcam capture for ALFRED vision with OS window context grounding.… (+9 more)

### Community 47 - "qcol"
Cohesion: 0.22
Nodes (7): QColor, QPixmap, _DropCanvas, _file_category(), _fmt_size(), qcol(), Pre-render the static grid-dot background into a transparent pixmap so…

### Community 48 - "ui.py"
Cohesion: 0.14
Nodes (13): core_avatar, get_brief_enabled(), save_brief_enabled(), pyqt6_qtcore, pyqt6_qtgui, pyqt6_qtmultimedia, pyqt6_qtwidgets, C (+5 more)

### Community 49 - "SpotifyClient"
Cohesion: 0.14
Nodes (10): High-performance Spotify client with connection pooling, token caching, device…, Loads Spotify credentials from config/api_keys.json or environment variables., Returns a valid access token, refreshing if needed., Adds a track to the playback queue., Sets Spotify volume percentage (0-100)., Returns available Spotify devices with 5-minute TTL caching., Toggles or sets shuffle mode., Sets repeat mode: 'track', 'context', or 'off'. (+2 more)

### Community 50 - "time"
Cohesion: 0.18
Nodes (10): asyncio, Performance Benchmark: dev_agent._parse_traceback Tests O(1) hash map lookups…, Measures lookup time across 50,000 mock project files and 500 stack frames., TestTracebackBenchmark, tests/test_cache.py — Comprehensive Test Suite for CentralizedCache. Tests: -…, tests/test_clipboard_manager.py — Unit tests for persistent semantically…, Unit and integration tests for screen_processor.py window context grounding.…, time (+2 more)

### Community 51 - "CustomizeOverlay"
Cohesion: 0.10
Nodes (9): QPointF, QRectF, CustomizeOverlay, _lbl(), HueWheel, Circular colour picker. The user drags the handle (small white circle) around…, Floating glassmorphic overlay for configuring Assistant Persona, Commander…, Highlight the selected voice pill; dim the rest. (+1 more)

### Community 52 - "computer_settings"
Cohesion: 0.12
Nodes (16): brightness_get(), brightness_set(), computer_settings(), dark_mode(), paste(), press_key(), Current brightness 0-100, or None where it cannot be read., Set brightness to an absolute percentage. Only used to restore a value captured… (+8 more)

### Community 53 - "echo.py"
Cohesion: 0.25
Nodes (4): is_ducked(), Return whether media ducking is currently active., Telling the user's voice apart from our own coming back through the speakers.…, numpy

### Community 54 - "install_and_download"
Cohesion: 0.16
Nodes (8): install_and_download(), is_installed(), is_ready(), True if the openwakeword package is importable (no model check)., True if openwakeword is installed AND its model files are present on disk. This…, One-click setup for the UI button: pip-install openwakeword if missing, then…, _work(), Combined state for the two wake-word buttons. Readiness is a cheap,…

### Community 55 - "server.py"
Cohesion: 0.12
Nodes (14): base64, index(), _ensure_certs(), _local_ip(), dashboard/server.py — ALFRED Local HTTP Dashboard Plain HTTP on port 8000 (no…, Return the best LAN-facing IPv4 address, no internet required., Make sure config/certs holds a TLS key pair, generating a self-signed one the…, _read() (+6 more)

### Community 56 - "._build_app"
Cohesion: 0.24
Nodes (6): _auth(), list_files(), revoke_devices(), _safe_filename(), upload_file(), wake_ep()

### Community 57 - "background_monitor.py"
Cohesion: 0.26
Nodes (13): add_monitor(), check_all(), _is_blocked(), list_monitors(), _load(), BackgroundMonitor — user-configured topic watching. Checks DDG news once per…, Run all pending topic checks (once per day per topic). Returns a list of…, remove_monitor() (+5 more)

### Community 58 - "TestProtocolEngine"
Cohesion: 0.11
Nodes (8): Verify that a tool failure halts subsequent steps immediately., Verify voice trigger word resolution (e.g. 'FCC CLAUDE')., Verify dynamic workflow creation with confirmation banner., Verify protocol_engine TOOL action handler dispatching., Verification Requirement: Define test_protocol in protocols.yaml that opens…, Verify variable interpolation into strings, lists, and dicts., Verify that if any step is blocked by path restrictions, the engine aborts…, TestProtocolEngine

### Community 59 - "PushToTalk"
Cohesion: 0.17
Nodes (6): PushToTalk, Begin watching. Returns the scope actually achieved., Feed a press/release from a Qt shortcut (non-Windows, or no hook)., Calls `on_change(held: bool)` whenever the chord is pressed or released. Start…, global' once a system-wide hook is running, else 'window'., Turn hold-to-talk on or off. Returns the scope actually achieved.

### Community 60 - "spotify_control.py"
Cohesion: 0.19
Nodes (16): _get_base_dir(), get_devices(), get_spotify_client(), manage_queue(), Any, Path, Spotify AI Agent & Playback Control for ALFRED. Provides seamless Spotify…, Main handler for the spotify_control action. (+8 more)

### Community 61 - "TestBackgroundWorkerPool"
Cohesion: 0.14
Nodes (6): Verify that calling interrupt() sets halt event, immediately stops active…, Verify that _safe_background_announce waits until ALFRED finishes speaking…, Verify queue_background_task is registered in TOOL_DECLARATIONS., Verify that queue_background_task returns immediately (sub-millisecond), and…, Dispatch a mock task and verify voice PTT interaction continues with sub-second…, TestBackgroundWorkerPool

### Community 62 - "ScreenCapturePayload"
Cohesion: 0.25
Nodes (3): Hybrid return payload for screen captures. - Behaves as a 3-tuple `(img_bytes,…, ScreenCapturePayload, tuple

### Community 63 - "stt.py"
Cohesion: 0.15
Nodes (8): ndarray, Speech-to-Text engines for MARK XL. Whisper – offline transcription via faster-…, Offline transcription using faster-whisper., Transcribe a float32 mono 16 kHz numpy array. Returns transcript string., Streaming transcription using Vosk., Feed raw int16 LE PCM bytes. Returns (text, is_final)., VoskSTT, WhisperSTT

### Community 65 - "save_app_icon"
Cohesion: 0.20
Nodes (10): Update App Icon Action for ALFRED Mark-LIV. Switches the application window,…, Updates the main application icon and taskbar badge in realtime., update_app_icon(), Save the chosen app icon setting to config., save_app_icon(), format_icon_display_name(), get_available_app_icons(), Format an icon file name into an authentic, sleek tactical insignia title. (+2 more)

### Community 66 - "._build_right_panel"
Cohesion: 0.18
Nodes (3): QHBoxLayout, Read api_keys.json config dict. Returns {} on any error., _read_full_config()

### Community 67 - ".__init__"
Cohesion: 0.11
Nodes (5): _fl(), Floating overlay panel shown when the ⚙ header button is toggled., Returns True if auto-start is currently registered on this OS., Open the API key and neural backend configuration overlay from settings., Update application and window icon in realtime.

### Community 68 - "_SysMetrics"
Cohesion: 0.21
Nodes (4): Thread-safe speech channel for plugins: lets a plugin ask JARVIS to say…, _nvml_gpu_windows(), Return NVIDIA GPU utilisation % using nvml.dll directly — zero subprocess., _SysMetrics

### Community 69 - "ProactiveEngine"
Cohesion: 0.22
Nodes (4): ProactiveEngine, ProactiveEngine 2.0 — context-aware, time-aware, non-repetitive background…, Decides when ALFRED should speak unprompted and builds a context-rich prompt.…, Build a context snapshot for Gemini. Rotates through three focus areas so…

### Community 70 - "PluginSettingsOverlay"
Cohesion: 0.17
Nodes (6): QPushButton, QVBoxLayout, PluginManagerOverlay, PluginSettingsOverlay, Floating overlay — lists discovered plugins with per-plugin ON/OFF toggles., Floating overlay — renders per-plugin settings forms. Fully generic: it…

### Community 71 - "._apply_name_update"
Cohesion: 0.20
Nodes (8): apply_ui_accent(), current_palette(), Applies DOSSIER CRT [A-34] (#8e9bff), VECTOR CRT [WAKU] (#a8ff3e), or BATMAN…, A snapshot of the accent-linked colours currently on class C., LIVE full theme change. Replaces the old palette colours with the new ones in…, Live preview — paints the whole interface the new colour (does NOT write to…, Update all name/theme-dependent UI elements and persist to config., retheme_all_widgets()

### Community 72 - "WakeWordDetector"
Cohesion: 0.20
Nodes (4): Runs the wake model in a dedicated thread. The mic thread calls feed() with raw…, Load the model and spawn the inference thread. Returns True on success. Safe to…, Called from the mic callback (real-time thread). Must stay cheap and never…, WakeWordDetector

### Community 73 - "get_active_window_info"
Cohesion: 0.20
Nodes (10): get_active_window_context(), get_active_window_info(), _get_linux_window_info(), _get_macos_window_info(), _get_windows_window_info(), Query foreground window handle, title, and process name on Windows., Query active frontmost window on macOS via Quartz or AppleScript fallback., Query active window on Linux via xdotool or wmctrl. (+2 more)

### Community 74 - "plugin_loader.py"
Cohesion: 0.19
Nodes (13): discover_plugins(), _load_error(), _opt_upper(), PluginRecord, Exception, Path, Plugin discovery, validation, collision detection, and dispatch. Discovery runs…, Returns a PluginRecord; .valid=False + .error set on any problem. Never raises. (+5 more)

### Community 75 - ".__init__"
Cohesion: 0.20
Nodes (7): chord_label(), Human-readable name of the chord, for the UI and the logs., get_push_to_talk_enabled(), get_wake_word_enabled(), Whether local wake-word gating is on (assistant sleeps until 'Hey Jarvis')., Hold-a-key-to-speak. When on, the mic is closed unless the chord is held., Repaint the push-to-talk row from the saved setting.

### Community 76 - "intel_notes.py"
Cohesion: 0.31
Nodes (8): _auto_detect_type(), _config_dir(), intel_notes(), _load_notes(), Path, actions/intel_notes.py — Dedicated Intel & Notes Terminal Action. Provides a…, Action handler called by Gemini / action_loader., _save_notes()

### Community 77 - ".add_clipboard_item"
Cohesion: 0.20
Nodes (7): classify_content_type(), _get_active_window_info(), Determine category: url, email, json, code, or text., Save history to disk atomically., Append item to history stack with deduplication and sensitive data filtering., Return (process_name, window_title) of the foreground window., Verify content type heuristic classification.

### Community 78 - ".broadcast"
Cohesion: 0.24
Nodes (7): auto_login(), clear_chat_ep(), device_login_ep(), login(), phone_audio_ws(), _derive_key(), SHA-256(sessionKey‖salt) → 32-byte AES-256 key (microseconds, no PBKDF2 needed).

### Community 79 - "LogWidget"
Cohesion: 0.25
Nodes (3): QTextEdit, LogWidget, Cancel any in-flight typing animation, drain the queue, and clear the display.

### Community 80 - "TestScreenProcessorWindowContext"
Cohesion: 0.18
Nodes (7): format_window_context(), Format the standard metadata block: [WINDOW_CONTEXT] App: <Name> | Title:…, Verifies system falls back to 'App: Unknown' without raising exceptions., Verifies that active window query resolves in < 15ms and adheres to schema., Verifies exact string formatting requirements., Verifies capture_screen() returns valid compressed image and window context., TestScreenProcessorWindowContext

### Community 81 - "DashboardServer"
Cohesion: 0.20
Nodes (3): DashboardServer, URL for manual browser entry. When HTTPS active, points to alias port (also…, Verify DashboardServer tracks background tasks and exposes them via endpoint.

### Community 82 - "MemoryOverlay"
Cohesion: 0.33
Nodes (4): MemoryOverlay, Everything ALFRED has stored about you, and when it learned it. Memory used to…, Take every item out of the layout and detach it from the widget tree in this…, Size the panel to its content, re-centre it, and repaint what the old size…

### Community 83 - "Optimized Approach"
Cohesion: 0.15
Nodes (12): Context, Core Implementation, Current State, Files Modified, Integration Points, Key Optimizations for Fast Loading, Optimized Approach, Optimized Spotify AI Agent Implementation Plan (+4 more)

### Community 84 - "TestAudioDucker"
Cohesion: 0.29
Nodes (4): patch, Verify that duck_media_apps lowers target media processes by 70% (0.3 factor),…, Verify Linux pulsectl ducking fallback logic., TestAudioDucker

### Community 85 - "._build_jarvis_icon"
Cohesion: 0.22
Nodes (4): Render an ALFRED tactical icon at 4× resolution and downsample for crisp…, Create a Windows .lnk shortcut WITHOUT launching PowerShell or cmd. Tries…, Resolve the user's REAL desktop directory instead of assuming ~/Desktop, which…, Create a desktop shortcut on Windows / macOS / Linux. Never opens a terminal,…

### Community 86 - "ClipboardManager"
Cohesion: 0.25
Nodes (5): ClipboardManager, Thread-safe persistent clipboard manager with semantic indexing., Load history from disk., Start background daemon thread monitoring OS clipboard., Stop background clipboard listener.

### Community 87 - ".play"
Cohesion: 0.33
Nodes (3): Search Spotify for tracks, albums, artists, or playlists., Starts playback of a query, URI, or resumes current playback. Attempts Web API…, Launches Spotify URI using the operating system handler.

### Community 88 - "json"
Cohesion: 0.15
Nodes (22): _base_dir(), _get_os(), Path, reminder(), _sanitise(), _schedule_linux(), _schedule_mac(), _schedule_windows() (+14 more)

### Community 89 - "is_heavenly_restricted"
Cohesion: 0.13
Nodes (19): apply_heal_patch(), Applies a user-approved heal patch via actions.file_controller with path…, _normalize(), open_app(), _is_heavenly_restricted_params(), check_action_params(), check_path_access(), get_allowed_c_roots() (+11 more)

### Community 90 - "._toggle_sentry_mode"
Cohesion: 0.33
Nodes (3): Toggle continuous visual context (camera stream) monitoring., Thread-safe: start live camera feed in the full HUD area., Thread-safe: stop the live camera feed.

### Community 92 - "_detect_action"
Cohesion: 0.40
Nodes (5): _detect_action(), _normalise(), Resolve a free-text description to an action name, locally. Returns {"action":…, What to tell the model when nothing matched. Names real actions so its retry…, _suggest()

### Community 93 - "capture_screen"
Cohesion: 0.29
Nodes (6): capture_screen(), _capture_screen(), _compress(), Captures primary or specified monitor, queries active OS window context,…, Default entry point used by main.py., Verification Requirement: Verify [WINDOW_CONTEXT] header contains VS Code and…

### Community 94 - "weather_report.py"
Cohesion: 0.50
Nodes (4): _log(), weather_action(), urllib_parse, webbrowser

### Community 95 - "._apply_ptt_shortcut"
Cohesion: 0.29
Nodes (5): qt_sequence(), The same chord as a QKeySequence string., _press(), Bind the chord inside the window when no global hook is available. On macOS and…, Report a windowed press/release to whoever owns the microphone.

### Community 96 - "installer.py"
Cohesion: 0.32
Nodes (7): _available(), install_for_config(), _pip(), MARK XL — Dependency auto-installer. Called automatically on first launch and…, Return True if the module can be imported (no actual import)., Install all missing packages required by *config*. Blocking — always call from…, importlib_util

### Community 98 - "_VolumeSliderPopup"
Cohesion: 0.33
Nodes (3): QFrame, Sleek tactical cyber popup for adjusting master background music volume.…, _VolumeSliderPopup

### Community 99 - "Daily Brief Protocol"
Cohesion: 0.50
Nodes (3): Daily Brief Protocol, Purpose, Rules

### Community 100 - "Email Handling Rules"
Cohesion: 0.50
Nodes (3): Email Handling Rules, Purpose, Rules

### Community 101 - "Executive Assistant Persona & Behavioral Standards"
Cohesion: 0.50
Nodes (3): Core Operational Rules, Executive Assistant Persona & Behavioral Standards, Persona & Demeanor

### Community 102 - "duck_media_apps"
Cohesion: 0.29
Nodes (7): _duck_linux(), duck_media_apps(), _worker(), _duck_windows(), Execute ducking on Linux via pulsectl., Lower external media application volume (by default to 30%, i.e. ducking by…, Execute ducking on Windows via pycaw.

### Community 103 - "/email-triage Workflow"
Cohesion: 0.50
Nodes (3): /email-triage Workflow, Objective, Steps

### Community 104 - "_template.py"
Cohesion: 0.50
Nodes (3): Drop-in ALFRED plugin template. Copy this file, rename it (no leading…, parameters: dict of the args Gemini extracted, matching PLUGIN['parameters'].…, run()

### Community 105 - ".control_playback"
Cohesion: 0.33
Nodes (5): Controls playback: pause, resume, skip_next, skip_previous. Combines Spotify…, Sends a native Windows WM_APPCOMMAND message to explicitly Pause, Play, or Stop., Sends a native Windows media key event as a hardware-level fallback., _send_app_command(), _send_media_key()

### Community 106 - "_get_base_dir"
Cohesion: 0.67
Nodes (3): _get_api_key(), _get_base_dir(), Path

### Community 107 - "pathlib"
Cohesion: 0.10
Nodes (27): actions/clipboard_manager.py — Persistent, Semantically Indexed Clipboard…, Daily Brief Action for ALFRED Mark-LIV. Provides the ultimate morning and daily…, concurrent_futures, Process-level Audio Ducking for ALFRED. Automatically ducks background media…, Execute unducking on Windows via pycaw, restoring exact prior volume levels., Execute unducking on Linux via pulsectl., _unduck_linux(), _worker() (+19 more)

### Community 110 - "._decrypt"
Cohesion: 0.40
Nodes (4): command(), ws_ep(), _decrypt_cbc(), Decrypt base64(IV[16] ‖ ciphertext) with AES-256-CBC + PKCS7.

### Community 111 - "_ensure_network_access"
Cohesion: 0.25
Nodes (3): _ensure_network_access(), Cross-platform, best-effort: open port in the OS firewall for LAN access. Runs…, Second HTTPS server on PORT+1 sharing the same app and in-memory state. Chrome…

### Community 116 - "format_visual_payload"
Cohesion: 0.40
Nodes (3): format_visual_payload(), Prepares the visual frame payload dictionary for the Gemini Live API…, Verifies metadata block is prepended directly to the visual frame payload.

### Community 129 - "._listen_audio"
Cohesion: 0.50
Nodes (3): callback(), _open_mic(), True while the speakers may still be finishing our last sentence.

### Community 130 - "clipboard_manager_action"
Cohesion: 0.50
Nodes (3): clipboard_manager_action(), Action handler called by ALFRED action dispatcher., Verify clipboard_manager TOOL action handler.

### Community 131 - "is_sensitive_content"
Cohesion: 0.50
Nodes (3): is_sensitive_content(), Detect if content originates from a password manager or contains high-entropy…, Verify that passwords, password managers, and secret tokens are scrubbed.

### Community 132 - "_make_uploads_dir"
Cohesion: 0.67
Nodes (3): _make_uploads_dir(), Path, Return (and create) the cross-platform uploads folder.

## Knowledge Gaps
- **49 isolated node(s):** `C`, `Purpose`, `Rules`, `Purpose`, `Rules` (+44 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1004 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **24 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `CentralizedCache` connect `CentralizedCache` to `time`, `pathlib`, `web_search.py`?**
  _High betweenness centrality (0.057) - this node is a cross-community bridge._
- **Why does `MainWindow` connect `MainWindow` to `.__init__`, `._build_right_panel`, `.__init__`, `.clear_chat`, `save_app_icon`, `._apply_name_update`, `system_monitor.py`, `JarvisUI`, `mono_font`, `.__init__`, `qcol`, `ui.py`, `._build_jarvis_icon`, `install_and_download`, `._toggle_sentry_mode`, `tech_font`, `._apply_ptt_shortcut`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._
- **Why does `JarvisUI` connect `JarvisUI` to `.__init__`, `.clear_chat`, `main.py`, `.__init__`, `._toggle_sentry_mode`, `._apply_name_update`, `.__init__`, `ui.py`, `JarvisLive`, `install_and_download`, `_tlog`, `._apply_ptt_shortcut`?**
  _High betweenness centrality (0.049) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `JarvisLive` (e.g. with `ProactiveEngine` and `SystemMonitor`) actually correct?**
  _`JarvisLive` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `C`, `Purpose`, `Rules` to the rest of the system?**
  _49 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `game_updater.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05987703822507351 - nodes in this community are weakly interconnected._
- **Should `file_controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06841046277665996 - nodes in this community are weakly interconnected._