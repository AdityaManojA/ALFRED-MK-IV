# Graph Report - Alfred-Mark-IV  (2026-09-27)

## Corpus Check
- 101 files · ~201,645 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 14 file(s) not represented in the graph (top: .ico 7, (none) 3, .obj 2)

## Summary
- 2646 nodes · 5157 edges · 142 communities (114 shown, 28 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 209 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `580551ce`
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
- get_input_device
- .__init__
- typing
- EchoGuard
- desktop.py
- action_loader.py
- HudCanvas
- JarvisLive
- config_manager.py
- setter
- .__init__
- plugin_loader.py
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
- ._build_right_panel
- QWidget
- TacticalAudioPlayerWidget
- VisemeStream
- screen_processor.py
- TestProtocolEngine
- qcol
- spotify_control.py
- server.py
- CustomizeOverlay
- computer_settings
- unduck_media_apps
- RemoteKeyOverlay
- ._receive_audio
- ._build_app
- sys
- json
- time
- LocalLLMManager
- TestBackgroundWorkerPool
- ScreenCapturePayload
- LocalSTTManager
- NotesTerminalWidget
- ui.py
- LocalTTSManager
- ALFRED — MARK-IV (Wayne Protocol Edition)
- _SysMetrics
- memory_manager.py
- audio_ducker.py
- ._apply_name_update
- WakeWordDetector
- get_active_window_info
- daily_brief.py
- ._ui_wake_toggle
- datetime
- LocalPipelineCoordinator
- ._aes_key
- LogWidget
- capture_screen
- DashboardServer
- MemoryOverlay
- SetupOverlay
- PushToTalk
- ._build_jarvis_icon
- ImagePopupOverlay
- confirm.py
- test_cache.py
- is_heavenly_restricted
- TestMemoryTrimBenchmark
- .request_reconnect
- _detect_action
- PluginManagerOverlay
- format_visual_payload
- ._apply_ptt_shortcut
- 🎙️ 5. Master Tactical Voice Command Codex & Operational Handbook
- ._build_system_instruction
- TestScreenProcessorWindowContext
- Daily Brief Protocol
- Email Handling Rules
- Executive Assistant Persona & Behavioral Standards
- Detailed Step-by-Step Guide: How to Switch to a Local API
- /email-triage Workflow
- _template.py
- 8. Spotify AI Agent: Dual-Tier Web API & Native Playback Architecture
- _get_base_dir
- 🎭 3. Example & Fun Tactical Commands ("Wayne Protocol" in Action)
- Graphify + Antigravity Project Workflow & Setup Guide
- _get_macos_wifi_interface
- ._decrypt
- _ensure_network_access
- rules/graphify.md
- workflows/graphify.md
- chromadb
- chromadb_config
- ClipboardPanel
- fastembed
- sentence_transformers
- TestAudioDucker
- watchdog_events
- watchdog_observers
- .clear_chat
- get_push_to_talk_enabled
- ._listen_audio
- _base_dir
- main.py
- background_monitor.py
- ._toggle_sentry_mode
- SubjectDossierCard
- audio_core
- Step 1: Install & Set Up Your Preferred Local LLM Server
- type_text
- 18. Quick Start & Installation
- get_base_dir
- create_local_pipeline

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
- `7. Dual-Mode Tactical Audio Matrix & Background Sound Engine` --references--> `audio_core()`  [INFERRED]
  readme.md → actions/audio_core.py
- `4. Security, Privacy & Defensive Architecture` --references--> `computer_control()`  [INFERRED]
  readme.md → actions/computer_control.py
- `1. File Opening (`open`)` --references--> `file_controller()`  [INFERRED]
  .agents/rules/file_exploration.md → actions/file_controller.py

## Import Cycles
- None detected.

## Communities (142 total, 28 thin omitted)

### Community 0 - "game_updater.py"
Cohesion: 0.06
Nodes (78): _build_google_flights_url(), flight_finder(), _format_spoken(), _format_text_report(), _get_base_dir(), _parse_date(), _parse_flights_with_gemini(), Path (+70 more)

### Community 1 - "file_controller.py"
Cohesion: 0.07
Nodes (63): copy_file(), create_file(), create_folder(), delete_file(), explore_folder(), file_controller(), find_files(), _format_size() (+55 more)

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
Cohesion: 0.07
Nodes (43): _ChangeHandler, _chunk_text(), crawl_and_index(), _delete_file_chunks(), _detokenize_tokens(), _extract_text_from_file(), _get_chroma_collection(), _get_embedding_model() (+35 more)

### Community 8 - "system_monitor.py"
Cohesion: 0.07
Nodes (38): _get_cpu_temp(), _get_gpu_usage(), get_system_status(), _is_private_or_loopback(), is_protected_process(), _nvml_gpu(), Any, actions/system_monitor.py — System Metric Checks, Process Tree Watchdog &… (+30 more)

### Community 9 - "JarvisUI"
Cohesion: 0.05
Nodes (20): main(), JarvisUI, Thread-safe: raise the irreversible-action gate. Called from action handlers…, Thread-safe: take the gate down., Thread-safe: feed a 0.0–1.0 live audio level to the HUD waveform. Called from…, Ask the avatar to look somewhere for a moment (see HoloAvatar.glance)., Thread-safe: post a schedule of (level, openness, width) mouth frames for…, Thread-safe: wipe the on-screen conversation chat feed. (+12 more)

### Community 10 - "protocol_engine.py"
Cohesion: 0.09
Nodes (41): create_protocol(), _do_save(), _ensure_user_protocols_dir(), execute_protocol(), _execute_tool(), get_action_registry(), _get_default_protocols_path(), get_protocols_file() (+33 more)

### Community 12 - "MainWindow"
Cohesion: 0.04
Nodes (13): QMainWindow, MainWindow, Slot — display camera preview overlay (main thread)., Slot — runs on Qt main thread. Updates and shows the content panel., Slot — Qt main thread. Lays a document review into the content panel., Slot — Qt main thread. Puts a fresh quiz on the board., Place a floating overlay in the middle of the HUD and show it., Update bottom-left tactical audio player to display and control Spotify… (+5 more)

### Community 13 - "dev_agent.py"
Cohesion: 0.06
Nodes (53): apply_heal_patch(), _build_project(), _classify_error(), dev_agent(), _diagnose_trace(), _extract_culprit_script(), _fix_files(), _get_model() (+45 more)

### Community 14 - "get_input_device"
Cohesion: 0.15
Nodes (14): list_devices(), Device names for 'input' or 'output'. Falls back to a synchronous query if the…, get_input_device(), get_output_device(), _patch_config(), Read-modify-write one or more keys in api_keys.json. Every setter in this file…, Microphone device name, or '' for the system default., Speaker device name, or '' for the system default. (+6 more)

### Community 15 - ".__init__"
Cohesion: 0.08
Nodes (7): QApplication, QDragEnterEvent, QDropEvent, CyberGraphicLineButton, FileDropZone, Tactical button rendered strictly with vector graphic lines, sharp 2px border…, _RootShim

### Community 16 - "typing"
Cohesion: 0.07
Nodes (29): Local Text-to-Speech wrappers for MARK XL. Provides unified interface for…, _compress_silence(), create_tts_player(), EdgeTTSEngine, ElevenLabsTTSEngine, _import_kokoro_pipeline(), KokoroTTSEngine, _synth() (+21 more)

### Community 17 - "EchoGuard"
Cohesion: 0.08
Nodes (14): band_energies(), EchoGuard, ndarray, Classifies microphone blocks while the assistant is speaking. Usage:…, True once the estimate rests on enough real echo to be trusted., Residual left by this room's own echo. Higher = harder to separate., False when the acoustics are too poor to judge on content alone. Speakers…, The residual a block must clear right now to count as a voice. (+6 more)

### Community 18 - "desktop.py"
Cohesion: 0.12
Nodes (36): _ask_gemini_for_desktop_action(), _build_sandbox(), clean_desktop(), desktop_control(), _execute_generated_code(), _get_api_key(), _get_base_dir(), get_current_wallpaper() (+28 more)

### Community 19 - "action_loader.py"
Cohesion: 0.14
Nodes (13): ActionRecord, ActionRegistry, _call_handler(), discover_actions(), _is_heavenly_restricted_params(), _opt_upper(), Path, Action discovery, validation, and dispatch — the built-in twin of… (+5 more)

### Community 20 - "HudCanvas"
Cohesion: 0.09
Nodes (15): QPainter, HudCanvas, Ask the avatar to look somewhere for a moment (see HoloAvatar.glance)., Thread-safe: hand over a schedule of (level, openness, width) frames. The…, Thread-safe entry point for the audio threads. Stores the louder of the…, True only when this canvas can actually be seen by the user., Draw the Avengers: Endgame Stark Arc Reactor at (cx, cy) with outer radius r., Draw subtle background CRT coordinate grid with + crosshairs (Screenshot 2). (+7 more)

### Community 21 - "JarvisLive"
Cohesion: 0.10
Nodes (10): JarvisLive, Called when user clicks the CLEAR button in desktop GUI., Called when phone/dashboard sends a clear-chat directive., Chord pressed or released — may arrive on the hotkey thread., Queue a background task and return task metadata immediately., Background task: voice alerts when metrics exceed thresholds., Check user-configured topics once per day; speak alerts when new headlines…, Periodically sweeps garbage during idle silence so full Generation 2… (+2 more)

### Community 22 - "config_manager.py"
Cohesion: 0.09
Nodes (36): ensure_config_dir(), get_app_icon(), get_assistant_name(), get_base_dir(), get_brief_enabled(), get_gemini_key(), get_hud_style(), get_llm_provider() (+28 more)

### Community 23 - "setter"
Cohesion: 0.10
Nodes (3): setter, _work(), Combined state for the two wake-word buttons. Readiness is a cheap,…

### Community 24 - ".__init__"
Cohesion: 0.11
Nodes (5): _fl(), Floating overlay panel shown when the ⚙ header button is toggled., Returns True if auto-start is currently registered on this OS., Open the API key and neural backend configuration overlay from settings., Update application and window icon in realtime.

### Community 25 - "plugin_loader.py"
Cohesion: 0.09
Nodes (25): _call_run(), discover_plugins(), _load_error(), _opt_upper(), PluginRecord, PluginRegistry, Exception, Path (+17 more)

### Community 26 - "_tlog"
Cohesion: 0.17
Nodes (9): broadcast_progress(), _deliver_news(), runner(), Announce background completion ensuring ALFRED does not talk over active speech., Execute a single background job, streaming [control] [background XX%] progress., Worker loop consuming background jobs from background_task_queue., Format terminal log report without emojis using red bracketed tags, and…, Two-phase briefing optimized for speed: Phase 1 — instant greeting (no tools) →… (+1 more)

### Community 27 - "computer_control.py"
Cohesion: 0.12
Nodes (32): _base_dir(), _clear_field(), _click(), _clipboard_get(), _clipboard_paste(), computer_control(), _drag(), _focus_window() (+24 more)

### Community 28 - "local_pipeline.py"
Cohesion: 0.17
Nodes (24): call_llm(), call_llm_stream(), call_llm_text(), _chat_endpoint(), check_model_available(), ensure_ollama_running(), _get_headers(), get_llm_provider() (+16 more)

### Community 29 - ".run"
Cohesion: 0.15
Nodes (10): BaseException, _get_api_key(), _is_reconnect_signal(), _do_shutdown(), _keep_context_of(), Summarise the current session in 1-2 sentences and save to long_term.json., Background task: periodically checks if the user has been silent long enough,…, Forward phone mic PCM chunks from dashboard queue into the Gemini Live session. (+2 more)

### Community 30 - "tech_font"
Cohesion: 0.11
Nodes (13): QFont, QVBoxLayout, _CameraPreview, CapabilitiesOverlay, _lbl(), mono_font(), PluginSettingsOverlay, Floating overlay that briefly shows what the camera captured. (+5 more)

### Community 31 - "TronScoreBackgroundPlayer"
Cohesion: 0.08
Nodes (12): control_playback(), QObject, _base_dir(), Path, Background music audio engine. Plays background score continuously on loop…, Set base normal volume (0.0 to 1.0). Speech ducking scales to 50% of base., Duck to 50% of base volume when speaking, restore to base volume when…, Called when Spotify plays a track. Pauses Tron background music, sets Spotify… (+4 more)

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
Cohesion: 0.12
Nodes (9): ProactiveEngine, Decides when ALFRED should speak unprompted and builds a context-rich prompt.…, _Popen, Exception, Turn hold-to-talk on or off. Returns the scope actually achieved., Raised inside the session TaskGroup to force a clean, voluntary reconnect (e.g.…, Session-scoped task: when a voluntary reconnect is requested, raise a signal…, _ReconnectSignal (+1 more)

### Community 36 - "audio_devices.py"
Cohesion: 0.12
Nodes (18): configure(), _display_name(), _is_pseudo(), prefetch(), _work(), _query(), _collect(), core/audio_devices.py — pick which microphone and which speakers ALFRED uses.… (+10 more)

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
Cohesion: 0.07
Nodes (39): _calculate_similarity(), _capture_screen_image(), find_element(), _gemini_grounding(), _get_api_key(), _get_frame_key(), get_onnx_session(), get_rapid_ocr() (+31 more)

### Community 42 - "._build_right_panel"
Cohesion: 0.25
Nodes (3): QHBoxLayout, Style the COGNITIVE TRACE toggle to reflect its on/off state., Show or hide the agent's internal reasoning trace in the chat log.

### Community 43 - "QWidget"
Cohesion: 0.11
Nodes (10): BiometricFingerprintWidget, CRTReconWidget, ImagePopupOverlay, MetricBar, QWidget, Halftone / CRT Dithered Optical Recon Scanner Widget (Screenshot 1: Top-Left…, Biometric Fingerprint Scanner Widget (Screenshot 1: Middle-Left Biometric Box).…, Tactical Wireframe Humanoid Telemetry Widget (Screenshot 1: Lower-Left… (+2 more)

### Community 44 - "TacticalAudioPlayerWidget"
Cohesion: 0.11
Nodes (7): QFrame, _EqualizerBarsWidget, Mini animated cyber audio wave visualizer., Sleek tactical cyber popup for adjusting master background music volume.…, Bottom-Left Cyber Tactical Audio Player Widget. Styled matching the HUD /…, TacticalAudioPlayerWidget, _VolumeSliderPopup

### Community 45 - "VisemeStream"
Cohesion: 0.13
Nodes (12): collections, coverage(), Text → mouth shape, fused with the audio the avatar is actually speaking. Why…, Reduce any character to a bare Latin letter, or "" if it has none. This is what…, Fraction of the letters in `text` we can reduce to a Latin sound., Split a line of speech into (viseme, duration-weight) pairs. Returns [] for…, Fuses the transcript's shape sequence onto the audio's timing. Thread note:…, Blend audio frames [(level, openness, width)] with the text queue. (+4 more)

### Community 46 - "screen_processor.py"
Cohesion: 0.18
Nodes (17): _capture_camera(), _cv2_backend(), _detect_camera_index(), _get_camera_index(), _get_os(), _load_config(), _probe_camera(), Screen & webcam capture for ALFRED vision with OS window context grounding.… (+9 more)

### Community 47 - "TestProtocolEngine"
Cohesion: 0.11
Nodes (8): Verify that a tool failure halts subsequent steps immediately., Verify voice trigger word resolution (e.g. 'FCC CLAUDE')., Verify dynamic workflow creation with confirmation banner., Verify protocol_engine TOOL action handler dispatching., Verification Requirement: Define test_protocol in protocols.yaml that opens…, Verify variable interpolation into strings, lists, and dicts., Verify that if any step is blocked by path restrictions, the engine aborts…, TestProtocolEngine

### Community 48 - "qcol"
Cohesion: 0.14
Nodes (7): QColor, QPixmap, _DropCanvas, _file_category(), _fmt_size(), qcol(), Pre-render the static grid-dot background into a transparent pixmap so…

### Community 49 - "spotify_control.py"
Cohesion: 0.05
Nodes (42): authorize_user(), _get_base_dir(), get_devices(), get_spotify_client(), manage_queue(), _OAuthCallbackHandler, Any, Path (+34 more)

### Community 50 - "server.py"
Cohesion: 0.11
Nodes (17): base64, index(), _ensure_certs(), _local_ip(), _make_uploads_dir(), Path, dashboard/server.py — ALFRED Local HTTP Dashboard Plain HTTP on port 8000 (no…, Return the best LAN-facing IPv4 address, no internet required. (+9 more)

### Community 51 - "CustomizeOverlay"
Cohesion: 0.11
Nodes (8): QPointF, QRectF, CustomizeOverlay, HueWheel, Circular colour picker. The user drags the handle (small white circle) around…, Floating glassmorphic overlay for configuring Assistant Persona, Commander…, Highlight the selected voice pill; dim the rest., Updates the selected colour; hex box + wheel stay in sync, theme is live-…

### Community 52 - "computer_settings"
Cohesion: 0.12
Nodes (16): brightness_get(), brightness_set(), computer_settings(), dark_mode(), press_key(), Current brightness 0-100, or None where it cannot be read., Set brightness to an absolute percentage. Only used to restore a value captured…, Current master volume 0-100, or None if this platform will not say. Undo needs… (+8 more)

### Community 53 - "unduck_media_apps"
Cohesion: 0.24
Nodes (7): Restore ducked media applications to their exact original volume levels. :param…, unduck_media_apps(), _pcm_level(), _pcm_visemes(), Stop JARVIS mid-speech: drain queued audio and open mic immediately., Map a block of int16 PCM samples to a 0.0–1.0 loudness level for the HUD…, Slice a PCM block into (level, openness, width) frames, one per 20 ms. Returns…

### Community 54 - "RemoteKeyOverlay"
Cohesion: 0.24
Nodes (4): Floating overlay — QR code for instant phone pairing + manual key fallback., Call from any thread when a phone successfully connects., RemoteKeyOverlay, _lbl()

### Community 55 - "._receive_audio"
Cohesion: 0.20
Nodes (6): FunctionResponse, _clean_transcript(), _is_repeat_chunk(), _run_tool_bounded(), Send a captured frame immediately after its tool response. The frame is already…, True if this transcript chunk has already been seen this turn. Guards against…

### Community 56 - "._build_app"
Cohesion: 0.15
Nodes (14): action_ep(), audio_ws(), _auth(), clear_chat_ep(), command(), download_file(), list_files(), phone_audio_ws() (+6 more)

### Community 57 - "sys"
Cohesion: 0.17
Nodes (12): _auto_detect_type(), _config_dir(), intel_notes(), _load_notes(), Path, actions/intel_notes.py — Dedicated Intel & Notes Terminal Action. Provides a…, Action handler called by Gemini / action_loader., _save_notes() (+4 more)

### Community 58 - "json"
Cohesion: 0.21
Nodes (11): json, _load_events(), Calendar Sync Plugin for ALFRED Mark-LIV. Tracks agenda, meetings,…, Execute calendar action., run(), _save_events(), Focus Protocol Plugin for ALFRED Mark-LIV. Manages deep work intervals,…, Execute focus protocol actions. (+3 more)

### Community 59 - "time"
Cohesion: 0.12
Nodes (16): Tactical Audio Core Control Action for ALFRED. Controls the tactical HUD's…, asyncio, core/cache.py — Centralized Caching Layer for ALFRED Mark-II. Provides high-…, Push-to-talk — hold a key, speak, release. Why this exists ---------------…, functools, hashlib, logging, math (+8 more)

### Community 60 - "LocalLLMManager"
Cohesion: 0.20
Nodes (7): LocalLLMManager, Handle tool calls by executing them and getting final response., Manages local LLM interactions., Set system prompt and available tools., Add message to conversation history., Clear conversation history., Generate response from local LLM.

### Community 61 - "TestBackgroundWorkerPool"
Cohesion: 0.12
Nodes (7): Verify that calling interrupt() sets halt event, immediately stops active…, Verify that _safe_background_announce waits until ALFRED finishes speaking…, Verify DashboardServer tracks background tasks and exposes them via endpoint., Verify queue_background_task is registered in TOOL_DECLARATIONS., Verify that queue_background_task returns immediately (sub-millisecond), and…, Dispatch a mock task and verify voice PTT interaction continues with sub-second…, TestBackgroundWorkerPool

### Community 62 - "ScreenCapturePayload"
Cohesion: 0.20
Nodes (4): Hybrid return payload for screen captures. - Behaves as a 3-tuple `(img_bytes,…, ScreenCapturePayload, _do_stream(), tuple

### Community 63 - "LocalSTTManager"
Cohesion: 0.05
Nodes (27): LocalSTTManager, audio_callback_wrapper(), Local Speech-to-Text wrappers for MARK XL. Provides unified interface for…, Process audio bytes for transcription based on engine type., Cancel any pending debounce timer, thread-safe., Reset the FINISH_MS countdown from zero., Timer callback: commit the accumulated sentence to the queue., Immediately commit whatever is in the buffer (+ optional extra word). (+19 more)

### Community 65 - "ui.py"
Cohesion: 0.13
Nodes (19): Action to show an image popup overlay., Update App Icon Action for ALFRED Mark-LIV. Switches the application window,…, Updates the main application icon and taskbar badge in realtime., update_app_icon(), core_avatar, Save the chosen app icon setting to config., save_app_icon(), pathlib (+11 more)

### Community 66 - "LocalTTSManager"
Cohesion: 0.11
Nodes (12): create_local_stt_engine(), Factory function to create a local STT manager., create_local_tts_engine(), LocalTTSManager, Flush any remaining text in buffer., Main loop for processing text queue and speaking., Factory function to create a local TTS manager., Manages local text-to-speech synthesis with streaming capabilities. (+4 more)

### Community 67 - "ALFRED — MARK-IV (Wayne Protocol Edition)"
Cohesion: 0.12
Nodes (15): 11. High-Performance Memory & Conversational Briefing Customizer, 12. Real-Time Insignia & Chassis Hot-Swapper, 13. Protocol Engine & Multi-Step Macro Playbooks (`config/protocols.yaml`), 14. Local Hybrid Visual Grounding (RapidOCR + ONNX + Gemini Fallback), 15. Process-Level Audio Ducking & Background Concurrency, 17. System Architecture & File Structure, 19. Configuration Reference (`config/api_keys.json`), 20. Knowledge Graph (`graphify`) (+7 more)

### Community 68 - "_SysMetrics"
Cohesion: 0.16
Nodes (6): Thread-safe speech channel for plugins: lets a plugin ask JARVIS to say…, Called from Qt main thread when user presses Remote Control., 1. What's New: Recent Enhancements, Bug Fixes & Stability Updates, _nvml_gpu_windows(), Return NVIDIA GPU utilisation % using nvml.dll directly — zero subprocess., _SysMetrics

### Community 69 - "memory_manager.py"
Cohesion: 0.10
Nodes (29): Update Daily Briefing Preferences Action for ALFRED Mark-LIV. Permanently…, _all_entries(), all_entries_for_ui(), _empty_memory(), _entry_value(), forget(), get_base_dir(), load_memory() (+21 more)

### Community 70 - "audio_ducker.py"
Cohesion: 0.12
Nodes (16): _duck_linux(), duck_media_apps(), _worker(), _duck_windows(), is_ducked(), Process-level Audio Ducking for ALFRED. Automatically ducks background media…, Execute unducking on Windows via pycaw, restoring exact prior volume levels., Execute ducking on Linux via pulsectl. (+8 more)

### Community 71 - "._apply_name_update"
Cohesion: 0.15
Nodes (10): apply_ui_accent(), current_palette(), Read api_keys.json config dict. Returns {} on any error., Applies DOSSIER CRT [A-34] (#8e9bff), VECTOR CRT [WAKU] (#a8ff3e), or BATMAN…, A snapshot of the accent-linked colours currently on class C., LIVE full theme change. Replaces the old palette colours with the new ones in…, Live preview — paints the whole interface the new colour (does NOT write to…, Update all name/theme-dependent UI elements and persist to config. (+2 more)

### Community 72 - "WakeWordDetector"
Cohesion: 0.20
Nodes (4): Runs the wake model in a dedicated thread. The mic thread calls feed() with raw…, Load the model and spawn the inference thread. Returns True on success. Safe to…, Called from the mic callback (real-time thread). Must stay cheap and never…, WakeWordDetector

### Community 73 - "get_active_window_info"
Cohesion: 0.20
Nodes (10): get_active_window_context(), get_active_window_info(), _get_linux_window_info(), _get_macos_window_info(), _get_windows_window_info(), Query foreground window handle, title, and process name on Windows., Query active frontmost window on macOS via Quartz or AppleScript fallback., Query active window on Linux via xdotool or wmctrl. (+2 more)

### Community 74 - "daily_brief.py"
Cohesion: 0.13
Nodes (18): daily_brief(), _get_gmail_brief(), _get_greeting(), _get_reminders_brief(), _get_system_vitals(), Daily Brief Action for ALFRED Mark-LIV. Provides the ultimate morning and daily…, Fetch unread emails summary via gmail_manager., Check scheduled reminders in ~/.alfred/reminders or ~/.jarvis/reminders. (+10 more)

### Community 75 - "._ui_wake_toggle"
Cohesion: 0.17
Nodes (5): Load the detector once (model loads on first start). Idempotent., Called from the detector thread when 'Hey Jarvis' is heard., Auto-sleep after the configured silence window (wake-word mode only)., Enable/disable wake word from the settings UI. Returns a status token:…, Manual sleep/wake button in the UI.

### Community 76 - "datetime"
Cohesion: 0.41
Nodes (11): _base_dir(), _get_os(), Path, reminder(), _sanitise(), _schedule_linux(), _schedule_mac(), _schedule_windows() (+3 more)

### Community 77 - "LocalPipelineCoordinator"
Cohesion: 0.09
Nodes (17): LocalPipelineCoordinator, stream_callback(), Coordinates STT → LLM → TTS flow., Set callbacks for UI updates., Log message via callback or print., Set UI state via callback., Start the local pipeline., Stop the local pipeline. (+9 more)

### Community 78 - "._aes_key"
Cohesion: 0.31
Nodes (5): auto_login(), device_login_ep(), login(), _derive_key(), SHA-256(sessionKey‖salt) → 32-byte AES-256 key (microseconds, no PBKDF2 needed).

### Community 79 - "LogWidget"
Cohesion: 0.25
Nodes (3): QTextEdit, LogWidget, Cancel any in-flight typing animation, drain the queue, and clear the display.

### Community 80 - "capture_screen"
Cohesion: 0.29
Nodes (6): capture_screen(), _capture_screen(), _compress(), Captures primary or specified monitor, queries active OS window context,…, Default entry point used by main.py., Verification Requirement: Verify [WINDOW_CONTEXT] header contains VS Code and…

### Community 82 - "MemoryOverlay"
Cohesion: 0.17
Nodes (8): ConfirmBanner, _HudOverlay, MemoryOverlay, Base for the floating panels placed by hand over the HUD. They are children of…, The gate in front of an action that cannot be taken back. The old confirmation…, Everything ALFRED has stored about you, and when it learned it. Memory used to…, Take every item out of the layout and detach it from the widget tree in this…, Size the panel to its content, re-centre it, and repaint what the old size…

### Community 84 - "PushToTalk"
Cohesion: 0.20
Nodes (5): PushToTalk, Begin watching. Returns the scope actually achieved., Feed a press/release from a Qt shortcut (non-Windows, or no hook)., Calls `on_change(held: bool)` whenever the chord is pressed or released. Start…, global' once a system-wide hook is running, else 'window'.

### Community 85 - "._build_jarvis_icon"
Cohesion: 0.22
Nodes (4): Render an ALFRED tactical icon at 4× resolution and downsample for crisp…, Create a Windows .lnk shortcut WITHOUT launching PowerShell or cmd. Tries…, Resolve the user's REAL desktop directory instead of assuming ~/Desktop, which…, Create a desktop shortcut on Windows / macOS / Linux. Never opens a terminal,…

### Community 86 - "ImagePopupOverlay"
Cohesion: 0.15
Nodes (9): action(), ImagePopupOverlay, QWidget, Handle mouse move for window dragging., Handle mouse release for window dragging., Show the popup centered over the parent widget., Show an image popup overlay., Popup overlay to display an image with a dismiss button. (+1 more)

### Community 87 - "confirm.py"
Cohesion: 0.25
Nodes (10): bind(), _log(), _Pending, core/confirm.py — a confirmation the model cannot forge. THE PROBLEM WITH THE…, Called by the UI when the user presses CONFIRM or CANCEL. Runs the stored…, Wire this module to the HUD. Called once from main.py at startup., Park an irreversible action behind the on-screen gate. Returns the sentence the…, request() (+2 more)

### Community 88 - "test_cache.py"
Cohesion: 0.22
Nodes (10): _get_live_weather(), Fetch live weather conditions without opening an external browser., Permanently saves daily briefing preferences into long-term memory., update_daily_briefing(), get_cache(), Returns the centralized cache client singleton., patch, tests/test_cache.py — Comprehensive Test Suite for CentralizedCache. Tests: -… (+2 more)

### Community 89 - "is_heavenly_restricted"
Cohesion: 0.22
Nodes (7): _normalize(), open_app(), is_heavenly_restricted(), Any, Check if any argument references the restricted Personal-Assistant directory., _is_heavenly_restricted(), Check if any argument references the restricted Personal-Assistant directory.

### Community 90 - "TestMemoryTrimBenchmark"
Cohesion: 0.29
Nodes (4): Measures execution time for 50,000 mock records. Under the old O(N^2)…, Preserves all items when memory is already below limit., Handles empty memory structure gracefully., TestMemoryTrimBenchmark

### Community 91 - ".request_reconnect"
Cohesion: 0.33
Nodes (3): Thread-safe: ask the run loop to tear down and rebuild the Live session. Called…, Voice picker applied. The voice is baked into the session at connect time, so a…, Microphone or speaker changed. Both streams are opened inside the session…

### Community 92 - "_detect_action"
Cohesion: 0.40
Nodes (5): _detect_action(), _normalise(), Resolve a free-text description to an action name, locally. Returns {"action":…, What to tell the model when nothing matched. Names real actions so its retry…, _suggest()

### Community 93 - "PluginManagerOverlay"
Cohesion: 0.43
Nodes (3): QPushButton, PluginManagerOverlay, Floating overlay — lists discovered plugins with per-plugin ON/OFF toggles.

### Community 94 - "format_visual_payload"
Cohesion: 0.40
Nodes (3): format_visual_payload(), Prepares the visual frame payload dictionary for the Gemini Live API…, Verifies metadata block is prepended directly to the visual frame payload.

### Community 95 - "._apply_ptt_shortcut"
Cohesion: 0.29
Nodes (5): qt_sequence(), The same chord as a QKeySequence string., _press(), Bind the chord inside the window when no global hook is available. On macOS and…, Report a windowed press/release to whoever owns the microphone.

### Community 96 - "🎙️ 5. Master Tactical Voice Command Codex & Operational Handbook"
Cohesion: 0.20
Nodes (10): 👁️ 1. Desktop Automation, Screen & Multimodal Vision, ⚙️ 2. Operating System, Hardware Settings & Applications, ⚡ 3. Compound Protocols & Workflow Macros, 🧠 4. Memory, History & Universal Reversibility, 📰 5. Intelligence, Briefings, News & Weather, 🎙️ 5. Master Tactical Voice Command Codex & Operational Handbook, 📱 6. Quantum Mobile Remote & Web Telemetry Uplink, 🎧 7. Spotify AI Agent & Music Streaming (+2 more)

### Community 97 - "._build_system_instruction"
Cohesion: 0.17
Nodes (10): Build a context snapshot for Gemini. Rotates through three focus areas so…, _describe_limits(), _describe_tools(), _load_system_prompt(), One line per capability, straight from the live tool declarations. Derived…, The other half of self-knowledge: what is out of reach, and why. Derived from…, Fill {tokens} in the prompt template. A plain replace rather than str.format:…, _render_prompt() (+2 more)

### Community 98 - "TestScreenProcessorWindowContext"
Cohesion: 0.18
Nodes (7): format_window_context(), Format the standard metadata block: [WINDOW_CONTEXT] App: <Name> | Title:…, Verifies system falls back to 'App: Unknown' without raising exceptions., Verifies that active window query resolves in < 15ms and adheres to schema., Verifies exact string formatting requirements., Verifies capture_screen() returns valid compressed image and window context., TestScreenProcessorWindowContext

### Community 99 - "Daily Brief Protocol"
Cohesion: 0.50
Nodes (3): Daily Brief Protocol, Purpose, Rules

### Community 100 - "Email Handling Rules"
Cohesion: 0.50
Nodes (3): Email Handling Rules, Purpose, Rules

### Community 101 - "Executive Assistant Persona & Behavioral Standards"
Cohesion: 0.50
Nodes (3): Core Operational Rules, Executive Assistant Persona & Behavioral Standards, Persona & Demeanor

### Community 102 - "Detailed Step-by-Step Guide: How to Switch to a Local API"
Cohesion: 0.22
Nodes (9): 2. 100% Local & Air-Gapped Offline Execution: Switching from Gemini to Local API, Configuration Template for LM Studio / vLLM (OpenAI-Compatible):, Configuration Template for Ollama:, Configuration Template for OpenRouter API (Frontier Multi-Model Gateway):, Detailed Step-by-Step Guide: How to Switch to a Local API, Gemini Live API vs. Local Offline API Comparison, Step 2: Configure ALFRED's Target Backend in `config/api_keys.json`, Step 3: Launch ALFRED & Verify Connection (+1 more)

### Community 103 - "/email-triage Workflow"
Cohesion: 0.50
Nodes (3): /email-triage Workflow, Objective, Steps

### Community 104 - "_template.py"
Cohesion: 0.50
Nodes (3): Drop-in ALFRED plugin template. Copy this file, rename it (no leading…, parameters: dict of the args Gemini extracted, matching PLUGIN['parameters'].…, run()

### Community 105 - "8. Spotify AI Agent: Dual-Tier Web API & Native Playback Architecture"
Cohesion: 0.22
Nodes (9): 8. Spotify AI Agent: Dual-Tier Web API & Native Playback Architecture, Dual-Tier Control Architecture, Elimination of the Toggle Inversion Bug, High-Performance Client & Anti-Feedback Architecture, Key Capabilities & Default Music Routing, Spotify API & OAuth 2.0 Setup Guide, Step 1: Create a Spotify Developer Application, Step 2: Add Credentials to `config/api_keys.json` (+1 more)

### Community 106 - "_get_base_dir"
Cohesion: 0.67
Nodes (3): _get_api_key(), _get_base_dir(), Path

### Community 107 - "🎭 3. Example & Fun Tactical Commands ("Wayne Protocol" in Action)"
Cohesion: 0.40
Nodes (5): 🎭 3. Example & Fun Tactical Commands ("Wayne Protocol" in Action), 🎵 Ambience, Scores & Entertainment, 🎩 Distinguished Butler & Persona Banter, 🛡️ Insignia & Batcave Customization, 👁️ Tactical Vision & Screen Grounding

### Community 110 - "._decrypt"
Cohesion: 0.50
Nodes (3): ws_ep(), _decrypt_cbc(), Decrypt base64(IV[16] ‖ ciphertext) with AES-256-CBC + PKCS7.

### Community 111 - "_ensure_network_access"
Cohesion: 0.25
Nodes (3): _ensure_network_access(), Cross-platform, best-effort: open port in the OS firewall for LAN access. Runs…, Second HTTPS server on PORT+1 sharing the same app and in-memory state. Chrome…

### Community 124 - "TestAudioDucker"
Cohesion: 0.29
Nodes (4): patch, Verify that duck_media_apps lowers target media processes by 70% (0.3 factor),…, Verify Linux pulsectl ducking fallback logic., TestAudioDucker

### Community 128 - "get_push_to_talk_enabled"
Cohesion: 0.29
Nodes (5): chord_label(), Human-readable name of the chord, for the UI and the logs., get_push_to_talk_enabled(), Hold-a-key-to-speak. When on, the mic is closed unless the chord is held., Repaint the push-to-talk row from the saved setting.

### Community 129 - "._listen_audio"
Cohesion: 0.40
Nodes (3): callback(), _open_mic(), True while the speakers may still be finishing our last sentence.

### Community 132 - "main.py"
Cohesion: 0.08
Nodes (23): ProactiveEngine 2.0 — context-aware, time-aware, non-repetitive background…, install_and_download(), is_installed(), is_ready(), True if the openwakeword package is importable (no model check)., True if openwakeword is installed AND its model files are present on disk. This…, One-click setup for the UI button: pip-install openwakeword if missing, then…, gc (+15 more)

### Community 135 - "background_monitor.py"
Cohesion: 0.33
Nodes (11): add_monitor(), check_all(), _is_blocked(), list_monitors(), _load(), BackgroundMonitor — user-configured topic watching. Checks DDG news once per…, Run all pending topic checks (once per day per topic). Returns a list of…, remove_monitor() (+3 more)

### Community 140 - "._toggle_sentry_mode"
Cohesion: 0.33
Nodes (3): Toggle continuous visual context (camera stream) monitoring., Thread-safe: start live camera feed in the full HUD area., Thread-safe: stop the live camera feed.

### Community 144 - "audio_core"
Cohesion: 0.50
Nodes (4): audio_core(), Any, Main handler for the Audio Core control action., 7. Dual-Mode Tactical Audio Matrix & Background Sound Engine

### Community 146 - "Step 1: Install & Set Up Your Preferred Local LLM Server"
Cohesion: 0.50
Nodes (4): Option A: Ollama (Recommended — Simplest Setup), Option B: LM Studio (Recommended for GUI Users), Option C: vLLM or llama.cpp (High-Throughput / Linux Servers), Step 1: Install & Set Up Your Preferred Local LLM Server

### Community 148 - "18. Quick Start & Installation"
Cohesion: 0.67
Nodes (3): 18. Quick Start & Installation, 1. Prerequisites, 2. Setup & Execution

## Knowledge Gaps
- **56 isolated node(s):** `Purpose`, `Rules`, `Purpose`, `Rules`, `Persona & Demeanor` (+51 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1100 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **28 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MainWindow` connect `MainWindow` to `get_push_to_talk_enabled`, `ui.py`, `._apply_name_update`, `._build_right_panel`, `QWidget`, `._toggle_sentry_mode`, `.__init__`, `qcol`, `setter`, `._build_jarvis_icon`, `config_manager.py`, `.closeEvent`, `.__init__`, `.clear_chat`, `tech_font`, `._apply_ptt_shortcut`?**
  _High betweenness centrality (0.081) - this node is a cross-community bridge._
- **Why does `JarvisLive` connect `JarvisLive` to `._listen_audio`, `main.py`, `system_monitor.py`, `JarvisUI`, `EchoGuard`, `_tlog`, `.run`, `.__init__`, `VisemeStream`, `unduck_media_apps`, `._receive_audio`, `time`, `TestBackgroundWorkerPool`, `_SysMetrics`, `WakeWordDetector`, `._ui_wake_toggle`, `DashboardServer`, `PushToTalk`, `.request_reconnect`, `._build_system_instruction`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Why does `JarvisUI` connect `JarvisUI` to `ui.py`, `.__init__`, `main.py`, `._apply_name_update`, `._toggle_sentry_mode`, `.__init__`, `JarvisLive`, `setter`, `.__init__`, `._apply_ptt_shortcut`, `.clear_chat`?**
  _High betweenness centrality (0.059) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `JarvisLive` (e.g. with `ProactiveEngine` and `SystemMonitor`) actually correct?**
  _`JarvisLive` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Purpose`, `Rules`, `Purpose` to the rest of the system?**
  _56 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `game_updater.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06190476190476191 - nodes in this community are weakly interconnected._
- **Should `file_controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06690140845070422 - nodes in this community are weakly interconnected._