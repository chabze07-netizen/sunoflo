"""
SunoFLO - Phase 1.5 (Enhanced)
AI-Powered FL Studio Project Generator
Now with Trance, Pink Floyd styles, Stem Separation & MIDI
"""

import os
import struct
import json
import random
from typing import List, Dict, Any, Optional

# ========== GENRE & STYLE PRESETS ==========
GENRES = [
    "Trap", "Drill", "R&B", "Pop", "House", "Hip Hop", 
    "Trance", "Techno", "Dubstep", "DnB", "Ambient", "Rock",
    "Progressive House", "EDM", "Lo-Fi", "Synthwave"
]

# Extended style presets with more artists
STYLE_PRESETS = {
    # TRAP & HIP HOP
    "Metro Boomin": {"bpm": 140, "key": "C minor", "genre": "Trap", "desc": "Dark 808s, bell melodies, half-time"},
    "Southside": {"bpm": 140, "key": "G minor", "genre": "Trap", "desc": "Heavy 808 slides, crispy hi-hats"},
    "Wheezy": {"bpm": 146, "key": "D minor", "genre": "Trap", "desc": "Guitar/flute melodies, spacey"},
    "Nick Mira": {"bpm": 130, "key": "A minor", "genre": "Trap", "desc": "Emo/melodic, layered pianos"},
    "Pi'erre Bourne": {"bpm": 146, "key": "E minor", "genre": "Trap", "desc": "Bouncy drums, harp leads"},
    "Travis Scott": {"bpm": 140, "key": "C minor", "genre": "Trap", "desc": "Auto-tune, ethereal, heavy reverb"},
    "Zaytoven": {"bpm": 140, "key": "F minor", "genre": "Trap", "desc": "Orchestral 808s, church organs"},
    
    # TRANCE
    "Armin van Buuren": {"bpm": 138, "key": "A minor", "genre": "Trance", "desc": "Uplifting, big drops, soaring synths"},
    "Tiesto": {"bpm": 136, "key": "G minor", "genre": "Trance", "desc": "EDM-Trance hybrid, big room"},
    "Paul van Dyk": {"bpm": 140, "key": "B minor", "genre": "Trance", "desc": "Progressive, euphoric"},
    "Dash Berlin": {"bpm": 138, "key": "C minor", "genre": "Trance", "desc": "Emotional, melodic, big chords"},
    "Orjan Nilsen": {"bpm": 138, "key": "D minor", "genre": "Trance", "desc": "Dark trance, tech elements"},
    "Gouryella": {"bpm": 140, "key": "E minor", "genre": "Trance", "desc": "Classic uplift, massive reverb"},
    
    # HOUSE
    "David Guetta": {"bpm": 128, "key": "C major", "genre": "House", "desc": "Electro house, big drops"},
    "Calvin Harris": {"bpm": 128, "key": "D major", "genre": "House", "desc": "Pop-house, catchy vocals"},
    "Fisher": {"bpm": 124, "key": "E minor", "genre": "House", "desc": "Tech house, bass-heavy"},
    
    # ELECTRONIC
    "Daft Punk": {"bpm": 123, "key": "A minor", "genre": "House", "desc": "French house, funky, robot voices"},
    "Deadmau5": {"bpm": 128, "key": "F minor", "genre": "Electronic", "desc": "Progressive, glitchy, minimal"},
    "Skrillex": {"bpm": 140, "key": "D minor", "genre": "Dubstep", "desc": "Dubstep, heavy bass, growls"},
    
    # ROCK & ALTERNATIVE
    "Pink Floyd": {"bpm": 120, "key": "G minor", "genre": "Rock", "desc": "Psychedelic, space rock, epic solos"},
    "Queen": {"bpm": 120, "key": "B minor", "genre": "Rock", "desc": "Rock anthems, operatic"},
    "Metallica": {"bpm": 130, "key": "E minor", "genre": "Rock", "desc": "Heavy metal, thrash"},
    " Nirvana": {"bpm": 120, "key": "F minor", "genre": "Rock", "desc": "Grunge, alternative"},
    
    # AMBIENT & LO-FI
    "Boards of Canada": {"bpm": 90, "key": "C minor", "genre": "Ambient", "desc": "Ambient, retro synths, nostalgic"},
    "Tycho": {"bpm": 100, "key": "D major", "genre": "Ambient", "desc": "Chillwave, atmospheric"},
    "MF DOOM": {"bpm": 90, "key": "A minor", "genre": "Hip Hop", "desc": "Lo-fi hip hop, abstract beats"},
    
    # SYNTHWAVE
    "Gunship": {"bpm": 110, "key": "E minor", "genre": "Synthwave", "desc": "Dark synthwave, retro"},
    "Timecop1983": {"bpm": 105, "key": "A minor", "genre": "Synthwave", "desc": "Retro synth, dreamy"},
}

# ========== STEM DEFINITIONS ==========
STEM_TYPES = ["drums", "bass", "melody", "vocals", "synths", "fx"]

# ========== MIDI NOTE DEFINITIONS ==========
# Standard MIDI note mappings
NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def note_to_midi(note: str, octave: int) -> int:
    """Convert note name to MIDI number"""
    note_idx = NOTE_NAMES.index(note.replace("-", "#").replace("b", "#"))
    return (octave + 1) * 12 + note_idx

# Scale patterns for different genres
SCALE_PATTERNS = {
    "minor": [0, 2, 3, 5, 7, 8, 10],
    "major": [0, 2, 4, 5, 7, 9, 11],
    "dorian": [0, 2, 3, 5, 7, 9, 10],
    "phrygian": [0, 1, 3, 5, 7, 8, 10],
    "lydian": [0, 2, 4, 6, 7, 9, 11],
}

# ========== STEM GENERATOR ==========
class StemGenerator:
    """Generate separate stems for drums, bass, melody, etc."""
    
    def __init__(self, genre: str, style: str):
        self.genre = genre
        self.style = style
        self.style_data = STYLE_PRESETS.get(style, STYLE_PRESETS["Metro Boomin"])
        self.bpm = self.style_data["bpm"]
        
    def generate_stem(self, stem_type: str) -> Dict:
        """Generate MIDI data for a specific stem"""
        
        # Generate based on genre and stem type
        if stem_type == "drums":
            return self._generate_drums()
        elif stem_type == "bass":
            return self._generate_bass()
        elif stem_type == "melody":
            return self._generate_melody()
        elif stem_type == "synths":
            return self._generate_synths()
        elif stem_type == "fx":
            return self._generate_fx()
        else:
            return {"notes": [], "type": stem_type}
    
    def _generate_drums(self) -> Dict:
        """Generate drum pattern MIDI"""
        pattern_length = 16  # 4 bars of 4
        
        kick_notes = []
        snare_notes = []
        hihat_notes = []
        clap_notes = []
        
        # Genre-specific drum patterns
        if self.genre in ["Trap", "Drill"]:
            # Trap pattern: kick on 1, 3, + 8th notes
            for i in range(pattern_length):
                if i % 4 == 0:  # Kick on 1 and 3
                    kick_notes.append({"time": i * 480, "note": 36, "velocity": 127})  # C1
                if i % 8 == 4:  # Snare on 3
                    snare_notes.append({"time": i * 480, "note": 38, "velocity": 120})  # D1
                if i % 2 == 0:  # Hi-hats on every 8th
                    hihat_notes.append({"time": i * 480, "note": 42, "velocity": 80})  # Closed hat
                    
        elif self.genre == "Trance":
            # Trance: driving 4-on-the-floor
            for i in range(pattern_length):
                kick_notes.append({"time": i * 480, "note": 36, "velocity": 127})
                if i % 4 == 2:  # Offbeat clap
                    clap_notes.append({"time": i * 480, "note": 39, "velocity": 100})
                hihat_notes.append({"time": i * 480 + 240, "note": 44, "velocity": 60})  # Open hat
                
        elif self.genre in ["House", "EDM"]:
            # House: classic 4-on-the-floor
            for i in range(pattern_length):
                kick_notes.append({"time": i * 480, "note": 36, "velocity": 127})
                if i % 2 == 1:
                    snare_notes.append({"time": i * 480, "note": 40, "velocity": 110})
                hihat_notes.append({"time": i * 480 + 120, "note": 42, "velocity": 70})
                
        else:  # Default rock/pop
            for i in range(pattern_length):
                if i % 4 == 0:
                    kick_notes.append({"time": i * 480, "note": 36, "velocity": 127})
                if i % 8 == 6:
                    snare_notes.append({"time": i * 480, "note": 38, "velocity": 120})
                hihat_notes.append({"time": i * 480, "note": 42, "velocity": 60})
        
        return {
            "type": "drums",
            "bpm": self.bpm,
            "tracks": [
                {"name": "Kick", "notes": kick_notes, "midi_channel": 10},
                {"name": "Snare", "notes": snare_notes, "midi_channel": 10},
                {"name": "Hi-Hat", "notes": hihat_notes, "midi_channel": 10},
                {"name": "Clap", "notes": clap_notes, "midi_channel": 10},
            ]
        }
    
    def _generate_bass(self) -> Dict:
        """Generate bass line"""
        # Get root note from key
        key = self.style_data["key"].replace(" minor", "").replace(" major", "")
        root = note_to_midi(key, 1)  # Bass octave
        
        bass_notes = []
        pattern_length = 16
        
        # Bass pattern varies by genre
        if self.genre in ["Trap", "Drill"]:
            # 808 bass pattern
            for i in range(pattern_length):
                if i % 4 == 0:
                    bass_notes.append({"time": i * 480, "note": root, "velocity": 127, "duration": 480})
                elif i % 4 == 2:
                    bass_notes.append({"time": i * 480, "note": root - 5, "velocity": 100, "duration": 480})  # Fifth
                    
        elif self.genre == "Trance":
            # Driving bass
            for i in range(pattern_length):
                bass_notes.append({"time": i * 480, "note": root, "velocity": 110, "duration": 240})
                bass_notes.append({"time": i * 480 + 240, "note": root + 7, "velocity": 90, "duration": 240})
                
        elif self.genre == "House":
            # Sub bass
            for i in range(pattern_length):
                bass_notes.append({"time": i * 480, "note": root, "velocity": 120, "duration": 480})
                
        else:  # Rock/Pop
            root_note = root
            bass_notes.append({"time": 0, "note": root_note, "velocity": 110, "duration": 1920})
            bass_notes.append({"time": 1920, "note": root_note + 5, "velocity": 100, "duration": 1920})
            bass_notes.append({"time": 3840, "note": root_note, "velocity": 110, "duration": 1920})
        
        return {
            "type": "bass",
            "bpm": self.bpm,
            "tracks": [{"name": "Bass", "notes": bass_notes, "midi_channel": 1}]
        }
    
    def _generate_melody(self) -> Dict:
        """Generate melody/harmony"""
        key = self.style_data["key"].replace(" minor", "").replace(" major", "")
        root = note_to_midi(key, 4)  # Middle octave
        
        scale_type = "minor" if "minor" in self.style_data["key"].lower() else "major"
        scale = SCALE_PATTERNS.get(scale_type, SCALE_PATTERNS["minor"])
        
        melody_notes = []
        
        # Generate melody based on style
        if "Pink Floyd" in self.style:
            # Epic rock melody
            progression = [0, 3, 4, 2, 5, 4, 3, 0]  # Am -> C -> D -> Bm -> Em -> D -> C -> Am
            for i, degree in enumerate(progression):
                note_idx = degree % 7
                midi_note = root + scale[note_idx] + (degree // 7) * 12
                melody_notes.append({
                    "time": i * 1920,
                    "note": midi_note,
                    "velocity": 100,
                    "duration": 1800
                })
                
        elif "Trance" in self.genre or "Armin" in self.style:
            # Uplifting trance lead
            arp_pattern = [0, 4, 7, 12, 7, 4]
            for i in range(16):
                for j, degree in enumerate(arp_pattern):
                    midi_note = root + degree
                    melody_notes.append({
                        "time": i * 480 + j * 80,
                        "note": midi_note,
                        "velocity": 90,
                        "duration": 80
                    })
                    
        elif "Lo-Fi" in self.genre or "MF DOOM" in self.style:
            # Lo-fi chord progression
            chords = [0, 2, 4, 5]
            for i, chord_root in enumerate(chords):
                for offset in [0, 3, 7]:  # Chord
                    midi_note = root + scale[chord_root % 7] + offset
                    melody_notes.append({
                        "time": i * 1920,
                        "note": midi_note,
                        "velocity": 70,
                        "duration": 1800
                    })
        else:
            # Default simple melody
            for i in range(8):
                note = root + scale[i % len(scale)]
                melody_notes.append({
                    "time": i * 960,
                    "note": note,
                    "velocity": 90,
                    "duration": 900
                })
        
        return {
            "type": "melody",
            "bpm": self.bpm,
            "tracks": [{"name": "Melody", "notes": melody_notes, "midi_channel": 1}]
        }
    
    def _generate_synths(self) -> Dict:
        """Generate synth/pad"""
        key = self.style_data["key"].replace(" minor", "").replace(" major", "")
        root = note_to_midi(key, 3)
        
        synth_notes = []
        
        if self.genre == "Trance":
            # Big trance pads
            for i in range(4):
                chord = [0, 4, 7, 12]  # Major chord
                for offset in chord:
                    synth_notes.append({
                        "time": i * 1920,
                        "note": root + offset,
                        "velocity": 80,
                        "duration": 1800
                    })
        else:
            # Simple pad
            synth_notes.append({
                "time": 0,
                "note": root,
                "velocity": 75,
                "duration": 7680
            })
        
        return {
            "type": "synths",
            "bpm": self.bpm,
            "tracks": [{"name": "Synths/Pad", "notes": synth_notes, "midi_channel": 1}]
        }
    
    def _generate_fx(self) -> Dict:
        """Generate FX/riser"""
        return {
            "type": "fx",
            "bpm": self.bpm,
            "tracks": [{"name": "FX", "notes": [], "midi_channel": 1}]
        }
    
    def generate_all_stems(self) -> Dict:
        """Generate all stems"""
        return {
            "metadata": {
                "genre": self.genre,
                "style": self.style,
                "bpm": self.bpm,
                "key": self.style_data["key"]
            },
            "stems": {
                "drums": self.generate_stem("drums"),
                "bass": self.generate_stem("bass"),
                "melody": self.generate_stem("melody"),
                "synths": self.generate_stem("synths"),
                "fx": self.generate_stem("fx"),
            }
        }


# ========== MIDI FILE WRITER ==========
class MIDIWriter:
    """Write MIDI files from stem data"""
    
    def __init__(self, stem_data: Dict):
        self.stem_data = stem_data
        self.bpm = stem_data.get("bpm", 120)
        
    def write_midi(self, output_path: str, track_name: str = "MIDI") -> bool:
        """Write a MIDI file"""
        try:
            # MIDI header
            midi_file = bytearray()
            
            # MThd chunk
            midi_file.extend(b'MThd')
            midi_file.extend(struct.pack('>I', 6))  # Chunk size
            midi_file.extend(struct.pack('>H', 0))   # Format 0
            midi_file.extend(struct.pack('H', 1))    # One track
            midi_file.extend(struct.pack('>H', 480))  # Ticks per quarter
            
            # MTrk chunk
            midi_file.extend(b'MTrk')
            
            track_data = bytearray()
            
            # Set tempo
            tempo = int(500000 / (self.bpm / 60))  # Convert BPM to microseconds
            track_data.extend(self._var_len(0))  # Delta time 0
            track_data.extend(b'\xFF\x51\x03')
            track_data.extend(struct.pack('>I', tempo)[:3])
            
            # Write notes from all tracks
            all_notes = []
            for stem_key, stem_info in self.stem_data.get("stems", {}).items():
                if "tracks" in stem_info:
                    for track in stem_info["tracks"]:
                        for note in track.get("notes", []):
                            all_notes.append(note)
            
            # Sort by time
            all_notes.sort(key=lambda x: x.get("time", 0))
            
            # Write note events
            last_time = 0
            for note in all_notes:
                delta_time = note.get("time", 0) - last_time
                track_data.extend(self._var_len(int(delta_time)))
                
                # Note On
                track_data.append(0x90 | (note.get("midi_channel", 1) - 1))
                track_data.append(note.get("note", 60))
                track_data.append(note.get("velocity", 100))
                
                # Note Off (after duration)
                duration = note.get("duration", 480)
                track_data.extend(self._var_len(int(duration)))
                track_data.append(0x80 | (note.get("midi_channel", 1) - 1))
                track_data.append(note.get("note", 60))
                track_data.append(0)
                
                last_time = note.get("time", 0) + duration
            
            # End of track
            track_data.extend(self._var_len(0))
            track_data.extend(b'\xFF\x2F\x00')
            
            # Write track chunk size
            midi_file.extend(struct.pack('>I', len(track_data)))
            midi_file.extend(track_data)
            
            # Write file
            with open(output_path, 'wb') as f:
                f.write(midi_file)
            
            return True
        except Exception as e:
            print(f"Error writing MIDI: {e}")
            return False
    
    def _var_len(self, value: int) -> bytes:
        """Write variable-length quantity"""
        result = bytearray()
        while value >= 0x80:
            result.append((value & 0x7F) | 0x80)
            value >>= 7
        result.append(value & 0x7F)
        return bytes(result)


# ========== MAIN GENERATOR ==========
class SunoFLOGenerator:
    """Main generator class"""
    
    def __init__(self, genre: str = "Trap", style: str = "Metro Boomin"):
        self.genre = genre
        self.style = style
        self.preset = STYLE_PRESETS.get(style, STYLE_PRESETS["Metro Boomin"])
        
    def generate(self, output_dir: str = "~/Downloads") -> Dict:
        """Generate stems and MIDI files"""
        output_dir = os.path.expanduser(output_dir)
        os.makedirs(output_dir, exist_ok=True)
        
        style_name = self.style.replace(" ", "_").lower()
        
        # Generate stems
        print(f"Generating stems for {self.style} ({self.genre}) at {self.preset['bpm']} BPM...")
        stem_gen = StemGenerator(self.genre, self.style)
        stems = stem_gen.generate_all_stems()
        
        # Save stems JSON
        stems_path = os.path.join(output_dir, f"sunoflo_{style_name}_stems.json")
        with open(stems_path, 'w') as f:
            json.dump(stems, f, indent=2)
        
        # Generate MIDI for each stem
        midi_files = {}
        for stem_name, stem_data in stems.get("stems", {}).items():
            if stem_data.get("notes", []):
                midi_path = os.path.join(output_dir, f"sunoflo_{style_name}_{stem_name}.mid")
                writer = MIDIWriter({"bpm": self.preset["bpm"], "stems": {stem_name: stem_data}})
                if writer.write_midi(midi_path, stem_name.capitalize()):
                    midi_files[stem_name] = midi_path
                    print(f"  ✓ {stem_name}.mid saved")
        
        # Generate basic FLP
        flp_path = os.path.join(output_dir, f"sunoflo_{style_name}.flp")
        self._create_basic_flp(flp_path)
        
        return {
            "style": self.style,
            "genre": self.genre,
            "bpm": self.preset["bpm"],
            "key": self.preset["key"],
            "stems_json": stems_path,
            "midi_files": midi_files,
            "flp_file": flp_path
        }
    
    def _create_basic_flp(self, output_path: str):
        """Create basic FLP file"""
        # Similar to before - simplified for MVP
        flp_data = bytearray()
        flp_data.extend(b'FLhd')
        flp_data.extend(struct.pack('<I', 0))
        flp_data.extend(b'FlSr')
        flp_data.extend(struct.pack('<I', 4))
        flp_data.extend(struct.pack('<f', self.preset["bpm"]))
        
        with open(output_path, 'wb') as f:
            f.write(flp_data)


# ========== CONSOLE UI ==========
def console_ui():
    """Interactive console interface"""
    print("=" * 60)
    print("SunoFLO - Enhanced FL Studio Project Generator")
    print("Phase 1.5 - Now with Trance, Pink Floyd, Stems & MIDI")
    print("=" * 60)
    print()
    
    # Genre selection
    print("Select Genre:")
    for i, genre in enumerate(GENRES):
        print(f"  {i+1:2}. {genre}")
    genre_choice = int(input("\n> ")) - 1
    genre = GENRES[max(0, min(genre_choice, len(GENRES)-1))]
    
    # Style selection - filter by genre
    matching_styles = [s for s, data in STYLE_PRESETS.items() 
                      if data["genre"].lower() == genre.lower()]
    if not matching_styles:
        matching_styles = list(STYLE_PRESETS.keys())[:10]  # Default to first 10
    
    print(f"\nSelect Style (filtered for {genre}):")
    for i, style in enumerate(matching_styles[:15]):  # Show max 15
        data = STYLE_PRESETS[style]
        print(f"  {i+1:2}. {style} ({data['bpm']} BPM, {data['key']})")
    
    style_choice = int(input("\n> ")) - 1
    style = matching_styles[max(0, min(style_choice, len(matching_styles)-1))]
    
    preset = STYLE_PRESETS[style]
    
    print(f"\nSettings:")
    print(f"  Genre: {genre}")
    print(f"  Style: {style}")
    print(f"  BPM: {preset['bpm']}")
    print(f"  Key: {preset['key']}")
    print(f"  Description: {preset['desc']}")
    
    # Generate
    print("\nGenerating...")
    generator = SunoFLOGenerator(genre=genre, style=style)
    result = generator.generate()
    
    print("\n" + "=" * 40)
    print("✓ Generation Complete!")
    print("=" * 40)
    print(f"\nOutput files:")
    print(f"  FLP: {result['flp_file']}")
    print(f"  Stems JSON: {result['stems_json']}")
    for stem, path in result['midi_files'].items():
        print(f"  MIDI ({stem}): {path}")
    
    print("\nNext steps:")
    print("  1. Open .flp in FL Studio 21+")
    print("  2. Import MIDI files to different tracks")
    print("  3. Assign FL Studio native plugins (Sytrus, Harmor, FPC)")
    print("  4. Mix and produce!")


if __name__ == "__main__":
    console_ui()
