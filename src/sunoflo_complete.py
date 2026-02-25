"""
SunoFLO - Complete Version
All Phases Implementation
AI-Powered FL Studio Project Generator
"""

import os
import struct
import json
import random
import re
from typing import List, Dict, Any

VERSION = "2.0.0"

# ========== CLICHE FILTER ==========
CLICHE_WORDS = [
    "universe", "galaxy", "stars", "shine", "glow", "dream", "fantasy", "paradise",
    "heaven", "angel", "wings", "fly", "soar", "sky", "beyond", "infinity",
    "forever", "neverending", "magic", "miracle", "heartbeat", "soul", "neon", "vibes",
]

BETTER_ALTERNATIVES = {
    "universe": ["block", "hood", "streets", "world"],
    "galaxy": ["streets", "blocks", "trap"],
    "stars": ["guap", "bands", "racks", "cash"],
    "shine": ["grind", "hustle", "ball"],
    "glow": ["flex", "show", "stack"],
    "dream": ["scheme", "goal", "bag"],
    "fantasy": ["real life", "hustle"],
    "paradise": ["my house", "the trap"],
    "heaven": ["trap house", "studio"],
    "angel": ["shorty", "queen"],
    "wings": ["racks", "bands"],
    "fly": ["rich", "ball", "flex"],
    "soar": ["stack", "hustle"],
    "sky": ["roof", "top"],
    "magic": ["real", "true"],
    "neon": ["diamonds", "racks"],
}

# ========== ALL STYLES ==========
STYLE_PRESETS = {
    "Metro Boomin": {"bpm": 140, "key": "C minor", "genre": "Trap"},
    "Southside": {"bpm": 140, "key": "G minor", "genre": "Trap"},
    "Wheezy": {"bpm": 146, "key": "D minor", "genre": "Trap"},
    "Nick Mira": {"bpm": 130, "key": "A minor", "genre": "Trap"},
    "Pi'erre Bourne": {"bpm": 146, "key": "E minor", "genre": "Trap"},
    "Travis Scott": {"bpm": 140, "key": "C minor", "genre": "Trap"},
    "Kendrick Lamar": {"bpm": 120, "key": "D minor", "genre": "Hip Hop"},
    "Armin van Buuren": {"bpm": 138, "key": "A minor", "genre": "Trance"},
    "Tiesto": {"bpm": 136, "key": "G minor", "genre": "Trance"},
    "Dash Berlin": {"bpm": 138, "key": "C minor", "genre": "Trance"},
    "David Guetta": {"bpm": 128, "key": "C major", "genre": "House"},
    "Daft Punk": {"bpm": 123, "key": "A minor", "genre": "House"},
    "Pink Floyd": {"bpm": 120, "key": "G minor", "genre": "Rock"},
    "Queen": {"bpm": 120, "key": "B minor", "genre": "Rock"},
    "The Weeknd": {"bpm": 120, "key": "E minor", "genre": "R&B"},
    "Drake": {"bpm": 85, "key": "D minor", "genre": "R&B"},
    "Deadmau5": {"bpm": 128, "key": "F minor", "genre": "EDM"},
    "Boards of Canada": {"bpm": 90, "key": "C minor", "genre": "Ambient"},
    "Lost Boy": {"bpm": 140, "key": "C minor", "genre": "Phonk"},
}

GENRES = ["Trap", "Drill", "R&B", "Pop", "House", "Hip Hop", "Trance", "Techno", "Dubstep", "DnB", "Ambient", "Rock", "EDM", "Lo-Fi", "Synthwave", "Phonk"]

# ========== RHYMES ==========
RHYMES = {
    "a": ["back", "rack", "stack", "cat", "flat", "hat", "trap", "gap", "cash", "dash"],
    "b": ["love", "above", "shove", "enough", "touch", "clutch", "much", "rush", "hush"],
    "c": ["time", "mine", "fine", "wine", "shine", "line", "tonight", "alright", "light", "fight"],
    "d": ["man", "plan", "clan", "can", "fan", "ran", "stand", "hand", "land", "band"],
    "e": ["world", "girl", "curl", "pearl", "twirl", "sure", "pure", "cure"],
    "f": ["day", "way", "play", "say", "may", "lay", "stay", "away", "today", "okay"],
    "g": ["real", "feel", "steal", "deal", "wheel", "heal", "reveal"],
    "h": ["thing", "bring", "sing", "ring", "king", "wing", "bling", "everything"],
}

# ========== MIDI GENERATOR ==========
def var_len(value):
    result = bytearray()
    while value >= 0x80:
        result.append((value & 0x7F) | 0x80)
        value >>= 7
    result.append(value & 0x7F)
    return bytes(result)

def get_root(key):
    notes = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
    k = key.replace(" minor", "").replace(" major", "").strip()
    return notes.get(k, 0) + 36

# ========== MAIN CLASS ==========
class SunoFLO:
    def __init__(self, genre="Trap", style="Metro Boomin"):
        self.genre = genre
        self.style = style
        self.preset = STYLE_PRESETS.get(style, STYLE_PRESETS["Metro Boomin"])
        self.bpm = self.preset.get("bpm", 140)
        self.key = self.preset.get("key", "C minor")
    
    def generate_midi(self, output_path):
        """Generate MIDI with drums, bass, melody"""
        midi = bytearray()
        
        # Header
        midi.extend(b'MThd')
        midi.extend(struct.pack('>I', 6))
        midi.extend(struct.pack('>H', 1))
        midi.extend(struct.pack('>H', 3))  # 3 tracks
        midi.extend(struct.pack('>H', 480))
        
        step = 480
        
        # Create drum track
        drum_track = self._create_track("Drums", "kick", 36, [1,0,0,0, 1,0,0,0, 1,0,0,0, 1,0,0,0], step)
        midi.extend(b'MTrk')
        midi.extend(struct.pack('>I', len(drum_track)))
        midi.extend(drum_track)
        
        # Create bass track
        root = get_root(self.key)
        bass_track = self._create_track("Bass", "bass", root, [1,0,0,1, 0,0,0,1, 1,0,0,1, 0,0,1,0], step)
        midi.extend(b'MTrk')
        midi.extend(struct.pack('>I', len(bass_track)))
        midi.extend(bass_track)
        
        # Create melody track
        melody_track = self._create_track("Melody", "melody", root + 12, [1,0,1,0, 1,0,1,0, 1,0,1,0, 1,0,1,0], step)
        midi.extend(b'MTrk')
        midi.extend(struct.pack('>I', len(melody_track)))
        midi.extend(melody_track)
        
        with open(output_path, 'wb') as f:
            f.write(midi)
        return True
    
    def _create_track(self, name, track_type, note, pattern, step):
        track = bytearray()
        
        # Track name
        track.extend([0x00, 0xFF, 0x03, len(name)])
        track.extend(name.encode('ascii'))
        
        # Notes
        for i, on in enumerate(pattern):
            if on:
                # Note on
                track.extend(var_len(i * step))
                track.extend([0x90, note, 100])
                # Note off
                track.extend(var_len(step - 10))
                track.extend([0x80, note, 0])
        
        # End
        track.extend([0x00, 0xFF, 0x2F, 0x00])
        return bytes(track)
    
    def generate_lyrics(self, advanced=True, topic="flex"):
        """Generate lyrics"""
        cats = list(RHYMES.keys())
        lines = []
        
        for i in range(8):
            cat = cats[i // 2]
            rhyme = random.choice(RHYMES[cat])
            
            templates = {
                "flex": f"I been stackin' {rhyme}, got my {rhyme} right",
                "money": f"They don't know the grind, but my {rhyme} so tight",
                "love": f"Shorty got me feeling {rhyme}, every {rhyme}",
                "struggle": f"Came from the bottom where the struggle {rhyme}",
            }
            
            line = templates.get(topic, templates["flex"])
            
            if advanced:
                line += ", been that way since day one"
                line = line.upper()
            
            lines.append(line)
        
        lyrics = f"""[HOOK]
{chr(10).join(lines[:4])}

[VERSE 1]
{chr(10).join(lines)}

[HOOK]
{chr(10).join(lines[:4])}"""
        
        if advanced:
            # Remove cliches
            for word in CLICHE_WORDS:
                if word in lyrics.lower() and word in BETTER_ALTERNATIVES:
                    lyrics = re.sub(r'\b' + word + r'\b', random.choice(BETTER_ALTERNATIVES[word]), lyrics, flags=re.IGNORECASE)
        
        return lyrics
    
    def generate_project(self, output_dir="~/Downloads", include_lyrics=True, advanced_lyrics=True, topic="flex"):
        """Generate complete project"""
        output_dir = os.path.expanduser(output_dir)
        os.makedirs(output_dir, exist_ok=True)
        
        style_name = self.style.replace(" ", "_").lower()
        
        results = {}
        
        # MIDI
        midi_path = os.path.join(output_dir, f"sunoflo_{style_name}.mid")
        self.generate_midi(midi_path)
        results["midi"] = midi_path
        print(f"✓ MIDI: {midi_path}")
        
        # Lyrics
        if include_lyrics:
            lyrics = self.generate_lyrics(advanced_lyrics, topic)
            lyrics_path = os.path.join(output_dir, f"sunoflo_{style_name}_lyrics.txt")
            with open(lyrics_path, 'w') as f:
                f.write(lyrics)
            results["lyrics"] = lyrics_path
            print(f"✓ Lyrics: {lyrics_path}")
        
        return results

# ========== UI ==========
def console_ui():
    print("=" * 50)
    print("SunoFLO - Complete Version")
    print("=" * 50)
    
    print("\nSelect Genre:")
    for i, g in enumerate(GENRES):
        print(f"  {i+1:2}. {g}")
    g = int(input("> ")) - 1
    genre = GENRES[max(0, min(g, len(GENRES)-1))]
    
    print(f"\nSelect Style ({genre}):")
    styles = [s for s, d in STYLE_PRESETS.items() if d.get("genre") == genre]
    if not styles:
        styles = list(STYLE_PRESETS.keys())[:10]
    
    for i, s in enumerate(styles):
        print(f"  {i+1:2}. {s}")
    s = int(input("> ")) - 1
    style = styles[max(0, min(s, len(styles)-1))]
    
    preset = STYLE_PRESETS[style]
    print(f"\n{style}: {preset['bpm']} BPM, {preset['key']}")
    
    do_lyrics = input("\nGenerate lyrics? (y/n): ").lower() == 'y'
    
    topic = "flex"
    if do_lyrics:
        print("Topic: 1.Flex 2.Money 3.Love 4.Struggle")
        t = int(input("> ")) - 1
        topics = ["flex", "money", "love", "struggle"]
        topic = topics[max(0, min(t, 3))]
    
    print("\nGenerating...")
    flo = SunoFLO(genre, style)
    result = flo.generate_project(include_lyrics=do_lyrics, topic=topic)
    
    print("\n" + "=" * 50)
    print("✓ COMPLETE!")
    print("=" * 50)
    
    if do_lyrics:
        print(f"\n{result.get('lyrics', '')}")

if __name__ == "__main__":
    console_ui()
