# Graph Report - Alfred-Mark-IV  (2026-09-27)

## Corpus Check
- 101 files · ~200,260 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 14 file(s) not represented in the graph (top: .ico 7, (none) 3, .obj 2)

## Summary
- 2638 nodes · 5142 edges · 143 communities (112 shown, 31 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 204 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1bed38ce`
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
- subprocess
- .__init__
- threading
- EchoGuard
- desktop.py
- load_api_keys
- qcol
- JarvisLive
- config_manager.py
- Detailed Step-by-Step Guide: How to Switch to a Local API
- ._tuning_config
- action_loader.py
- _tlog
- computer_control.py
- llm_client.py
- .run
- tech_font
- TronScoreBackgroundPlayer
- _BrowserSession
- _RootShim
- .test_error_isolation_in_concurrent_tasks
- .__init__
- audio_devices.py
- GraphManager
- gmail_manager.py
- CentralizedCache
- crypto-js.min.js
- screen_find.py
- HueWheel
- QWidget
- TacticalAudioPlayerWidget
- VisemeStream
- screen_processor.py
- _DropCanvas
- get_input_device
- spotify_control.py
- server.py
- CustomizeOverlay
- computer_settings
- echo.py
- ClipboardPanel
- ._receive_audio
- ._build_app
- main.py
- find_element
- ui.py
- setter
- TestBackgroundWorkerPool
- ScreenCapturePayload
- LocalSTTManager
- NotesTerminalWidget
- save_app_icon
- LocalTTSManager
- ALFRED — MARK-IV (Wayne Protocol Edition)
- _SysMetrics
- memory_manager.py
- PluginSettingsOverlay
- ._apply_name_update
- WakeWordDetector
- get_active_window_info
- daily_brief.py
- datetime
- LocalLLMManager
- LocalPipelineCoordinator
- ._aes_key
- LogWidget
- capture_screen
- DashboardServer
- MemoryOverlay
- SetupOverlay
- TestAudioDucker
- ._build_jarvis_icon
- ImagePopupOverlay
- confirm.py
- AudioDeviceOverlay
- is_heavenly_restricted
- ._toggle_sentry_mode
- _VolumeSliderPopup
- _detect_action
- format_visual_payload
- _gemini_grounding
- ._apply_ptt_shortcut
- CapabilitiesOverlay
- ._quiz_render
- .__init__
- Daily Brief Protocol
- Email Handling Rules
- Executive Assistant Persona & Behavioral Standards
- 🎙️ 3. Master Tactical Voice Command Codex & Operational Handbook
- /email-triage Workflow
- _template.py
- 6. Spotify AI Agent: Dual-Tier Web API & Native Playback Architecture
- _get_base_dir
- os
- Graphify + Antigravity Project Workflow & Setup Guide
- _get_macos_wifi_interface
- _resolve_ws_auth
- _ensure_network_access
- rules/graphify.md
- workflows/graphify.md
- chromadb
- chromadb_config
- ._build_config
- fastembed
- sentence_transformers
- get_push_to_talk_enabled
- watchdog_events
- watchdog_observers
- format_window_context
- get_brief_enabled
- ._play_audio
- get_plugin_config
- _base_dir
- audio_core
- re
- /deep-work Workflow
- local_pipeline.py
- ._wake_state
- 17. Quick Start & Installation
- .get_audio_core_status
- Step 1: Install & Set Up Your Preferred Local LLM Server
- ._style_think_btn
- get_base_dir

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

## Communities (143 total, 31 thin omitted)

### Community 0 - "game_updater.py"
Cohesion: 0.06
Nodes (78): _build_google_flights_url(), flight_finder(), _format_spoken(), _format_text_report(), _get_base_dir(), _parse_date(), _parse_flights_with_gemini(), Path (+70 more)

### Community 1 - "file_controller.py"
Cohesion: 0.07
Nodes (62): copy_file(), create_file(), create_folder(), delete_file(), explore_folder(), file_controller(), find_files(), _format_size() (+54 more)

### Community 2 - "clipboard_manager.py"
Cohesion: 0.05
Nodes (42): add_clipboard_item(), classify_content_type(), clipboard_manager_action(), ClipboardManager, cosine_similarity(), _get_active_window_info(), get_recent_clipboards(), is_sensitive_content() (+34 more)

### Community 3 - "file_processor.py"
Cohesion: 0.08
Nodes (45): _detect_type(), file_processor(), _file_size_str(), _gemini_client(), _output_path(), _process_archive(), _process_audio(), _process_code() (+37 more)

### Community 4 - "web_search.py"
Cohesion: 0.06
Nodes (45): _compare(), _fetch_item(), _ddg_news(), _ddg_search(), _format_ddg(), _format_news(), _gemini_available(), _gemini_headlines() (+37 more)

### Community 5 - "code_helper.py"
Cohesion: 0.05
Nodes (60): _build(), _clean_code(), code_helper(), _detect_intent(), _edit_action(), _explain_action(), _fix_code(), _get_gemini() (+52 more)

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
Cohesion: 0.04
Nodes (20): JarvisUI, Update application and window icon in realtime., Thread-safe: raise the irreversible-action gate. Called from action handlers…, Thread-safe: take the gate down., Thread-safe: feed a 0.0–1.0 live audio level to the HUD waveform. Called from…, Ask the avatar to look somewhere for a moment (see HoloAvatar.glance)., Thread-safe: post a schedule of (level, openness, width) mouth frames for…, Thread-safe: wipe the on-screen conversation chat feed. (+12 more)

### Community 10 - "protocol_engine.py"
Cohesion: 0.06
Nodes (49): create_protocol(), _do_save(), _ensure_user_protocols_dir(), execute_protocol(), _execute_tool(), get_action_registry(), _get_default_protocols_path(), get_protocols_file() (+41 more)

### Community 12 - "MainWindow"
Cohesion: 0.05
Nodes (15): QHBoxLayout, QMainWindow, MainWindow, _fl(), Slot — display camera preview overlay (main thread)., Floating overlay panel shown when the ⚙ header button is toggled., Slot — runs on Qt main thread. Updates and shows the content panel., Slot — Qt main thread. Lays a document review into the content panel. (+7 more)

### Community 13 - "dev_agent.py"
Cohesion: 0.12
Nodes (27): _build_project(), _classify_error(), _extract_culprit_script(), _fix_files(), _get_model(), _has_error(), _install_dependencies(), _is_rate_limit() (+19 more)

### Community 14 - "subprocess"
Cohesion: 0.16
Nodes (15): install_and_download(), is_installed(), is_ready(), Local wake-word detection for ALFRED ("Hey Jarvis"). Design goals: • ZERO cost…, True if the openwakeword package is importable (no model check)., True if openwakeword is installed AND its model files are present on disk. This…, One-click setup for the UI button: pip-install openwakeword if missing, then…, _check_assets() (+7 more)

### Community 15 - ".__init__"
Cohesion: 0.08
Nodes (7): QDragEnterEvent, QDropEvent, CyberGraphicLineButton, FileDropZone, Tactical Dossier Card Widget (Screenshot 1: Exact recreation of SUBJECT A-34…, Tactical button rendered strictly with vector graphic lines, sharp 2px border…, SubjectDossierCard

### Community 16 - "threading"
Cohesion: 0.09
Nodes (17): Tactical Audio Core Control Action for ALFRED. Controls the tactical HUD's…, Local Text-to-Speech wrappers for MARK XL. Provides unified interface for…, create_tts_player(), EdgeTTSEngine, ElevenLabsTTSEngine, _play_audio_bytes(), Text-to-Speech engines for MARK XL. EdgeTTS – free Microsoft TTS (internet…, Microsoft EdgeTTS – free, requires internet. (+9 more)

### Community 17 - "EchoGuard"
Cohesion: 0.08
Nodes (14): band_energies(), EchoGuard, ndarray, Classifies microphone blocks while the assistant is speaking. Usage:…, True once the estimate rests on enough real echo to be trusted., Residual left by this room's own echo. Higher = harder to separate., False when the acoustics are too poor to judge on content alone. Speakers…, The residual a block must clear right now to count as a voice. (+6 more)

### Community 18 - "desktop.py"
Cohesion: 0.12
Nodes (35): _ask_gemini_for_desktop_action(), _build_sandbox(), clean_desktop(), desktop_control(), _execute_generated_code(), _get_api_key(), _get_base_dir(), get_current_wallpaper() (+27 more)

### Community 19 - "load_api_keys"
Cohesion: 0.13
Nodes (16): get_app_icon(), get_assistant_name(), get_gemini_key(), get_hud_style(), get_llm_provider(), get_openrouter_key(), get_openrouter_model(), get_user_name() (+8 more)

### Community 20 - "qcol"
Cohesion: 0.08
Nodes (19): QColor, QPainter, QPixmap, HudCanvas, qcol(), Ask the avatar to look somewhere for a moment (see HoloAvatar.glance)., Thread-safe: hand over a schedule of (level, openness, width) frames. The…, Thread-safe entry point for the audio threads. Stores the louder of the… (+11 more)

### Community 21 - "JarvisLive"
Cohesion: 0.09
Nodes (12): JarvisLive, Called when user clicks the CLEAR button in desktop GUI., Called when phone/dashboard sends a clear-chat directive., Chord pressed or released — may arrive on the hotkey thread., Load the detector once (model loads on first start). Idempotent., Called from the detector thread when 'Hey Jarvis' is heard., Auto-sleep after the configured silence window (wake-word mode only)., Enable/disable wake word from the settings UI. Returns a status token:… (+4 more)

### Community 22 - "config_manager.py"
Cohesion: 0.15
Nodes (19): ensure_config_dir(), get_base_dir(), Path, Persist the chosen Live voice. Unknown names collapse to the default so a bad…, Read-modify-write one key without disturbing the rest of the config., Merge `values` into a namespace's stored config (read-modify-write, like every…, Persist assistant name and user name to config., save_api_keys() (+11 more)

### Community 23 - "Detailed Step-by-Step Guide: How to Switch to a Local API"
Cohesion: 0.22
Nodes (9): 1. 100% Local & Air-Gapped Offline Execution: Switching from Gemini to Local API, Configuration Template for LM Studio / vLLM (OpenAI-Compatible):, Configuration Template for Ollama:, Configuration Template for OpenRouter API (Frontier Multi-Model Gateway):, Detailed Step-by-Step Guide: How to Switch to a Local API, Gemini Live API vs. Local Offline API Comparison, Step 2: Configure ALFRED's Target Backend in `config/api_keys.json`, Step 3: Launch ALFRED & Verify Connection (+1 more)

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

### Community 28 - "llm_client.py"
Cohesion: 0.18
Nodes (23): call_llm(), call_llm_stream(), call_llm_text(), _chat_endpoint(), check_model_available(), ensure_ollama_running(), _get_headers(), get_llm_provider() (+15 more)

### Community 29 - ".run"
Cohesion: 0.14
Nodes (10): BaseException, _get_api_key(), _is_reconnect_signal(), _keep_context_of(), Background task: voice alerts when metrics exceed thresholds., Check user-configured topics once per day; speak alerts when new headlines…, Periodically sweeps garbage during idle silence so full Generation 2…, Forward phone mic PCM chunks from dashboard queue into the Gemini Live session. (+2 more)

### Community 30 - "tech_font"
Cohesion: 0.12
Nodes (13): QFont, QVBoxLayout, _row(), _CameraPreview, mono_font(), Floating overlay that briefly shows what the camera captured., Floating overlay — QR code for instant phone pairing + manual key fallback., Call from any thread when a phone successfully connects. (+5 more)

### Community 31 - "TronScoreBackgroundPlayer"
Cohesion: 0.08
Nodes (12): control_playback(), QObject, _base_dir(), Path, Background music audio engine. Plays background score continuously on loop…, Set base normal volume (0.0 to 1.0). Speech ducking scales to 50% of base., Duck to 50% of base volume when speaking, restore to base volume when…, Called when Spotify plays a track. Pauses Tron background music, sets Spotify… (+4 more)

### Community 32 - "_BrowserSession"
Cohesion: 0.05
Nodes (23): browser_control(), _BrowserSession, _detect_default_browser(), _find_exe_windows(), _find_opera_windows(), _firefox_profile_dir(), _log(), _normalize_url() (+15 more)

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
Cohesion: 0.12
Nodes (21): _clean_header_str(), _extract_body_snippet(), fetch_unread_emails(), gmail_manager(), _load_gmail_creds(), Any, Gmail Manager Action for ALFRED Mark-LIV. Provides full Gmail connectivity: -…, Send an email using Gmail SMTP SSL. (+13 more)

### Community 39 - "CentralizedCache"
Cohesion: 0.06
Nodes (22): CentralizedCache, _canonicalize(), decorator(), wrapper(), Any, Stores value in cache with TTL. Fails open gracefully if storage fails., Deletes a key from cache. Fails open gracefully., Invalidates all keys starting with prefix. Useful for mutation hooks. (+14 more)

### Community 41 - "screen_find.py"
Cohesion: 0.15
Nodes (18): _calculate_similarity(), _get_frame_key(), get_onnx_session(), get_rapid_ocr(), _ocr_grounding(), Any, ndarray, actions/screen_find.py — Local Hybrid Element Grounding for ALFRED. Performs… (+10 more)

### Community 42 - "HueWheel"
Cohesion: 0.20
Nodes (4): QPointF, QRectF, HueWheel, Circular colour picker. The user drags the handle (small white circle) around…

### Community 43 - "QWidget"
Cohesion: 0.08
Nodes (10): BiometricFingerprintWidget, CRTReconWidget, ImagePopupOverlay, MetricBar, QWidget, Halftone / CRT Dithered Optical Recon Scanner Widget (Screenshot 1: Top-Left…, Biometric Fingerprint Scanner Widget (Screenshot 1: Middle-Left Biometric Box).…, Tactical Wireframe Humanoid Telemetry Widget (Screenshot 1: Lower-Left… (+2 more)

### Community 44 - "TacticalAudioPlayerWidget"
Cohesion: 0.16
Nodes (4): _EqualizerBarsWidget, Mini animated cyber audio wave visualizer., Bottom-Left Cyber Tactical Audio Player Widget. Styled matching the HUD /…, TacticalAudioPlayerWidget

### Community 45 - "VisemeStream"
Cohesion: 0.13
Nodes (12): collections, coverage(), Text → mouth shape, fused with the audio the avatar is actually speaking. Why…, Reduce any character to a bare Latin letter, or "" if it has none. This is what…, Fraction of the letters in `text` we can reduce to a Latin sound., Split a line of speech into (viseme, duration-weight) pairs. Returns [] for…, Fuses the transcript's shape sequence onto the audio's timing. Thread note:…, Blend audio frames [(level, openness, width)] with the text queue. (+4 more)

### Community 46 - "screen_processor.py"
Cohesion: 0.19
Nodes (16): _capture_camera(), _cv2_backend(), _detect_camera_index(), _get_camera_index(), _get_os(), _load_config(), _probe_camera(), Screen & webcam capture for ALFRED vision with OS window context grounding.… (+8 more)

### Community 47 - "_DropCanvas"
Cohesion: 0.33
Nodes (3): _DropCanvas, _file_category(), _fmt_size()

### Community 48 - "get_input_device"
Cohesion: 0.22
Nodes (9): get_input_device(), get_output_device(), _patch_config(), Read-modify-write one or more keys in api_keys.json. Every setter in this file…, Microphone device name, or '' for the system default., Speaker device name, or '' for the system default., save_input_device(), save_openrouter_config() (+1 more)

### Community 49 - "spotify_control.py"
Cohesion: 0.05
Nodes (42): authorize_user(), _get_base_dir(), get_devices(), get_spotify_client(), manage_queue(), _OAuthCallbackHandler, Any, Path (+34 more)

### Community 50 - "server.py"
Cohesion: 0.07
Nodes (24): _get_live_weather(), Fetch live weather conditions without opening an external browser., asyncio, base64, core/cache.py — Centralized Caching Layer for ALFRED Mark-II. Provides high-…, _make_uploads_dir(), Path, dashboard/server.py — ALFRED Local HTTP Dashboard Plain HTTP on port 8000 (no… (+16 more)

### Community 51 - "CustomizeOverlay"
Cohesion: 0.14
Nodes (10): CustomizeOverlay, _lbl(), format_icon_display_name(), get_available_app_icons(), Floating glassmorphic overlay for configuring Assistant Persona, Commander…, Highlight the selected voice pill; dim the rest., Updates the selected colour; hex box + wheel stay in sync, theme is live-…, Format an icon file name into an authentic, sleek tactical insignia title. (+2 more)

### Community 52 - "computer_settings"
Cohesion: 0.12
Nodes (16): brightness_get(), brightness_set(), computer_settings(), dark_mode(), paste(), press_key(), Current brightness 0-100, or None where it cannot be read., Set brightness to an absolute percentage. Only used to restore a value captured… (+8 more)

### Community 53 - "echo.py"
Cohesion: 0.10
Nodes (14): _duck_linux(), duck_media_apps(), _worker(), _duck_windows(), is_ducked(), Execute ducking on Linux via pulsectl., Lower external media application volume (by default to 30%, i.e. ducking by…, Restore ducked media applications to their exact original volume levels. :param… (+6 more)

### Community 55 - "._receive_audio"
Cohesion: 0.20
Nodes (6): FunctionResponse, _clean_transcript(), _is_repeat_chunk(), _run_tool_bounded(), Send a captured frame immediately after its tool response. The frame is already…, True if this transcript chunk has already been seen this turn. Guards against…

### Community 56 - "._build_app"
Cohesion: 0.22
Nodes (10): action_ep(), _auth(), clear_chat_ep(), command(), list_files(), revoke_devices(), _safe_filename(), status_ep() (+2 more)

### Community 57 - "main.py"
Cohesion: 0.09
Nodes (28): add_monitor(), check_all(), _is_blocked(), list_monitors(), _load(), BackgroundMonitor — user-configured topic watching. Checks DDG news once per…, Run all pending topic checks (once per day per topic). Returns a list of…, remove_monitor() (+20 more)

### Community 58 - "find_element"
Cohesion: 0.12
Nodes (14): _screen_find(), find_element(), is_icon_query(), Determine if target query is specifically targeting an icon/non-text element., Main entry point for local hybrid UI element grounding. 1. Executes RapidOCR on…, Action handler called by ALFRED action dispatcher., screen_find(), 8. Full Desktop Control & Operating System Automation (+6 more)

### Community 59 - "ui.py"
Cohesion: 0.11
Nodes (23): ProactiveEngine 2.0 — context-aware, time-aware, non-repetitive background…, Action to show an image popup overlay., core_avatar, json, math, memory/graph_manager.py — Dynamic Knowledge Graph Manager for Graphify Manages…, networkx, pathlib (+15 more)

### Community 60 - "setter"
Cohesion: 0.12
Nodes (3): setter, Thread-safe UI slot: wipe chat display., Wipe chat log and trigger any registered callback (e.g. backend/mobile sync).

### Community 61 - "TestBackgroundWorkerPool"
Cohesion: 0.12
Nodes (7): Verify that calling interrupt() sets halt event, immediately stops active…, Verify that _safe_background_announce waits until ALFRED finishes speaking…, Verify DashboardServer tracks background tasks and exposes them via endpoint., Verify queue_background_task is registered in TOOL_DECLARATIONS., Verify that queue_background_task returns immediately (sub-millisecond), and…, Dispatch a mock task and verify voice PTT interaction continues with sub-second…, TestBackgroundWorkerPool

### Community 62 - "ScreenCapturePayload"
Cohesion: 0.20
Nodes (4): Hybrid return payload for screen captures. - Behaves as a 3-tuple `(img_bytes,…, ScreenCapturePayload, _do_stream(), tuple

### Community 63 - "LocalSTTManager"
Cohesion: 0.05
Nodes (28): LocalSTTManager, audio_callback_wrapper(), Local Speech-to-Text wrappers for MARK XL. Provides unified interface for…, Process audio bytes for transcription based on engine type., Cancel any pending debounce timer, thread-safe., Reset the FINISH_MS countdown from zero., Timer callback: commit the accumulated sentence to the queue., Immediately commit whatever is in the buffer (+ optional extra word). (+20 more)

### Community 65 - "save_app_icon"
Cohesion: 0.40
Nodes (5): Update App Icon Action for ALFRED Mark-LIV. Switches the application window,…, Updates the main application icon and taskbar badge in realtime., update_app_icon(), Save the chosen app icon setting to config., save_app_icon()

### Community 66 - "LocalTTSManager"
Cohesion: 0.15
Nodes (8): LocalTTSManager, Flush any remaining text in buffer., Main loop for processing text queue and speaking., Manages local text-to-speech synthesis with streaming capabilities., Start the TTS processing thread., Stop the TTS processing thread., Add text to be spoken (non-blocking)., Add a sentence to be spoken, with sentence boundary detection.

### Community 67 - "ALFRED — MARK-IV (Wayne Protocol Edition)"
Cohesion: 0.12
Nodes (15): 10. Real-Time Insignia & Chassis Hot-Swapper, 11. Protocol Engine & Multi-Step Macro Playbooks (`config/protocols.yaml`), 12. Local Hybrid Visual Grounding (RapidOCR + ONNX + Gemini Fallback), 13. Process-Level Audio Ducking & Background Concurrency, 15. Bug Fixes & Stability Updates, 16. System Architecture & File Structure, 18. Configuration Reference (`config/api_keys.json`), 19. Knowledge Graph (`graphify`) (+7 more)

### Community 68 - "_SysMetrics"
Cohesion: 0.13
Nodes (7): Thread-safe speech channel for plugins: lets a plugin ask JARVIS to say…, Thread-safe: ask the run loop to tear down and rebuild the Live session. Called…, Voice picker applied. The voice is baked into the session at connect time, so a…, Microphone or speaker changed. Both streams are opened inside the session…, _nvml_gpu_windows(), Return NVIDIA GPU utilisation % using nvml.dll directly — zero subprocess., _SysMetrics

### Community 69 - "memory_manager.py"
Cohesion: 0.08
Nodes (34): Update Daily Briefing Preferences Action for ALFRED Mark-LIV. Permanently…, Permanently saves daily briefing preferences into long-term memory., update_daily_briefing(), _do_shutdown(), Summarise the current session in 1-2 sentences and save to long_term.json., _all_entries(), all_entries_for_ui(), _empty_memory() (+26 more)

### Community 70 - "PluginSettingsOverlay"
Cohesion: 0.20
Nodes (5): QPushButton, PluginManagerOverlay, PluginSettingsOverlay, Floating overlay — lists discovered plugins with per-plugin ON/OFF toggles., Floating overlay — renders per-plugin settings forms. Fully generic: it…

### Community 71 - "._apply_name_update"
Cohesion: 0.14
Nodes (10): apply_ui_accent(), current_palette(), Read api_keys.json config dict. Returns {} on any error., Applies DOSSIER CRT [A-34] (#8e9bff), VECTOR CRT [WAKU] (#a8ff3e), or BATMAN…, A snapshot of the accent-linked colours currently on class C., LIVE full theme change. Replaces the old palette colours with the new ones in…, Live preview — paints the whole interface the new colour (does NOT write to…, Update all name/theme-dependent UI elements and persist to config. (+2 more)

### Community 72 - "WakeWordDetector"
Cohesion: 0.20
Nodes (4): Runs the wake model in a dedicated thread. The mic thread calls feed() with raw…, Load the model and spawn the inference thread. Returns True on success. Safe to…, Called from the mic callback (real-time thread). Must stay cheap and never…, WakeWordDetector

### Community 73 - "get_active_window_info"
Cohesion: 0.14
Nodes (12): get_active_window_context(), get_active_window_info(), _get_linux_window_info(), _get_macos_window_info(), _get_windows_window_info(), Query foreground window handle, title, and process name on Windows., Query active frontmost window on macOS via Quartz or AppleScript fallback., Query active window on Linux via xdotool or wmctrl. (+4 more)

### Community 74 - "daily_brief.py"
Cohesion: 0.15
Nodes (15): daily_brief(), _get_gmail_brief(), _get_greeting(), _get_reminders_brief(), _get_system_vitals(), Daily Brief Action for ALFRED Mark-LIV. Provides the ultimate morning and daily…, Fetch unread emails summary via gmail_manager., Check scheduled reminders in ~/.alfred/reminders or ~/.jarvis/reminders. (+7 more)

### Community 75 - "datetime"
Cohesion: 0.13
Nodes (24): _auto_detect_type(), _config_dir(), intel_notes(), _load_notes(), Path, actions/intel_notes.py — Dedicated Intel & Notes Terminal Action. Provides a…, Action handler called by Gemini / action_loader., _save_notes() (+16 more)

### Community 76 - "LocalLLMManager"
Cohesion: 0.18
Nodes (8): LocalLLMManager, stream_callback(), Handle tool calls by executing them and getting final response., Manages local LLM interactions., Set system prompt and available tools., Add message to conversation history., Clear conversation history., Generate response from local LLM.

### Community 77 - "LocalPipelineCoordinator"
Cohesion: 0.10
Nodes (16): LocalPipelineCoordinator, Coordinates STT → LLM → TTS flow., Set callbacks for UI updates., Log message via callback or print., Set UI state via callback., Start the local pipeline., Stop the local pipeline., Callback for audio from STT manager. (+8 more)

### Community 78 - "._aes_key"
Cohesion: 0.31
Nodes (5): auto_login(), device_login_ep(), login(), _derive_key(), SHA-256(sessionKey‖salt) → 32-byte AES-256 key (microseconds, no PBKDF2 needed).

### Community 79 - "LogWidget"
Cohesion: 0.25
Nodes (3): QTextEdit, LogWidget, Cancel any in-flight typing animation, drain the queue, and clear the display.

### Community 80 - "capture_screen"
Cohesion: 0.22
Nodes (8): capture_screen(), _capture_screen(), _compress(), Captures primary or specified monitor, queries active OS window context,…, Default entry point used by main.py., Verification Requirement: Verify [WINDOW_CONTEXT] header contains VS Code and…, Verifies capture_screen() returns valid compressed image and window context., TestScreenProcessorWindowContext

### Community 82 - "MemoryOverlay"
Cohesion: 0.15
Nodes (8): ConfirmBanner, _HudOverlay, MemoryOverlay, Base for the floating panels placed by hand over the HUD. They are children of…, The gate in front of an action that cannot be taken back. The old confirmation…, Everything ALFRED has stored about you, and when it learned it. Memory used to…, Take every item out of the layout and detach it from the widget tree in this…, Size the panel to its content, re-centre it, and repaint what the old size…

### Community 84 - "TestAudioDucker"
Cohesion: 0.29
Nodes (4): patch, Verify that duck_media_apps lowers target media processes by 70% (0.3 factor),…, Verify Linux pulsectl ducking fallback logic., TestAudioDucker

### Community 85 - "._build_jarvis_icon"
Cohesion: 0.22
Nodes (4): Render an ALFRED tactical icon at 4× resolution and downsample for crisp…, Create a Windows .lnk shortcut WITHOUT launching PowerShell or cmd. Tries…, Resolve the user's REAL desktop directory instead of assuming ~/Desktop, which…, Create a desktop shortcut on Windows / macOS / Linux. Never opens a terminal,…

### Community 86 - "ImagePopupOverlay"
Cohesion: 0.15
Nodes (9): action(), ImagePopupOverlay, QWidget, Handle mouse move for window dragging., Handle mouse release for window dragging., Show the popup centered over the parent widget., Show an image popup overlay., Popup overlay to display an image with a dismiss button. (+1 more)

### Community 87 - "confirm.py"
Cohesion: 0.19
Nodes (13): bind(), _log(), _Pending, pending_title(), core/confirm.py — a confirmation the model cannot forge. THE PROBLEM WITH THE…, Called by the UI when the user presses CONFIRM or CANCEL. Runs the stored…, when nothing is waiting. Lets an action avoid stacking two banners., Wire this module to the HUD. Called once from main.py at startup. (+5 more)

### Community 88 - "AudioDeviceOverlay"
Cohesion: 0.22
Nodes (3): AudioDeviceOverlay, Choose which microphone ALFRED listens to and which speakers it uses. Both…, Place a floating overlay in the middle of the HUD and show it.

### Community 89 - "is_heavenly_restricted"
Cohesion: 0.10
Nodes (26): apply_heal_patch(), dev_agent(), _diagnose_trace(), heal_execution_error(), _heuristic_repair(), Parses stderr and stack traces to isolate error category, line number, and…, Attempts fast, deterministic rule-based fixes for standard syntax and import…, r""" Automated diagnostic and self-repair engine for tool and script execution… (+18 more)

### Community 90 - "._toggle_sentry_mode"
Cohesion: 0.33
Nodes (3): Toggle continuous visual context (camera stream) monitoring., Thread-safe: start live camera feed in the full HUD area., Thread-safe: stop the live camera feed.

### Community 91 - "_VolumeSliderPopup"
Cohesion: 0.33
Nodes (3): QFrame, Sleek tactical cyber popup for adjusting master background music volume.…, _VolumeSliderPopup

### Community 92 - "_detect_action"
Cohesion: 0.40
Nodes (5): _detect_action(), _normalise(), Resolve a free-text description to an action name, locally. Returns {"action":…, What to tell the model when nothing matched. Names real actions so its retry…, _suggest()

### Community 93 - "format_visual_payload"
Cohesion: 0.40
Nodes (3): format_visual_payload(), Prepares the visual frame payload dictionary for the Gemini Live API…, Verifies metadata block is prepended directly to the visual frame payload.

### Community 94 - "_gemini_grounding"
Cohesion: 0.22
Nodes (9): _capture_screen_image(), _gemini_grounding(), _get_api_key(), _onnx_element_grounding(), Capture current screen into a PIL Image., Run local ONNX element detector (OmniParser-v2 / Florence-2). Returns:…, Fallback visual grounding via Gemini Live / Flash API., Retrieve Gemini API key from api_keys.json or environment. (+1 more)

### Community 95 - "._apply_ptt_shortcut"
Cohesion: 0.29
Nodes (5): qt_sequence(), The same chord as a QKeySequence string., _press(), Bind the chord inside the window when no global hook is available. On macOS and…, Report a windowed press/release to whoever owns the microphone.

### Community 98 - ".__init__"
Cohesion: 0.33
Nodes (4): index(), _local_ip(), Return the best LAN-facing IPv4 address, no internet required., _read()

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

### Community 107 - "os"
Cohesion: 0.19
Nodes (10): Process-level Audio Ducking for ALFRED. Automatically ducks background media…, Execute unducking on Windows via pycaw, restoring exact prior volume levels., Execute unducking on Linux via pulsectl., _unduck_linux(), _worker(), _unduck_windows(), Push-to-talk — hold a key, speak, release. Why this exists ---------------…, os (+2 more)

### Community 110 - "_resolve_ws_auth"
Cohesion: 0.20
Nodes (7): audio_ws(), download_file(), phone_audio_ws(), _resolve_ws_auth(), ws_ep(), _decrypt_cbc(), Decrypt base64(IV[16] ‖ ciphertext) with AES-256-CBC + PKCS7.

### Community 111 - "_ensure_network_access"
Cohesion: 0.20
Nodes (5): _ensure_certs(), _ensure_network_access(), Cross-platform, best-effort: open port in the OS firewall for LAN access. Runs…, Second HTTPS server on PORT+1 sharing the same app and in-memory state. Chrome…, Make sure config/certs holds a TLS key pair, generating a self-signed one the…

### Community 116 - "._build_config"
Cohesion: 0.33
Nodes (5): LiveConnectConfig, get_proactive_audio_enabled(), get_voice(), Return the configured Live voice, falling back to the default if unset or if…, Whether the model gets to decide an utterance was not aimed at it and stay…

### Community 124 - "get_push_to_talk_enabled"
Cohesion: 0.40
Nodes (3): get_push_to_talk_enabled(), Hold-a-key-to-speak. When on, the mic is closed unless the chord is held., Repaint the push-to-talk row from the saved setting.

### Community 127 - "format_window_context"
Cohesion: 0.50
Nodes (3): format_window_context(), Format the standard metadata block: [WINDOW_CONTEXT] App: <Name> | Title:…, Verifies exact string formatting requirements.

### Community 129 - "._play_audio"
Cohesion: 0.20
Nodes (7): callback(), _open_mic(), _pcm_level(), _pcm_visemes(), True while the speakers may still be finishing our last sentence., Map a block of int16 PCM samples to a 0.0–1.0 loudness level for the HUD…, Slice a PCM block into (level, openness, width) frames, one per 20 ms. Returns…

### Community 130 - "get_plugin_config"
Cohesion: 0.50
Nodes (4): get_plugin_config(), get_plugin_setting(), All stored values for a namespace (empty dict if none set yet)., A single value from a namespace, or `default` if unset.

### Community 132 - "audio_core"
Cohesion: 0.50
Nodes (4): audio_core(), Any, Main handler for the Audio Core control action., 5. Dual-Mode Tactical Audio Matrix & Background Sound Engine

### Community 133 - "re"
Cohesion: 0.40
Nodes (3): main(), remove_emojis_from_headings(), re

### Community 134 - "/deep-work Workflow"
Cohesion: 0.50
Nodes (3): /deep-work Workflow, Objective, Steps

### Community 135 - "local_pipeline.py"
Cohesion: 0.25
Nodes (7): create_local_pipeline(), Local audio pipeline coordinator for MARK XL. Handles STT → LLM → TTS flow for…, Create and configure a local pipeline coordinator., create_local_stt_engine(), Factory function to create a local STT manager., create_local_tts_engine(), Factory function to create a local TTS manager.

### Community 137 - "17. Quick Start & Installation"
Cohesion: 0.67
Nodes (3): 17. Quick Start & Installation, 1. Prerequisites, 2. Setup & Execution

### Community 139 - "Step 1: Install & Set Up Your Preferred Local LLM Server"
Cohesion: 0.50
Nodes (4): Option A: Ollama (Recommended — Simplest Setup), Option B: LM Studio (Recommended for GUI Users), Option C: vLLM or llama.cpp (High-Throughput / Linux Servers), Step 1: Install & Set Up Your Preferred Local LLM Server

## Knowledge Gaps
- **52 isolated node(s):** `Purpose`, `Rules`, `Purpose`, `Rules`, `Persona & Demeanor` (+47 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1095 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **31 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `JarvisUI` connect `JarvisUI` to `.__init__`, `._toggle_sentry_mode`, `._apply_name_update`, `._wake_state`, `.__init__`, `get_push_to_talk_enabled`, `JarvisLive`, `echo.py`, `main.py`, `_tlog`, `ui.py`, `setter`, `._apply_ptt_shortcut`?**
  _High betweenness centrality (0.080) - this node is a cross-community bridge._
- **Why does `MainWindow` connect `MainWindow` to `get_brief_enabled`, `._wake_state`, `.get_audio_core_status`, `._style_think_btn`, `.__init__`, `tech_font`, `QWidget`, `_DropCanvas`, `CustomizeOverlay`, `ui.py`, `setter`, `._apply_name_update`, `MemoryOverlay`, `._build_jarvis_icon`, `AudioDeviceOverlay`, `._toggle_sentry_mode`, `._apply_ptt_shortcut`, `CapabilitiesOverlay`, `._quiz_render`, `get_push_to_talk_enabled`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Why does `JarvisLive` connect `JarvisLive` to `._play_audio`, `web_search.py`, `system_monitor.py`, `JarvisUI`, `._speak_local`, `EchoGuard`, `._tuning_config`, `_tlog`, `llm_client.py`, `.run`, `.__init__`, `VisemeStream`, `server.py`, `echo.py`, `._receive_audio`, `main.py`, `TestBackgroundWorkerPool`, `_SysMetrics`, `memory_manager.py`, `WakeWordDetector`, `DashboardServer`, `._build_config`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `JarvisLive` (e.g. with `ProactiveEngine` and `SystemMonitor`) actually correct?**
  _`JarvisLive` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Purpose`, `Rules`, `Purpose` to the rest of the system?**
  _52 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `game_updater.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06190476190476191 - nodes in this community are weakly interconnected._
- **Should `file_controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06841046277665996 - nodes in this community are weakly interconnected._