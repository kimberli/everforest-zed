#!/usr/bin/env python3
"""
Generate Everforest Zed themes from color variants and mapping logic.
"""

import json
import os
from typing import Dict, Any

def load_colors() -> Dict[str, Any]:
    """Load color variants from colors.json"""
    with open('colors.json', 'r') as f:
        return json.load(f)

def create_zed_theme_style(colors: Dict[str, str]) -> Dict[str, Any]:
    """Create Zed theme style object from color palette"""
    
    # Helper function to add transparency
    def with_alpha(color: str, alpha: str) -> str:
        return f"{color}{alpha}"
    
    style = {
        # Border colors
        "border": colors["bg_dim"],
        "border.variant": colors["bg_dim"], 
        "border.focused": colors["bg0"],
        "border.selected": colors["bg_dim"],
        "border.transparent": colors["bg_dim"],
        "border.disabled": colors["bg_dim"],
        
        # Surface colors
        "elevated_surface.background": colors["bg1"],
        "surface.background": colors["bg0"],
        "background": colors["bg0"],
        
        # Element colors
        "element.background": colors["bg_dim"],
        "element.hover": colors["bg1"],
        "element.active": None,
        "element.selected": colors["bg_dim"],
        "element.disabled": None,
        
        # Drop target
        "drop_target.background": colors["bg1"],
        
        # Ghost elements
        "ghost_element.background": None,
        "ghost_element.hover": with_alpha(colors["bg0"], "00"),
        "ghost_element.active": None,
        "ghost_element.selected": with_alpha(colors["bg_dim"], "80"),
        "ghost_element.disabled": None,
        
        # Text colors
        "text": colors["fg"],
        "text.muted": colors["grey0"],
        "text.placeholder": colors["grey0"],
        "text.disabled": colors["grey0"],
        "text.accent": colors["green"],
        
        # Icon colors
        "icon": colors["fg"],
        "icon.muted": colors["grey0"],
        "icon.disabled": colors["grey0"],
        "icon.placeholder": colors["grey0"],
        "icon.accent": colors["green"],
        
        # UI component backgrounds
        "status_bar.background": colors["bg_dim"],
        "title_bar.background": colors["bg_dim"],
        "toolbar.background": colors["bg0"],
        "tab_bar.background": colors["bg_dim"],
        "tab.inactive_background": colors["bg_dim"],
        "tab.active_background": colors["bg0"],
        "search.match_background": colors["bg_yellow"],
        "panel.background": colors["bg_dim"],
        "panel.focused_border": colors["green"],
        "pane.focused_border": colors["green"],
        
        # Scrollbar
        "scrollbar.thumb.background": with_alpha(colors["bg3"], "80"),
        "scrollbar.thumb.hover_background": colors["bg3"],
        "scrollbar.thumb.border": with_alpha(colors["bg3"], "80"),
        "scrollbar.track.background": colors["bg0"],
        "scrollbar.track.border": with_alpha(colors["bg0"], "00"),
        
        # Editor
        "editor.foreground": colors["fg"],
        "editor.background": colors["bg0"],
        "editor.gutter.background": colors["bg0"],
        "editor.subheader.background": colors["bg1"],
        "editor.active_line.background": with_alpha(colors["bg_dim"], "90"),
        "editor.highlighted_line.background": with_alpha(colors["bg_dim"], "30"),
        "editor.line_number": with_alpha(colors["grey0"], "80"),
        "editor.active_line_number": colors["fg"],
        "editor.invisible": colors["grey0"],
        "editor.wrap_guide": colors["bg1"],
        "editor.active_wrap_guide": colors["bg_dim"],
        "editor.document_highlight.read_background": with_alpha(colors["bg_blue"], "40"),
        "editor.document_highlight.write_background": with_alpha(colors["bg_red"], "40"),
        
        # Terminal
        "terminal.background": colors["bg0"],
        "terminal.foreground": colors["fg"],
        "terminal.bright_foreground": colors["fg"],
        "terminal.dim_foreground": colors["grey0"],
        "terminal.ansi.black": colors["bg1"],
        "terminal.ansi.bright_black": colors["grey1"],
        "terminal.ansi.dim_black": colors["grey0"],
        "terminal.ansi.red": colors["red"],
        "terminal.ansi.bright_red": colors["red"],
        "terminal.ansi.dim_red": with_alpha(colors["red"], "80"),
        "terminal.ansi.green": colors["green"],
        "terminal.ansi.bright_green": colors["green"],
        "terminal.ansi.dim_green": with_alpha(colors["green"], "80"),
        "terminal.ansi.yellow": colors["yellow"],
        "terminal.ansi.bright_yellow": colors["yellow"],
        "terminal.ansi.dim_yellow": with_alpha(colors["yellow"], "80"),
        "terminal.ansi.blue": colors["blue"],
        "terminal.ansi.bright_blue": colors["blue"],
        "terminal.ansi.dim_blue": with_alpha(colors["blue"], "80"),
        "terminal.ansi.magenta": colors["purple"],
        "terminal.ansi.bright_magenta": colors["purple"],
        "terminal.ansi.dim_magenta": with_alpha(colors["purple"], "80"),
        "terminal.ansi.cyan": colors["aqua"],
        "terminal.ansi.bright_cyan": colors["aqua"],
        "terminal.ansi.dim_cyan": with_alpha(colors["aqua"], "80"),
        "terminal.ansi.white": colors["fg"],
        "terminal.ansi.bright_white": colors["fg"],
        "terminal.ansi.dim_white": colors["grey2"],
        
        # Link text
        "link_text.hover": colors["green"],
        
        # Status colors
        "conflict": colors["purple"],
        "conflict.background": colors["bg_purple"],
        "conflict.border": colors["purple"],
        "created": colors["green"],
        "created.background": colors["bg_green"],
        "created.border": colors["green"],
        "deleted": colors["red"],
        "deleted.background": colors["bg_red"],
        "deleted.border": colors["red"],
        "error": colors["red"],
        "error.background": colors["bg_red"],
        "error.border": colors["red"],
        "hidden": colors["grey0"],
        "hidden.background": None,
        "hidden.border": None,
        "hint": colors["aqua"],
        "hint.background": colors["bg_green"],
        "hint.border": colors["aqua"],
        "ignored": colors["grey0"],
        "ignored.background": None,
        "ignored.border": None,
        "info": colors["blue"],
        "info.background": colors["bg_blue"],
        "info.border": colors["blue"],
        "modified": colors["yellow"],
        "modified.background": colors["bg_yellow"],
        "modified.border": colors["yellow"],
        "predictive": colors["grey0"],
        "predictive.background": None,
        "predictive.border": None,
        "renamed": colors["aqua"],
        "renamed.background": colors["bg_green"],
        "renamed.border": colors["aqua"],
        "success": colors["green"],
        "success.background": colors["bg_green"],
        "success.border": colors["green"],
        "unreachable": colors["grey0"],
        "unreachable.background": None,
        "unreachable.border": None,
        "warning": colors["yellow"],
        "warning.background": colors["bg_yellow"],
        "warning.border": colors["yellow"],
        
        # Players
        "players": [
            {
                "cursor": colors["fg"],
                "selection": colors["bg_dim"],
                "background": colors["bg_dim"]
            }
        ],
        
        # Syntax highlighting
        "syntax": {
            "attribute": {
                "color": colors["purple"],
                "font_style": None,
                "font_weight": None
            },
            "constant": {
                "color": colors["purple"],
                "font_style": None,
                "font_weight": None
            },
            "constructor": {
                "color": colors["green"],
                "font_style": None,
                "font_weight": None
            },
            "comment": {
                "color": colors["grey1"],
                "font_style": "italic",
                "font_weight": None
            },
            "function": {
                "color": colors["green"],
                "font_style": None,
                "font_weight": None
            },
            "keyword": {
                "color": colors["red"],
                "font_style": None,
                "font_weight": None
            },
            "number": {
                "color": colors["purple"],
                "font_style": None,
                "font_weight": None
            },
            "operator": {
                "color": colors["orange"],
                "font_style": None,
                "font_weight": None
            },
            "property": {
                "color": colors["aqua"],
                "font_style": None,
                "font_weight": None
            },
            "string": {
                "color": colors["green"],
                "font_style": None,
                "font_weight": None
            },
            "string.escape": {
                "color": colors["aqua"],
                "font_style": None,
                "font_weight": None
            },
            "type": {
                "color": colors["yellow"],
                "font_style": None,
                "font_weight": None
            },
            "variable": {
                "color": colors["fg"],
                "font_style": None,
                "font_weight": None
            }
        }
    }
    
    return style

def generate_theme_file(theme_name: str, appearance: str, variants: list) -> Dict[str, Any]:
    """Generate complete Zed theme file with all variants"""
    
    theme_file = {
        "$schema": "https://zed.dev/schema/themes/v0.1.0.json",
        "name": theme_name,
        "author": "Kimberli Zhong",
        "themes": variants
    }
    
    return theme_file

def main():
    """Generate all Everforest Zed theme files"""
    
    # Load colors data
    colors_data = load_colors()
    
    # Create themes directory if it doesn't exist
    os.makedirs('themes', exist_ok=True)
    
    # Generate dark themes
    dark_variants = []
    for contrast in ['hard', 'medium', 'soft']:
        # Combine background and foreground colors
        bg_colors = colors_data['dark']['background'][contrast]
        fg_colors = colors_data['dark']['foreground']
        all_colors = {**bg_colors, **fg_colors}
        
        # Generate theme variant
        variant_name = f"Everforest Dark {contrast.title()}"
        style = create_zed_theme_style(all_colors)
        
        dark_variants.append({
            "name": variant_name,
            "appearance": "dark",
            "style": style
        })
    
    # Generate light themes  
    light_variants = []
    for contrast in ['hard', 'medium', 'soft']:
        # Combine background and foreground colors
        bg_colors = colors_data['light']['background'][contrast]
        fg_colors = colors_data['light']['foreground']
        all_colors = {**bg_colors, **fg_colors}
        
        # Generate theme variant
        variant_name = f"Everforest Light {contrast.title()}"
        style = create_zed_theme_style(all_colors)
        
        light_variants.append({
            "name": variant_name,
            "appearance": "light", 
            "style": style
        })
    
    # Write theme files
    dark_theme = generate_theme_file("Everforest Dark", "dark", dark_variants)
    light_theme = generate_theme_file("Everforest Light", "light", light_variants)
    
    with open('themes/everforest-dark.json', 'w') as f:
        json.dump(dark_theme, f, indent=4)
    
    with open('themes/everforest-light.json', 'w') as f:
        json.dump(light_theme, f, indent=4)
    
    print("✅ Generated Everforest Zed themes:")
    print("   - themes/everforest-dark.json (Hard, Medium, Soft)")
    print("   - themes/everforest-light.json (Hard, Medium, Soft)")
    print("\n🎨 Theme variants created:")
    for variant in dark_variants + light_variants:
        print(f"   - {variant['name']}")

if __name__ == "__main__":
    main()
