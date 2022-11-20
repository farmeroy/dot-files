from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import extension

import os
from libqtile import hook



mod = "mod4"
terminal = "/usr/bin/kitty" 
FONTSIZE = 14
FOREGROUND = '#c6c8d1'
FONT = 'Ubuntu'

@hook.subscribe.startup_once
def picom_start():
    os.system("picom -b")

@hook.subscribe.startup_complete
def network_widget():
    os.system("nm-applet &")
    os.system("xss-lock -n /usr/lib/xsecurelock/dimmer -l --  xsecurelock &")

@lazy.function
def adjust_margins(qtile, amount):
    qtile.current_layout.margin += amount
    if qtile.current_layout.margin < 1:
        qtile.current_layout.margin = 0
    qtile.current_group.layout_all()


floating_layout=True

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], 'd', lazy.spawn("rofi -show run"), desc="Launch rofi"),
    Key([mod], 'f', lazy.spawn('rofi -show filebrowser'), desc="launch rofi filebrowser"),
    Key([mod], "t", lazy.spawn('telegram-desktop'), desc="launch telegram"),
    Key([], 'Print', lazy.spawn("flameshot gui"), desc="Screenshot with flameshot"),
    Key([], 'XF86AudioLowerVolume', lazy.spawn("pactl set-sink-volume  alsa_output.pci-0000_05_00.6.analog-stereo -5%"), desc="lower volume"),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn("pactl set-sink-volume alsa_output.pci-0000_05_00.6.analog-stereo +5%"), desc="raise volume"),
    Key([], 'XF86AudioMute', lazy.spawn("pactl set-sink-mute alsa_output.pci-0000_05_00.6.analog-stereo toggle"), desc="raise volume"),
    Key([], 'XF86AudioMicMute', lazy.spawn("pactl set-source-mute alsa_input.pci-0000_05_00.6.analog-stereo toggle"), desc="raise volume"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl -d 'amdgpu_bl0' set +5%"), desc="Brightness up"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl -d 'amdgpu_bl0' set 5%-"), desc="Brightness down"),
    Key(['control', 'mod1'], 'l', lazy.spawn('xsecurelock'), desc="Lock the screen"),
    KeyChord([mod], 'o', [
        Key([], 'j', lazy.spawn("picom-trans -c -10")),
        Key([], 'k', lazy.spawn('picom-trans -c +10')),
        ],
        mode="Opacity"
        ),
    KeyChord([mod], 'm', [
        Key([], 'j',adjust_margins(amount=2), desc="Margin increase" ),
        Key([], 'k', adjust_margins(amount=(-2)), desc="Decrease margins")
        ],
        mode="Margins"),
    Key([mod, 'control'], 'f', lazy.window.toggle_floating(), desc="float current window")
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
groups.append(ScratchPad('scratchpad', [
    DropDown('term', 'kitty', width=0.4, height=0.5, x=0.3, y=0.2, opacity=1),
    ]))
keys.extend([
    Key([], "F11", lazy.group['scratchpad'].dropdown_toggle('term')),
    ])


layouts = [
    layout.Columns(
        border_focus=[ "#91aCD1"],
        border_focus_stack=[ "#e9b189"],
        border_width=2,
        margin=1,
        insert_position=1,
        ),
    layout.Max(),
]

widget_defaults = dict(
    font=FONT,
    fontsize=FONTSIZE,
    padding=6,
    foreground=FOREGROUND,
    )
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper="/usr/share/backgrounds/spirited.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    scale=0.6
                    ),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(
                    ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(
                    ),
                # widget.Backlight(
                #     backlight_name='amdgpu_bl0',
                #     fmt='Bright: {}'
                #     ),
                widget.Sep(
                    ),
                widget.Pomodoro(
                    color_inactive=FOREGROUND,
                    ),
                widget.Sep(
                    ),
                widget.PulseVolume(
                    fmt=' Vol: {}'
                    ),
                widget.Sep(
                    ),
                widget.Battery(
                    format=' Bat: {percent:2.0%} {hour:d}:{min:02d}h'
                    ),
                widget.Sep(
                    ),
                widget.Clock(
                    format=" %a %H:%M ",
                    # timezone="America/Los_Angeles",
                    timezone="America/New_York"
                    ),
                # widget.QuickExit(),
            ],
            size=28,
            background='#111111'
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class='telegram-desktop'),
        Match(wm_class="skype"),
        Match(wm_class='around'),
    ],

)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
