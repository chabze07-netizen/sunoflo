"""
SunoFLO - Ultimate Version
Massive Lyric Library + Artist Styles + Suno Prompts
"""

import random
import json

# ========== MASSIVE ARTIST LIBRARY ==========
ARTIST_STYLES = {
    # TRAP
    "Metro Boomin": {"bpm": 140, "key": "C minor", "genre": "Trap", "desc": "Dark 808s, bell melodies, half-time", "instruments": ["Sytrus", "Harmor", "FPC"], "mood": "dark"},
    "Southside": {"bpm": 140, "key": "G minor", "genre": "Trap", "desc": "Heavy 808 slides, crispy hi-hats", "instruments": ["Sytrus", "Harmor", "FPC"], "mood": "aggressive"},
    "Wheezy": {"bpm": 146, "key": "D minor", "genre": "Trap", "desc": "Guitar/flute melodies, spacey", "instruments": ["Sytrus", "Harmor", "Sakura"], "mood": "spacey"},
    "Nick Mira": {"bpm": 130, "key": "A minor", "genre": "Trap", "desc": "Emo/melodic, layered pianos", "instruments": ["Sytrus", "Harmor"], "mood": "emo"},
    "Pi'erre Bourne": {"bpm": 146, "key": "E minor", "genre": "Trap", "desc": "Bouncy drums, harp leads", "instruments": ["Sytrus", "Harmor"], "mood": "bouncy"},
    "Travis Scott": {"bpm": 140, "key": "C minor", "genre": "Trap", "desc": "Auto-tune, ethereal, heavy reverb", "instruments": ["Sytrus", "Harmor"], "mood": "ethereal"},
    "Zaytoven": {"bpm": 140, "key": "F minor", "genre": "Trap", "desc": "Orchestral 808s, church organs", "instruments": ["Sytrus", "Harmor"], "mood": "orchestral"},
    "London On Da Track": {"bpm": 145, "key": "G minor", "genre": "Trap", "desc": "Young Thug style, bouncy", "instruments": ["Sytrus", "Harmor"], "mood": "bouncy"},
    "Tay Keith": {"bpm": 145, "key": "C minor", "genre": "Trap", "desc": "Hard 808s, minimal", "instruments": ["Sytrus", "FPC"], "mood": "hard"},
    "Cash Cobain": {"bpm": 138, "key": "D minor", "genre": "Trap", "desc": "Sample drill, gritty 808s", "instruments": ["Sytrus", "FPC"], "mood": "gritty"},
    
    # R&B
    "The Weeknd": {"bpm": 120, "key": "E minor", "genre": "R&B", "desc": "Dark R&B, atmospheric", "instruments": ["Harmor", "Sytrus"], "mood": "dark"},
    "Drake": {"bpm": 85, "key": "D minor", "genre": "R&B", "desc": "Melodic rap, emotional", "instruments": ["Sytrus", "Harmor"], "mood": "emotional"},
    "SZA": {"bpm": 95, "key": "C minor", "genre": "R&B", "desc": "Alternative R&B, introspective", "instruments": ["Harmor", "Sytrus"], "mood": " introspective"},
    "Bryson Tiller": {"bpm": 90, "key": "G minor", "genre": "R&B", "desc": "Trap-soul, moody", "instruments": ["Sytrus", "Harmor"], "mood": "moody"},
    "Giveon": {"bpm": 88, "key": "D minor", "genre": "R&B", "desc": "Deep baritone, romantic", "instruments": ["Harmor"], "mood": "romantic"},
    "H.E.R.": {"bpm": 92, "key": "A minor", "genre": "R&B", "desc": "Guitar-driven, soulful", "instruments": ["Harmor", "Sytrus"], "mood": "soulful"},
    
    # HIP HOP
    "Kendrick Lamar": {"bpm": 120, "key": "D minor", "genre": "Hip Hop", "desc": "Conscious, storytelling", "instruments": ["Sytrus", "Harmor"], "mood": "conscious"},
    "J Cole": {"bpm": 90, "key": "G minor", "genre": "Hip Hop", "desc": "Thoughtful, melodic", "instruments": ["Sytrus", "Harmor"], "mood": "thoughtful"},
    "Nas": {"bpm": 92, "key": "C minor", "genre": "Hip Hop", "desc": "Boom bap, lyrical", "instruments": ["Sytrus"], "mood": "lyrical"},
    "Jay-Z": {"bpm": 95, "key": "D minor", "genre": "Hip Hop", "desc": "Marcy Marquis style", "instruments": ["Sytrus"], "mood": "classic"},
    "Kanye West": {"bpm": 130, "key": "F minor", "genre": "Hip Hop", "desc": "Chipmunk soul, production", "instruments": ["Sytrus", "Harmor"], "mood": "soulful"},
    "MF DOOM": {"bpm": 90, "key": "A minor", "genre": "Hip Hop", "desc": "Abstract, lo-fi", "instruments": ["Harmor"], "mood": "abstract"},
    
    # TRANCE
    "Armin van Buuren": {"bpm": 138, "key": "A minor", "genre": "Trance", "desc": "Uplifting, big drops", "instruments": ["Sytrus", "Harmor"], "mood": "uplifting"},
    "Tiesto": {"bpm": 136, "key": "G minor", "genre": "Trance", "desc": "EDM-Trance hybrid", "instruments": ["Sytrus", "Harmor"], "mood": "energetic"},
    "Dash Berlin": {"bpm": 138, "key": "C minor", "genre": "Trance", "desc": "Emotional, melodic", "instruments": ["Harmor", "Sytrus"], "mood": "emotional"},
    "Paul van Dyk": {"bpm": 140, "key": "B minor", "genre": "Trance", "desc": "Progressive, euphoric", "instruments": ["Sytrus", "Harmor"], "mood": "euphoric"},
    "Gouryella": {"bpm": 140, "key": "E minor", "genre": "Trance", "desc": "Classic uplift, massive reverb", "instruments": ["Harmor", "Sytrus"], "mood": "uplifting"},
    "Orjan Nilsen": {"bpm": 138, "key": "D minor", "genre": "Trance", "desc": "Dark trance, tech elements", "instruments": ["Sytrus"], "mood": "dark"},
    "Aly & Fila": {"bpm": 138, "key": "A minor", "genre": "Trance", "desc": "Egyptian trance", "instruments": ["Sytrus", "Harmor"], "mood": "uplifting"},
    
    # HOUSE
    "David Guetta": {"bpm": 128, "key": "C major", "genre": "House", "desc": "Electro house, big drops", "instruments": ["Sytrus", "Harmor"], "mood": "energetic"},
    "Calvin Harris": {"bpm": 128, "key": "D major", "genre": "House", "desc": "Pop-house, catchy", "instruments": ["Sytrus", "Harmor"], "mood": "catchy"},
    "Fisher": {"bpm": 124, "key": "E minor", "genre": "House", "desc": "Tech house, bass-heavy", "instruments": ["Sytrus", "FPC"], "mood": "bass-heavy"},
    "Daft Punk": {"bpm": 123, "key": "A minor", "genre": "House", "desc": "French house, funky", "instruments": ["Harmor", "Sytrus"], "mood": "funky"},
    "Diplo": {"bpm": 100, "key": "G major", "genre": "House", "desc": "World house, festival", "instruments": ["Sytrus", "Harmor"], "mood": "festival"},
    "Disclosure": {"bpm": 124, "key": "F minor", "genre": "House", "desc": "UK garage, deep", "instruments": ["Harmor", "Sytrus"], "mood": "deep"},
    
    # ROCK
    "Pink Floyd": {"bpm": 120, "key": "G minor", "genre": "Rock", "desc": "Psychedelic, space rock", "instruments": ["Harmor", "GMS"], "mood": "psychedelic"},
    "Queen": {"bpm": 120, "key": "B minor", "genre": "Rock", "desc": "Rock anthems, operatic", "instruments": ["Sytrus", "Harmor"], "mood": "anthem"},
    "Metallica": {"bpm": 130, "key": "E minor", "genre": "Rock", "desc": "Heavy metal, thrash", "instruments": ["Sytrus"], "mood": "heavy"},
    "Nirvana": {"bpm": 120, "key": "F minor", "genre": "Rock", "desc": "Grunge, alternative", "instruments": ["Harmor"], "mood": "grunge"},
    "AC/DC": {"bpm": 130, "key": "A minor", "genre": "Rock", "desc": "Hard rock, blues-based", "instruments": ["Sytrus"], "mood": "hard"},
    
    # EDM
    "Deadmau5": {"bpm": 128, "key": "F minor", "genre": "EDM", "desc": "Progressive, glitchy", "instruments": ["Sytrus", "Harmor"], "mood": "progressive"},
    "Skrillex": {"bpm": 140, "key": "D minor", "genre": "Dubstep", "desc": "Dubstep, heavy bass", "instruments": ["Sytrus"], "mood": "heavy"},
    "Excision": {"bpm": 140, "key": "D minor", "genre": "Dubstep", "desc": "Riddim, massive bass", "instruments": ["Sytrus"], "mood": "heavy"},
    
    # AMBIENT
    "Boards of Canada": {"bpm": 90, "key": "C minor", "genre": "Ambient", "desc": "Ambient, retro synths", "instruments": ["Harmor"], "mood": "ambient"},
    "Tycho": {"bpm": 100, "key": "D major", "genre": "Ambient", "desc": "Chillwave, atmospheric", "instruments": ["Harmor"], "mood": "chill"},
    "Brian Eno": {"bpm": 70, "key": "E minor", "genre": "Ambient", "desc": "Ambient pioneer", "instruments": ["Harmor"], "mood": "ambient"},
    
    # PHONK
    "Lost Boy": {"bpm": 140, "key": "C minor", "genre": "Phonk", "desc": "Cowbell phonk", "instruments": ["Sytrus", "FPC"], "mood": "aggressive"},
    "South Phonk": {"bpm": 145, "key": "G minor", "genre": "Phonk", "desc": "Drift phonk", "instruments": ["Sytrus", "Harmor"], "mood": "drift"},
    "Yung Mal": {"bpm": 142, "key": "F minor", "genre": "Phonk", "desc": "ATL phonk", "instruments": ["Sytrus"], "mood": "aggressive"},
}

# ========== MASSIVE LYRIC THEMES ==========
LYRIC_THEMES = {
    "flex": {
        "topics": ["money", "success", "status", "power", "luxury"],
        "mood": "aggressive, confident",
        "lines": [
            "Started from the bottom, now I'm here",
            "They don't know the struggle, but they know the fame",
            "Bank account look different, it's a different view",
            "I was down bad, now I'm counting bands",
            "Flex on 'em, they can't do what I do",
            "Got my money right, never second guess",
            "From the trap to the top, that's success",
            "Real ones stayed, fake ones left",
        ]
    },
    "struggle": {
        "topics": ["hardship", "grind", "pain", "growth", "triumph"],
        "mood": "emotional, reflective",
        "lines": [
            "Came from nothing, had to fight to get this",
            "They didn't believe, now they can't deny",
            "Late nights grinding while they were sleeping",
            "Pain made me stronger, now I'm reaping",
            "Started with nothing but a dream and drive",
            "Every scar on my back, I wear with pride",
            "From the mud to the top, I survived",
            "They tried to break me, now I'm elevated",
        ]
    },
    "love": {
        "topics": ["romance", "lust", "heartbreak", "devotion"],
        "mood": "romantic, emotional",
        "lines": [
            "You're the one I need, can't let you go",
            "Late nights thinking 'bout you, I can't sleep",
            "Heart full of love, but it been hurt before",
            "You my ride or die, that's for sure",
            "Never thought I'd find love like this",
            "With you I found what I been missing",
            "Baby you're my everything",
            "We meant to be, that's what I believe",
        ]
    },
    "hustle": {
        "topics": ["work", "grind", "ambition", "goals"],
        "mood": "motivational, driven",
        "lines": [
            "Wake up early, go to work, that's the grind",
            "Stack paper, that's the mission",
            "No days off, that's the vision",
            "Hustle hard, never stop",
            "Got my eyes on the prize, won't stop",
            "Working twice as hard to get ahead",
            "They don't know the hours I put in",
            "Grind never stops, that's how I live",
        ]
    },
    "party": {
        "topics": ["celebration", "vibes", "turn up"],
        "mood": "energetic, fun",
        "lines": [
            "Tonight we turning up, no sleep",
            "DJ play my song, let me hear it bump",
            "Shots coming fast, we about to drunk",
            "Party don't stop, that's how we funk",
            "In the club with my squad, we lit",
            "Celebrating every win, that's it",
            "Turn the music up, let it bump",
            "We don't quit, we just jump",
        ]
    },
    "street": {
        "topics": ["reality", "block", "survival", "loyalty"],
        "mood": "raw, honest",
        "lines": [
            "On my block, that's where I'm from",
            "Real ones know, fake ones don't",
            "The struggle real, can't fake that",
            "Block taught me how to get bread",
            "Streets talk, I listen, I learned",
            "Real is rare, fake is common",
            "From the block to the check",
            "This the life, no pretending",
        ]
    }
}

# ========== SONG STRUCTURES ==========
SONG_STRUCTURES = {
    "classic": {
        "sections": ["Intro", "Verse 1", "Hook", "Verse 2", "Hook", "Bridge", "Hook", "Outro"],
        "pattern": "I-V1-H-V2-H-B-H-O"
    },
    "modern": {
        "sections": ["Intro", "Hook", "Verse 1", "Hook", "Verse 2", "Hook", "Outro"],
        "pattern": "I-H-V1-H-V2-H-O"
    },
    "trap": {
        "sections": ["Intro", "Verse 1", "Pre-Hook", "Hook", "Verse 2", "Hook", "Verse 3", "Hook"],
        "pattern": "I-V1-PH-H-V2-H-V3-H"
    },
    "rn_b": {
        "sections": ["Intro", "Verse 1", "Hook", "Verse 2", "Hook", "Bridge", "Hook", "Outro"],
        "pattern": "I-V1-H-V2-H-B-H-O"
    },
    "trance": {
        "sections": ["Intro", "Break", "Build", "Drop 1", "Break", "Build", "Drop 2", "Outro"],
        "pattern": "I-B-BD1-B-BD2-O"
    },
    "rock": {
        "sections": ["Intro", "Verse 1", "Pre-Chorus", "Chorus", "Verse 2", "Chorus", "Bridge", "Chorus", "Outro"],
        "pattern": "I-V1-PC-V2-B-BC-O"
    }
}

# ========== SUNO PROMPT TEMPLATES ==========
SUNO_PROMPTS = {
    "trap": {
        "template": "Dark {genre} beat, {bpm} BPM, {key}, {mood}, heavy 808s, {instrument} melody, crispy hi-hats, hard-hitting drums, {adlib}, synth lead, aggressive bass, modern {genre} production",
        "adlibs": ["yeah", "uh", "gang", "flex", "hunnid"]
    },
    "rnb": {
        "template": "{genre} track, {bpm} BPM, {key}, {mood}, smooth {instrument} chords, soft drums, atmospheric pad, romantic melody, emotional vocals, soulful production",
        "adlibs": ["baby", "oh", "love", "yeah"]
    },
    "hip_hop": {
        "template": "{genre} boom bap beat, {bpm} BPM, {key}, {mood}, classic drum pattern, dusty sample, {instrument} loop, bass-heavy, lyrical instrumental",
        "adlibs": ["yeah", "uh", "bruh"]
    },
    "trance": {
        "template": "{genre} anthem, {bpm} BPM, {key}, {mood}, soaring synth lead, massive reverb, driving bass, uplifting arpeggio, euphoric buildup, huge drop, festival-ready",
        "adlibs": ["rise", "go", "let it go"]
    },
    "house": {
        "template": "{genre} groove, {bpm} BPM, {key}, {mood}, four-on-the-floor kick, catchy synth hook, groovy bassline, energetic build, festival anthem",
        "adlibs": ["yeah", "come on"]
    },
    "rock": {
        "template": "{genre} track, {bpm} BPM, {key}, {mood}, distorted guitar riff, powerful drums, anthemic chorus, raw energy, {instrument} driven",
        "adlibs": ["yeah", "rock"]
    },
    "phonk": {
        "template": "{genre} beat, {bpm} BPM, {key}, {mood}, cowbell, heavy 808s, distorted hi-hats, Memphis style, {instrument} melody, aggressive, dark",
        "adlibs": ["drift", "skrrt", "fuck"]
    }
}

# ========== MAIN GENERATOR ==========
class SunoFLO_Ultimate:
    def __init__(self, artist="Metro Boomin", theme="flex", structure="trap"):
        self.artist = artist
        self.theme = theme
        self.structure = structure
        self.style = ARTIST_STYLES.get(artist, ARTIST_STYLES["Metro Boomin"])
        self.theme_data = LYRIC_THEMES.get(theme, LYRIC_THEMES["flex"])
        self.song_structure = SONG_STRUCTURES.get(structure, SONG_STRUCTURES["classic"])
    
    def generate_lyrics(self) -> str:
        """Generate structured lyrics"""
        lines = self.theme_data["lines"]
        structure = self.song_structure["sections"]
        
        lyrics = []
        
        for section in structure:
            lyrics.append(f"[{section.upper()}]")
            
            if "Hook" in section or "Chorus" in section:
                # Hook - catchy, short
                for _ in range(4):
                    lyrics.append(random.choice(lines))
            elif "Verse" in section:
                # Verse - storytelling
                for _ in range(8):
                    lyrics.append(random.choice(lines))
            elif "Intro" in section or "Outro" in section:
                lyrics.append(random.choice(lines[:2]))
            elif "Break" in section or "Bridge" in section:
                lyrics.append(random.choice(lines[2:4]))
            elif "Pre" in section:
                lyrics.append(random.choice(lines[:4]))
            
            lyrics.append("")
        
        return "\n".join(lyrics)
    
    def generate_suno_prompt(self) -> str:
        """Generate optimized Suno AI prompt"""
        genre = self.style["genre"].lower()
        prompt_template = SUNO_PROMPTS.get(genre, SUNO_PROMPTS["trap"])
        
        prompt = prompt_template["template"].format(
            genre=genre,
            bpm=self.style["bpm"],
            key=self.style["key"],
            mood=self.style["mood"],
            instrument=random.choice(self.style["instruments"]),
            adlib=random.choice(prompt_template["adlibs"])
        )
        
        return prompt
    
    def generate_project(self) -> dict:
        """Generate complete project"""
        return {
            "artist": self.artist,
            "style": self.style,
            "theme": self.theme,
            "structure": self.structure,
            "bpm": self.style["bpm"],
            "key": self.style["key"],
            "lyrics": self.generate_lyrics(),
            "suno_prompt": self.generate_suno_prompt()
        }

# ========== CLI ==========
def main():
    print("=" * 60)
    print("SunoFLO - ULTIMATE VERSION")
    print("Massive Library - 50+ Artists - Suno Prompts")
    print("=" * 60)
    
    # List artists by genre
    print("\n📋 ARTISTS BY GENRE:")
    genres = {}
    for artist, data in ARTIST_STYLES.items():
        g = data["genre"]
        if g not in genres:
            genres[g] = []
        genres[g].append(artist)
    
    for genre, artists in genres.items():
        print(f"\n{genre}: {', '.join(artists[:5])}{'...' if len(artists) > 5 else ''}")
    
    # Select artist
    print("\n" + "="*40)
    artists_list = list(ARTIST_STYLES.keys())
    for i, artist in enumerate(artists_list):
        print(f"{i+1:3}. {artist}")
    
    a = int(input("\nSelect Artist > ")) - 1
    artist = artists_list[max(0, min(a, len(artists_list)-1))]
    
    # Select theme
    print("\n📝 THEMES:")
    themes = list(LYRIC_THEMES.keys())
    for i, theme in enumerate(themes):
        print(f"{i+1:3}. {theme}")
    
    t = int(input("Select Theme > ")) - 1
    theme = themes[max(0, min(t, len(themes)-1))]
    
    # Select structure
    print("\n🎵 SONG STRUCTURES:")
    structures = list(SONG_STRUCTURES.keys())
    for i, s in enumerate(structures):
        print(f"{i+1:3}. {s}")
    
    s = int(input("Select Structure > ")) - 1
    structure = structures[max(0, min(s, len(structures)-1))]
    
    # Generate
    print("\n" + "="*40)
    print("Generating...")
    
    flo = SunoFLO_Ultimate(artist, theme, structure)
    project = flo.generate_project()
    
    print("\n" + "="*60)
    print(f"🎤 {project['artist']}")
    print(f"📀 BPM: {project['bpm']} | Key: {project['key']}")
    print(f"🎵 Structure: {project['structure']}")
    print("="*60)
    
    print("\n📝 LYRICS:")
    print(project['lyrics'])
    
    print("\n" + "="*60)
    print("� Suno AI Prompt (copy this to Suno):")
    print("="*60)
    print(project['suno_prompt'])
    print("="*60)
    
    # Save
    with open(f"/home/simon/Downloads/sunoflo_ultimate_{artist.replace(' ', '_')}.txt", "w") as f:
        f.write(f"Artist: {project['artist']}\n")
        f.write(f"BPM: {project['bpm']}, Key: {project['key']}\n\n")
        f.write("LYRICS:\n")
        f.write(project['lyrics'])
        f.write("\n\nSUNO PROMPT:\n")
        f.write(project['suno_prompt'])
    
    print(f"\n✅ Saved to ~/Downloads/sunoflo_ultimate_{artist.replace(' ', '_')}.txt")

if __name__ == "__main__":
    main()
