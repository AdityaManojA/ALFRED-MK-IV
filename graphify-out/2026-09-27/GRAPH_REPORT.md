# Graph Report - Alfred-Mark-IV  (2026-09-27)

## Corpus Check
- 101 files · ~200,988 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 14 file(s) not represented in the graph (top: .ico 7, (none) 3, .obj 2)

## Summary
- 2640 nodes · 5151 edges · 146 communities (113 shown, 33 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 209 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `598dfc87`
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
- ui.py
- FileDropZone
- tts.py
- EchoGuard
- desktop.py
- load_api_keys
- HudCanvas
- JarvisLive
- config_manager.py
- setter
- ._tuning_config
- action_loader.py
- _tlog
- computer_control.py
- local_pipeline.py
- .run
- tech_font
- TronScoreBackgroundPlayer
- _BrowserSession
- ClipboardManager
- .test_error_isolation_in_concurrent_tasks
- .__init__
- audio_devices.py
- GraphManager
- gmail_manager.py
- CentralizedCache
- crypto-js.min.js
- screen_find.py
- HueWheel
- .__init__
- TacticalAudioPlayerWidget
- VisemeStream
- screen_processor.py
- qcol
- get_input_device
- spotify_control.py
- server.py
- CustomizeOverlay
- computer_settings
- unduck_media_apps
- RemoteKeyOverlay
- ._receive_audio
- ._build_app
- background_monitor.py
- find_element
- json
- LocalLLMManager
- TestBackgroundWorkerPool
- ScreenCapturePayload
- LocalSTTManager
- NotesTerminalWidget
- save_app_icon
- LocalTTSManager
- ALFRED — MARK-IV (Wayne Protocol Edition)
- _SysMetrics
- memory_manager.py
- CyberGraphicLineButton
- ._apply_name_update
- WakeWordDetector
- get_active_window_info
- daily_brief.py
- datetime
- time
- LocalPipelineCoordinator
- ._aes_key
- LogWidget
- test_screen_processor.py
- DashboardServer
- MemoryOverlay
- SetupOverlay
- PushToTalk
- Path
- ImagePopupOverlay
- confirm.py
- test_cache.py
- is_heavenly_restricted
- ._build_config
- _VolumeSliderPopup
- _detect_action
- delete_file
- _gemini_grounding
- get_push_to_talk_enabled
- .load_track
- _undo_create
- TestScreenProcessorWindowContext
- Daily Brief Protocol
- Email Handling Rules
- Executive Assistant Persona & Behavioral Standards
- CapabilitiesOverlay
- /email-triage Workflow
- _template.py
- _get_base_dir
- os
- Graphify + Antigravity Project Workflow & Setup Guide
- _get_macos_wifi_interface
- ._decrypt
- _ensure_network_access
- rules/graphify.md
- workflows/graphify.md
- chromadb
- chromadb_config
- setup.py
- fastembed
- sentence_transformers
- TestAudioDucker
- watchdog_events
- watchdog_observers
- format_window_context
- TestMemoryTrimBenchmark
- ._listen_audio
- get_plugin_config
- File & Folder Exploration and Notes Directives
- wake_word.py
- intel_notes.py
- /deep-work Workflow
- main.py
- File & Folder Exploration Workflow
- get_hud_style
- get_base_dir
- _EqualizerBarsWidget
- ._paint_3d_vector_globe
- control_playback
- ._save_session_summary
- ._on_screen
- type_text
- _get_base_dir
- .push_visemes

## God Nodes (most connected - your core abstractions)
1. `MainWindow` - 101 edges
2. `JarvisLive` - 66 edges
3. `JarvisUI` - 49 edges
4. `tech_font()` - 38 edges
5. `mono_font()` - 37 edges
6. `_BrowserSession` - 32 edges
7. `TronScoreBackgroundPlayer` - 32 edges
8. `computer_control()` - 26 edges
9. `is_heavenly_restricted()` - 26 edges
10. `DashboardServer` - 26 edges

## Surprising Connections (you probably didn't know these)
- `1. File Opening (`open`)` --references--> `file_controller()`  [INFERRED]
  .agents/rules/file_exploration.md → actions/file_controller.py
- `2. Folder Exploration (`explore`)` --references--> `file_controller()`  [INFERRED]
  .agents/rules/file_exploration.md → actions/file_controller.py
- `Step 1: Target Identification` --references--> `file_controller()`  [INFERRED]
  .agents/workflows/file_explorer.md → actions/file_controller.py
- `3. Dedicated Intel & Notes Terminal (`intel_notes`)` --references--> `intel_notes()`  [INFERRED]
  .agents/rules/file_exploration.md → actions/intel_notes.py
- `High-Performance Client & Anti-Feedback Architecture` --references--> `SpotifyClient`  [INFERRED]
  readme.md → actions/spotify_control.py

## Import Cycles
- None detected.

## Communities (146 total, 33 thin omitted)

### Community 0 - "game_updater.py"
Cohesion: 0.06
Nodes (81): _build_google_flights_url(), flight_finder(), _format_spoken(), _format_text_report(), _get_base_dir(), _parse_date(), _parse_flights_with_gemini(), Path (+73 more)

### Community 1 - "file_controller.py"
Cohesion: 0.21
Nodes (26): copy_file(), create_file(), create_folder(), explore_folder(), file_controller(), find_files(), _format_size(), get_disk_usage() (+18 more)

### Community 2 - "clipboard_manager.py"
Cohesion: 0.09
Nodes (26): add_clipboard_item(), classify_content_type(), clipboard_manager_action(), _get_active_window_info(), get_recent_clipboards(), is_sensitive_content(), paste_clipboard_item(), Any (+18 more)

### Community 3 - "file_processor.py"
Cohesion: 0.08
Nodes (45): _detect_type(), file_processor(), _file_size_str(), _gemini_client(), _output_path(), _process_archive(), _process_audio(), _process_code() (+37 more)

### Community 4 - "web_search.py"
Cohesion: 0.10
Nodes (36): _compare(), _fetch_item(), _ddg_news(), _ddg_search(), _format_ddg(), _format_news(), _gemini_available(), _gemini_headlines() (+28 more)

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
Nodes (37): _get_cpu_temp(), _get_gpu_usage(), get_system_status(), _is_private_or_loopback(), is_protected_process(), _nvml_gpu(), Any, actions/system_monitor.py — System Metric Checks, Process Tree Watchdog &… (+29 more)

### Community 9 - "JarvisUI"
Cohesion: 0.04
Nodes (23): JarvisUI, Toggle continuous visual context (camera stream) monitoring., Update application and window icon in realtime., Thread-safe: raise the irreversible-action gate. Called from action handlers…, Thread-safe: take the gate down., Thread-safe: feed a 0.0–1.0 live audio level to the HUD waveform. Called from…, Ask the avatar to look somewhere for a moment (see HoloAvatar.glance)., Thread-safe: post a schedule of (level, openness, width) mouth frames for… (+15 more)

### Community 10 - "protocol_engine.py"
Cohesion: 0.06
Nodes (49): create_protocol(), _do_save(), _ensure_user_protocols_dir(), execute_protocol(), _execute_tool(), get_action_registry(), _get_default_protocols_path(), get_protocols_file() (+41 more)

### Community 12 - "MainWindow"
Cohesion: 0.04
Nodes (19): QMainWindow, MainWindow, _fl(), Read api_keys.json config dict. Returns {} on any error., Slot — display camera preview overlay (main thread)., Slot — runs on Qt main thread. Updates and shows the content panel., Slot — Qt main thread. Lays a document review into the content panel., Slot — Qt main thread. Puts a fresh quiz on the board. (+11 more)

### Community 13 - "dev_agent.py"
Cohesion: 0.09
Nodes (38): apply_heal_patch(), _build_project(), _classify_error(), dev_agent(), _diagnose_trace(), _extract_culprit_script(), _fix_files(), _get_model() (+30 more)

### Community 14 - "ui.py"
Cohesion: 0.13
Nodes (16): Action to show an image popup overlay., core_avatar, math, memory/graph_manager.py — Dynamic Knowledge Graph Manager for Graphify Manages…, networkx, pathlib, psutil, pyqt6_qtcore (+8 more)

### Community 15 - "FileDropZone"
Cohesion: 0.21
Nodes (3): QDragEnterEvent, QDropEvent, FileDropZone

### Community 16 - "tts.py"
Cohesion: 0.07
Nodes (25): Local Text-to-Speech wrappers for MARK XL. Provides unified interface for…, _compress_silence(), create_tts_player(), EdgeTTSEngine, ElevenLabsTTSEngine, _import_kokoro_pipeline(), KokoroTTSEngine, _synth() (+17 more)

### Community 17 - "EchoGuard"
Cohesion: 0.07
Nodes (15): band_energies(), EchoGuard, ndarray, Telling the user's voice apart from our own coming back through the speakers.…, Classifies microphone blocks while the assistant is speaking. Usage:…, True once the estimate rests on enough real echo to be trusted., Residual left by this room's own echo. Higher = harder to separate., False when the acoustics are too poor to judge on content alone. Speakers… (+7 more)

### Community 18 - "desktop.py"
Cohesion: 0.12
Nodes (36): _ask_gemini_for_desktop_action(), _build_sandbox(), clean_desktop(), desktop_control(), _execute_generated_code(), _get_api_key(), _get_base_dir(), get_current_wallpaper() (+28 more)

### Community 19 - "load_api_keys"
Cohesion: 0.16
Nodes (14): get_app_icon(), get_assistant_name(), get_gemini_key(), get_llm_provider(), get_openrouter_key(), get_openrouter_model(), get_user_name(), get_wake_word_enabled() (+6 more)

### Community 20 - "HudCanvas"
Cohesion: 0.12
Nodes (12): QPainter, HudCanvas, Ask the avatar to look somewhere for a moment (see HoloAvatar.glance)., Thread-safe entry point for the audio threads. Stores the louder of the…, Draw the Avengers: Endgame Stark Arc Reactor at (cx, cy) with outer radius r., Draw subtle background CRT coordinate grid with + crosshairs (Screenshot 2)., Futuristic Oscilloscope Waveforms spanning across the globe (Screenshot 1 & 2…, Live cycling Hexadecimal & Telemetry stream (directly from Screenshot 1). (+4 more)

### Community 21 - "JarvisLive"
Cohesion: 0.09
Nodes (10): JarvisLive, Called when user clicks the CLEAR button in desktop GUI., Called when phone/dashboard sends a clear-chat directive., Chord pressed or released — may arrive on the hotkey thread., Called from the detector thread when 'Hey Jarvis' is heard., Auto-sleep after the configured silence window (wake-word mode only)., Enable/disable wake word from the settings UI. Returns a status token:…, Manual sleep/wake button in the UI. (+2 more)

### Community 22 - "config_manager.py"
Cohesion: 0.15
Nodes (19): ensure_config_dir(), get_brief_enabled(), Persist the chosen Live voice. Unknown names collapse to the default so a bad…, Read-modify-write one key without disturbing the rest of the config., Merge `values` into a namespace's stored config (read-modify-write, like every…, Persist assistant name and user name to config., save_api_keys(), save_assistant_config() (+11 more)

### Community 23 - "setter"
Cohesion: 0.09
Nodes (5): setter, _work(), Combined state for the two wake-word buttons. Readiness is a cheap,…, Thread-safe UI slot: wipe chat display., Wipe chat log and trigger any registered callback (e.g. backend/mobile sync).

### Community 24 - "._tuning_config"
Cohesion: 0.22
Nodes (7): The optional knobs, kept apart so one bad field can be dropped wholesale. Every…, get_media_resolution(), get_thinking_enabled(), get_turn_tuning(), Whether the Live model may spend tokens thinking before it answers. Off by…, How eagerly the server decides you have stopped speaking. OFF by default, and…, How finely the model tokenises the screenshots and camera frames it is sent.…

### Community 25 - "action_loader.py"
Cohesion: 0.05
Nodes (40): ActionRecord, ActionRegistry, _call_handler(), discover_actions(), _is_heavenly_restricted_params(), _opt_upper(), Path, Action discovery, validation, and dispatch — the built-in twin of… (+32 more)

### Community 26 - "_tlog"
Cohesion: 0.14
Nodes (11): broadcast_progress(), _deliver_news(), main(), runner(), Queue a background task and return task metadata immediately., Announce background completion ensuring ALFRED does not talk over active speech., Execute a single background job, streaming [control] [background XX%] progress., Worker loop consuming background jobs from background_task_queue. (+3 more)

### Community 27 - "computer_control.py"
Cohesion: 0.17
Nodes (27): _base_dir(), _clear_field(), _click(), _clipboard_get(), _clipboard_paste(), computer_control(), _drag(), _focus_window() (+19 more)

### Community 28 - "local_pipeline.py"
Cohesion: 0.16
Nodes (26): call_llm(), call_llm_stream(), call_llm_text(), _chat_endpoint(), check_model_available(), ensure_ollama_running(), get_base_dir(), _get_headers() (+18 more)

### Community 29 - ".run"
Cohesion: 0.14
Nodes (10): BaseException, _get_api_key(), _is_reconnect_signal(), _keep_context_of(), Background task: voice alerts when metrics exceed thresholds., Check user-configured topics once per day; speak alerts when new headlines…, Periodically sweeps garbage during idle silence so full Generation 2…, Forward phone mic PCM chunks from dashboard queue into the Gemini Live session. (+2 more)

### Community 30 - "tech_font"
Cohesion: 0.09
Nodes (15): QFont, QHBoxLayout, QPushButton, QVBoxLayout, _row(), _CameraPreview, mono_font(), PluginManagerOverlay (+7 more)

### Community 31 - "TronScoreBackgroundPlayer"
Cohesion: 0.11
Nodes (6): QObject, Background music audio engine. Plays background score continuously on loop…, Duck to 50% of base volume when speaking, restore to base volume when…, Called when Spotify plays a track. Pauses Tron background music, sets Spotify…, Specifically pause the local TRON audio core player regardless of mode., TronScoreBackgroundPlayer

### Community 32 - "_BrowserSession"
Cohesion: 0.05
Nodes (23): browser_control(), _BrowserSession, _detect_default_browser(), _find_exe_windows(), _find_opera_windows(), _firefox_profile_dir(), _log(), _normalize_url() (+15 more)

### Community 33 - "ClipboardManager"
Cohesion: 0.09
Nodes (14): ClipboardManager, cosine_similarity(), Compute cosine similarity between two float vectors., Thread-safe persistent clipboard manager with semantic indexing., Lazily initialize local fastembed model., Compute 384-dimensional vector embedding for text., Load history from disk., Save history to disk atomically. (+6 more)

### Community 34 - ".test_error_isolation_in_concurrent_tasks"
Cohesion: 0.29
Nodes (5): Verify that an exception in one concurrent task does not break or cancel…, Verify that a batch of tasks run with a concurrency limit of 5 scales sub-…, TestConcurrencyLimiter, execute_task(), safe_run()

### Community 35 - ".__init__"
Cohesion: 0.11
Nodes (10): ProactiveEngine, Decides when ALFRED should speak unprompted and builds a context-rich prompt.…, Build a context snapshot for Gemini. Rotates through three focus areas so…, _Popen, Exception, Turn hold-to-talk on or off. Returns the scope actually achieved., Raised inside the session TaskGroup to force a clean, voluntary reconnect (e.g.…, Session-scoped task: when a voluntary reconnect is requested, raise a signal… (+2 more)

### Community 36 - "audio_devices.py"
Cohesion: 0.12
Nodes (20): configure(), _display_name(), _is_pseudo(), list_devices(), prefetch(), _work(), _query(), _collect() (+12 more)

### Community 37 - "GraphManager"
Cohesion: 0.11
Nodes (14): GraphManager, Any, Path, Save the graph data to the JSON file atomically., Add an entity node to the graph. Returns True if successful., Add a relationship (edge) between two nodes. Returns True if successful., Apply exponential decay to all temporary nodes. Returns the number of nodes…, Query the knowledge graph for a concept and return connected subgraph up to… (+6 more)

### Community 38 - "gmail_manager.py"
Cohesion: 0.10
Nodes (24): _clean_header_str(), _extract_body_snippet(), fetch_unread_emails(), gmail_manager(), _load_gmail_creds(), Any, Gmail Manager Action for ALFRED Mark-LIV. Provides full Gmail connectivity: -…, Send an email using Gmail SMTP SSL. (+16 more)

### Community 39 - "CentralizedCache"
Cohesion: 0.06
Nodes (22): CentralizedCache, _canonicalize(), decorator(), wrapper(), Any, Stores value in cache with TTL. Fails open gracefully if storage fails., Deletes a key from cache. Fails open gracefully., Invalidates all keys starting with prefix. Useful for mutation hooks. (+14 more)

### Community 41 - "screen_find.py"
Cohesion: 0.15
Nodes (18): _calculate_similarity(), _get_frame_key(), get_onnx_session(), get_rapid_ocr(), _ocr_grounding(), Any, ndarray, actions/screen_find.py — Local Hybrid Element Grounding for ALFRED. Performs… (+10 more)

### Community 42 - "HueWheel"
Cohesion: 0.20
Nodes (4): QPointF, QRectF, HueWheel, Circular colour picker. The user drags the handle (small white circle) around…

### Community 43 - ".__init__"
Cohesion: 0.07
Nodes (14): BiometricFingerprintWidget, ClipboardPanel, CRTReconWidget, ImagePopupOverlay, MetricBar, QWidget, Halftone / CRT Dithered Optical Recon Scanner Widget (Screenshot 1: Top-Left…, Biometric Fingerprint Scanner Widget (Screenshot 1: Middle-Left Biometric Box).… (+6 more)

### Community 45 - "VisemeStream"
Cohesion: 0.13
Nodes (12): collections, coverage(), Text → mouth shape, fused with the audio the avatar is actually speaking. Why…, Reduce any character to a bare Latin letter, or "" if it has none. This is what…, Fraction of the letters in `text` we can reduce to a Latin sound., Split a line of speech into (viseme, duration-weight) pairs. Returns [] for…, Fuses the transcript's shape sequence onto the audio's timing. Thread note:…, Blend audio frames [(level, openness, width)] with the text queue. (+4 more)

### Community 46 - "screen_processor.py"
Cohesion: 0.15
Nodes (19): _base_dir(), _capture_camera(), _cv2_backend(), _detect_camera_index(), _get_camera_index(), _get_os(), _load_config(), _probe_camera() (+11 more)

### Community 47 - "qcol"
Cohesion: 0.18
Nodes (7): QColor, QPixmap, _DropCanvas, _file_category(), _fmt_size(), qcol(), Pre-render the static grid-dot background into a transparent pixmap so…

### Community 48 - "get_input_device"
Cohesion: 0.22
Nodes (9): get_input_device(), get_output_device(), _patch_config(), Read-modify-write one or more keys in api_keys.json. Every setter in this file…, Microphone device name, or '' for the system default., Speaker device name, or '' for the system default., save_input_device(), save_openrouter_config() (+1 more)

### Community 49 - "spotify_control.py"
Cohesion: 0.05
Nodes (42): authorize_user(), _get_base_dir(), get_devices(), get_spotify_client(), manage_queue(), _OAuthCallbackHandler, Any, Path (+34 more)

### Community 50 - "server.py"
Cohesion: 0.11
Nodes (17): base64, index(), _ensure_certs(), _local_ip(), _make_uploads_dir(), Path, dashboard/server.py — ALFRED Local HTTP Dashboard Plain HTTP on port 8000 (no…, Return the best LAN-facing IPv4 address, no internet required. (+9 more)

### Community 51 - "CustomizeOverlay"
Cohesion: 0.14
Nodes (10): CustomizeOverlay, _lbl(), format_icon_display_name(), get_available_app_icons(), Floating glassmorphic overlay for configuring Assistant Persona, Commander…, Highlight the selected voice pill; dim the rest., Updates the selected colour; hex box + wheel stay in sync, theme is live-…, Format an icon file name into an authentic, sleek tactical insignia title. (+2 more)

### Community 52 - "computer_settings"
Cohesion: 0.12
Nodes (16): brightness_get(), brightness_set(), computer_settings(), dark_mode(), press_key(), Current brightness 0-100, or None where it cannot be read., Set brightness to an absolute percentage. Only used to restore a value captured…, Current master volume 0-100, or None if this platform will not say. Undo needs… (+8 more)

### Community 53 - "unduck_media_apps"
Cohesion: 0.11
Nodes (15): _duck_linux(), duck_media_apps(), _worker(), _duck_windows(), Execute ducking on Linux via pulsectl., Lower external media application volume (by default to 30%, i.e. ducking by…, Restore ducked media applications to their exact original volume levels. :param…, Execute ducking on Windows via pycaw. (+7 more)

### Community 54 - "RemoteKeyOverlay"
Cohesion: 0.16
Nodes (6): Called from Qt main thread when user presses Remote Control., 15. Bug Fixes & Stability Updates, Floating overlay — QR code for instant phone pairing + manual key fallback., Call from any thread when a phone successfully connects., RemoteKeyOverlay, _lbl()

### Community 55 - "._receive_audio"
Cohesion: 0.20
Nodes (6): FunctionResponse, _clean_transcript(), _is_repeat_chunk(), _run_tool_bounded(), Send a captured frame immediately after its tool response. The frame is already…, True if this transcript chunk has already been seen this turn. Guards against…

### Community 56 - "._build_app"
Cohesion: 0.15
Nodes (14): action_ep(), audio_ws(), _auth(), clear_chat_ep(), command(), download_file(), list_files(), phone_audio_ws() (+6 more)

### Community 57 - "background_monitor.py"
Cohesion: 0.21
Nodes (14): add_monitor(), check_all(), _is_blocked(), list_monitors(), _load(), BackgroundMonitor — user-configured topic watching. Checks DDG news once per…, Run all pending topic checks (once per day per topic). Returns a list of…, remove_monitor() (+6 more)

### Community 58 - "find_element"
Cohesion: 0.12
Nodes (14): _screen_find(), find_element(), is_icon_query(), Determine if target query is specifically targeting an icon/non-text element., Main entry point for local hybrid UI element grounding. 1. Executes RapidOCR on…, Action handler called by ALFRED action dispatcher., screen_find(), 8. Full Desktop Control & Operating System Automation (+6 more)

### Community 59 - "json"
Cohesion: 0.15
Nodes (14): core/cache.py — Centralized Caching Layer for ALFRED Mark-II. Provides high-…, functools, hashlib, json, _load_events(), Calendar Sync Plugin for ALFRED Mark-LIV. Tracks agenda, meetings,…, Execute calendar action., run() (+6 more)

### Community 60 - "LocalLLMManager"
Cohesion: 0.13
Nodes (11): LocalLLMManager, Handle tool calls by executing them and getting final response., Manages local LLM interactions., Set system prompt and available tools., Add message to conversation history., Clear conversation history., Generate response from local LLM., create_local_stt_engine() (+3 more)

### Community 61 - "TestBackgroundWorkerPool"
Cohesion: 0.12
Nodes (7): Verify that calling interrupt() sets halt event, immediately stops active…, Verify that _safe_background_announce waits until ALFRED finishes speaking…, Verify DashboardServer tracks background tasks and exposes them via endpoint., Verify queue_background_task is registered in TOOL_DECLARATIONS., Verify that queue_background_task returns immediately (sub-millisecond), and…, Dispatch a mock task and verify voice PTT interaction continues with sub-second…, TestBackgroundWorkerPool

### Community 62 - "ScreenCapturePayload"
Cohesion: 0.20
Nodes (4): Hybrid return payload for screen captures. - Behaves as a 3-tuple `(img_bytes,…, ScreenCapturePayload, _do_stream(), tuple

### Community 63 - "LocalSTTManager"
Cohesion: 0.05
Nodes (25): LocalSTTManager, audio_callback_wrapper(), Process audio bytes for transcription based on engine type., Cancel any pending debounce timer, thread-safe., Reset the FINISH_MS countdown from zero., Timer callback: commit the accumulated sentence to the queue., Immediately commit whatever is in the buffer (+ optional extra word)., Process audio using Vosk streaming STT. Final results are held for FINISH_MS… (+17 more)

### Community 65 - "save_app_icon"
Cohesion: 0.40
Nodes (5): Update App Icon Action for ALFRED Mark-LIV. Switches the application window,…, Updates the main application icon and taskbar badge in realtime., update_app_icon(), Save the chosen app icon setting to config., save_app_icon()

### Community 66 - "LocalTTSManager"
Cohesion: 0.15
Nodes (8): LocalTTSManager, Flush any remaining text in buffer., Main loop for processing text queue and speaking., Manages local text-to-speech synthesis with streaming capabilities., Start the TTS processing thread., Stop the TTS processing thread., Add text to be spoken (non-blocking)., Add a sentence to be spoken, with sentence boundary detection.

### Community 67 - "ALFRED — MARK-IV (Wayne Protocol Edition)"
Cohesion: 0.04
Nodes (48): 10. Real-Time Insignia & Chassis Hot-Swapper, 11. Protocol Engine & Multi-Step Macro Playbooks (`config/protocols.yaml`), 12. Local Hybrid Visual Grounding (RapidOCR + ONNX + Gemini Fallback), 13. Process-Level Audio Ducking & Background Concurrency, 16. System Architecture & File Structure, 17. Quick Start & Installation, 18. Configuration Reference (`config/api_keys.json`), 19. Knowledge Graph (`graphify`) (+40 more)

### Community 68 - "_SysMetrics"
Cohesion: 0.13
Nodes (7): Thread-safe speech channel for plugins: lets a plugin ask JARVIS to say…, Thread-safe: ask the run loop to tear down and rebuild the Live session. Called…, Voice picker applied. The voice is baked into the session at connect time, so a…, Microphone or speaker changed. Both streams are opened inside the session…, _nvml_gpu_windows(), Return NVIDIA GPU utilisation % using nvml.dll directly — zero subprocess., _SysMetrics

### Community 69 - "memory_manager.py"
Cohesion: 0.11
Nodes (28): Update Daily Briefing Preferences Action for ALFRED Mark-LIV. Permanently…, _all_entries(), all_entries_for_ui(), _empty_memory(), _entry_value(), forget(), get_base_dir(), load_memory() (+20 more)

### Community 71 - "._apply_name_update"
Cohesion: 0.20
Nodes (8): apply_ui_accent(), current_palette(), Applies DOSSIER CRT [A-34] (#8e9bff), VECTOR CRT [WAKU] (#a8ff3e), or BATMAN…, A snapshot of the accent-linked colours currently on class C., LIVE full theme change. Replaces the old palette colours with the new ones in…, Live preview — paints the whole interface the new colour (does NOT write to…, Update all name/theme-dependent UI elements and persist to config., retheme_all_widgets()

### Community 72 - "WakeWordDetector"
Cohesion: 0.17
Nodes (5): Runs the wake model in a dedicated thread. The mic thread calls feed() with raw…, Load the model and spawn the inference thread. Returns True on success. Safe to…, Called from the mic callback (real-time thread). Must stay cheap and never…, WakeWordDetector, Load the detector once (model loads on first start). Idempotent.

### Community 73 - "get_active_window_info"
Cohesion: 0.20
Nodes (10): get_active_window_context(), get_active_window_info(), _get_linux_window_info(), _get_macos_window_info(), _get_windows_window_info(), Query foreground window handle, title, and process name on Windows., Query active frontmost window on macOS via Quartz or AppleScript fallback., Query active window on Linux via xdotool or wmctrl. (+2 more)

### Community 74 - "daily_brief.py"
Cohesion: 0.21
Nodes (12): daily_brief(), _get_gmail_brief(), _get_greeting(), _get_reminders_brief(), _get_system_vitals(), Daily Brief Action for ALFRED Mark-LIV. Provides the ultimate morning and daily…, Fetch unread emails summary via gmail_manager., Check scheduled reminders in ~/.alfred/reminders or ~/.jarvis/reminders. (+4 more)

### Community 75 - "datetime"
Cohesion: 0.41
Nodes (11): _base_dir(), _get_os(), Path, reminder(), _sanitise(), _schedule_linux(), _schedule_mac(), _schedule_windows() (+3 more)

### Community 76 - "time"
Cohesion: 0.10
Nodes (19): Tactical Audio Core Control Action for ALFRED. Controls the tactical HUD's…, asyncio, Push-to-talk — hold a key, speak, release. Why this exists ---------------…, Local Speech-to-Text wrappers for MARK XL. Provides unified interface for…, Speech-to-Text engines for MARK XL. Whisper – offline transcription via faster-…, clear(), history(), peek() (+11 more)

### Community 77 - "LocalPipelineCoordinator"
Cohesion: 0.09
Nodes (17): LocalPipelineCoordinator, stream_callback(), Coordinates STT → LLM → TTS flow., Set callbacks for UI updates., Log message via callback or print., Set UI state via callback., Start the local pipeline., Stop the local pipeline. (+9 more)

### Community 78 - "._aes_key"
Cohesion: 0.31
Nodes (5): auto_login(), device_login_ep(), login(), _derive_key(), SHA-256(sessionKey‖salt) → 32-byte AES-256 key (microseconds, no PBKDF2 needed).

### Community 79 - "LogWidget"
Cohesion: 0.29
Nodes (3): QTextEdit, LogWidget, Cancel any in-flight typing animation, drain the queue, and clear the display.

### Community 80 - "test_screen_processor.py"
Cohesion: 0.20
Nodes (9): capture_screen(), _capture_screen(), _compress(), format_visual_payload(), Prepares the visual frame payload dictionary for the Gemini Live API…, Captures primary or specified monitor, queries active OS window context,…, Default entry point used by main.py., Unit and integration tests for screen_processor.py window context grounding.… (+1 more)

### Community 82 - "MemoryOverlay"
Cohesion: 0.10
Nodes (11): AudioDeviceOverlay, ConfirmBanner, _HudOverlay, MemoryOverlay, Base for the floating panels placed by hand over the HUD. They are children of…, The gate in front of an action that cannot be taken back. The old confirmation…, Choose which microphone ALFRED listens to and which speakers it uses. Both…, Everything ALFRED has stored about you, and when it learned it. Memory used to… (+3 more)

### Community 84 - "PushToTalk"
Cohesion: 0.15
Nodes (7): chord_label(), PushToTalk, Begin watching. Returns the scope actually achieved., Feed a press/release from a Qt shortcut (non-Windows, or no hook)., Human-readable name of the chord, for the UI and the logs., Calls `on_change(held: bool)` whenever the chord is pressed or released. Start…, global' once a system-wide hook is running, else 'window'.

### Community 85 - "Path"
Cohesion: 0.17
Nodes (6): _base_dir(), Path, Render an ALFRED tactical icon at 4× resolution and downsample for crisp…, Create a Windows .lnk shortcut WITHOUT launching PowerShell or cmd. Tries…, Resolve the user's REAL desktop directory instead of assuming ~/Desktop, which…, Create a desktop shortcut on Windows / macOS / Linux. Never opens a terminal,…

### Community 86 - "ImagePopupOverlay"
Cohesion: 0.15
Nodes (9): action(), ImagePopupOverlay, QWidget, Handle mouse move for window dragging., Handle mouse release for window dragging., Show the popup centered over the parent widget., Show an image popup overlay., Popup overlay to display an image with a dismiss button. (+1 more)

### Community 87 - "confirm.py"
Cohesion: 0.23
Nodes (10): bind(), _log(), _Pending, core/confirm.py — a confirmation the model cannot forge. THE PROBLEM WITH THE…, Called by the UI when the user presses CONFIRM or CANCEL. Runs the stored…, Wire this module to the HUD. Called once from main.py at startup., Park an irreversible action behind the on-screen gate. Returns the sentence the…, request() (+2 more)

### Community 88 - "test_cache.py"
Cohesion: 0.16
Nodes (10): _get_live_weather(), Fetch live weather conditions without opening an external browser., Permanently saves daily briefing preferences into long-term memory., update_daily_briefing(), Performance Benchmark: memory_manager._trim_to_limit Tests execution time and…, patch, tests/test_cache.py — Comprehensive Test Suite for CentralizedCache. Tests: -…, Tests that weather queries are cached and subsequently invalidated by… (+2 more)

### Community 89 - "is_heavenly_restricted"
Cohesion: 0.13
Nodes (18): _is_restricted_path(), _normalize(), open_app(), check_action_params(), check_path_access(), get_allowed_c_roots(), is_heavenly_restricted(), is_safe_path() (+10 more)

### Community 90 - "._build_config"
Cohesion: 0.33
Nodes (5): LiveConnectConfig, get_proactive_audio_enabled(), get_voice(), Return the configured Live voice, falling back to the default if unset or if…, Whether the model gets to decide an utterance was not aimed at it and stay…

### Community 91 - "_VolumeSliderPopup"
Cohesion: 0.33
Nodes (3): QFrame, Sleek tactical cyber popup for adjusting master background music volume.…, _VolumeSliderPopup

### Community 92 - "_detect_action"
Cohesion: 0.40
Nodes (5): _detect_action(), _normalise(), Resolve a free-text description to an action name, locally. Returns {"action":…, What to tell the model when nothing matched. Names real actions so its retry…, _suggest()

### Community 93 - "delete_file"
Cohesion: 0.31
Nodes (11): delete_file(), _get_desktop(), _get_documents(), _get_downloads(), _get_music(), _get_pictures(), _get_videos(), Path (+3 more)

### Community 94 - "_gemini_grounding"
Cohesion: 0.22
Nodes (9): _capture_screen_image(), _gemini_grounding(), _get_api_key(), _onnx_element_grounding(), Capture current screen into a PIL Image., Run local ONNX element detector (OmniParser-v2 / Florence-2). Returns:…, Fallback visual grounding via Gemini Live / Flash API., Retrieve Gemini API key from api_keys.json or environment. (+1 more)

### Community 95 - "get_push_to_talk_enabled"
Cohesion: 0.14
Nodes (9): qt_sequence(), The same chord as a QKeySequence string., get_push_to_talk_enabled(), Hold-a-key-to-speak. When on, the mic is closed unless the chord is held., _press(), Floating overlay panel shown when the ⚙ header button is toggled., Repaint the push-to-talk row from the saved setting., Bind the chord inside the window when no global hook is available. On macOS and… (+1 more)

### Community 96 - ".load_track"
Cohesion: 0.20
Nodes (3): Set base normal volume (0.0 to 1.0). Speech ducking scales to 50% of base., Restores Tron legacy score as the default active audio., Specifically resume/play the local TRON audio core player.

### Community 97 - "_undo_create"
Cohesion: 0.22
Nodes (7): Reverse of a move: put it back where it came from., Reverse of a create: remove what we made — and only if we still made it.…, Reverse of a write: restore the old contents, or remove a file that did not…, _undo_create(), _undo_move(), _fn(), _undo_write()

### Community 98 - "TestScreenProcessorWindowContext"
Cohesion: 0.22
Nodes (5): Verifies system falls back to 'App: Unknown' without raising exceptions., Verification Requirement: Verify [WINDOW_CONTEXT] header contains VS Code and…, Verifies that active window query resolves in < 15ms and adheres to schema., Verifies capture_screen() returns valid compressed image and window context., TestScreenProcessorWindowContext

### Community 99 - "Daily Brief Protocol"
Cohesion: 0.50
Nodes (3): Daily Brief Protocol, Purpose, Rules

### Community 100 - "Email Handling Rules"
Cohesion: 0.50
Nodes (3): Email Handling Rules, Purpose, Rules

### Community 101 - "Executive Assistant Persona & Behavioral Standards"
Cohesion: 0.50
Nodes (3): Core Operational Rules, Executive Assistant Persona & Behavioral Standards, Persona & Demeanor

### Community 103 - "/email-triage Workflow"
Cohesion: 0.50
Nodes (3): /email-triage Workflow, Objective, Steps

### Community 104 - "_template.py"
Cohesion: 0.50
Nodes (3): Drop-in ALFRED plugin template. Copy this file, rename it (no leading…, parameters: dict of the args Gemini extracted, matching PLUGIN['parameters'].…, run()

### Community 106 - "_get_base_dir"
Cohesion: 0.67
Nodes (3): _get_api_key(), _get_base_dir(), Path

### Community 107 - "os"
Cohesion: 0.16
Nodes (12): is_ducked(), Process-level Audio Ducking for ALFRED. Automatically ducks background media…, Execute unducking on Windows via pycaw, restoring exact prior volume levels., Execute unducking on Linux via pulsectl., Return whether media ducking is currently active., _unduck_linux(), _worker(), _unduck_windows() (+4 more)

### Community 110 - "._decrypt"
Cohesion: 0.50
Nodes (3): ws_ep(), _decrypt_cbc(), Decrypt base64(IV[16] ‖ ciphertext) with AES-256-CBC + PKCS7.

### Community 111 - "_ensure_network_access"
Cohesion: 0.25
Nodes (3): _ensure_network_access(), Cross-platform, best-effort: open port in the OS firewall for LAN access. Runs…, Second HTTPS server on PORT+1 sharing the same app and in-memory state. Chrome…

### Community 116 - "setup.py"
Cohesion: 0.36
Nodes (7): _check_assets(), _check_python(), main(), MARK LIV — one-time setup. Installs the Python dependencies for THIS operating…, Fail immediately and clearly rather than deep inside a pip resolver. A wrong…, The avatar's face is a shipped file; a truncated clone should say so., _run()

### Community 124 - "TestAudioDucker"
Cohesion: 0.29
Nodes (4): patch, Verify that duck_media_apps lowers target media processes by 70% (0.3 factor),…, Verify Linux pulsectl ducking fallback logic., TestAudioDucker

### Community 127 - "format_window_context"
Cohesion: 0.50
Nodes (3): format_window_context(), Format the standard metadata block: [WINDOW_CONTEXT] App: <Name> | Title:…, Verifies exact string formatting requirements.

### Community 128 - "TestMemoryTrimBenchmark"
Cohesion: 0.29
Nodes (4): Measures execution time for 50,000 mock records. Under the old O(N^2)…, Preserves all items when memory is already below limit., Handles empty memory structure gracefully., TestMemoryTrimBenchmark

### Community 129 - "._listen_audio"
Cohesion: 0.40
Nodes (3): callback(), _open_mic(), True while the speakers may still be finishing our last sentence.

### Community 130 - "get_plugin_config"
Cohesion: 0.50
Nodes (4): get_plugin_config(), get_plugin_setting(), All stored values for a namespace (empty dict if none set yet)., A single value from a namespace, or `default` if unset.

### Community 131 - "File & Folder Exploration and Notes Directives"
Cohesion: 0.40
Nodes (4): 1. File Opening (`open`), 2. Folder Exploration (`explore`), 3. Dedicated Intel & Notes Terminal (`intel_notes`), File & Folder Exploration and Notes Directives

### Community 132 - "wake_word.py"
Cohesion: 0.31
Nodes (8): install_and_download(), is_installed(), is_ready(), Local wake-word detection for ALFRED ("Hey Jarvis"). Design goals: • ZERO cost…, True if the openwakeword package is importable (no model check)., True if openwakeword is installed AND its model files are present on disk. This…, One-click setup for the UI button: pip-install openwakeword if missing, then…, queue

### Community 133 - "intel_notes.py"
Cohesion: 0.31
Nodes (8): _auto_detect_type(), _config_dir(), intel_notes(), _load_notes(), Path, actions/intel_notes.py — Dedicated Intel & Notes Terminal Action. Provides a…, Action handler called by Gemini / action_loader., _save_notes()

### Community 134 - "/deep-work Workflow"
Cohesion: 0.50
Nodes (3): /deep-work Workflow, Objective, Steps

### Community 135 - "main.py"
Cohesion: 0.10
Nodes (19): audio_core(), Any, Main handler for the Audio Core control action., ProactiveEngine 2.0 — context-aware, time-aware, non-repetitive background…, create_local_pipeline(), Create and configure a local pipeline coordinator., gc, google (+11 more)

### Community 136 - "File & Folder Exploration Workflow"
Cohesion: 0.40
Nodes (4): File & Folder Exploration Workflow, Step 1: Target Identification, Step 2: Open File vs Explore Folder, Step 3: Record Intel or Links

## Knowledge Gaps
- **51 isolated node(s):** `Purpose`, `Rules`, `Purpose`, `Rules`, `Persona & Demeanor` (+46 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1095 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **33 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MainWindow` connect `MainWindow` to `CapabilitiesOverlay`, `._apply_name_update`, `JarvisUI`, `.__init__`, `ui.py`, `qcol`, `MemoryOverlay`, `CustomizeOverlay`, `Path`, `confirm.py`, `setter`, `RemoteKeyOverlay`, `config_manager.py`, `tech_font`, `get_push_to_talk_enabled`?**
  _High betweenness centrality (0.081) - this node is a cross-community bridge._
- **Why does `JarvisLive` connect `JarvisLive` to `._listen_audio`, `main.py`, `system_monitor.py`, `JarvisUI`, `EchoGuard`, `._save_session_summary`, `._tuning_config`, `_tlog`, `local_pipeline.py`, `.run`, `.__init__`, `VisemeStream`, `unduck_media_apps`, `RemoteKeyOverlay`, `._receive_audio`, `background_monitor.py`, `TestBackgroundWorkerPool`, `_SysMetrics`, `WakeWordDetector`, `time`, `DashboardServer`, `PushToTalk`, `._build_config`?**
  _High betweenness centrality (0.065) - this node is a cross-community bridge._
- **Why does `JarvisUI` connect `JarvisUI` to `.__init__`, `main.py`, `._apply_name_update`, `.__init__`, `ui.py`, `JarvisLive`, `unduck_media_apps`, `setter`, `RemoteKeyOverlay`, `_tlog`, `get_push_to_talk_enabled`?**
  _High betweenness centrality (0.059) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `JarvisLive` (e.g. with `ProactiveEngine` and `SystemMonitor`) actually correct?**
  _`JarvisLive` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Purpose`, `Rules`, `Purpose` to the rest of the system?**
  _51 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `game_updater.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05616605616605617 - nodes in this community are weakly interconnected._
- **Should `clipboard_manager.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09446693657219973 - nodes in this community are weakly interconnected._