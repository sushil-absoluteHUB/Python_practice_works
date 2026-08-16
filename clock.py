import math
import time
import datetime
import tkinter as tk
from tkinter import ttk

class Theme:
    """Color palette definition for clock themes."""
    def __init__(self, name, bg, clock_bg, ring_outer, ring_inner, 
                 hour_ticks, minute_ticks, numbers, 
                 hour_hand, min_hand, sec_hand, pivot_color, 
                 accent_color, text_color, subdial_bg):
        self.name = name
        self.bg = bg
        self.clock_bg = clock_bg
        self.ring_outer = ring_outer
        self.ring_inner = ring_inner
        self.hour_ticks = hour_ticks
        self.minute_ticks = minute_ticks
        self.numbers = numbers
        self.hour_hand = hour_hand
        self.min_hand = min_hand
        self.sec_hand = sec_hand
        self.pivot_color = pivot_color
        self.accent_color = accent_color
        self.text_color = text_color
        self.subdial_bg = subdial_bg

THEMES = {
    "Cyberpunk Neon": Theme("Cyberpunk Neon", "#0d0f18", "#131726", "#00f3ff", "#ff0055", "#00f3ff", "#4a5568", "#e2e8f0", "#ffffff", "#00f3ff", "#ff0055", "#ff0055", "#00f3ff", "#00f3ff", "#1a2035"),
    "Luxury Dark": Theme("Luxury Dark", "#121212", "#1e1e1e", "#d4af37", "#333333", "#d4af37", "#666666", "#f0f0f0", "#e0e0e0", "#ffffff", "#d4af37", "#d4af37", "#d4af37", "#d4af37", "#262626"),
    "Slate Minimal": Theme("Slate Minimal", "#1e293b", "#0f172a", "#38bdf8", "#1e293b", "#f8fafc", "#64748b", "#cbd5e1", "#f1f5f9", "#94a3b8", "#38bdf8", "#38bdf8", "#38bdf8", "#38bdf8", "#1e293b"),
    "Emerald Night": Theme("Emerald Night", "#06201b", "#0b2e27", "#10b981", "#047857", "#a7f3d0", "#065f46", "#ecfdf5", "#ffffff", "#6ee7b7", "#10b981", "#10b981", "#10b981", "#34d399", "#064e3b"),
    "Classic Pearl": Theme("Classic Pearl", "#f1f5f9", "#ffffff", "#334155", "#cbd5e1", "#0f172a", "#94a3b8", "#1e293b", "#0f172a", "#334155", "#e11d48", "#e11d48", "#2563eb", "#0f172a", "#f8fafc")
}

TIMEZONES = {
    "Local Time": None, "UTC": 0, "EST (UTC-5)": -5, "PST (UTC-8)": -8,
    "GMT (UTC+0)": 0, "CET (UTC+1)": 1, "IST (UTC+5:30)": 5.5, "JST (UTC+9)": 9, "AEST (UTC+10)": 10
}

class AnalogClockApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Premium Analog Clock")
        self.geometry("620x720")
        self.minsize(450, 520)

        self.current_theme = THEMES["Cyberpunk Neon"]
        self.smooth_sweep = tk.BooleanVar(value=True)
        self.show_digital = tk.BooleanVar(value=True)
        self.always_on_top = tk.BooleanVar(value=False)
        self.selected_timezone = tk.StringVar(value="Local Time")

        self.configure(bg=self.current_theme.bg)
        self._setup_ui()

        # Keyboard shortcuts
        self.bind("<space>", lambda e: self.smooth_sweep.set(not self.smooth_sweep.get()))
        self.bind("<t>", lambda e: self._cycle_theme())
        self.bind("<d>", lambda e: self.show_digital.set(not self.show_digital.get()))
        self.bind("<a>", lambda e: self._toggle_always_on_top())

        self._update_clock()

    def _setup_ui(self):
        # Controls Header
        self.control_frame = tk.Frame(self, bg=self.current_theme.bg, pady=10, padx=15)
        self.control_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(self.control_frame, text="Theme:", fg="#a0aec0", bg=self.current_theme.bg, font=("Segoe UI", 9, "bold")).grid(row=0, column=0, padx=5, sticky="w")
        self.theme_combo = ttk.Combobox(self.control_frame, values=list(THEMES.keys()), state="readonly", width=15)
        self.theme_combo.set(self.current_theme.name)
        self.theme_combo.bind("<<ComboboxSelected>>", self._on_theme_change)
        self.theme_combo.grid(row=0, column=1, padx=5, sticky="w")

        tk.Label(self.control_frame, text="Timezone:", fg="#a0aec0", bg=self.current_theme.bg, font=("Segoe UI", 9, "bold")).grid(row=0, column=2, padx=5, sticky="w")
        self.tz_combo = ttk.Combobox(self.control_frame, values=list(TIMEZONES.keys()), state="readonly", width=14)
        self.tz_combo.set(self.selected_timezone.get())
        self.tz_combo.bind("<<ComboboxSelected>>", lambda e: self.selected_timezone.set(self.tz_combo.get()))
        self.tz_combo.grid(row=0, column=3, padx=5, sticky="w")

        self.opts_frame = tk.Frame(self.control_frame, bg=self.current_theme.bg)
        self.opts_frame.grid(row=1, column=0, columnspan=4, pady=(8, 0), sticky="w")

        self.cb_smooth = tk.Checkbutton(self.opts_frame, text="Smooth Sweep", variable=self.smooth_sweep, bg=self.current_theme.bg, fg=self.current_theme.text_color)
        self.cb_smooth.pack(side=tk.LEFT, padx=(0, 15))

        self.cb_digital = tk.Checkbutton(self.opts_frame, text="Digital Time", variable=self.show_digital, bg=self.current_theme.bg, fg=self.current_theme.text_color)
        self.cb_digital.pack(side=tk.LEFT, padx=15)

        self.cb_top = tk.Checkbutton(self.opts_frame, text="Always on Top", variable=self.always_on_top, command=self._toggle_always_on_top, bg=self.current_theme.bg, fg=self.current_theme.text_color)
        self.cb_top.pack(side=tk.LEFT, padx=15)

        # Main Clock Canvas
        self.canvas = tk.Canvas(self, bg=self.current_theme.bg, highlightthickness=0)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Digital Info Banner
        self.info_frame = tk.Frame(self, bg=self.current_theme.bg, pady=10)
        self.info_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.digital_label = tk.Label(self.info_frame, text="00:00:00 AM", font=("Consolas", 18, "bold"), bg=self.current_theme.bg, fg=self.current_theme.text_color)
        self.digital_label.pack()

        self.date_label = tk.Label(self.info_frame, text="", font=("Segoe UI", 11), bg=self.current_theme.bg, fg="#94a3b8")
        self.date_label.pack(pady=(2, 0))

        self.hint_label = tk.Label(self.info_frame, text="Shortcuts: [Space] Sweep Mode | [T] Cycle Theme | [D] Digital Display | [A] Always on Top", font=("Segoe UI", 8), bg=self.current_theme.bg, fg="#64748b")
        self.hint_label.pack(pady=(6, 0))

    def _on_theme_change(self, event=None):
        theme_name = self.theme_combo.get()
        if theme_name in THEMES:
            self.current_theme = THEMES[theme_name]
            self.configure(bg=self.current_theme.bg)
            self.canvas.configure(bg=self.current_theme.bg)
            self.control_frame.configure(bg=self.current_theme.bg)

    def _cycle_theme(self):
        theme_names = list(THEMES.keys())
        idx = (theme_names.index(self.current_theme.name) + 1) % len(theme_names)
        self.theme_combo.set(theme_names[idx])
        self._on_theme_change()

    def _toggle_always_on_top(self):
        self.attributes("-topmost", self.always_on_top.get())

    def _get_current_time_components(self):
        tz_offset = TIMEZONES.get(self.selected_timezone.get(), None)
        if tz_offset is None:
            return datetime.datetime.now()
        else:
            utc_now = datetime.datetime.now(datetime.timezone.utc)
            return utc_now + datetime.timedelta(hours=tz_offset)

    def _update_clock(self):
        self._redraw_clock()
        self.after(16, self._update_clock)

    def _redraw_clock(self):
        self.canvas.delete("all")
        width, height = self.canvas.winfo_width(), self.canvas.winfo_height()
        if width < 50 or height < 50:
            return

        cx, cy = width / 2, height / 2
        radius = min(width, height) / 2 - 20
        theme = self.current_theme
        now = self._get_current_time_components()

        if self.show_digital.get():
            self.digital_label.pack()
            self.digital_label.configure(text=now.strftime("%I:%M:%S %p"))
        else:
            self.digital_label.pack_forget()

        self.date_label.configure(text=now.strftime("%A, %b %d, %Y"))

        # Draw outer & inner rings
        self.canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, outline=theme.ring_outer, width=5)
        r_inner = radius - 5
        self.canvas.create_oval(cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner, fill=theme.clock_bg, outline=theme.ring_inner, width=3)

        # Subdial (24h)
        sub_r, sub_cy, sub_cx = radius * 0.22, cy + radius * 0.40, cx
        self.canvas.create_oval(sub_cx - sub_r, sub_cy - sub_r, sub_cx + sub_r, sub_cy + sub_r, fill=theme.subdial_bg, outline=theme.ring_inner, width=1.5)

        # Ticks & Numbers
        for i in range(60):
            angle = math.radians(i * 6 - 90)
            r_in = radius - (24 if i % 5 == 0 else 16)
            r_out = radius - 10
            x1, y1 = cx + r_in * math.cos(angle), cy + r_in * math.sin(angle)
            x2, y2 = cx + r_out * math.cos(angle), cy + r_out * math.sin(angle)
            self.canvas.create_line(x1, y1, x2, y2, fill=theme.hour_ticks if i % 5 == 0 else theme.minute_ticks, width=3.5 if i % 5 == 0 else 1.5)

        num_radius = radius - 42
        font_size = max(10, int(radius * 0.10))
        for num in range(1, 13):
            angle = math.radians(num * 30 - 90)
            nx, ny = cx + num_radius * math.cos(angle), cy + num_radius * math.sin(angle)
            self.canvas.create_text(nx, ny, text=str(num), fill=theme.numbers, font=("Segoe UI", font_size, "bold"))

        # Hand calculations
        sec_val = (now.second + now.microsecond / 1_000_000.0) if self.smooth_sweep.get() else float(now.second)
        min_val = now.minute + sec_val / 60.0
        hour_val = (now.hour % 12) + min_val / 60.0

        sec_angle = math.radians(sec_val * 6 - 90)
        min_angle = math.radians(min_val * 6 - 90)
        hour_angle = math.radians(hour_val * 30 - 90)

        # Draw Hour, Minute, Second hands
        self.canvas.create_line(cx - radius*0.1*math.cos(hour_angle), cy - radius*0.1*math.sin(hour_angle), cx + radius*0.5*math.cos(hour_angle), cy + radius*0.5*math.sin(hour_angle), fill=theme.hour_hand, width=max(4, radius*0.035), capstyle=tk.ROUND)
        self.canvas.create_line(cx - radius*0.12*math.cos(min_angle), cy - radius*0.12*math.sin(min_angle), cx + radius*0.72*math.cos(min_angle), cy + radius*0.72*math.sin(min_angle), fill=theme.min_hand, width=max(3, radius*0.024), capstyle=tk.ROUND)
        self.canvas.create_line(cx - radius*0.2*math.cos(sec_angle), cy - radius*0.2*math.sin(sec_angle), cx + radius*0.84*math.cos(sec_angle), cy + radius*0.84*math.sin(sec_angle), fill=theme.sec_hand, width=max(1.5, radius*0.012), capstyle=tk.ROUND)

        # Pivot center
        p_r = max(5, radius * 0.04)
        self.canvas.create_oval(cx - p_r, cy - p_r, cx + p_r, cy + p_r, fill=theme.pivot_color, outline=theme.clock_bg, width=2)

if __name__ == "__main__":
    app = AnalogClockApp()
    app.mainloop()