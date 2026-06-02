#!/usr/bin/env python3
"""
WordForge — Word + Symbol + Number Generator
Phillip's Custom Tool | Built with tkinter

GitHub: https://github.com/NyetNighy/WordForge
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import random
import string
import os

# ──────────────────────────────────────────────
# WORD LISTS
# ──────────────────────────────────────────────

ADJECTIVES = [
    # 3-9 chars
    "dark", "light", "swift", "bold", "grim", "soft", "loud", "wild", "tame", "pure",
    "cold", "warm", "fast", "slow", "deep", "vast", "high", "low", "new", "old",
    "cool", "flat", "sharp", "pale", "gold", "blue", "grey", "rose", "iron", "void",
    "zero", "flux", "hex", "neo", "retro", "viral", "sonic", "nova", "apex", "core",
    "echo", "grim", "haze", "icon", "jax", "kira", "lynx", "mesh", "node", "onyx",
    "prim", "quad", "rush", "sync", "titan", "ultra", "volt", "warp", "xeno", "yaku",
    "zeal", "arc", "blaze", "byte", "cipher", "daemon", "enigma", "frost", "ghost",
    "hybrid", "index", "jet", "kraken", "laser", "mystic", "nexus", "orbit", "pixel",
    "quark", "raven", "storm", "tech", "venom", "wolf", "yonder", "zenith", "alpha",
    "beta", "gamma", "delta", "omega",
    # 10-16 chars
    "crystalline", "nebulous", "shadowfax", "platinum", "cerulean", "obsidian",
    "emerald", "spectrum", "velocity", "momentum", "catalyst", "paradox", "ironclad",
    "stormborn", "eclipse", "thunder", "midnight", "daybreak", "wilderness", "nightfall",
    "quickstep", "brightest", "darkness", "frozen", "infinite", "labyrinth", "cascade",
    "labyrinth", "fortress", "absolute", "titanium", "radiant", "spectral", "phantom",
    "wraithborne", "chronicle", "vanguard", "stronghold", "warlord", "sentinel",
    "lightning", "aftermath", "magnetic", "clockwise", "hyperdrive", "nightshade"
]

NOUNS = [
    # 3-9 chars
    "hawk", "wolf", "fox", "bear", "crow", "lion", "viper", "phoenix", "blade",
    "chain", "core", "drift", "edge", "fire", "gear", "helm", "iron", "jack", "king",
    "link", "mask", "node", "path", "reign", "shell", "tank", "unit", "vein", "wave",
    "zone", "arc", "bay", "deck", "fist", "gate", "hold", "isle", "jade", "knot",
    "loop", "mark", "neon", "prism", "rift", "soul", "trap", "vault", "ward", "yell",
    "zero", "bolt", "claw", "dust", "grid", "hack", "key", "lava", "opus", "peak",
    "rust", "skull", "tide", "wisp", "yew", "atom", "data", "end", "fork", "kilo",
    "logic", "macro", "nexus", "prime", "quest", "realm", "shade", "trace", "vibe",
    # 10-16 chars
    "laboratory", "fortress", "citadel", "sentinel", "vanguard", "stormfront",
    "blacksmith", "warlord", "shadowbox", "pandemonium", "catalyst", "labyrinth",
    "monolith", "bastion", "harbinger", "sovereign", "executioner", "nightmare",
    "chronicle", "anomaly", "paradox", "titanfall", "phantom", "wraith", "spectre",
    "avenger", "guardian", "champion", "commander", "destroyer", "oblivion",
    "silhouette", "overlord", "underlord", "hellfire", "frostbite", "earthquake",
    "thunderbolt", "lightning", "shadowrealm", "ironclad", "stormbringer", "wraithborne"
]

VERBS = [
    # 3-9 chars
    "blaze", "crash", "drift", "echo", "flip", "glitch", "hack", "jack", "kick",
    "launch", "morph", "null", "orbit", "pulse", "query", "rise", "sync", "trace",
    "unlock", "warp", "dash", "flash", "grind", "jolt", "link", "max", "output",
    "push", "shift", "twist", "void", "wipe", "yank", "zoom", "burn", "forge",
    "break", "spark", "surge", "bolt", "claw", "crush", "fuse", "glow", "rush",
    # 10-16 chars
    "accelerate", "overclock", "synchronize", "catalyze", "randomize", "synthesize",
    "initialize", "finalize", "maximize", "optimize", "crystallize", "annihilate",
    "disintegrate", "disassemble", "reprogram", "overcharge", "undermine", "shortcut",
    "transcend", "dominate", "calibrate", "incinerate", "obliterate", "calcinate"
]

TECH = [
    # 3-9 chars
    "api", "bash", "cache", "daemon", "encode", "firewall", "gateway", "hash",
    "input", "java", "kernel", "linux", "macro", "node", "openssl", "proxy",
    "query", "root", "socket", "token", "unix", "virus", "wget", "xml", "yaml",
    "zip", "admin", "backup", "debug", "exec", "grep", "host", "json", "kube",
    "mysql", "nginx", "redis", "sql", "tcp", "url", "vpn", "www", "bios", "cdn",
    "cms", "cpu", "dhcp", "dns", "ftp", "gpu", "hdd", "i/o", "lan", "mac", "nat",
    "os/", "ram", "san", "ssd", "tcp", "udp", "vlan", "wan", "xss", "xml",
    # 10-16 chars
    "algorithm", "bandwidth", "bitstream", "blueprint", "bootstrap", "broadband",
    "bytecode", "checksum", "compiler", "compress", "darknet", "database",
    "decryption", "developer", "download", "electron", "ethernet", "exception",
    "firewall", "framework", "fullstack", "gateway", "hardware", "hostname",
    "instance", "interface", "keyboard", "localhost", "mainframe", "malware",
    "metadata", "microchip", "modem", "motherboard", "network", "override",
    "partition", "password", "platform", "process", "protocol", "proxy",
    "redirect", "registry", "runtime", "schedule", "script Kiddie", "security",
    "server", "snapshot", "software", "sourcecode", "storage", "subnet",
    "syntax", "terminal", "transmit", "Trojan", "username", "variable",
    "virtualize", "wireless", "workstation", "zeroday", "rootkit", "keylogger"
]

MYTH = [
    # 3-9 chars
    "ares", "athena", "atlas", "bane", "chaos", "charon", "crypto", "deimos",
    "eos", "eris", "fury", "gaia", "griffin", "hades", "hermes", "hydra", "iris",
    "juno", "jupiter", "loki", "medusa", "nemesis", "oracle", "pluto", "poseidon",
    "pyro", "ra", "rune", "scylla", "sigma", "terra", "venom", "vortex", "wrath",
    "xenon", "yami", "zeus", "apollo", "aztec", "brute", "dagon", "ember", "fable",
    "gothic", "helix", "inferno", "justice", "kronos", "midas", "nemo", "nyx",
    # 10-16 chars
    "ares", "athena", "atlas", "bane", "chaos", "charon", "crypto", "deimos",
    "eos", "eris", "fury", "gaia", "griffin", "hades", "hephaestus", "hermes",
    "hydra", "iris", "juno", "jupiter", "kronos", "loki", "medusa", "nemesis",
    "nova", "onyx", "oracle", "phoenix", "pluto", "poseidon", "pyro", "ra",
    "rune", "scylla", "sigma", "terra", "ultra", "venom", "vortex", "wrath",
    "xenon", "yami", "zeus", "apollo", "aztec", "brute", "chaos", "dagon",
    "ember", "fable", "gothic", "helix", "inferno", "justice", "morpheus",
    "persephone", "thanatos", "cerberus", "chimera", "minotaur", "basilisk",
    "leviathan", "behemoth", "seraphim", "cherubim", "archangel", "demon",
    "hellfire", "infernal", "celestial", "ethereal", "obsidian", "immortal",
    "shadowbane", "voidwalker", "stormbringer", "lightbringer", "doombringer"
]

GAMING = [
    # 3-9 chars
    "ace", "boss", "camp", "dash", "elite", "frag", "gank", "hp", "icon", "jack",
    "kills", "lobby", "mp", "nexus", "ops", "pawn", "raid", "spawn", "tank", "ultra",
    "victory", "wipe", "xp", "zerg", "cloak", "doom", "ender", "forge", "glitch",
    "hardcore", "infuse", "jump", "knight", "legend", "mage", "ninja", "omega",
    "pixel", "quarry", "roam", "shadow", "turbo", "unity", "warden", "yordle",
    "zealot", "assassin", "barbarian", "berserker", "conjurer", "druid", "enchanter",
    "gladiator", "hunter", "illusionist", "jouster", "kinetic", "lancer", "marksman",
    # 10-16 chars
    "battlefield", "battle royale", "blackops", "bloodbath", "campaign",
    "checkpoint", "clutch", "cooldown", "combobreaker", "dropzone", "endgame",
    "headshot", "highscore", "hitmarker", "homescreen", "killstreak", "laststand",
    "loadout", "multiplayer", "noob", "one-shot", "overtime", "pixelwar",
    "playthrough", "powerup", "ragequit", "respawn", "run", "scoreboard",
    "secondwind", "skeleton", "solo", "speedrun", "summon", "summit", "tactical",
    "teamwork", "thirdperson", "thriller", "tournament", "viewport", "wave",
    "zone", "bossfight", "crowd control", "critical hit", "double xp",
    "elimination", "final boss", "game over", "health pack", "inventory",
    "kill feed", "last breath", "match point", "respawn", "score"
]

CUSTOM_WORDS = []

ALL_WORDS = ADJECTIVES + NOUNS + VERBS + TECH + MYTH + GAMING

# ──────────────────────────────────────────────
# SYMBOLS
# ──────────────────────────────────────────────

SYMBOL_SETS = {
    "All Symbols (!@#$%^&*)": "!@#$%^&*",
    "Classic (!@#$%)": "!@#$%",
    "Safe (~`#@!)": "~`#@!",
    "Math (#%^)": "#%^",
    "Dash (_-:)": "_-:",
    "Brackets ([{]}])": "[{]}])",
    "Pipes & Slashes (|/\\)": "|/\\",
    "Dots & Commas (.,;)": ".,;",
    "Custom": "CUSTOM"
}

# ──────────────────────────────────────────────
# THEME
# ──────────────────────────────────────────────

BG = "#0d1117"
FG = "#c9d1d9"
ACCENT = "#58a6ff"
GREEN = "#3fb950"
ORANGE = "#d29922"
PURPLE = "#bc8cff"
RED = "#f85149"
ENTRY_BG = "#161b22"
ENTRY_FG = "#f0f6fc"

# ──────────────────────────────────────────────
# APP
# ──────────────────────────────────────────────

class WordForgeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WordForge v2.0")
        self.root.configure(bg=BG)
        self.root.geometry("940x820")
        self.root.resizable(True, True)

        self.symbol_choice = tk.StringVar(value="All Symbols (!@#$%^&*)")
        self.custom_symbol = tk.StringVar(value="!@#$%&*")
        self.number_from = tk.StringVar(value="01")
        self.number_to = tk.StringVar(value="99")
        self.word_len_min = tk.IntVar(value=3)
        self.word_len_max = tk.IntVar(value=10)
        self.word_category = tk.StringVar(value="All Words")
        self.capitalize = tk.BooleanVar(value=False)
        self.custom_words_var = tk.StringVar(value="")
        self.results = []

        self._build_header()
        self._build_controls()
        self._build_results()

    def _build_header(self):
        tk.Label(
            self.root, text="⚡ WordForge v2.0 ⚡",
            font=("Consolas", 22, "bold"),
            bg=BG, fg=ACCENT
        ).pack(pady=(16, 4))

        tk.Label(
            self.root,
            text="Word + Symbol + Number → Password List Generator",
            font=("Consolas", 10),
            bg=BG, fg="#8b949e"
        ).pack(pady=(0, 10))

    def _section_label(self, text):
        tk.Label(
            self.root, text=text,
            font=("Consolas", 10, "bold"),
            bg=BG, fg=ACCENT, anchor="w"
        ).pack(fill="x", padx=22, pady=(12, 4))

    def _build_controls(self):
        frame = tk.Frame(self.root, bg=BG)
        frame.pack(fill="x", padx=22, pady=(0, 8))

        # ── Row 1: Category + Word Length ──
        self._section_label("📖 WORD CATEGORY")
        row1 = tk.Frame(frame, bg=BG)
        row1.pack(fill="x")

        cats = ["All Words", "Adjectives", "Nouns", "Verbs", "Tech", "Myth", "Gaming", "Custom Words"]
        cat_menu = tk.OptionMenu(
            row1, self.word_category,
            *cats, command=self._on_category_change
        )
        cat_menu.config(
            bg=ENTRY_BG, fg=ENTRY_FG, activebackground=ACCENT,
            font=("Consolas", 9), width=18,
            highlightthickness=0, borderwidth=0
        )
        cat_menu["menu"].config(bg=ENTRY_BG, fg=ENTRY_FG, font=("Consolas", 9))
        cat_menu.pack(side="left", padx=(0, 14))

        tk.Label(row1, text="Word Length:", bg=BG, fg=FG, font=("Consolas", 9)).pack(side="left", padx=(10, 4))

        len_frame = tk.Frame(row1, bg=BG)
        len_frame.pack(side="left")

        tk.Label(len_frame, text="Min", bg=BG, fg="#8b949e", font=("Consolas", 8)).grid(row=0, column=0, padx=(0, 4))
        tk.Label(len_frame, text="Max", bg=BG, fg="#8b949e", font=("Consolas", 8)).grid(row=0, column=1, padx=(8, 0))

        self.len_min_spin = tk.Spinbox(
            len_frame, from_=2, to=16, width=5,
            textvariable=self.word_len_min,
            bg=ENTRY_BG, fg=ENTRY_FG, font=("Consolas", 9),
            highlightthickness=0, borderwidth=0, buttonbackground=BG
        )
        self.len_min_spin.grid(row=1, column=0, padx=(0, 8))

        tk.Label(len_frame, text="→", bg=BG, fg="#8b949e", font=("Consolas", 9)).grid(row=1, column=1)

        self.len_max_spin = tk.Spinbox(
            len_frame, from_=2, to=20, width=5,
            textvariable=self.word_len_max,
            bg=ENTRY_BG, fg=ENTRY_FG, font=("Consolas", 9),
            highlightthickness=0, borderwidth=0, buttonbackground=BG
        )
        self.len_max_spin.grid(row=1, column=2, padx=(8, 0))

        # ── Row 2: Symbol + Number Range ──
        self._section_label("🔣 SYMBOL")
        row2 = tk.Frame(frame, bg=BG)
        row2.pack(fill="x", pady=(4, 0))

        sym_menu = tk.OptionMenu(
            row2, self.symbol_choice,
            *SYMBOL_SETS.keys(),
            command=self._on_symbol_change
        )
        sym_menu.config(
            bg=ENTRY_BG, fg=ENTRY_FG, activebackground=ACCENT,
            font=("Consolas", 9), width=22,
            highlightthickness=0, borderwidth=0
        )
        sym_menu["menu"].config(bg=ENTRY_BG, fg=ENTRY_FG, font=("Consolas", 9))
        sym_menu.pack(side="left", padx=(0, 10))

        self.custom_entry = tk.Entry(
            row2, textvariable=self.custom_symbol,
            bg=ENTRY_BG, fg=ENTRY_FG, font=("Consolas", 9),
            width=14, insertbackground=ACCENT,
            highlightbackground=ACCENT, highlightthickness=1
        )
        self.custom_entry.pack(side="left", padx=(0, 20))

        tk.Label(row2, text="Number:", bg=BG, fg=FG, font=("Consolas", 9)).pack(side="left", padx=(0, 4))
        self.num_from_spin = tk.Spinbox(
            row2, from_=0, to=98, width=5,
            textvariable=self.number_from,
            bg=ENTRY_BG, fg=ENTRY_FG, font=("Consolas", 9),
            highlightthickness=0, borderwidth=0, buttonbackground=BG, format="%02.0f"
        )
        self.num_from_spin.pack(side="left", padx=(4, 6))
        tk.Label(row2, text="→", bg=BG, fg="#8b949e", font=("Consolas", 10)).pack(side="left")
        self.num_to_spin = tk.Spinbox(
            row2, from_=1, to=99, width=5,
            textvariable=self.number_to,
            bg=ENTRY_BG, fg=ENTRY_FG, font=("Consolas", 9),
            highlightthickness=0, borderwidth=0, buttonbackground=BG, format="%02.0f"
        )
        self.num_to_spin.pack(side="left", padx=(6, 20))

        self.cap_check = tk.Checkbutton(
            row2, text="🔠 Capitalise first letter",
            variable=self.capitalize,
            bg=BG, fg=ACCENT, activebackground=BG, activeforeground=ACCENT,
            selectcolor=ENTRY_BG, font=("Consolas", 9, "bold"),
            highlightthickness=0
        )
        self.cap_check.pack(side="left")

        # ── Row 3: Custom Words + Load File ──
        self._section_label("📝 CUSTOM WORD LIST (optional)")
        row3 = tk.Frame(frame, bg=BG)
        row3.pack(fill="x", pady=(4, 0))

        self.custom_words_entry = tk.Entry(
            row3, textvariable=self.custom_words_var,
            bg=ENTRY_BG, fg=ENTRY_FG, font=("Consolas", 8),
            insertbackground=ACCENT, highlightbackground=ACCENT, highlightthickness=1,
            width=50
        )
        self.custom_words_entry.pack(side="left", padx=(0, 10))

        tk.Label(row3, text="(comma-separated words, one per line, or load from file)",
                 bg=BG, fg="#484f58", font=("Consolas", 8)).pack(side="left")

        load_btn = tk.Button(
            row3, text="📂 Load .txt",
            command=self._load_word_file,
            bg=ENTRY_BG, fg=PURPLE,
            font=("Consolas", 9, "bold"),
            activebackground=PURPLE, activeforeground="#0d1117",
            relief="flat", padx=10, pady=4,
            cursor="hand2"
        )
        load_btn.pack(side="left", padx=(8, 0))

        clear_words_btn = tk.Button(
            row3, text="✖",
            command=self._clear_custom_words,
            bg=ENTRY_BG, fg=RED,
            font=("Consolas", 9, "bold"),
            activebackground=RED, activeforeground="#0d1117",
            relief="flat", padx=8, pady=4,
            cursor="hand2"
        )
        clear_words_btn.pack(side="left", padx=(4, 0))

        # ── Generate Button ──
        btn_frame = tk.Frame(self.root, bg=BG)
        btn_frame.pack(fill="x", padx=22, pady=(14, 0))

        generate_btn = tk.Button(
            btn_frame,
            text="⚡  GENERATE 20 RESULTS",
            command=self._generate,
            bg=ACCENT, fg="#0d1117",
            font=("Consolas", 13, "bold"),
            activebackground="#79c0ff", activeforeground="#0d1117",
            relief="flat", padx=20, pady=10,
            cursor="hand2"
        )
        generate_btn.pack(fill="x", pady=(0, 4))

        tk.Label(
            btn_frame,
            text="Enter ↵ to generate  •  Tab ↹ between fields  •  Ctrl+A select all",
            font=("Consolas", 8), bg=BG, fg="#484f58"
        ).pack()

    def _build_results(self):
        self._section_label("📋 RESULTS")

        result_frame = tk.Frame(self.root, bg=BG)
        result_frame.pack(fill="both", expand=True, padx=22, pady=(4, 10))

        self.result_text = scrolledtext.ScrolledText(
            result_frame,
            bg="#0d1117", fg=GREEN,
            font=("Consolas", 11),
            insertbackground=ACCENT,
            relief="flat", padx=10, pady=10,
            highlightthickness=0, wrap="none"
        )
        self.result_text.pack(fill="both", expand=True)
        self.result_text.bind("<Control-c>", lambda e: self._copy_selection())
        self.result_text.bind("<Control-a>", lambda e: self._select_all())
        self.result_text.bind("<Return>", lambda e: self._generate())

        # Bottom action bar
        action_frame = tk.Frame(self.root, bg=BG)
        action_frame.pack(fill="x", padx=22, pady=(0, 12))

        copy_btn = tk.Button(
            action_frame, text="📋 Copy All",
            command=self._copy_all,
            bg=ENTRY_BG, fg=ACCENT,
            font=("Consolas", 10, "bold"),
            activebackground=ACCENT, activeforeground="#0d1117",
            relief="flat", padx=16, pady=6, cursor="hand2"
        )
        copy_btn.pack(side="left")

        save_btn = tk.Button(
            action_frame, text="💾 Save to File",
            command=self._save_to_file,
            bg=ENTRY_BG, fg=PURPLE,
            font=("Consolas", 10, "bold"),
            activebackground=PURPLE, activeforeground="#0d1117",
            relief="flat", padx=16, pady=6, cursor="hand2"
        )
        save_btn.pack(side="left", padx=(10, 0))

        clear_btn = tk.Button(
            action_frame, text="🗑 Clear",
            command=self._clear_results,
            bg=ENTRY_BG, fg=ORANGE,
            font=("Consolas", 10, "bold"),
            activebackground=ORANGE, activeforeground="#0d1117",
            relief="flat", padx=16, pady=6, cursor="hand2"
        )
        clear_btn.pack(side="left", padx=(10, 0))

        self.status_label = tk.Label(
            action_frame, text="Ready — configure settings and click Generate",
            font=("Consolas", 9), bg=BG, fg="#484f58", anchor="e"
        )
        self.status_label.pack(side="right", fill="x", expand=True)

    # ── Helpers ──────────────────────────────────

    def _on_category_change(self, *args):
        if self.word_category.get() == "Custom Words":
            self.custom_words_entry.focus()

    def _on_symbol_change(self, *args):
        if self.symbol_choice.get() == "Custom":
            self.custom_entry.configure(state="normal")
            self.custom_entry.focus()
        else:
            self.custom_entry.configure(state="readonly")

    def _load_word_file(self):
        path = filedialog.askopenfilename(
            title="Load Custom Word List",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            initialdir=os.path.expanduser("~")
        )
        if path:
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    raw = f.read()
                # Split by newlines or commas, filter empty
                words = [w.strip().lower() for w in raw.replace(",", "\n").splitlines() if w.strip()]
                if not words:
                    messagebox.showwarning("Empty File", "No words found in file.")
                    return
                self.custom_words_var.set(f"[{len(words)} words loaded from {os.path.basename(path)}]")
                # Store the words directly in the app
                global CUSTOM_WORDS
                CUSTOM_WORDS = words
                self.status_label.config(text=f"Loaded {len(words)} custom words from file", fg=GREEN)
            except Exception as e:
                messagebox.showerror("Load Error", f"Could not load file:\n{e}")

    def _clear_custom_words(self):
        global CUSTOM_WORDS
        CUSTOM_WORDS = []
        self.custom_words_var.set("")
        self.status_label.config(text="Custom words cleared", fg=ORANGE)

    def _get_words(self):
        global CUSTOM_WORDS
        cat = self.word_category.get()

        if cat == "Custom Words":
            # Try from entry field first (comma-separated)
            raw = self.custom_words_var.get()
            if raw and not raw.startswith("[") and len(raw) > 2:
                CUSTOM_WORDS = [w.strip().lower() for w in raw.replace(",", "\n").splitlines() if w.strip()]
            if not CUSTOM_WORDS:
                messagebox.showwarning("No Words", "No custom words entered. Type words in the field or load a .txt file.")
                return []
            pool = CUSTOM_WORDS
        else:
            pool_map = {
                "All Words": ALL_WORDS,
                "Adjectives": ADJECTIVES,
                "Nouns": NOUNS,
                "Verbs": VERBS,
                "Tech": TECH,
                "Myth": MYTH,
                "Gaming": GAMING,
            }
            pool = pool_map.get(cat, ALL_WORDS)

        min_len = self.word_len_min.get()
        max_len = self.word_len_max.get()
        return [w for w in pool if min_len <= len(w) <= max_len]

    def _get_symbols(self):
        choice = self.symbol_choice.get()
        if choice == "Custom":
            return self.custom_symbol.get() or "!@#$%&*"
        return SYMBOL_SETS.get(choice, "!@#$%&*")

    def _generate(self):
        words = self._get_words()
        symbols = self._get_symbols()
        num_from = int(self.number_from.get())
        num_to = int(self.number_to.get())
        capitalize = self.capitalize.get()

        if not words:
            messagebox.showwarning("No Words", "No words match your length filter.\nTry increasing Min/Max word length.")
            return
        if not symbols:
            messagebox.showwarning("No Symbol", "Please enter at least one symbol character.")
            return
        if num_from > num_to:
            messagebox.showwarning("Invalid Range", "Number 'From' cannot be greater than 'To'.")
            return

        results = []
        for _ in range(20):
            word = random.choice(words)
            sym = random.choice(symbols)
            num = random.randint(num_from, min(num_to, 99))
            if capitalize:
                word = word.capitalize()
            else:
                word = word.lower()
            results.append(f"{word}{sym}{num:02d}")

        self.results = results

        self.result_text.delete("1.0", "end")
        for i, result in enumerate(results, 1):
            self.result_text.insert("end", f"  {i:02d}.  {result}\n")

        self.result_text.tag_config("sel", background=ACCENT, foreground="#0d1117")

        cap_label = "Capitalised" if capitalize else "lowercase"
        self.status_label.config(
            text=f"Generated {len(results)} results ({cap_label}) — {len(words)} words in pool | "
                 f"Symbols: {symbols} | Numbers: {num_from:02d}–{num_to:02d}",
            fg=GREEN
        )

    def _copy_selection(self):
        try:
            text = self.result_text.get("sel.first", "sel.last")
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            self.status_label.config(text="Copied to clipboard!", fg=GREEN)
        except tk.TclError:
            pass

    def _select_all(self):
        self.result_text.tag_add("sel", "1.0", "end")
        return "break"

    def _copy_all(self):
        if not self.results:
            self.status_label.config(text="Nothing to copy — generate first", fg=ORANGE)
            return
        text = "\n".join(self.results)
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.status_label.config(text=f"Copied {len(self.results)} results to clipboard!", fg=GREEN)

    def _save_to_file(self):
        if not self.results:
            self.status_label.config(text="Nothing to save — generate first", fg=ORANGE)
            return
        path = filedialog.asksaveasfilename(
            title="Save Results",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            initialdir=os.path.expanduser("~"),
            initialfile="wordforge_results.txt"
        )
        if path:
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write("# WordForge v2.0 Results\n")
                    f.write(f"# Category: {self.word_category.get()}\n")
                    f.write(f"# Word Length: {self.word_len_min.get()}–{self.word_len_max.get()}\n")
                    f.write(f"# Symbols: {self._get_symbols()}\n")
                    f.write(f"# Number Range: {self.number_from.get()}–{self.number_to.get()}\n")
                    f.write(f"# Capitalise: {self.capitalize.get()}\n")
                    f.write(f"# Generated: 20 results\n\n")
                    for i, r in enumerate(self.results, 1):
                        f.write(f"{i:02d}. {r}\n")
                self.status_label.config(text=f"Saved to {os.path.basename(path)}", fg=GREEN)
            except Exception as e:
                messagebox.showerror("Save Error", f"Could not save file:\n{e}")

    def _clear_results(self):
        self.result_text.delete("1.0", "end")
        self.results = []
        self.status_label.config(text="Cleared", fg=ORANGE)


# ──────────────────────────────────────────────
# LAUNCH
# ──────────────────────────────────────────────

if __name__ == "__main__":
    root = tk.Tk()
    app = WordForgeApp(root)
    root.mainloop()