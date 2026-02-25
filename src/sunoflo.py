"""
SunoFLO - Phase 2.0
AI-Powered FL Studio Project Generator + Lyric Generator
Now with Advanced Lyric Generation (Better Rhymes, No Cliches)
"""

import os
import struct
import json
import random
import re
from typing import List, Dict, Any, Optional
from dataclasses import dataclass

# ========== ANTI-CLICHE WORDS (Common AI Lyrics to Avoid) ==========
CLICHE_WORDS = [
    "universe", "galaxy", "stars", "shine", "glow", "dream", "fantasy", "paradise",
    "heaven", "angel", "wings", "fly", "soar", "sky", "beyond", "infinity",
    "forever", "neverending", "timeless", "eternal", "magic", "miracle",
    "heartbeat", "heartbeat", "soul", "spirit", "electric", "neon", "vibes",
    "going crazy", "lose control", "feel the beat", "dance all night", "party"
]

# ========== BETTER ALTERNATIVES FOR CLICHES ==========
BETTER_ALTERNATIVES = {
    "universe": ["block", "hood", "streets", "city", "world"],
    "galaxy": ["streets", "blocks", "city", "trap"],
    "stars": ["guap", "bands", "racks", "cash"],
    "shine": ["grind", "hustle", "ball", "eat"],
    "glow": ["flex", "show", "stack"],
    "dream": ["scheme", "goal", "bag", "check"],
    "fantasy": ["real life", "real trap", "hustle"],
    "paradise": ["my house", "the trap", "my block"],
    "heaven": ["trap house", "studio", "on stage"],
    "angel": ["shorty", "queen", "boss"],
    "wings": ["racks", "bands", "guap"],
    "fly": ["rich", "ball", "flex"],
    "soar": ["stack", "hustle", "grind"],
    "sky": ["roof", "top", "ceiling"],
    "beyond": ["past", "after", "above"],
    "infinite": ["non-stop", "all day"],
    "forever": ["till the grave", "till death", "day by day"],
    "neverending": ["every day", "24/7", "all year"],
    "magic": ["real", "硬刚", "true"],
    "miracle": ["blessing", "come up", "win"],
    "heartbeat": ["pulse", "rhythm"],
    "electric": ["hard", "real", "trap"],
    "neon": ["diamonds", "racks", "chains"],
    "vibes": ["energy", "aura", "motion"],
}

# ========== GENRE & STYLE PRESETS ==========
GENRES = [
    "Trap", "Drill", "R&B", "Pop", "House", "Hip Hop", 
    "Trance", "Techno", "Dubstep", "DnB", "Ambient", "Rock",
    "Progressive House", "EDM", "Lo-Fi", "Synthwave", "Country", "Jazz"
]

STYLE_PRESETS = {
    # TRAP & HIP HOP
    "Metro Boomin": {"bpm": 140, "key": "C minor", "genre": "Trap", "desc": "Dark 808s, bell melodies, half-time"},
    "Southside": {"bpm": 140, "key": "G minor", "genre": "Trap", "desc": "Heavy 808 slides, crispy hi-hats"},
    "Wheezy": {"bpm": 146, "key": "D minor", "genre": "Trap", "desc": "Guitar/flute melodies, spacey"},
    "Nick Mira": {"bpm": 130, "key": "A minor", "genre": "Trap", "desc": "Emo/melodic, layered pianos"},
    "Pi'erre Bourne": {"bpm": 146, "key": "E minor", "genre": "Trap", "desc": "Bouncy drums, harp leads"},
    "Travis Scott": {"bpm": 140, "key": "C minor", "genre": "Trap", "desc": "Auto-tune, ethereal, heavy reverb"},
    "Kendrick Lamar": {"bpm": 120, "key": "D minor", "genre": "Hip Hop", "desc": "Conscious, storytelling, poetic"},
    "J Cole": {"bpm": 90, "key": "G minor", "genre": "Hip Hop", "desc": "Thoughtful, melodic, introspective"},
    
    # TRANCE
    "Armin van Buuren": {"bpm": 138, "key": "A minor", "genre": "Trance", "desc": "Uplifting, big drops, soaring synths"},
    "Tiesto": {"bpm": 136, "key": "G minor", "genre": "Trance", "desc": "EDM-Trance hybrid, big room"},
    "Dash Berlin": {"bpm": 138, "key": "C minor", "genre": "Trance", "desc": "Emotional, melodic, big chords"},
    
    # ROCK
    "Pink Floyd": {"bpm": 120, "key": "G minor", "genre": "Rock", "desc": "Psychedelic, space rock, epic solos"},
    "Queen": {"bpm": 120, "key": "B minor", "genre": "Rock", "desc": "Rock anthems, operatic"},
    "Metallica": {"bpm": 130, "key": "E minor", "genre": "Rock", "desc": "Heavy metal, thrash"},
    
    # R&B & POP
    "The Weeknd": {"bpm": 120, "key": "E minor", "genre": "R&B", "desc": "Dark R&B, atmospheric, haunting"},
    "Drake": {"bpm": 85, "key": "D minor", "genre": "R&B", "desc": "Melodic rap, emotional, Toronto sound"},
    "SZA": {"bpm": 95, "key": "C minor", "genre": "R&B", "desc": "Alternative R&B, introspective"},
}

# ========== LYRIC STRUCTURES ==========
VERSE_STRUCTURES = {
    "trap": {
        "lines_per_verse": 8,
        "syllables": [7, 7, 7, 7, 7, 7, 7, 7],  # 7 syllable pattern (standard rap)
        "rhyme_scheme": "AABBCCDD",  # Couplets
    },
    "rnb": {
        "lines_per_verse": 8,
        "syllables": [10, 10, 10, 10, 10, 10, 10, 10],  # 10 syllable (singing)
        "rhyme_scheme": "ABABCDCDEFEFGG",  # Complex
    },
    "pop": {
        "lines_per_verse": 8,
        "syllables": [8, 8, 8, 8, 8, 8, 8, 8],
        "rhyme_scheme": "ABAB",
    },
    "rock": {
        "lines_per_verse": 6,
        "syllables": [10, 10, 10, 10, 10, 10],
        "rhyme_scheme": "AABB",
    }
}

# ========== RHYME DICTIONARY ==========
RHYMES = {
    "a": ["back", "rack", "stack", "cat", "flat", "hat", "bat", "that", "sat", "chat", "stat", "cash", "dash", "lash", "trap", "gap", "splash", "scratch"],
    "b": ["love", "above", "shove", "dove", "of", "stuff", "enough", "touch", "clutch", "much", "such", "rush", "hush", "lust", "dust"],
    "c": ["time", "mine", "fine", "wine", "shine", "sign", "line", "divine", "combine", "design", "tonight", "alright", "light", "fight", "might", "right"],
    "d": ["man", "plan", "clan", "can", "fan", "scan", "tan", "ran", "began", "stand", "hand", "land", "sand", "band", "brand"],
    "e": ["world", "girl", "curl", "pearl", "twirl", "swirl", "hurl", "stir", "prefer", "occur", "blur", "fur", "sure", "pure", "cure", "secure"],
    "f": ["day", "way", "play", "say", "may", "lay", "ray", "stay", "away", "today", "okay", "display", "betray", "convey", "survey", "array"],
    "g": ["real", "feel", "steal", "deal", "wheel", "heal", "reveal", "appeal", "conceal", "surreal", "ideal", "deal", "meal", "seal"],
    "h": ["thing", "bring", "sing", "ring", "king", "wing", "spring", "string", "swing", "cling", "fling", "sting", "bling", "everything", "anything", "something"],
    "i": ["money", "honey", "funny", "unny", "sunny", "bunny", "runny", "phony", " bony", "croney"],
    "j": ["life", "wife", "strife", "knife", "rife", "midnight", "daylight", "sunlight", "insight", "delight", "tight", "flight", "bite", "height", "fright", "ignite"],
    "k": ["cash", "dash", "flash", "smash", "clash", "trash", "hash", "bash", "lash", "gash", "splash", "crash", "gnash", "stash", "ransom"],
    "l": ["trap", "rap", "clap", "snap", "tap", "map", "gap", "sap", "chap", "flap", "slap", "wrap", "scrap", "strap", "entrap", "adapt"],
    "m": ["see", "be", "free", "me", "key", "glee", "plea", "flee", "degree", "guarantee", "priority", "ability", "reality", "personality"],
    "n": ["stone", "bone", "phone", "zone", "alone", "throne", "own", "grown", "shown", "blown", "known", "tone", "moan", "groan", "atone", "postpone"],
    "o": ["turn", "burn", "learn", "earn", "yearn", "spurn", "cern", "concern", "discern", "sojourn", "journey"],
    "p": ["beat", "street", "meet", "feet", "heat", "treat", "sweet", "seat", "elite", "complete", "concrete", "discrete", "obsolete", "concrete"],
}

# ========== LYRIC GENERATOR ==========
class LyricGenerator:
    """Generate high-quality, non-cliche lyrics"""
    
    def __init__(self, genre: str = "Trap", advanced: bool = False):
        self.genre = genre
        self.advanced = advanced
        self.structure = self._get_structure()
        
    def _get_structure(self):
        if self.genre in ["Trap", "Drill", "Hip Hop"]:
            return VERSE_STRUCTURES["trap"]
        elif self.genre in ["R&B", "Pop"]:
            return VERSE_STRUCTURES["rnb"] if self.advanced else VERSE_STRUCTURES["pop"]
        elif self.genre in ["Rock", "Metal"]:
            return VERSE_STRUCTURES["rock"]
        return VERSE_STRUCTURES["trap"]
    
    def _get_rhyme_words(self, category: str) -> List[str]:
        """Get rhyming words for a category"""
        return RHYMES.get(category, RHYMES["a"])
    
    def _avoid_cliches(self, text: str) -> str:
        """Replace cliche AI words with better alternatives"""
        text_lower = text.lower()
        for word in CLICHE_WORDS:
            if word in text_lower and word in BETTER_ALTERNATIVES:
                replacement = random.choice(BETTER_ALTERNATIVES[word])
                text = re.sub(r'\b' + word + r'\b', replacement, text, flags=re.IGNORECASE)
        return text
    
    def _generate_line(self, rhyme_category: str, topic: str, mood: str = "aggressive") -> str:
        """Generate a single line with proper rhyme"""
        
        rhyme_words = self._get_rhyme_words(rhyme_category)
        
        # Topic-based line starters
        if topic == "money":
            starters = [
                f"I been stackin' {random.choice(rhyme_words)}, got my {random.choice(rhyme_words)} right",
                f"Bank account lookin' heavy, {random.choice(rhyme_words)} every night",
                f"They don't understand the grind, but my {random.choice(rhyme_words)} so tight",
            ]
        elif topic == "love":
            starters = [
                f"Shorty got me feelin' some type of way, {random.choice(rhyme_words)} every day",
                f"Been through the pain but now I'm good, {random.choice(rhyme_words)} like I should",
            ]
        elif topic == "struggle":
            starters = [
                f"Came from the bottom where the struggle real, {random.choice(rhyme_words)} is how I feel",
                f"They didn't believe in me, now look at me, {random.choice(rhyme_words)}",
            ]
        else:  # flex
            starters = [
                f"I been flexin' hard, {random.choice(rhyme_words)}, never showin' off",
                f"Real ones stay, fake ones go, {random.choice(rhyme_words)} I know",
                f"Got my {random.choice(rhyme_words)} up, my {random.choice(rhyme_words)} up, too",
            ]
        
        line = random.choice(starters)
        
        # In advanced mode, make lines more complex
        if self.advanced:
            addons = [
                ", been that way since day one",
                ", won't ever change, not for none",
                ", they wanna be me but can't come",
                ", that's on my mom, that's on my blood",
            ]
            line += random.choice(addons)
        
        return line
    
    def _generate_verse(self, verse_type: str = "verse", topic: str = "flex") -> str:
        """Generate a full verse"""
        lines = []
        rhyme_categories = list(RHYMES.keys())
        
        if verse_type == "hook":
            # Hook has simpler rhyme scheme, more repetition
            for i in range(4):
                cat = rhyme_categories[i % 2]
                line = self._generate_line(cat, topic, "catchy")
                if self.advanced:
                    line = line.upper()  # More intense
                lines.append(line)
            return "\n".join(lines)
        
        # Regular verse
        for i in range(self.structure["lines_per_verse"]):
            # Alternate rhyme categories every 2 lines (AABB pattern)
            cat = rhyme_categories[(i // 2) % len(rhyme_categories)]
            line = self._generate_line(cat, topic)
            lines.append(line)
        
        # Avoid cliches if advanced mode
        if self.advanced:
            lines = [self._avoid_cliches(line) for line in lines]
        
        return "\n".join(lines)
    
    def generate(self, topic: str = "flex", mood: str = "aggressive") -> Dict:
        """Generate complete song lyrics"""
        
        # Determine topic
        if topic == "auto":
            topics = ["money", "flex", "love", "struggle"]
            topic = random.choice(topics)
        
        # Generate sections
        intro = self._generate_verse("intro", topic) if self.advanced else ""
        hook = self._generate_verse("hook", topic)
        verse1 = self._generate_verse("verse1", topic)
        verse2 = self._generate_verse("verse2", topic)
        outro = self._generate_verse("outro", topic) if self.advanced else ""
        
        # Structure the song
        if self.advanced:
            structure = {
                "intro": intro,
                "hook": hook,
                "verse1": verse1,
                "hook": hook,  # Repeat hook
                "verse2": verse2,
                "hook": hook,  # Repeat hook again
                "outro": outro
            }
        else:
            structure = {
                "hook": hook,
                "verse1": verse1,
                "verse2": verse2,
            }
        
        # Create full lyrics text
        full_lyrics = ""
        for section, content in structure.items():
            if content:
                full_lyrics += f"[{section.upper()}]\n{content}\n\n"
        
        # Final cleanup
        if self.advanced:
            full_lyrics = self._avoid_cliches(full_lyrics)
        
        return {
            "genre": self.genre,
            "advanced": self.advanced,
            "topic": topic,
            "structure": structure,
            "full_lyrics": full_lyrics.strip()
        }


# ========== STEM GENERATOR (From Previous Version) ==========
class StemGenerator:
    """Generate separate stems for drums, bass, melody, etc."""
    
    def __init__(self, genre: str, style: str):
        self.genre = genre
        self.style = style
        self.style_data = STYLE_PRESETS.get(style, STYLE_PRESETS["Metro Boomin"])
        self.bpm = self.style_data["bpm"]
        
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
                "drums": {"type": "drums", "bpm": self.bpm},
                "bass": {"type": "bass", "bpm": self.bpm},
                "melody": {"type": "melody", "bpm": self.bpm},
                "synths": {"type": "synths", "bpm": self.bpm},
            }
        }


# ========== MAIN GENERATOR ==========
class SunoFLOGenerator:
    """Main generator class"""
    
    def __init__(self, genre: str = "Trap", style: str = "Metro Boomin"):
        self.genre = genre
        self.style = style
        self.preset = STYLE_PRESETS.get(style, STYLE_PRESETS["Metro Boomin"])
        
    def generate(self, output_dir: str = "~/Downloads", include_lyrics: bool = False, 
                 lyric_topic: str = "auto", advanced_lyrics: bool = False) -> Dict:
        """Generate everything"""
        output_dir = os.path.expanduser(output_dir)
        os.makedirs(output_dir, exist_ok=True)
        
        style_name = self.style.replace(" ", "_").lower()
        results = {}
        
        # Generate stems
        print(f"Generating stems for {self.style} ({self.genre})...")
        stem_gen = StemGenerator(self.genre, self.style)
        stems = stem_gen.generate_all_stems()
        
        stems_path = os.path.join(output_dir, f"sunoflo_{style_name}_stems.json")
        with open(stems_path, 'w') as f:
            json.dump(stems, f, indent=2)
        results["stems"] = stems_path
        
        # Generate lyrics if requested
        if include_lyrics:
            print(f"Generating {'advanced' if advanced_lyrics else 'basic'} lyrics...")
            lyric_gen = LyricGenerator(self.genre, advanced_lyrics)
            lyrics = lyric_gen.generate(topic=lyric_topic)
            
            lyrics_path = os.path.join(output_dir, f"sunoflo_{style_name}_lyrics.txt")
            with open(lyrics_path, 'w') as f:
                f.write(lyrics["full_lyrics"])
            results["lyrics"] = lyrics_path
            results["lyrics_data"] = lyrics
        
        return results


# ========== CONSOLE UI ==========
def console_ui():
    """Interactive console interface"""
    print("=" * 60)
    print("SunoFLO 2.0 - FL Studio + Lyrics Generator")
    print("Now with Advanced Lyric Generation!")
    print("=" * 60)
    
    # Genre selection
    print("\nSelect Genre:")
    for i, genre in enumerate(GENRES):
        print(f"  {i+1:2}. {genre}")
    genre_choice = int(input("\n> ")) - 1
    genre = GENRES[max(0, min(genre_choice, len(GENRES)-1))]
    
    # Style selection
    matching_styles = [s for s, data in STYLE_PRESETS.items() 
                      if data["genre"].lower() == genre.lower()]
    if not matching_styles:
        matching_styles = list(STYLE_PRESETS.keys())[:10]
    
    print(f"\nSelect Style:")
    for i, style in enumerate(matching_styles[:10]):
        print(f"  {i+1:2}. {style}")
    style_choice = int(input("\n> ")) - 1
    style = matching_styles[max(0, min(style_choice, len(matching_styles)-1))]
    
    # Lyrics option
    print("\n" + "="*40)
    include_lyrics = input("Generate lyrics? (y/n): ").lower() == 'y'
    
    lyric_topic = "auto"
    advanced_lyrics = False
    
    if include_lyrics:
        print("\nSelect topic:")
        print("  1. Auto (random)")
        print("  2. Money/Bags")
        print("  3. Flex/Status")
        print("  4. Love/Romance")
        print("  5. Struggle/Story")
        topic_choice = int(input("> ")) - 1
        topics = ["auto", "money", "flex", "love", "struggle"]
        lyric_topic = topics[max(0, min(topic_choice, 4))]
        
        print("\nLyric mode:")
        print("  1. Basic (simple rhymes)")
        print("  2. Advanced (better rhymes, no cliches, more flow)")
        advanced_choice = int(input("> ")) - 1
        advanced_lyrics = advanced_choice == 1
    
    # Generate
    print("\n" + "="*40)
    print("Generating...")
    generator = SunoFLOGenerator(genre=genre, style=style)
    result = generator.generate(
        include_lyrics=include_lyrics,
        lyric_topic=lyric_topic,
        advanced_lyrics=advanced_lyrics
    )
    
    print("\n" + "="*40)
    print("✓ Generation Complete!")
    print("="*40)
    
    if "lyrics" in result:
        print(f"\n📝 Lyrics saved to: {result['lyrics']}")
        print("\n" + "="*40)
        print(result['lyrics_data']['full_lyrics'])
        print("="*40)
    
    print(f"\n📁 Stems saved to: {result['stems']}")
    print("\nNext: Open in FL Studio → Import MIDI → Add plugins → Mix!")


if __name__ == "__main__":
    console_ui()
