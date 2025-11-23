# generator.py

KANJI_DB = {
    # A系
    "a": [
        {"kanji": "愛", "meaning_en": "love, affection", "description": "Represents deep love and affection. This character embodies warmth, care, and emotional connection.", "tags": ["kind", "soft", "cute"]},
        {"kanji": "亜", "meaning_en": "Asia, second", "description": "Originally meaning 'Asia' or 'second'. Conveys a sense of strength and connection to the East.", "tags": ["cool", "strong"]},
        {"kanji": "彩", "meaning_en": "color, beauty", "description": "Symbolizes vibrant colors and artistic beauty. Perfect for creative and expressive personalities.", "tags": ["cute", "soft"]},
        {"kanji": "明", "meaning_en": "bright, clear", "description": "Represents brightness, clarity, and intelligence. Suggests a person who illuminates others' lives.", "tags": ["smart", "cool"]},
        {"kanji": "空", "meaning_en": "sky, heaven", "description": "Evokes the boundless sky and freedom. Represents limitless potential and dreams.", "tags": ["soft", "cool"]},
        {"kanji": "藍", "meaning_en": "indigo", "description": "A deep blue color, symbolizing depth, sophistication, and tranquility.", "tags": ["cool", "soft"]},
        {"kanji": "蒼", "meaning_en": "blue, pale", "description": "Represents the pale blue of the sky or sea. Conveys elegance and natural beauty.", "tags": ["cool", "strong"]},
    ],
    "ai": [
        {"kanji": "愛", "meaning_en": "love", "description": "The ultimate expression of love and compassion. One of the most cherished characters in Japanese.", "tags": ["kind", "soft", "cute"]},
        {"kanji": "藍", "meaning_en": "indigo", "description": "Deep indigo blue, representing sophistication and calm depth.", "tags": ["cool", "soft"]},
        {"kanji": "哀", "meaning_en": "sorrow, pity", "description": "Expresses empathy and emotional depth. Represents sensitivity and understanding.", "tags": ["soft"]},
    ],
    "an": [
        {"kanji": "杏", "meaning_en": "apricot", "description": "The apricot blossom symbolizes gentle beauty and sweetness. Associated with spring and renewal.", "tags": ["cute", "soft"]},
        {"kanji": "安", "meaning_en": "peace, calm", "description": "Represents peace, safety, and tranquility. A character that brings comfort and stability.", "tags": ["kind", "soft"]},
        {"kanji": "庵", "meaning_en": "hermitage, cottage", "description": "A peaceful retreat or cottage. Symbolizes simplicity and serenity.", "tags": ["soft", "cool"]},
    ],
    "ao": [
        {"kanji": "葵", "meaning_en": "hollyhock, althea", "description": "A beautiful flower symbolizing nobility and grace. Often associated with elegance.", "tags": ["cute", "soft"]},
        {"kanji": "碧", "meaning_en": "blue, green", "description": "The color of clear ocean or jade. Represents purity and natural beauty.", "tags": ["cool", "strong"]},
        {"kanji": "青", "meaning_en": "blue, green", "description": "The color of youth, freshness, and vitality. Symbolizes new beginnings.", "tags": ["cool", "strong"]},
    ],
    
    # E系
    "e": [
        {"kanji": "恵", "meaning_en": "blessing, kindness", "description": "Represents divine blessings and generous kindness. A character of grace and benevolence.", "tags": ["kind", "soft"]},
        {"kanji": "英", "meaning_en": "hero, excellence", "description": "Symbolizes heroism, excellence, and outstanding ability. Perfect for leaders and achievers.", "tags": ["strong", "cool"]},
        {"kanji": "絵", "meaning_en": "picture, painting", "description": "Represents artistic expression and creativity. Associated with visual beauty and imagination.", "tags": ["cute", "soft"]},
        {"kanji": "江", "meaning_en": "inlet, bay", "description": "A body of water, representing flow, adaptability, and connection.", "tags": ["cool", "smart"]},
        {"kanji": "慧", "meaning_en": "wisdom, intelligence", "description": "Deep wisdom and sharp intelligence. Represents mental clarity and insight.", "tags": ["smart", "cool"]},
        {"kanji": "笑", "meaning_en": "smile, laugh", "description": "Represents joy, laughter, and happiness. Brings warmth and positivity.", "tags": ["cute", "kind"]},
    ],
    "ei": [
        {"kanji": "英", "meaning_en": "excellent, hero", "description": "Excellence and heroic qualities. Represents outstanding achievement and bravery.", "tags": ["strong", "cool"]},
        {"kanji": "栄", "meaning_en": "prosperity, glory", "description": "Symbolizes prosperity, honor, and flourishing success.", "tags": ["strong", "cool"]},
        {"kanji": "瑛", "meaning_en": "sparkle of jewelry", "description": "The brilliant sparkle of gemstones. Represents rare beauty and value.", "tags": ["cute", "cool"]},
        {"kanji": "映", "meaning_en": "reflect, project", "description": "To reflect or project light. Symbolizes influence and radiance.", "tags": ["cool", "smart"]},
    ],
    "en": [
        {"kanji": "円", "meaning_en": "circle, yen", "description": "Represents completeness, harmony, and perfection through its circular shape.", "tags": ["cool", "soft"]},
        {"kanji": "縁", "meaning_en": "connection, fate", "description": "The threads of fate that connect people. Represents destiny and meaningful relationships.", "tags": ["soft", "kind"]},
    ],
    
    # I系
    "i": [
        {"kanji": "衣", "meaning_en": "clothing, elegance", "description": "Represents elegance, refinement, and the beauty of fine garments.", "tags": ["cute", "soft"]},
        {"kanji": "伊", "meaning_en": "Italy, that one", "description": "Originally used for Italy, now conveys sophistication and distinction.", "tags": ["cool"]},
        {"kanji": "依", "meaning_en": "rely on, depend", "description": "Represents trust, support, and interdependence. Symbolizes reliable relationships.", "tags": ["soft", "kind"]},
        {"kanji": "惟", "meaning_en": "consider, reflect", "description": "Deep thought and contemplation. Represents wisdom through reflection.", "tags": ["smart", "cool"]},
        {"kanji": "維", "meaning_en": "maintain, support", "description": "To maintain and preserve. Symbolizes stability and foundational strength.", "tags": ["strong", "cool"]},
    ],
    "in": [
        {"kanji": "音", "meaning_en": "sound, noise", "description": "Represents music, harmony, and the beauty of sound. Perfect for artistic souls.", "tags": ["soft", "cute"]},
        {"kanji": "韻", "meaning_en": "rhyme, rhythm", "description": "The rhythm and flow of poetry and music. Symbolizes artistic harmony.", "tags": ["cool", "smart"]},
    ],
    
    # O系
    "o": [
        {"kanji": "央", "meaning_en": "center, middle", "description": "The center or heart of things. Represents balance and being at the core.", "tags": ["cool", "strong"]},
        {"kanji": "緒", "meaning_en": "cord, beginning", "description": "The cord that binds or the beginning of something. Symbolizes connections and new starts.", "tags": ["soft", "kind"]},
        {"kanji": "桜", "meaning_en": "cherry blossom", "description": "Japan's most beloved flower, symbolizing beauty, renewal, and the fleeting nature of life.", "tags": ["cute", "soft"]},
        {"kanji": "織", "meaning_en": "weave, fabric", "description": "The art of weaving threads together. Represents craftsmanship and intricate beauty.", "tags": ["soft", "cute"]},
        {"kanji": "雄", "meaning_en": "male, hero", "description": "Masculine strength and heroic qualities. Symbolizes power and courage.", "tags": ["strong", "cool"]},
    ],
    "ou": [
        {"kanji": "桜", "meaning_en": "cherry blossom", "description": "The iconic cherry blossom, representing ephemeral beauty and the cycle of life.", "tags": ["cute", "soft"]},
        {"kanji": "欧", "meaning_en": "Europe", "description": "Represents Europe and Western culture. Conveys international sophistication.", "tags": ["cool", "strong"]},
        {"kanji": "王", "meaning_en": "king", "description": "Royal authority and leadership. Symbolizes nobility and commanding presence.", "tags": ["strong", "cool"]},
    ],
    
    # U系
    "u": [
        {"kanji": "優", "meaning_en": "gentle, superior", "description": "Combines gentleness with excellence. Represents grace, kindness, and outstanding ability.", "tags": ["kind", "soft"]},
        {"kanji": "海", "meaning_en": "ocean, sea", "description": "The vast ocean with its depth and mystery. Symbolizes boundless potential and adventure.", "tags": ["cool", "strong"]},
        {"kanji": "羽", "meaning_en": "feather, wing", "description": "Light as a feather, representing freedom, grace, and the ability to soar.", "tags": ["cute", "soft"]},
        {"kanji": "歌", "meaning_en": "song, poem", "description": "The art of song and poetry. Symbolizes artistic expression and emotional depth.", "tags": ["cute", "soft"]},
        {"kanji": "宇", "meaning_en": "universe, space", "description": "The vastness of the universe. Represents cosmic scale and infinite possibilities.", "tags": ["cool", "strong"]},
    ],
    
    # KA系
    "ka": [
        {"kanji": "花", "meaning_en": "flower", "description": "Universal symbol of beauty and growth. Represents blooming potential and natural elegance.", "tags": ["cute", "soft"]},
        {"kanji": "香", "meaning_en": "fragrance", "description": "Pleasant fragrance and aroma. Symbolizes refinement and lasting impressions.", "tags": ["cute", "soft"]},
        {"kanji": "佳", "meaning_en": "excellent, beautiful", "description": "Excellence and beauty combined. Represents admirable qualities and grace.", "tags": ["soft", "kind"]},
        {"kanji": "華", "meaning_en": "splendor, flower", "description": "Magnificent splendor and glory. More elaborate than simple 'flower', suggesting luxury.", "tags": ["strong", "cute"]},
        {"kanji": "夏", "meaning_en": "summer", "description": "The vibrant season of summer. Represents energy, warmth, and vitality.", "tags": ["cool", "strong"]},
        {"kanji": "果", "meaning_en": "fruit, result", "description": "The fruit of one's efforts. Symbolizes achievement and sweet rewards.", "tags": ["cute", "soft"]},
        {"kanji": "歌", "meaning_en": "song, poem", "description": "Musical and poetic expression. Represents harmony and artistic soul.", "tags": ["cute", "soft"]},
        {"kanji": "楓", "meaning_en": "maple", "description": "The maple tree with its beautiful autumn colors. Symbolizes change and natural beauty.", "tags": ["soft", "cool"]},
        {"kanji": "風", "meaning_en": "wind", "description": "The invisible force of wind. Represents freedom, change, and natural power.", "tags": ["cool", "strong"]},
    ],
    "kai": [
        {"kanji": "海", "meaning_en": "ocean, sea", "description": "The mighty ocean with endless horizons. Symbolizes vast potential and adventure.", "tags": ["cool", "strong"]},
        {"kanji": "快", "meaning_en": "pleasant, comfortable", "description": "Pleasant feelings and comfort. Represents joy and well-being.", "tags": ["cool", "kind"]},
        {"kanji": "開", "meaning_en": "open, start", "description": "To open or begin. Symbolizes new opportunities and pioneering spirit.", "tags": ["strong", "cool"]},
        {"kanji": "凱", "meaning_en": "triumph, victory", "description": "Triumphant victory and success. Represents achievement and glory.", "tags": ["strong", "cool"]},
    ],
    "ke": [
        {"kanji": "桂", "meaning_en": "cinnamon tree", "description": "The fragrant cinnamon tree. Symbolizes natural elegance and lasting value.", "tags": ["soft", "kind"]},
        {"kanji": "恵", "meaning_en": "blessing", "description": "Divine blessings and favor. Represents grace and good fortune.", "tags": ["kind", "soft"]},
        {"kanji": "景", "meaning_en": "scenery, view", "description": "Beautiful scenery and landscapes. Symbolizes perspective and natural beauty.", "tags": ["cool", "soft"]},
        {"kanji": "圭", "meaning_en": "jade tablet", "description": "A precious jade tablet used in ancient ceremonies. Represents purity and value.", "tags": ["cool", "strong"]},
    ],
    "ki": [
        {"kanji": "希", "meaning_en": "hope, rare", "description": "Precious hope and rare beauty. Symbolizes optimism and uniqueness.", "tags": ["soft", "kind"]},
        {"kanji": "輝", "meaning_en": "radiance, shine", "description": "Brilliant radiance and shine. Represents luminous presence and glory.", "tags": ["strong", "cool"]},
        {"kanji": "樹", "meaning_en": "tree, timber", "description": "Strong trees and timber. Symbolizes growth, stability, and natural strength.", "tags": ["strong", "cool"]},
        {"kanji": "紀", "meaning_en": "chronicle, era", "description": "Historical records and eras. Represents lasting legacy and significance.", "tags": ["cool", "smart"]},
        {"kanji": "貴", "meaning_en": "precious, noble", "description": "Precious value and nobility. Symbolizes high status and worth.", "tags": ["cool", "strong"]},
        {"kanji": "葵", "meaning_en": "hollyhock", "description": "The noble hollyhock flower. Associated with aristocracy and elegance.", "tags": ["cute", "soft"]},
        {"kanji": "季", "meaning_en": "season", "description": "The changing seasons. Represents natural cycles and timely beauty.", "tags": ["soft", "cool"]},
        {"kanji": "妃", "meaning_en": "queen, princess", "description": "Royal consort or princess. Symbolizes nobility and grace.", "tags": ["cute", "soft"]},
    ],
    "ko": [
        {"kanji": "心", "meaning_en": "heart, mind", "description": "The core of emotions and thoughts. Represents sincerity and inner strength.", "tags": ["kind", "soft"]},
        {"kanji": "湖", "meaning_en": "lake", "description": "Calm, reflective waters of a lake. Symbolizes tranquility and depth.", "tags": ["soft", "cool"]},
        {"kanji": "光", "meaning_en": "light, ray", "description": "Radiant light illuminating darkness. Represents hope, clarity, and guidance.", "tags": ["cool", "strong"]},
        {"kanji": "虹", "meaning_en": "rainbow", "description": "The colorful rainbow after rain. Symbolizes hope, diversity, and beauty.", "tags": ["cute", "soft"]},
        {"kanji": "琴", "meaning_en": "koto (instrument)", "description": "Traditional Japanese string instrument. Represents musical elegance and culture.", "tags": ["soft", "cute"]},
        {"kanji": "幸", "meaning_en": "happiness, fortune", "description": "Good fortune and happiness. One of the most positive characters.", "tags": ["kind", "cute"]},
    ],
    "kou": [
        {"kanji": "幸", "meaning_en": "happiness", "description": "Pure happiness and good fortune. Brings joy and positive energy.", "tags": ["kind", "cute"]},
        {"kanji": "光", "meaning_en": "light", "description": "Brilliant light shining forth. Represents illumination and radiance.", "tags": ["cool", "strong"]},
        {"kanji": "功", "meaning_en": "achievement, merit", "description": "Merit earned through effort. Symbolizes accomplishment and success.", "tags": ["strong", "cool"]},
        {"kanji": "航", "meaning_en": "navigate, sail", "description": "To navigate across oceans. Represents adventure and exploration.", "tags": ["cool", "strong"]},
        {"kanji": "孝", "meaning_en": "filial piety", "description": "Filial piety and respect. Core Confucian value of family devotion.", "tags": ["kind", "strong"]},
        {"kanji": "晃", "meaning_en": "clear, bright", "description": "Bright and shining. Represents radiant clarity.", "tags": ["cool", "strong"]},
        {"kanji": "紅", "meaning_en": "crimson, deep red", "description": "Deep red color. Symbolizes passion and intensity.", "tags": ["strong", "cute"]},
        {"kanji": "煌", "meaning_en": "glitter, gleam", "description": "Glittering brilliance. Represents dazzling beauty.", "tags": ["cool", "strong"]},
        {"kanji": "公", "meaning_en": "public, prince", "description": "Public or noble lord. Symbolizes fairness and nobility.", "tags": ["strong", "cool"]},
        {"kanji": "広", "meaning_en": "wide, spacious", "description": "Wide expanse. Represents breadth and openness.", "tags": ["cool", "strong"]},
        {"kanji": "皇", "meaning_en": "emperor, imperial", "description": "Imperial majesty. Symbolizes supreme authority.", "tags": ["strong", "cool"]},
        {"kanji": "鋼", "meaning_en": "steel", "description": "Hard steel. Symbolizes strength and durability.", "tags": ["strong", "cool"]},
        {"kanji": "香", "meaning_en": "fragrance, incense", "description": "Sweet fragrance. Represents pleasant aroma.", "tags": ["cute", "soft"]},
    ],
    "ku": [
        {"kanji": "空", "meaning_en": "sky, heaven", "description": "The boundless sky above. Symbolizes freedom, dreams, and infinite potential.", "tags": ["cool", "soft"]},
        {"kanji": "久", "meaning_en": "long time, eternity", "description": "Lasting eternally. Represents endurance and timeless quality.", "tags": ["cool", "smart"]},
        {"kanji": "玖", "meaning_en": "beautiful black jewel", "description": "A rare black gemstone. Symbolizes mysterious beauty and value.", "tags": ["cool", "soft"]},
    ],
    
    # GA系
    "ga": [
        {"kanji": "雅", "meaning_en": "elegance, grace", "description": "Refined elegance and graceful sophistication. Represents cultured beauty.", "tags": ["cool", "soft"]},
        {"kanji": "画", "meaning_en": "picture, stroke", "description": "Pictures and artistic strokes. Symbolizes creativity and visual expression.", "tags": ["cool", "smart"]},
        {"kanji": "芽", "meaning_en": "bud, sprout", "description": "A budding sprout full of potential. Represents new growth and promise.", "tags": ["cute", "soft"]},
        {"kanji": "我", "meaning_en": "ego, self", "description": "Self and ego. Represents individual identity and autonomy.", "tags": ["strong", "cool"]},
    ],
    "gi": [
        {"kanji": "義", "meaning_en": "justice, righteousness", "description": "Righteous justice and moral integrity. Represents strong principles and honor.", "tags": ["strong", "cool"]},
        {"kanji": "技", "meaning_en": "skill, technique", "description": "Mastered skills and techniques. Symbolizes expertise and craftsmanship.", "tags": ["cool", "smart"]},
        {"kanji": "宜", "meaning_en": "suitable, proper", "description": "Suitable and appropriate. Represents fitness and propriety.", "tags": ["cool"]},
    ],
    
    # SA系
    "sa": [
        {"kanji": "咲", "meaning_en": "blossom", "description": "Flowers blooming beautifully. Represents flourishing and joyful growth.", "tags": ["cute", "soft"]},
        {"kanji": "沙", "meaning_en": "sand", "description": "Fine sand of beaches. Symbolizes natural beauty and countless possibilities.", "tags": ["soft", "cool"]},
        {"kanji": "紗", "meaning_en": "gauze, silk", "description": "Delicate silk gauze. Represents refined elegance and softness.", "tags": ["cute", "soft"]},
        {"kanji": "佐", "meaning_en": "assistant", "description": "To assist and support. Symbolizes helpful nature and cooperation.", "tags": ["cool", "smart"]},
        {"kanji": "幸", "meaning_en": "happiness", "description": "Happiness and good fortune combined. Brings positive energy.", "tags": ["kind", "cute"]},
        {"kanji": "桜", "meaning_en": "cherry blossom", "description": "Japan's beloved cherry blossom. Symbolizes beauty and the preciousness of life.", "tags": ["cute", "soft"]},
        {"kanji": "彩", "meaning_en": "color", "description": "Vibrant colors and artistic beauty. Represents creativity and expression.", "tags": ["cute", "soft"]},
    ],
    "sai": [
        {"kanji": "彩", "meaning_en": "color, beauty", "description": "Beautiful colors and artistic flair. Symbolizes vibrant personality.", "tags": ["cute", "soft"]},
        {"kanji": "才", "meaning_en": "talent, genius", "description": "Natural talent and genius. Represents exceptional ability.", "tags": ["smart", "cool"]},
        {"kanji": "最", "meaning_en": "most, maximum", "description": "The ultimate or maximum. Symbolizes being at the peak.", "tags": ["strong", "cool"]},
    ],
    "se": [
        {"kanji": "星", "meaning_en": "star", "description": "Stars twinkling in the night sky. Represents dreams, guidance, and celestial beauty.", "tags": ["cute", "cool"]},
        {"kanji": "誠", "meaning_en": "sincerity, truth", "description": "Absolute sincerity and truth. Symbolizes honest and genuine character.", "tags": ["strong", "cool"]},
        {"kanji": "瀬", "meaning_en": "rapids, current", "description": "Fast-flowing rapids. Represents dynamic energy and natural flow.", "tags": ["cool", "strong"]},
    ],
    "shi": [
        {"kanji": "詩", "meaning_en": "poem, poetry", "description": "Beautiful poetry and verse. Represents artistic expression and emotional depth.", "tags": ["soft", "smart"]},
        {"kanji": "志", "meaning_en": "intention, will", "description": "Strong will and determination. Symbolizes purpose-driven character.", "tags": ["strong", "cool"]},
        {"kanji": "紫", "meaning_en": "purple, violet", "description": "The noble color purple. Traditionally associated with royalty and mystery.", "tags": ["cute", "soft"]},
        {"kanji": "史", "meaning_en": "history", "description": "Historical records and legacy. Represents lasting significance.", "tags": ["smart", "cool"]},
        {"kanji": "獅", "meaning_en": "lion", "description": "The mighty lion. Symbolizes courage, strength, and leadership.", "tags": ["strong", "cool"]},
        {"kanji": "士", "meaning_en": "samurai, gentleman", "description": "Warrior gentleman with honor. Represents dignity and martial skill.", "tags": ["strong", "cool"]},
    ],
    "shou": [
        {"kanji": "翔", "meaning_en": "soar, fly", "description": "To soar through the skies. Represents freedom, ambition, and reaching heights.", "tags": ["cool", "strong"]},
        {"kanji": "渉", "meaning_en": "ford, traverse", "description": "To cross waters and overcome obstacles. Symbolizes perseverance.", "tags": ["cool", "strong"]},
        {"kanji": "章", "meaning_en": "chapter, badge", "description": "A chapter or badge of honor. Represents achievement and distinction.", "tags": ["cool", "smart"]},
    ],
    "su": [
        {"kanji": "澄", "meaning_en": "clear, pure", "description": "Crystal clear water. Symbolizes purity, clarity, and transparent honesty.", "tags": ["soft", "cool"]},
        {"kanji": "寿", "meaning_en": "longevity, congratulations", "description": "Long life and celebrations. One of the most auspicious characters.", "tags": ["kind", "strong"]},
        {"kanji": "涼", "meaning_en": "cool, refreshing", "description": "Cool and refreshing breeze. Represents comfort and pleasant atmosphere.", "tags": ["cool", "soft"]},
        {"kanji": "鈴", "meaning_en": "bell", "description": "The clear sound of bells. Symbolizes clarity, joy, and attention.", "tags": ["cute", "soft"]},
    ],
    
    # ZA系
    "za": [
        {"kanji": "座", "meaning_en": "seat, constellation", "description": "Seat or constellation. Represents position and celestial connection.", "tags": ["cool"]},
    ],
    
    # TA系
    "ta": [
        {"kanji": "太", "meaning_en": "thick, big", "description": "Thick and substantial. Represents strength, abundance, and solid foundation.", "tags": ["strong", "cool"]},
        {"kanji": "多", "meaning_en": "many, much", "description": "Abundance and plenty. Symbolizes wealth and variety.", "tags": ["cool"]},
        {"kanji": "大", "meaning_en": "large, great", "description": "Great size and magnitude. Represents grandness and importance.", "tags": ["strong", "cool"]},
        {"kanji": "汰", "meaning_en": "wash, cleanse", "description": "To wash and purify. Symbolizes renewal and clarity.", "tags": ["cool", "strong"]},
        {"kanji": "妥", "meaning_en": "appropriate, settle", "description": "Appropriate and well-settled. Represents harmony and balance.", "tags": ["soft", "cool"]},
    ],
    "tai": [
        {"kanji": "大", "meaning_en": "big, great", "description": "Great and mighty. Symbolizes importance and significant presence.", "tags": ["strong", "cool"]},
        {"kanji": "泰", "meaning_en": "peaceful, great", "description": "Peaceful greatness. Combines strength with tranquility.", "tags": ["strong", "cool"]},
        {"kanji": "太", "meaning_en": "thick, big", "description": "Thick and robust. Represents solid strength and stability.", "tags": ["strong", "cool"]},
    ],
    "chi": [
        {"kanji": "智", "meaning_en": "wisdom", "description": "Deep wisdom and knowledge. Represents intellectual depth and insight.", "tags": ["smart", "cool"]},
        {"kanji": "千", "meaning_en": "thousand", "description": "A thousand, representing abundance and vast numbers. Symbolizes plenty.", "tags": ["cool", "soft"]},
        {"kanji": "知", "meaning_en": "know, wisdom", "description": "To know and understand. Represents learning and intelligence.", "tags": ["smart", "cool"]},
        {"kanji": "地", "meaning_en": "earth, ground", "description": "The solid earth beneath us. Symbolizes foundation and stability.", "tags": ["strong", "cool"]},
    ],
    "tsu": [
        {"kanji": "月", "meaning_en": "moon", "description": "The beautiful moon. Represents mystery, beauty, and cyclical renewal.", "tags": ["soft", "cool"]},
        {"kanji": "都", "meaning_en": "capital, metropolis", "description": "A great capital city. Symbolizes sophistication and centrality.", "tags": ["cool", "strong"]},
        {"kanji": "津", "meaning_en": "harbor, port", "description": "A harbor or port. Represents connection and safe haven.", "tags": ["cool", "strong"]},
    ],
    "te": [
        {"kanji": "天", "meaning_en": "heaven, sky", "description": "The heavens above. Represents divine nature and lofty aspirations.", "tags": ["cool", "strong"]},
        {"kanji": "哲", "meaning_en": "philosophy, wisdom", "description": "Philosophical wisdom. Symbolizes deep thinking and intellectual pursuit.", "tags": ["smart", "cool"]},
    ],
    "to": [
        {"kanji": "人", "meaning_en": "person", "description": "A human being. The most fundamental character representing humanity.", "tags": ["cool"]},
        {"kanji": "斗", "meaning_en": "Big Dipper", "description": "The Big Dipper constellation. Represents guidance and celestial navigation.", "tags": ["cool", "strong"]},
        {"kanji": "音", "meaning_en": "sound", "description": "Sound and music. Symbolizes harmony and artistic expression.", "tags": ["soft", "cute"]},
        {"kanji": "登", "meaning_en": "climb, ascend", "description": "To climb and ascend. Represents ambition and upward progress.", "tags": ["strong", "cool"]},
        {"kanji": "翔", "meaning_en": "soar", "description": "Soaring high in the sky. Symbolizes freedom and achievement.", "tags": ["cool", "strong"]},
        {"kanji": "都", "meaning_en": "capital", "description": "Metropolitan capital. Represents sophistication and importance.", "tags": ["cool", "strong"]},
    ],
    
    # DA系
    "da": [
        {"kanji": "太", "meaning_en": "thick, big", "description": "Thick and substantial. Represents abundance and strength.", "tags": ["strong", "cool"]},
        {"kanji": "大", "meaning_en": "large", "description": "Large and great. Symbolizes importance and grandeur.", "tags": ["strong", "cool"]},
    ],
    "dan": [
        {"kanji": "暖", "meaning_en": "warm", "description": "Warmth and comfort. Represents kindness and nurturing.", "tags": ["kind", "soft"]},
        {"kanji": "壇", "meaning_en": "platform, altar", "description": "Sacred platform or altar. Symbolizes elevated status.", "tags": ["cool", "strong"]},
    ],
    
    # NA系
    "na": [
        {"kanji": "奈", "meaning_en": "Nara, what", "description": "Associated with ancient Nara. Represents cultural heritage and beauty.", "tags": ["soft", "kind"]},
        {"kanji": "菜", "meaning_en": "vegetable, greens", "description": "Fresh vegetables and greens. Symbolizes health, nature, and growth.", "tags": ["cute", "soft"]},
        {"kanji": "那", "meaning_en": "what, beautiful", "description": "Questioning beauty. Represents curiosity and aesthetic appreciation.", "tags": ["cool", "soft"]},
        {"kanji": "南", "meaning_en": "south", "description": "The southern direction. Associated with warmth and sunlight.", "tags": ["cool", "soft"]},
        {"kanji": "七", "meaning_en": "seven", "description": "The lucky number seven. Symbolizes good fortune.", "tags": ["cute", "cool"]},
    ],
    "nao": [
        {"kanji": "直", "meaning_en": "straight, honest", "description": "Straight and honest. Represents integrity and directness.", "tags": ["strong", "cool"]},
        {"kanji": "尚", "meaning_en": "still, furthermore", "description": "Still more, going further. Symbolizes continuous improvement.", "tags": ["cool", "smart"]},
        {"kanji": "奈", "meaning_en": "what, beautiful", "description": "Beautiful questioning. Represents grace from Nara.", "tags": ["soft", "kind"]},
    ],
    "ni": [
        {"kanji": "仁", "meaning_en": "benevolence, compassion", "description": "Benevolence and humanity. One of Confucian core virtues.", "tags": ["kind", "strong"]},
        {"kanji": "虹", "meaning_en": "rainbow", "description": "Beautiful rainbow. Symbolizes hope, promise, and diversity.", "tags": ["cute", "soft"]},
        {"kanji": "二", "meaning_en": "two", "description": "The number two. Represents partnership and balance.", "tags": ["cool"]},
    ],
    "no": [
        {"kanji": "乃", "meaning_en": "from, possessive", "description": "Possessive particle. Elegant and flowing character.", "tags": ["soft", "cool"]},
        {"kanji": "野", "meaning_en": "field, plain", "description": "Open fields and plains. Symbolizes freedom and natural expanse.", "tags": ["cool", "strong"]},
        {"kanji": "希", "meaning_en": "hope, rare", "description": "Hope and rarity. Represents precious optimism.", "tags": ["soft", "kind"]},
    ],
    
    # HA系
    "ha": [
        {"kanji": "羽", "meaning_en": "feather, wing", "description": "Soft feathers and wings. Symbolizes freedom, grace, and flight.", "tags": ["soft", "cute"]},
        {"kanji": "葉", "meaning_en": "leaf", "description": "Green leaves. Represents nature, growth, and renewal.", "tags": ["soft", "cute"]},
        {"kanji": "波", "meaning_en": "wave", "description": "Ocean waves. Symbolizes rhythm, flow, and natural power.", "tags": ["cool", "soft"]},
        {"kanji": "花", "meaning_en": "flower", "description": "Beautiful flowers. Universal symbol of beauty and blooming.", "tags": ["cute", "soft"]},
        {"kanji": "晴", "meaning_en": "clear weather", "description": "Clear sunny skies. Represents optimism and clarity.", "tags": ["cool", "kind"]},
    ],
    "haru": [
        {"kanji": "春", "meaning_en": "spring", "description": "The spring season. Symbolizes renewal, youth, and new beginnings.", "tags": ["soft", "cute"]},
        {"kanji": "晴", "meaning_en": "clear, sunny", "description": "Clear sunny weather. Represents brightness and positive outlook.", "tags": ["cool", "kind"]},
        {"kanji": "治", "meaning_en": "govern, cure", "description": "To govern or heal. Symbolizes order and restoration.", "tags": ["strong", "cool"]},
        {"kanji": "陽", "meaning_en": "sunshine", "description": "Bright sunshine. Symbolizes warmth and positivity.", "tags": ["cool", "strong"]},
        {"kanji": "温", "meaning_en": "warm", "description": "Warmth and gentleness. Represents comfort and kindness.", "tags": ["kind", "soft"]},
    ],
    "hi": [
        {"kanji": "陽", "meaning_en": "sunshine, positive", "description": "Bright sunshine. Represents positivity, warmth, and yang energy.", "tags": ["cool", "strong"]},
        {"kanji": "日", "meaning_en": "sun, day", "description": "The sun and daylight. Symbolizes life, energy, and clarity.", "tags": ["cool", "strong"]},
        {"kanji": "妃", "meaning_en": "princess, queen", "description": "Royal princess or queen. Represents nobility and grace.", "tags": ["cute", "soft"]},
        {"kanji": "姫", "meaning_en": "princess", "description": "Princess or noble lady. Symbolizes elegance and refinement.", "tags": ["cute", "soft"]},
        {"kanji": "飛", "meaning_en": "fly", "description": "To fly through the air. Represents freedom and soaring ambition.", "tags": ["cool", "strong"]},
        {"kanji": "緋", "meaning_en": "scarlet", "description": "Vibrant scarlet red. Symbolizes passion and intensity.", "tags": ["strong", "cute"]},
        {"kanji": "火", "meaning_en": "fire", "description": "Fire and flames. Represents passion, energy, and transformation.", "tags": ["strong", "cool"]},
    ],
    "hiro": [
        {"kanji": "広", "meaning_en": "wide, spacious", "description": "Wide and spacious. Symbolizes breadth, openness, and generosity.", "tags": ["cool", "strong"]},
        {"kanji": "裕", "meaning_en": "abundant, rich", "description": "Abundance and richness. Represents prosperity and plenty.", "tags": ["kind", "cool"]},
        {"kanji": "博", "meaning_en": "extensive, doctor", "description": "Extensive knowledge. Symbolizes wisdom and broad understanding.", "tags": ["smart", "cool"]},
    ],
    "ho": [
        {"kanji": "帆", "meaning_en": "sail", "description": "Ship's sail. Symbolizes adventure, journey, and forward movement.", "tags": ["cool", "soft"]},
        {"kanji": "歩", "meaning_en": "walk, step", "description": "To walk step by step. Represents steady progress and journey.", "tags": ["cool", "strong"]},
        {"kanji": "穂", "meaning_en": "ear of grain", "description": "Grain ears at harvest. Symbolizes fruition and abundance.", "tags": ["soft", "cute"]},
    ],
    
    # BA系
    "ba": [
        {"kanji": "馬", "meaning_en": "horse", "description": "The noble horse. Symbolizes speed, freedom, and elegance.", "tags": ["strong", "cool"]},
        {"kanji": "葉", "meaning_en": "leaf", "description": "Green leaf. Represents growth and nature's vitality.", "tags": ["soft", "cute"]},
    ],
    
    # MA系
    "ma": [
        {"kanji": "真", "meaning_en": "truth, genuine", "description": "Absolute truth and genuineness. Represents authenticity and reality.", "tags": ["cool", "smart"]},
        {"kanji": "舞", "meaning_en": "dance, graceful", "description": "Graceful dance. Symbolizes elegance, art, and flowing movement.", "tags": ["cute", "soft"]},
        {"kanji": "茉", "meaning_en": "jasmine", "description": "Fragrant jasmine flower. Represents sweetness and purity.", "tags": ["cute", "soft"]},
        {"kanji": "麻", "meaning_en": "hemp, flax", "description": "Hemp or linen. Symbolizes natural simplicity and utility.", "tags": ["cool", "soft"]},
        {"kanji": "万", "meaning_en": "ten thousand", "description": "Ten thousand, countless. Represents vast numbers and abundance.", "tags": ["strong", "cool"]},
        {"kanji": "磨", "meaning_en": "polish, grind", "description": "To polish and refine. Symbolizes improvement and perfection.", "tags": ["cool", "strong"]},
    ],
    "mai": [
        {"kanji": "舞", "meaning_en": "dance", "description": "Beautiful dance performance. Represents artistic grace.", "tags": ["cute", "soft"]},
        {"kanji": "麻", "meaning_en": "hemp, flax", "description": "Natural hemp fiber. Symbolizes simplicity and strength.", "tags": ["cool", "soft"]},
        {"kanji": "米", "meaning_en": "rice, America", "description": "Rice grain or America. Represents sustenance or internationality.", "tags": ["cool"]},
    ],
    "mi": [
        {"kanji": "美", "meaning_en": "beauty", "description": "Pure beauty. One of the most beloved characters representing aesthetic perfection.", "tags": ["cute", "soft"]},
        {"kanji": "実", "meaning_en": "fruit, truth", "description": "Fruit or reality. Represents tangible results and truth.", "tags": ["kind", "cool"]},
        {"kanji": "海", "meaning_en": "ocean, sea", "description": "The vast ocean. Symbolizes depth, mystery, and boundless potential.", "tags": ["cool", "strong"]},
        {"kanji": "未", "meaning_en": "not yet, future", "description": "Not yet, the future. Represents potential and what's to come.", "tags": ["cool", "soft"]},
        {"kanji": "魅", "meaning_en": "charm, enchant", "description": "Enchanting charm. Symbolizes attractive and captivating personality.", "tags": ["cute", "cool"]},
        {"kanji": "三", "meaning_en": "three", "description": "The number three. Represents stability and completeness.", "tags": ["cool"]},
        {"kanji": "深", "meaning_en": "deep, profound", "description": "Deep and profound. Symbolizes depth of character and thought.", "tags": ["cool", "smart"]},
    ],
    "michi": [
        {"kanji": "道", "meaning_en": "path, way", "description": "The path or way. Represents life journey and proper conduct (as in 'way of').", "tags": ["cool", "smart"]},
        {"kanji": "路", "meaning_en": "road, path", "description": "Road or route. Symbolizes journey and direction.", "tags": ["cool", "strong"]},
    ],
    "mu": [
        {"kanji": "夢", "meaning_en": "dream", "description": "Dreams and aspirations. Represents hope, imagination, and goals.", "tags": ["soft", "cute"]},
        {"kanji": "武", "meaning_en": "military, brave", "description": "Military prowess and bravery. Symbolizes courage and martial skill.", "tags": ["strong", "cool"]},
        {"kanji": "無", "meaning_en": "nothing, none", "description": "Nothingness or absence. In Zen, represents empty potential.", "tags": ["cool", "smart"]},
    ],
    "mo": [
        {"kanji": "萌", "meaning_en": "budding, sprout", "description": "Young sprouts budding. Symbolizes fresh growth and potential.", "tags": ["cute", "soft"]},
        {"kanji": "桃", "meaning_en": "peach", "description": "Peach fruit and blossoms. Represents sweetness and charm.", "tags": ["cute", "soft"]},
        {"kanji": "百", "meaning_en": "hundred", "description": "One hundred. Represents plenty and completeness.", "tags": ["cool"]},
        {"kanji": "望", "meaning_en": "hope, desire", "description": "Hope and aspirations. Symbolizes looking forward with desire.", "tags": ["cool", "strong"]},
        {"kanji": "茂", "meaning_en": "luxuriant, flourish", "description": "Luxuriant growth. Represents flourishing and prosperity.", "tags": ["strong", "cool"]},
    ],
    
    # YA系
    "ya": [
        {"kanji": "也", "meaning_en": "to be, also", "description": "Classical particle meaning 'to be'. Adds classical elegance.", "tags": ["cool"]},
        {"kanji": "弥", "meaning_en": "increasingly, all the more", "description": "Increasingly, more and more. Represents growth and expansion.", "tags": ["cool", "strong"]},
        {"kanji": "矢", "meaning_en": "arrow", "description": "Arrow flying straight. Symbolizes directness and purpose.", "tags": ["strong", "cool"]},
        {"kanji": "夜", "meaning_en": "night", "description": "The nighttime. Represents mystery, calm, and depth.", "tags": ["cool", "soft"]},
        {"kanji": "耶", "meaning_en": "question mark, Jesus", "description": "Question particle, also used for Jesus. Adds contemplative quality.", "tags": ["cool"]},
    ],
    "yu": [
        {"kanji": "優", "meaning_en": "gentle, superior", "description": "Gentle excellence. Combines kindness with outstanding ability.", "tags": ["kind", "soft"]},
        {"kanji": "悠", "meaning_en": "permanence, leisurely", "description": "Permanent and unhurried. Symbolizes calm endurance.", "tags": ["cool", "soft"]},
        {"kanji": "結", "meaning_en": "tie, bind", "description": "To tie and connect. Represents relationships and unity.", "tags": ["soft", "kind"]},
        {"kanji": "柚", "meaning_en": "citron, yuzu", "description": "Fragrant yuzu citrus. Symbolizes refreshing uniqueness.", "tags": ["cute", "soft"]},
        {"kanji": "由", "meaning_en": "reason, cause", "description": "Reason or origin. Represents logical thinking and roots.", "tags": ["smart", "cool"]},
        {"kanji": "祐", "meaning_en": "help, assist", "description": "Divine help and assistance. Symbolizes support and blessing.", "tags": ["kind", "cool"]},
        {"kanji": "夢", "meaning_en": "dream", "description": "Dreams and visions. Represents aspirations and imagination.", "tags": ["soft", "cute"]},
    ],
    "yuki": [
        {"kanji": "雪", "meaning_en": "snow", "description": "Pure white snow. Symbolizes purity, beauty, and tranquility.", "tags": ["soft", "cute"]},
        {"kanji": "幸", "meaning_en": "happiness", "description": "Happiness and good fortune. Brings joy and blessings.", "tags": ["kind", "cute"]},
    ],
    "yo": [
        {"kanji": "葉", "meaning_en": "leaf", "description": "Green leaves. Represents nature and life force.", "tags": ["soft", "cute"]},
        {"kanji": "陽", "meaning_en": "sunshine", "description": "Bright sunshine. Symbolizes warmth and positive energy.", "tags": ["cool", "strong"]},
        {"kanji": "世", "meaning_en": "world, generation", "description": "The world or generation. Represents era and society.", "tags": ["cool", "smart"]},
        {"kanji": "代", "meaning_en": "generation, era", "description": "Generation or substitute. Symbolizes time and succession.", "tags": ["cool"]},
        {"kanji": "夜", "meaning_en": "night", "description": "Nighttime. Represents mystery and quiet depth.", "tags": ["cool", "soft"]},
    ],
    
    # RA系
    "ra": [
        {"kanji": "羅", "meaning_en": "gauze, thin silk", "description": "Thin silk gauze. Symbolizes delicate elegance and refinement.", "tags": ["cool", "soft"]},
        {"kanji": "良", "meaning_en": "good, excellent", "description": "Good and excellent. Represents positive quality and virtue.", "tags": ["kind", "cool"]},
        {"kanji": "蘭", "meaning_en": "orchid", "description": "Elegant orchid flower. Symbolizes refinement and grace.", "tags": ["cute", "soft"]},
        {"kanji": "楽", "meaning_en": "music, comfort", "description": "Music and enjoyment. Represents joy and artistic pleasure.", "tags": ["cute", "kind"]},
    ],
    "ran": [
        {"kanji": "蘭", "meaning_en": "orchid", "description": "Beautiful orchid. Symbolizes nobility and subtle beauty.", "tags": ["cute", "soft"]},
        {"kanji": "欄", "meaning_en": "column, railing", "description": "Column or railing. Represents structure and support.", "tags": ["cool"]},
    ],
    "ri": [
        {"kanji": "理", "meaning_en": "logic, reason", "description": "Logic and rational thinking. Symbolizes intellect and understanding.", "tags": ["smart", "cool"]},
        {"kanji": "里", "meaning_en": "village, hometown", "description": "Village or hometown. Represents roots and community.", "tags": ["soft", "kind"]},
        {"kanji": "莉", "meaning_en": "jasmine", "description": "White jasmine flower. Symbolizes purity and sweet fragrance.", "tags": ["cute", "soft"]},
        {"kanji": "梨", "meaning_en": "pear", "description": "Pear fruit. Represents sweetness and natural beauty.", "tags": ["cute", "soft"]},
        {"kanji": "利", "meaning_en": "profit, advantage", "description": "Advantage and benefit. Symbolizes usefulness and gain.", "tags": ["cool", "strong"]},
        {"kanji": "璃", "meaning_en": "glassy, lapis lazuli", "description": "Lapis lazuli gemstone. Represents precious beauty and clarity.", "tags": ["cool", "soft"]},
        {"kanji": "吏", "meaning_en": "official, officer", "description": "Government official. Symbolizes authority and responsibility.", "tags": ["cool", "strong"]},
    ],
    "riku": [
        {"kanji": "陸", "meaning_en": "land, shore", "description": "Solid land. Represents stability and grounded strength.", "tags": ["strong", "cool"]},
        {"kanji": "睦", "meaning_en": "friendly, harmonious", "description": "Harmonious friendship. Symbolizes peace and good relations.", "tags": ["kind", "soft"]},
    ],
    "rin": [
        {"kanji": "凛", "meaning_en": "dignified, cold", "description": "Dignified and cool. Represents noble bearing and clarity.", "tags": ["cool", "strong"]},
        {"kanji": "林", "meaning_en": "forest, woods", "description": "Forest of trees. Symbolizes nature and abundance.", "tags": ["cool", "soft"]},
        {"kanji": "倫", "meaning_en": "ethics, companion", "description": "Ethics and moral code. Represents principled character.", "tags": ["smart", "cool"]},
        {"kanji": "鈴", "meaning_en": "bell", "description": "Ringing bell. Symbolizes clarity and joyful sound.", "tags": ["cute", "soft"]},
    ],
    "ru": [
        {"kanji": "瑠", "meaning_en": "lapis lazuli", "description": "Beautiful lapis lazuli stone. Represents rare beauty and value.", "tags": ["cool", "soft"]},
        {"kanji": "流", "meaning_en": "flow, current", "description": "Flowing water or current. Symbolizes movement and adaptability.", "tags": ["cool", "strong"]},
        {"kanji": "留", "meaning_en": "detain, fasten", "description": "To stay or fasten. Represents stability and presence.", "tags": ["cool"]},
    ],
    "rei": [
        {"kanji": "麗", "meaning_en": "lovely, beautiful", "description": "Lovely and beautiful. Represents refined beauty and elegance.", "tags": ["cute", "soft"]},
        {"kanji": "怜", "meaning_en": "wise, clever", "description": "Clever wisdom. Symbolizes sharp intelligence and insight.", "tags": ["smart", "cool"]},
        {"kanji": "玲", "meaning_en": "tinkling of jade", "description": "Tinkling sound of jade. Represents delicate beauty and clarity.", "tags": ["cute", "soft"]},
        {"kanji": "礼", "meaning_en": "courtesy, thanks", "description": "Courtesy and respect. Symbolizes proper manners and gratitude.", "tags": ["kind", "cool"]},
        {"kanji": "零", "meaning_en": "zero, fall", "description": "Zero or falling dew. Represents beginning or purity.", "tags": ["cool", "soft"]},
        {"kanji": "鈴", "meaning_en": "bell", "description": "Clear ringing bell. Symbolizes clarity and joy.", "tags": ["cute", "soft"]},
    ],
    "ren": [
        {"kanji": "蓮", "meaning_en": "lotus", "description": "Sacred lotus flower. Symbolizes purity rising from mud, enlightenment.", "tags": ["soft", "cute"]},
        {"kanji": "恋", "meaning_en": "love, romance", "description": "Romantic love. Represents passion and deep affection.", "tags": ["cute", "soft"]},
        {"kanji": "連", "meaning_en": "connect, link", "description": "Connection and continuity. Symbolizes relationships and unity.", "tags": ["cool", "strong"]},
        {"kanji": "廉", "meaning_en": "honest, inexpensive", "description": "Honesty and modesty. Symbolizes integrity.", "tags": ["kind", "cool"]},
        {"kanji": "錬", "meaning_en": "refine, train", "description": "To refine and train. Represents discipline and improvement.", "tags": ["strong", "cool"]},
    ],
    "ro": [
        {"kanji": "路", "meaning_en": "road, path", "description": "Road or pathway. Represents journey and direction in life.", "tags": ["cool", "strong"]},
        {"kanji": "呂", "meaning_en": "spine, backbone", "description": "Backbone or spine. Symbolizes core strength and structure.", "tags": ["strong", "cool"]},
    ],
    
    # WA系
    "wa": [
        {"kanji": "和", "meaning_en": "harmony, peace", "description": "Harmony and peace. Core value in Japanese culture representing balance.", "tags": ["kind", "soft"]},
        {"kanji": "環", "meaning_en": "ring, circle", "description": "Ring or circle. Symbolizes completeness and eternal connection.", "tags": ["cool", "soft"]},
        {"kanji": "輪", "meaning_en": "wheel, ring", "description": "Wheel or ring. Represents cycles and continuous movement.", "tags": ["cool", "soft"]},
        {"kanji": "湾", "meaning_en": "gulf, bay", "description": "Bay or gulf. Symbolizes shelter and natural harbor.", "tags": ["cool", "soft"]},
    ],
    
    # JI系
    "ji": [
        {"kanji": "慈", "meaning_en": "mercy, compassion", "description": "Deep compassion and mercy. Represents loving kindness.", "tags": ["kind", "soft"]},
        {"kanji": "次", "meaning_en": "next, following", "description": "The next in sequence. Symbolizes progression and future.", "tags": ["cool"]},
        {"kanji": "二", "meaning_en": "two, second", "description": "The number two. Represents partnership and duality.", "tags": ["cool"]},
        {"kanji": "治", "meaning_en": "govern, cure", "description": "To govern or heal. Symbolizes order and restoration.", "tags": ["strong", "cool"]},
        {"kanji": "路", "meaning_en": "road, path", "description": "Road or pathway. Represents journey through life.", "tags": ["cool", "strong"]},
    ],
    "jin": [
        {"kanji": "仁", "meaning_en": "benevolence, humanity", "description": "Benevolence and humaneness. Core Confucian virtue of compassion.", "tags": ["kind", "strong"]},
        {"kanji": "神", "meaning_en": "god, spirit", "description": "Divine spirit or deity. Represents sacred power and spirituality.", "tags": ["strong", "cool"]},
        {"kanji": "迅", "meaning_en": "swift, rapid", "description": "Swift and quick. Symbolizes speed and efficiency.", "tags": ["strong", "cool"]},
    ],
    "ju": [
        {"kanji": "樹", "meaning_en": "tree", "description": "Strong tree. Symbolizes growth and natural stability.", "tags": ["strong", "cool"]},
        {"kanji": "寿", "meaning_en": "longevity, celebration", "description": "Long life and celebration. Very auspicious character.", "tags": ["kind", "strong"]},
        {"kanji": "珠", "meaning_en": "pearl, jewel", "description": "Precious pearl. Represents rare beauty and value.", "tags": ["cute", "soft"]},
    ],
    "jun": [
        {"kanji": "純", "meaning_en": "pure, genuine", "description": "Pure and genuine. Represents authenticity and innocence.", "tags": ["soft", "kind"]},
        {"kanji": "順", "meaning_en": "obey, order", "description": "Order and harmony. Symbolizes smooth flow and compliance.", "tags": ["soft", "cool"]},
        {"kanji": "潤", "meaning_en": "moist, profit", "description": "Moist and润. Represents abundance and prosperity.", "tags": ["cool", "kind"]},
    ],
    
    # ZU系
    "zu": [
        {"kanji": "図", "meaning_en": "diagram, plan", "description": "Diagram or plan. Symbolizes design and strategy.", "tags": ["smart", "cool"]},
    ],
    
    # BI系
    "bi": [
        {"kanji": "美", "meaning_en": "beauty", "description": "Pure beauty. Ultimate expression of aesthetic perfection.", "tags": ["cute", "soft"]},
        {"kanji": "備", "meaning_en": "prepare, provide", "description": "To prepare and provide. Represents readiness and completeness.", "tags": ["cool", "strong"]},
        {"kanji": "微", "meaning_en": "delicate, minute", "description": "Delicate and subtle. Symbolizes refinement and attention to detail.", "tags": ["soft", "smart"]},
    ],
    
    # PI系
    "pi": [
        {"kanji": "妃", "meaning_en": "princess, queen", "description": "Royal princess. Symbolizes nobility and grace.", "tags": ["cute", "soft"]},
    ],
    
    # FU系
    "fu": [
        {"kanji": "風", "meaning_en": "wind, style", "description": "Wind and style. Represents natural flow and elegance.", "tags": ["cool", "strong"]},
        {"kanji": "富", "meaning_en": "wealth, abundant", "description": "Wealth and abundance. Symbolizes prosperity and richness.", "tags": ["strong", "cool"]},
        {"kanji": "芙", "meaning_en": "lotus", "description": "Lotus flower (hibiscus). Represents purity and beauty.", "tags": ["cute", "soft"]},
        {"kanji": "楓", "meaning_en": "maple", "description": "Maple tree. Symbolizes autumn beauty and change.", "tags": ["soft", "cool"]},
        {"kanji": "文", "meaning_en": "sentence, culture", "description": "Writing and culture. Represents literacy and civilization.", "tags": ["smart", "cool"]},
    ],
    "fumi": [
        {"kanji": "文", "meaning_en": "writing, literature", "description": "Literature and culture. Symbolizes learning and expression.", "tags": ["smart", "cool"]},
        {"kanji": "史", "meaning_en": "history, chronicle", "description": "Historical records. Represents legacy and documentation.", "tags": ["smart", "cool"]},
    ],
    
    # BU系
    "bu": [
        {"kanji": "武", "meaning_en": "military, martial", "description": "Martial prowess. Symbolizes warrior spirit and bravery.", "tags": ["strong", "cool"]},
        {"kanji": "舞", "meaning_en": "dance", "description": "Graceful dance. Represents artistic movement and elegance.", "tags": ["cute", "soft"]},
    ],
    
    # HE系
    "he": [
        {"kanji": "平", "meaning_en": "flat, peace", "description": "Flat and peaceful. Represents tranquility and equality.", "tags": ["soft", "kind"]},
        {"kanji": "辺", "meaning_en": "area, vicinity", "description": "Area or vicinity. Symbolizes surroundings and environment.", "tags": ["cool"]},
    ],
    
    # BE系
    "be": [
        {"kanji": "紅", "meaning_en": "crimson, deep red", "description": "Deep crimson red. Represents passion and vivid beauty.", "tags": ["strong", "cute"]},
    ],
    
    # ME系
    "me": [
        {"kanji": "芽", "meaning_en": "bud, sprout", "description": "Young bud sprouting. Symbolizes new beginnings and potential.", "tags": ["cute", "soft"]},
        {"kanji": "恵", "meaning_en": "blessing, favor", "description": "Divine blessing. Represents grace and good fortune.", "tags": ["kind", "soft"]},
        {"kanji": "愛", "meaning_en": "love", "description": "Pure love. Most cherished expression of affection.", "tags": ["kind", "cute"]},
    ],
    "mei": [
        {"kanji": "明", "meaning_en": "bright, clear", "description": "Brightness and clarity. Symbolizes illumination and intelligence.", "tags": ["smart", "cool"]},
        {"kanji": "芽", "meaning_en": "bud, sprout", "description": "Budding sprout. Represents fresh growth.", "tags": ["cute", "soft"]},
        {"kanji": "銘", "meaning_en": "inscription, signature", "description": "Inscription or motto. Symbolizes lasting legacy.", "tags": ["cool", "strong"]},
    ],
    
    # GE系
    "ge": [
        {"kanji": "夏", "meaning_en": "summer", "description": "Vibrant summer season. Represents energy and warmth.", "tags": ["cool", "strong"]},
    ],
    
    # DE系
    "de": [
        {"kanji": "出", "meaning_en": "exit, emerge", "description": "To emerge or come forth. Symbolizes beginning and expression.", "tags": ["cool", "strong"]},
    ],
    
    # NE系
    "ne": [
        {"kanji": "音", "meaning_en": "sound", "description": "Sound and music. Represents harmony and artistic expression.", "tags": ["soft", "cute"]},
        {"kanji": "根", "meaning_en": "root, origin", "description": "Root or foundation. Symbolizes origin and stability.", "tags": ["strong", "cool"]},
        {"kanji": "寧", "meaning_en": "rather, peaceful", "description": "Peaceful and calm. Represents tranquility and preference.", "tags": ["soft", "kind"]},
    ],
    "nen": [
        {"kanji": "念", "meaning_en": "thought, sense", "description": "Thought and mindfulness. Symbolizes awareness and intention.", "tags": ["smart", "cool"]},
    ],
    
    # ZEN系
    "zen": [
        {"kanji": "善", "meaning_en": "good, virtuous", "description": "Goodness and virtue. Represents moral excellence.", "tags": ["kind", "strong"]},
        {"kanji": "禅", "meaning_en": "Zen, meditation", "description": "Zen Buddhism and meditation. Symbolizes enlightenment and peace.", "tags": ["smart", "cool"]},
        {"kanji": "全", "meaning_en": "whole, complete", "description": "Wholeness and completeness. Symbolizes totality.", "tags": ["cool", "strong"]},
    ],
    
    # SO系
    "so": [
        {"kanji": "蒼", "meaning_en": "blue, pale", "description": "Pale blue color. Represents sky and elegance.", "tags": ["cool", "strong"]},
        {"kanji": "爽", "meaning_en": "refreshing, bracing", "description": "Refreshing and invigorating. Symbolizes vitality.", "tags": ["cool", "strong"]},
        {"kanji": "想", "meaning_en": "concept, think", "description": "Thought and imagination. Represents creative thinking.", "tags": ["smart", "cool"]},
        {"kanji": "奏", "meaning_en": "play music, report", "description": "To play music. Symbolizes artistic performance.", "tags": ["cute", "soft"]},
    ],
    "sou": [
        {"kanji": "颯", "meaning_en": "sudden, sound of wind", "description": "Sound of rushing wind. Represents swift elegance.", "tags": ["cool", "strong"]},
        {"kanji": "想", "meaning_en": "thought, imagination", "description": "Imagination and ideas. Symbolizes creativity.", "tags": ["smart", "cool"]},
        {"kanji": "創", "meaning_en": "create, genesis", "description": "To create something new. Represents innovation.", "tags": ["cool", "strong"]},
        {"kanji": "奏", "meaning_en": "play music, report", "description": "Musical performance. Symbolizes artistic expression.", "tags": ["cute", "soft"]},
        {"kanji": "壮", "meaning_en": "robust, manly", "description": "Robust manliness. Represents vigor and strength.", "tags": ["strong", "cool"]},
        {"kanji": "総", "meaning_en": "general, total", "description": "Total and comprehensive. Represents completeness.", "tags": ["cool", "strong"]},
    ],
    
    # ZO系
    "zo": [
        {"kanji": "造", "meaning_en": "create, build", "description": "To create or build. Symbolizes craftsmanship and creation.", "tags": ["strong", "cool"]},
    ],
    "zou": [
        {"kanji": "蔵", "meaning_en": "storehouse, hide", "description": "Storehouse or treasury. Represents preservation and storage.", "tags": ["cool", "strong"]},
    ],
    
    # DO系
    "do": [
        {"kanji": "土", "meaning_en": "earth, soil", "description": "Earth and soil. Represents foundation and grounding.", "tags": ["strong", "cool"]},
        {"kanji": "道", "meaning_en": "way, path", "description": "The way or path. Fundamental concept of proper conduct.", "tags": ["cool", "smart"]},
    ],
    "dou": [
        {"kanji": "道", "meaning_en": "way, path", "description": "The way or path. Represents life path and philosophy.", "tags": ["cool", "smart"]},
        {"kanji": "堂", "meaning_en": "hall, temple", "description": "Grand hall or temple. Symbolizes dignity and sacred space.", "tags": ["strong", "cool"]},
    ],
    
    # RYO系
    "ryo": [
        {"kanji": "涼", "meaning_en": "cool, refreshing", "description": "Cool and refreshing. Represents comfort and pleasant coolness.", "tags": ["cool", "soft"]},
        {"kanji": "良", "meaning_en": "good, fine", "description": "Good and excellent. Symbolizes quality and virtue.", "tags": ["kind", "cool"]},
        {"kanji": "諒", "meaning_en": "understand, forgive", "description": "Understanding and forgiveness. Represents empathy.", "tags": ["kind", "smart"]},
        {"kanji": "遼", "meaning_en": "distant, vast", "description": "Distant and vast. Symbolizes great expanse.", "tags": ["cool", "strong"]},
    ],
    
    # KYO系
    "kyo": [
        {"kanji": "京", "meaning_en": "capital", "description": "Ancient capital. Represents cultural center and tradition.", "tags": ["cool", "strong"]},
        {"kanji": "恭", "meaning_en": "respectful, polite", "description": "Respectful and courteous. Symbolizes proper manners.", "tags": ["kind", "soft"]},
        {"kanji": "響", "meaning_en": "echo, sound", "description": "Resonating echo. Represents lasting impact and influence.", "tags": ["cool", "strong"]},
        {"kanji": "杏", "meaning_en": "apricot", "description": "Apricot blossom. Symbolizes gentle beauty.", "tags": ["cute", "soft"]},
    ],
    "kyou": [
        {"kanji": "京", "meaning_en": "capital city", "description": "Capital city. Represents centrality and importance.", "tags": ["cool", "strong"]},
        {"kanji": "教", "meaning_en": "teach, religion", "description": "Teaching and education. Symbolizes knowledge transmission.", "tags": ["smart", "cool"]},
        {"kanji": "協", "meaning_en": "cooperate, unite", "description": "Cooperation and unity. Represents working together.", "tags": ["kind", "cool"]},
    ],
    
    # SHO系
    "sho": [
        {"kanji": "翔", "meaning_en": "soar, fly", "description": "To soar high. Represents freedom and ambition.", "tags": ["cool", "strong"]},
        {"kanji": "昌", "meaning_en": "prosperous, bright", "description": "Prosperity and brightness. Symbolizes flourishing.", "tags": ["strong", "cool"]},
        {"kanji": "彰", "meaning_en": "clear, manifest", "description": "Clear and manifest. Represents clarity and recognition.", "tags": ["cool", "strong"]},
        {"kanji": "勝", "meaning_en": "victory, win", "description": "Victory and triumph. Symbolizes success and winning.", "tags": ["strong", "cool"]},
        {"kanji": "正", "meaning_en": "correct, righteous", "description": "Correct and righteous. Represents integrity and justice.", "tags": ["strong", "cool"]},
    ],
    
    # CHO系
    "cho": [
        {"kanji": "蝶", "meaning_en": "butterfly", "description": "Beautiful butterfly. Symbolizes transformation and grace.", "tags": ["cute", "soft"]},
        {"kanji": "長", "meaning_en": "long, leader", "description": "Long or leader. Represents endurance and authority.", "tags": ["strong", "cool"]},
        {"kanji": "朝", "meaning_en": "morning, dynasty", "description": "Morning or dynasty. Symbolizes new beginnings.", "tags": ["cool", "strong"]},
    ],
    "chou": [
        {"kanji": "蝶", "meaning_en": "butterfly", "description": "Graceful butterfly. Represents metamorphosis and beauty.", "tags": ["cute", "soft"]},
        {"kanji": "長", "meaning_en": "chief, long", "description": "Chief or lengthy. Symbolizes leadership and duration.", "tags": ["strong", "cool"]},
    ],
    
    # NYO系
    "nyo": [
        {"kanji": "如", "meaning_en": "likeness, as if", "description": "Likeness or similarity. Represents comparison and metaphor.", "tags": ["cool", "smart"]},
    ],
    
    # HYO系
    "hyo": [
        {"kanji": "氷", "meaning_en": "ice", "description": "Ice and frost. Symbolizes purity and coolness.", "tags": ["cool", "soft"]},
        {"kanji": "標", "meaning_en": "mark, sign", "description": "Mark or sign. Represents goals and indicators.", "tags": ["cool", "strong"]},
    ],
    "hyou": [
        {"kanji": "豹", "meaning_en": "leopard, panther", "description": "Leopard or panther. Symbolizes strength and speed.", "tags": ["strong", "cool"]},
    ],
    
    # MYO系
    "myo": [
        {"kanji": "妙", "meaning_en": "mysterious, exquisite", "description": "Mysterious excellence. Represents subtle beauty and wonder.", "tags": ["cute", "soft"]},
        {"kanji": "明", "meaning_en": "bright", "description": "Bright and clear. Symbolizes illumination.", "tags": ["smart", "cool"]},
    ],
    "myou": [
        {"kanji": "明", "meaning_en": "bright, light", "description": "Brightness and light. Represents clarity and wisdom.", "tags": ["smart", "cool"]},
    ],
    
    # RYU系
    "ryu": [
        {"kanji": "龍", "meaning_en": "dragon", "description": "Mighty dragon. Symbolizes power, wisdom, and good fortune.", "tags": ["strong", "cool"]},
        {"kanji": "流", "meaning_en": "flow, current", "description": "Flowing current. Represents natural movement and adaptation.", "tags": ["cool", "strong"]},
        {"kanji": "柳", "meaning_en": "willow", "description": "Graceful willow tree. Symbolizes flexibility and elegance.", "tags": ["soft", "cute"]},
        {"kanji": "隆", "meaning_en": "prosperity, high", "description": "Prosperity and elevation. Represents success and prominence.", "tags": ["strong", "cool"]},
    ],
    "ryuu": [
        {"kanji": "龍", "meaning_en": "dragon", "description": "Powerful dragon. Ultimate symbol of strength in East Asian culture.", "tags": ["strong", "cool"]},
        {"kanji": "竜", "meaning_en": "dragon", "description": "Dragon (simplified). Represents power and mystique.", "tags": ["strong", "cool"]},
    ],
    
    # KYU系
    "kyu": [
        {"kanji": "久", "meaning_en": "long time", "description": "Long duration. Symbolizes eternity and endurance.", "tags": ["cool", "smart"]},
        {"kanji": "球", "meaning_en": "ball, sphere", "description": "Sphere or globe. Represents completeness and the world.", "tags": ["cool"]},
        {"kanji": "弓", "meaning_en": "bow, archery", "description": "Bow for archery. Symbolizes focus and martial skill.", "tags": ["strong", "cool"]},
    ],
    "kyuu": [
        {"kanji": "九", "meaning_en": "nine", "description": "The number nine. Lucky number representing longevity.", "tags": ["cool"]},
        {"kanji": "究", "meaning_en": "research, investigate", "description": "Deep research. Represents scholarly pursuit.", "tags": ["smart", "cool"]},
    ],
    
    # SHU系
    "shu": [
        {"kanji": "朱", "meaning_en": "vermillion, cinnabar", "description": "Vermillion red color. Represents vibrant energy and nobility.", "tags": ["strong", "cute"]},
        {"kanji": "珠", "meaning_en": "pearl, gem", "description": "Precious pearl. Symbolizes rare beauty.", "tags": ["cute", "soft"]},
        {"kanji": "秀", "meaning_en": "excel, outstanding", "description": "Outstanding excellence. Represents superiority.", "tags": ["strong", "cool"]},
        {"kanji": "修", "meaning_en": "discipline, study", "description": "Discipline and cultivation. Symbolizes self-improvement.", "tags": ["smart", "cool"]},
        {"kanji": "周", "meaning_en": "circumference, around", "description": "Circumference and completeness. Represents thoroughness.", "tags": ["cool", "smart"]},
    ],
    "shuu": [
        {"kanji": "秋", "meaning_en": "autumn, fall", "description": "Autumn season. Symbolizes harvest and maturity.", "tags": ["cool", "soft"]},
        {"kanji": "舟", "meaning_en": "boat, ship", "description": "Boat or ship. Represents journey and navigation.", "tags": ["cool", "strong"]},
        {"kanji": "州", "meaning_en": "state, province", "description": "State or province. Symbolizes territory and governance.", "tags": ["cool", "strong"]},
    ],
    
    # GYO系
    "gyo": [
        {"kanji": "暁", "meaning_en": "dawn, daybreak", "description": "Dawn breaking. Symbolizes new beginnings and enlightenment.", "tags": ["cool", "strong"]},
    ],
    
    # NYU系
    "nyu": [
        {"kanji": "柔", "meaning_en": "soft, gentle", "description": "Softness and flexibility. Represents gentle strength.", "tags": ["soft", "kind"]},
    ],
    
    # 追加の音節
    "kei": [
        {"kanji": "恵", "meaning_en": "blessing, favor", "description": "Divine blessing and grace. Represents benevolence.", "tags": ["kind", "soft"]},
        {"kanji": "慶", "meaning_en": "jubilation, congratulate", "description": "Celebration and joy. Symbolizes auspicious occasions.", "tags": ["kind", "cool"]},
        {"kanji": "圭", "meaning_en": "jade scepter", "description": "Jade ceremonial scepter. Represents nobility and purity.", "tags": ["cool", "strong"]},
        {"kanji": "桂", "meaning_en": "cinnamon tree", "description": "Fragrant cinnamon tree. Symbolizes lasting value.", "tags": ["soft", "kind"]},
        {"kanji": "蛍", "meaning_en": "firefly", "description": "Glowing firefly. Represents gentle light and summer nights.", "tags": ["cute", "soft"]},
        {"kanji": "敬", "meaning_en": "respect, honor", "description": "Respect and honor. Symbolizes reverence.", "tags": ["kind", "strong"]},
        {"kanji": "景", "meaning_en": "scenery, view", "description": "Beautiful scenery. Represents landscape and perspective.", "tags": ["cool", "soft"]},
        {"kanji": "啓", "meaning_en": "open, enlighten", "description": "To enlighten and open. Represents awakening.", "tags": ["smart", "cool"]},
    ],
    "ken": [
        {"kanji": "健", "meaning_en": "healthy, strong", "description": "Health and vigor. Represents physical and mental strength.", "tags": ["strong", "cool"]},
        {"kanji": "賢", "meaning_en": "wise, intelligent", "description": "Wisdom and intelligence. Symbolizes smart judgment.", "tags": ["smart", "cool"]},
        {"kanji": "謙", "meaning_en": "humble, modest", "description": "Humility and modesty. Represents virtue and self-restraint.", "tags": ["kind", "soft"]},
        {"kanji": "憲", "meaning_en": "law, constitution", "description": "Law and constitution. Symbolizes order and justice.", "tags": ["strong", "cool"]},
        {"kanji": "研", "meaning_en": "polish, study", "description": "To polish and研究. Represents refinement through study.", "tags": ["smart", "cool"]},
    ],
    "saki": [
        {"kanji": "咲", "meaning_en": "blossom, bloom", "description": "Flowers blooming. Represents flourishing and joy.", "tags": ["cute", "soft"]},
        {"kanji": "早", "meaning_en": "early, fast", "description": "Early or quick. Symbolizes promptness and initiative.", "tags": ["cool", "strong"]},
    ],
    "shin": [
        {"kanji": "心", "meaning_en": "heart, mind", "description": "Heart and spirit. Represents sincerity and core being.", "tags": ["kind", "soft"]},
        {"kanji": "真", "meaning_en": "true, genuine", "description": "Truth and authenticity. Symbolizes reality and honesty.", "tags": ["cool", "smart"]},
        {"kanji": "新", "meaning_en": "new, fresh", "description": "New and fresh. Represents innovation and renewal.", "tags": ["cool", "strong"]},
        {"kanji": "信", "meaning_en": "faith, trust", "description": "Faith and trustworthiness. Symbolizes reliability.", "tags": ["strong", "cool"]},
        {"kanji": "神", "meaning_en": "god, divine", "description": "Divine spirit. Represents sacred power.", "tags": ["strong", "cool"]},
        {"kanji": "進", "meaning_en": "advance, progress", "description": "To advance forward. Symbolizes progress and development.", "tags": ["strong", "cool"]},
    ],
    "ten": [
        {"kanji": "天", "meaning_en": "heaven, sky", "description": "The heavens above. Represents divine realm and nature.", "tags": ["cool", "strong"]},
        {"kanji": "典", "meaning_en": "ceremony, rule", "description": "Ceremony and classical rules. Symbolizes tradition.", "tags": ["cool", "smart"]},
    ],
    "tomo": [
        {"kanji": "友", "meaning_en": "friend", "description": "Friendship. Represents companionship and loyalty.", "tags": ["kind", "cool"]},
        {"kanji": "智", "meaning_en": "wisdom", "description": "Wisdom and knowledge. Symbolizes intelligence.", "tags": ["smart", "cool"]},
        {"kanji": "朋", "meaning_en": "companion, friend", "description": "Close companion. Represents deep friendship.", "tags": ["kind", "cool"]},
    ],
    "aki": [
        {"kanji": "秋", "meaning_en": "autumn", "description": "Autumn season. Symbolizes maturity and harvest.", "tags": ["cool", "soft"]},
        {"kanji": "明", "meaning_en": "bright", "description": "Bright and clear. Represents clarity and dawn.", "tags": ["smart", "cool"]},
        {"kanji": "晶", "meaning_en": "sparkle, crystal", "description": "Sparkling crystal. Symbolizes brilliance and purity.", "tags": ["cute", "cool"]},
        {"kanji": "彰", "meaning_en": "manifest, clear", "description": "Clear manifestation. Represents recognition.", "tags": ["cool", "strong"]},
        {"kanji": "亮", "meaning_en": "clear, help", "description": "Clear brightness. Symbolizes clarity and assistance.", "tags": ["cool", "kind"]},
    ],
    "asa": [
        {"kanji": "朝", "meaning_en": "morning", "description": "Morning dawn. Symbolizes fresh starts and hope.", "tags": ["cool", "kind"]},
        {"kanji": "麻", "meaning_en": "hemp, linen", "description": "Hemp fiber. Represents natural simplicity.", "tags": ["cool", "soft"]},
    ],
    "aya": [
        {"kanji": "彩", "meaning_en": "color, beauty", "description": "Colorful beauty. Represents artistic vibrancy.", "tags": ["cute", "soft"]},
        {"kanji": "綾", "meaning_en": "design, twill", "description": "Woven design pattern. Symbolizes intricate beauty.", "tags": ["cute", "soft"]},
        {"kanji": "文", "meaning_en": "sentence, pattern", "description": "Pattern or文. Represents文化 and expression.", "tags": ["smart", "cool"]},
    ],
    "eri": [
        {"kanji": "絵", "meaning_en": "picture, painting", "description": "Picture or painting. Represents artistic creation.", "tags": ["cute", "soft"]},
        {"kanji": "恵", "meaning_en": "blessing", "description": "Blessed favor. Symbolizes grace.", "tags": ["kind", "soft"]},
        {"kanji": "衿", "meaning_en": "collar, neck", "description": "Collar or neck. Represents elegance.", "tags": ["soft", "cute"]},
    ],
    "iku": [
        {"kanji": "育", "meaning_en": "raise, nurture", "description": "To nurture and raise. Represents growth and care.", "tags": ["kind", "soft"]},
        {"kanji": "郁", "meaning_en": "fragrant, cultured", "description": "Cultured fragrance. Symbolizes refinement.", "tags": ["soft", "cool"]},
    ],
    "umi": [
        {"kanji": "海", "meaning_en": "ocean, sea", "description": "Vast ocean. Represents boundless depth and adventure.", "tags": ["cool", "strong"]},
    ],
    "nana": [
        {"kanji": "七", "meaning_en": "seven", "description": "Lucky number seven. Symbolizes good fortune.", "tags": ["cute", "cool"]},
        {"kanji": "菜", "meaning_en": "greens, vegetables", "description": "Fresh vegetables. Represents health and nature.", "tags": ["cute", "soft"]},
        {"kanji": "奈", "meaning_en": "what, Nara", "description": "Ancient Nara. Symbolizes cultural heritage.", "tags": ["soft", "kind"]},
    ],
    "kazu": [
        {"kanji": "一", "meaning_en": "one, first", "description": "Number one. Represents unity and being first.", "tags": ["cool", "strong"]},
        {"kanji": "和", "meaning_en": "harmony", "description": "Harmony and peace. Core Japanese value.", "tags": ["kind", "soft"]},
        {"kanji": "数", "meaning_en": "number, count", "description": "Numbers and counting. Represents quantity.", "tags": ["smart", "cool"]},
    ],
    "masa": [
        {"kanji": "正", "meaning_en": "correct, righteous", "description": "Correctness and righteousness. Represents integrity.", "tags": ["strong", "cool"]},
        {"kanji": "雅", "meaning_en": "elegant, graceful", "description": "Elegant grace. Symbolizes refined beauty.", "tags": ["cool", "soft"]},
        {"kanji": "昌", "meaning_en": "prosperous", "description": "Prosperity. Represents flourishing success.", "tags": ["strong", "cool"]},
        {"kanji": "政", "meaning_en": "politics, govern", "description": "Government and politics. Symbolizes leadership.", "tags": ["strong", "cool"]},
    ],
    "nori": [
        {"kanji": "則", "meaning_en": "rule, law", "description": "Rules and laws. Represents order and principles.", "tags": ["strong", "cool"]},
        {"kanji": "典", "meaning_en": "ceremony, classic", "description": "Classic ceremony. Symbolizes tradition.", "tags": ["cool", "smart"]},
        {"kanji": "憲", "meaning_en": "constitution", "description": "Constitutional law. Represents fundamental order.", "tags": ["strong", "cool"]},
    ],
    "kana": [
        {"kanji": "奏", "meaning_en": "play music", "description": "To perform music. Represents artistic expression.", "tags": ["cute", "soft"]},
        {"kanji": "叶", "meaning_en": "grant, fulfill", "description": "To grant wishes. Symbolizes fulfillment of dreams.", "tags": ["kind", "soft"]},
        {"kanji": "香", "meaning_en": "fragrance", "description": "Sweet fragrance. Represents pleasant aroma.", "tags": ["cute", "soft"]},
    ],
    "aoi": [
        {"kanji": "葵", "meaning_en": "hollyhock", "description": "Hollyhock flower. Associated with nobility and elegance.", "tags": ["cute", "soft"]},
        {"kanji": "蒼", "meaning_en": "blue, pale", "description": "Pale blue. Represents sky and elegance.", "tags": ["cool", "strong"]},
        {"kanji": "碧", "meaning_en": "blue-green, jade", "description": "Blue-green jade. Symbolizes precious natural beauty.", "tags": ["cool", "strong"]},
    ],
    "kaori": [
        {"kanji": "香", "meaning_en": "fragrance", "description": "Sweet fragrance. Represents pleasant aroma and lasting impression.", "tags": ["cute", "soft"]},
        {"kanji": "薫", "meaning_en": "fragrance, scent", "description": "Aromatic fragrance. Symbolizes refined scent.", "tags": ["soft", "cute"]},
    ],
    "kaede": [
        {"kanji": "楓", "meaning_en": "maple", "description": "Maple tree. Symbolizes autumn beauty and graceful change.", "tags": ["soft", "cool"]},
    ],
    "sakura": [
        {"kanji": "桜", "meaning_en": "cherry blossom", "description": "Cherry blossom. Japan's most beloved flower, symbolizing beauty and life's transience.", "tags": ["cute", "soft"]},
    ],
    "momoka": [
        {"kanji": "桃", "meaning_en": "peach", "description": "Sweet peach. Represents charm and sweetness.", "tags": ["cute", "soft"]},
        {"kanji": "百", "meaning_en": "hundred", "description": "One hundred. Symbolizes completeness and plenty.", "tags": ["cool"]},
    ],
    "sumire": [
        {"kanji": "菫", "meaning_en": "violet flower", "description": "Violet flower. Symbolizes modesty and faithfulness.", "tags": ["cute", "soft"]},
    ],
    "tsubaki": [
        {"kanji": "椿", "meaning_en": "camellia", "description": "Camellia flower. Represents elegance and longevity.", "tags": ["cute", "soft"]},
    ],
    "ayame": [
        {"kanji": "菖", "meaning_en": "iris", "description": "Iris flower. Symbolizes good news and courage.", "tags": ["cute", "soft"]},
        {"kanji": "彩", "meaning_en": "color", "description": "Colorful beauty. Represents artistic vibrancy.", "tags": ["cute", "soft"]},
    ],
    "yui": [
        {"kanji": "結", "meaning_en": "tie, bind", "description": "To tie and bind. Represents connection and unity.", "tags": ["soft", "kind"]},
        {"kanji": "唯", "meaning_en": "solely, only", "description": "Solely and uniquely. Symbolizes being one of a kind.", "tags": ["cool", "soft"]},
        {"kanji": "優", "meaning_en": "gentle, superior", "description": "Gentle excellence. Represents graceful superiority.", "tags": ["kind", "soft"]},
        {"kanji": "由", "meaning_en": "reason, cause", "description": "Reason and origin. Symbolizes logical foundation.", "tags": ["smart", "cool"]},
    ],
    "yuu": [
        {"kanji": "優", "meaning_en": "gentle, superior", "description": "Gentle superiority. Combines kindness with excellence.", "tags": ["kind", "soft"]},
        {"kanji": "勇", "meaning_en": "courage, brave", "description": "Courage and bravery. Represents fearless spirit.", "tags": ["strong", "cool"]},
        {"kanji": "悠", "meaning_en": "permanence, leisurely", "description": "Permanent ease. Symbolizes calm endurance.", "tags": ["cool", "soft"]},
        {"kanji": "夕", "meaning_en": "evening", "description": "Evening twilight. Represents peaceful end of day.", "tags": ["soft", "cool"]},
        {"kanji": "裕", "meaning_en": "abundant, rich", "description": "Abundant prosperity. Symbolizes wealth and plenty.", "tags": ["kind", "cool"]},
        {"kanji": "祐", "meaning_en": "help, assist", "description": "Divine assistance. Represents helpful support.", "tags": ["kind", "cool"]},
        {"kanji": "雄", "meaning_en": "male, hero", "description": "Heroic masculinity. Symbolizes powerful leadership.", "tags": ["strong", "cool"]},
    ],
    "yuna": [
        {"kanji": "優", "meaning_en": "gentle", "description": "Gentle grace. Represents kind excellence.", "tags": ["kind", "soft"]},
        {"kanji": "柚", "meaning_en": "yuzu citrus", "description": "Fragrant yuzu. Symbolizes refreshing uniqueness.", "tags": ["cute", "soft"]},
    ],
    "yume": [
        {"kanji": "夢", "meaning_en": "dream", "description": "Dreams and aspirations. Represents hope and imagination.", "tags": ["soft", "cute"]},
        {"kanji": "結", "meaning_en": "tie, bind", "description": "Binding connection. Symbolizes relationships.", "tags": ["soft", "kind"]},
    ],
    "ichi": [
        {"kanji": "一", "meaning_en": "one, first", "description": "The number one. Represents unity, beginning, and being number one.", "tags": ["cool", "strong"]},
        {"kanji": "市", "meaning_en": "city, market", "description": "City or marketplace. Symbolizes commerce and urban life.", "tags": ["cool"]},
    ],
    "dai": [
        {"kanji": "大", "meaning_en": "big, great", "description": "Great and large. Symbolizes magnitude and importance.", "tags": ["strong", "cool"]},
       {"kanji": "代", "meaning_en": "generation, era", "description": "Generation or era. Represents time period and succession.", "tags": ["cool"]},
        {"kanji": "題", "meaning_en": "topic, title", "description": "Topic or title. Symbolizes subject matter and theme.", "tags": ["smart", "cool"]},
    ],
    "gen": [
        {"kanji": "元", "meaning_en": "origin, foundation", "description": "Origin and foundation. Represents fundamental source.", "tags": ["strong", "cool"]},
        {"kanji": "源", "meaning_en": "source, origin", "description": "Source or wellspring. Symbolizes original beginning.", "tags": ["cool", "strong"]},
        {"kanji": "厳", "meaning_en": "strict, severe", "description": "Strictness and severity. Represents discipline and dignity.", "tags": ["strong", "cool"]},
        {"kanji": "玄", "meaning_en": "mysterious, deep black", "description": "Mysterious depth. Symbolizes profound mystery.", "tags": ["cool", "smart"]},
    ],
    "gou": [
        {"kanji": "豪", "meaning_en": "powerful, magnificent", "description": "Powerful magnificence. Represents splendor and might.", "tags": ["strong", "cool"]},
        {"kanji": "剛", "meaning_en": "strong, hard", "description": "Hardness and strength. Symbolizes unyielding power.", "tags": ["strong", "cool"]},
    ],
    "hou": [
        {"kanji": "豊", "meaning_en": "abundant, rich", "description": "Abundance and richness. Represents prosperity and plenty.", "tags": ["kind", "cool"]},
        {"kanji": "宝", "meaning_en": "treasure, jewel", "description": "Precious treasure. Symbolizes valuable possessions.", "tags": ["cute", "cool"]},
        {"kanji": "方", "meaning_en": "direction, way", "description": "Direction or method. Represents approach and path.", "tags": ["cool", "smart"]},
        {"kanji": "芳", "meaning_en": "fragrant, virtuous", "description": "Fragrant virtue. Symbolizes good reputation and aroma.", "tags": ["soft", "kind"]},
    ],
    "jou": [
        {"kanji": "城", "meaning_en": "castle", "description": "Majestic castle. Represents strength, protection, and nobility.", "tags": ["strong", "cool"]},
        {"kanji": "上", "meaning_en": "above, superior", "description": "Above and superior. Symbolizes excellence and high status.", "tags": ["strong", "cool"]},
        {"kanji": "条", "meaning_en": "article, clause", "description": "Article or clause. Represents rules and stipulations.", "tags": ["cool", "smart"]},
        {"kanji": "浄", "meaning_en": "clean, pure", "description": "Purity and cleanliness. Symbolizes purification.", "tags": ["soft", "kind"]},
    ],
    "maki": [
        {"kanji": "真", "meaning_en": "truth", "description": "Genuine truth. Represents authenticity.", "tags": ["cool", "smart"]},
        {"kanji": "牧", "meaning_en": "pasture, breed", "description": "Pasture land. Symbolizes pastoral care and raising.", "tags": ["soft", "cool"]},
        {"kanji": "槙", "meaning_en": "Chinese black pine", "description": "Evergreen pine tree. Represents endurance and constancy.", "tags": ["strong", "cool"]},
    ],
    "miku": [
        {"kanji": "未", "meaning_en": "not yet, future", "description": "The future未. Represents potential and what's coming.", "tags": ["cool", "soft"]},
        {"kanji": "美", "meaning_en": "beauty", "description": "Beautiful perfection. Symbolizes aesthetic excellence.", "tags": ["cute", "soft"]},
    ],
    "mina": [
        {"kanji": "美", "meaning_en": "beauty", "description": "Beautiful grace. Represents loveliness.", "tags": ["cute", "soft"]},
        {"kanji": "皆", "meaning_en": "all, everyone", "description": "Everyone together. Symbolizes unity and inclusiveness.", "tags": ["kind", "cool"]},
    ],
    "mio": [
        {"kanji": "澪", "meaning_en": "water channel", "description": "Navigable water channel. Represents flow and guidance.", "tags": ["cool", "soft"]},
        {"kanji": "美", "meaning_en": "beauty", "description": "Beautiful elegance. Symbolizes aesthetic appeal.", "tags": ["cute", "soft"]},
    ],
    "reo": [
        {"kanji": "礼", "meaning_en": "courtesy", "description": "Respectful courtesy. Represents good manners.", "tags": ["kind", "cool"]},
        {"kanji": "怜", "meaning_en": "wise, clever", "description": "Clever wisdom. Symbolizes sharp intelligence.", "tags": ["smart", "cool"]},
    ],
    "sora": [
        {"kanji": "空", "meaning_en": "sky, heaven", "description": "Vast sky. Represents limitless freedom and dreams.", "tags": ["soft", "cool"]},
        {"kanji": "宙", "meaning_en": "space, universe", "description": "Cosmic space. Symbolizes the universe and infinity.", "tags": ["cool", "strong"]},
        {"kanji": "昊", "meaning_en": "vast sky", "description": "Vast expanse of sky. Represents limitless potential.", "tags": ["cool", "strong"]},
    ],
    "taka": [
        {"kanji": "高", "meaning_en": "high, tall", "description": "High and elevated. Represents lofty aspirations.", "tags": ["strong", "cool"]},
        {"kanji": "貴", "meaning_en": "precious, noble", "description": "Precious nobility. Symbolizes high value and status.", "tags": ["cool", "strong"]},
        {"kanji": "隆", "meaning_en": "prosperity, high", "description": "Prosperous elevation. Represents success and prominence.", "tags": ["strong", "cool"]},
        {"kanji": "孝", "meaning_en": "filial piety", "description": "Filial devotion. Core Confucian virtue of respect for parents.", "tags": ["kind", "strong"]},
        {"kanji": "崇", "meaning_en": "revere, worship", "description": "Reverence and worship. Represents deep respect.", "tags": ["strong", "cool"]},
    ],
    "tou": [
        {"kanji": "透", "meaning_en": "transparent, penetrate", "description": "Transparency. Represents clarity and insight.", "tags": ["cool", "smart"]},
        {"kanji": "冬", "meaning_en": "winter", "description": "Winter season. Symbolizes endurance and quiet beauty.", "tags": ["cool", "soft"]},
        {"kanji": "桃", "meaning_en": "peach", "description": "Peach fruit and blossoms. Represents sweetness and charm.", "tags": ["cute", "soft"]},
        {"kanji": "藤", "meaning_en": "wisteria", "description": "Wisteria flowers. Symbolizes elegance and longevity.", "tags": ["soft", "cute"]},
        {"kanji": "東", "meaning_en": "east", "description": "Eastern direction. Represents sunrise and new beginnings.", "tags": ["cool", "strong"]},
        {"kanji": "灯", "meaning_en": "lamp, light", "description": "Lamp or light. Symbolizes guidance and illumination.", "tags": ["soft", "kind"]},
    ],
    "hatsu": [
        {"kanji": "初", "meaning_en": "first, beginning", "description": "First time or beginning. Represents new starts.", "tags": ["cool", "soft"]},
        {"kanji": "発", "meaning_en": "depart, emit", "description": "To emit or start. Symbolizes initiative and departure.", "tags": ["strong", "cool"]},
    ],
    "hana": [
        {"kanji": "花", "meaning_en": "flower", "description": "Beautiful flower. Universal symbol of beauty and growth.", "tags": ["cute", "soft"]},
        {"kanji": "華", "meaning_en": "splendor, flower", "description": "Magnificent splendor. More elaborate than simple flower.", "tags": ["strong", "cute"]},
        {"kanji": "英", "meaning_en": "excellence", "description": "Excellence and heroism. Represents outstanding ability.", "tags": ["strong", "cool"]},
    ],
    "natsu": [
        {"kanji": "夏", "meaning_en": "summer", "description": "Summer season. Represents vitality and warmth.", "tags": ["cool", "strong"]},
        {"kanji": "捺", "meaning_en": "press, seal", "description": "To press or seal. Symbolizes making one's mark.", "tags": ["strong", "cool"]},
    ],
    "fuyu": [
        {"kanji": "冬", "meaning_en": "winter", "description": "Winter season. Symbolizes quiet strength and endurance.", "tags": ["cool", "soft"]},
    ],
    "setsu": [
        {"kanji": "雪", "meaning_en": "snow", "description": "Pure white snow. Symbolizes purity and beauty.", "tags": ["soft", "cute"]},
        {"kanji": "節", "meaning_en": "node, season", "description": "Joint or season. Represents proper timing and moderation.", "tags": ["cool", "smart"]},
        {"kanji": "説", "meaning_en": "explain, theory", "description": "Explanation and theory. Symbolizes reasoning and teaching.", "tags": ["smart", "cool"]},
    ],
    "tetsu": [
        {"kanji": "哲", "meaning_en": "philosophy, wisdom", "description": "Philosophical wisdom. Represents deep thinking and insight.", "tags": ["smart", "cool"]},
        {"kanji": "徹", "meaning_en": "penetrate, pierce", "description": "To penetrate thoroughly. Symbolizes complete understanding.", "tags": ["strong", "cool"]},
        {"kanji": "鉄", "meaning_en": "iron, steel", "description": "Iron metal. Represents strength and durability.", "tags": ["strong", "cool"]},
    ],
    "satoshi": [
        {"kanji": "聡", "meaning_en": "wise, intelligent", "description": "Intelligent wisdom. Represents quick understanding.", "tags": ["smart", "cool"]},
        {"kanji": "智", "meaning_en": "wisdom, intellect", "description": "Wisdom and knowledge. Symbolizes intelligence.", "tags": ["smart", "cool"]},
        {"kanji": "敏", "meaning_en": "quick, clever", "description": "Quick cleverness. Represents agility of mind.", "tags": ["smart", "cool"]},
    ],
    "takeshi": [
        {"kanji": "武", "meaning_en": "military, martial", "description": "Martial prowess. Symbolizes warrior spirit.", "tags": ["strong", "cool"]},
        {"kanji": "剛", "meaning_en": "strong, hard", "description": "Strong and hard. Represents unyielding strength.", "tags": ["strong", "cool"]},
        {"kanji": "健", "meaning_en": "healthy, strong", "description": "Health and vigor. Symbolizes robustness.", "tags": ["strong", "cool"]},
    ],
    "gaku": [
        {"kanji": "学", "meaning_en": "study, learning", "description": "Study and learning. Represents education and scholarship.", "tags": ["smart", "cool"]},
        {"kanji": "岳", "meaning_en": "mountain peak", "description": "Mountain peak. Symbolizes lofty heights and strength.", "tags": ["strong", "cool"]},
        {"kanji": "楽", "meaning_en": "music, comfort", "description": "Music and enjoyment. Represents pleasure and art.", "tags": ["cute", "kind"]},
    ],
   "gaku": [
        {"kanji": "学", "meaning_en": "study, learning", "description": "Study and learning. Represents education and scholarship.", "tags": ["smart", "cool"]},
        {"kanji": "岳", "meaning_en": "mountain peak", "description": "Mountain peak. Symbolizes lofty heights and strength.", "tags": ["strong", "cool"]},
        {"kanji": "楽", "meaning_en": "music, comfort", "description": "Music and enjoyment. Represents pleasure and art.", "tags": ["cute", "kind"]},
    ],
    
    # さらなる追加
    "bel": [
        {"kanji": "鈴", "meaning_en": "bell", "description": "Clear ringing bell. Symbolizes joy and clarity.", "tags": ["cute", "soft", "joyful"]},
    ],
    "ben": [
        {"kanji": "弁", "meaning_en": "speech, dialect", "description": "Speech and eloquence. Represents communication skill.", "tags": ["smart", "cool"]},
    ],
    "ber": [
        {"kanji": "紅", "meaning_en": "crimson", "description": "Deep crimson color. Represents passion and intensity.", "tags": ["strong", "energetic"]},
    ],
    "bot": [
        {"kanji": "牡", "meaning_en": "male, bull", "description": "Male strength. Symbolizes masculinity and power.", "tags": ["strong", "brave"]},
    ],
    "den": [
        {"kanji": "伝", "meaning_en": "transmit, convey", "description": "To transmit knowledge. Represents communication and legacy.", "tags": ["smart", "cool"]},
        {"kanji": "田", "meaning_en": "rice field", "description": "Rice paddy field. Symbolizes agriculture and sustenance.", "tags": ["natural", "calm"]},
    ],
    "eto": [
        {"kanji": "絵", "meaning_en": "picture", "description": "Picture and painting. Represents artistic expression.", "tags": ["artistic", "cute"]},
    ],
    "gan": [
        {"kanji": "願", "meaning_en": "wish, request", "description": "Wish and prayer. Symbolizes hope and desire.", "tags": ["soft", "kind", "joyful"]},
        {"kanji": "眼", "meaning_en": "eye, vision", "description": "Eye and vision. Represents insight and perception.", "tags": ["smart", "cool"]},
        {"kanji": "岩", "meaning_en": "rock, crag", "description": "Solid rock. Symbolizes strength and stability.", "tags": ["strong", "brave"]},
    ],
    "go": [
        {"kanji": "吾", "meaning_en": "I, my", "description": "Self and identity. Represents personal autonomy.", "tags": ["strong", "cool"]},
        {"kanji": "悟", "meaning_en": "enlightenment", "description": "Buddhist enlightenment. Symbolizes awakening and wisdom.", "tags": ["smart", "mysterious"]},
        {"kanji": "五", "meaning_en": "five", "description": "The number five. Represents balance and the five elements.", "tags": ["cool"]},
    ],
    "gou": [
        {"kanji": "郷", "meaning_en": "hometown, village", "description": "Hometown and native place. Symbolizes roots and belonging.", "tags": ["soft", "kind", "natural"]},
    ],
    "han": [
        {"kanji": "帆", "meaning_en": "sail", "description": "Ship's sail. Symbolizes journey and adventure.", "tags": ["cool", "energetic"]},
        {"kanji": "繁", "meaning_en": "flourish, prosperity", "description": "Flourishing prosperity. Represents abundance and growth.", "tags": ["strong", "joyful"]},
        {"kanji": "半", "meaning_en": "half", "description": "Half or semi. Represents balance and duality.", "tags": ["cool"]},
    ],
    "hei": [
        {"kanji": "平", "meaning_en": "peace, flat", "description": "Peace and flatness. Symbolizes tranquility and equality.", "tags": ["calm", "kind"]},
        {"kanji": "兵", "meaning_en": "soldier, army", "description": "Soldier and military. Represents martial strength.", "tags": ["strong", "brave"]},
    ],
    "hon": [
        {"kanji": "本", "meaning_en": "book, origin", "description": "Book or origin. Symbolizes knowledge and roots.", "tags": ["smart", "cool"]},
    ],
    "hou": [
        {"kanji": "法", "meaning_en": "law, method", "description": "Law and dharma. Represents order and justice.", "tags": ["strong", "smart"]},
        {"kanji": "報", "meaning_en": "report, news", "description": "Report and information. Symbolizes communication.", "tags": ["smart", "cool"]},
        {"kanji": "鳳", "meaning_en": "phoenix", "description": "Mythical phoenix bird. Represents rebirth and majesty.", "tags": ["strong", "mysterious", "elegant"]},
    ],
    "ise": [
        {"kanji": "伊", "meaning_en": "that one, Italy", "description": "Elegant pronoun. Symbolizes distinction and sophistication.", "tags": ["elegant", "cool"]},
    ],
    "ito": [
        {"kanji": "糸", "meaning_en": "thread, string", "description": "Thread or string. Represents connection and weaving.", "tags": ["soft", "artistic"]},
    ],
    "jiro": [
        {"kanji": "二", "meaning_en": "two, second", "description": "Second son or number two. Traditional Japanese naming.", "tags": ["cool"]},
    ],
    "jo": [
        {"kanji": "女", "meaning_en": "woman, female", "description": "Woman and femininity. Represents grace and strength.", "tags": ["soft", "kind"]},
        {"kanji": "序", "meaning_en": "preface, order", "description": "Preface and序列. Symbolizes beginning and organization.", "tags": ["smart", "cool"]},
    ],
    "jun": [
        {"kanji": "淳", "meaning_en": "pure, honest", "description": "Pure and honest character. Represents sincerity.", "tags": ["kind", "calm"]},
        {"kanji": "隼", "meaning_en": "falcon, peregrine", "description": "Swift falcon. Symbolizes speed and precision.", "tags": ["strong", "cool", "energetic"]},
    ],
    "kage": [
        {"kanji": "影", "meaning_en": "shadow, silhouette", "description": "Shadow and reflection. Represents mystery and depth.", "tags": ["mysterious", "cool"]},
        {"kanji": "景", "meaning_en": "scenery", "description": "Beautiful scenery. Symbolizes natural beauty.", "tags": ["natural", "soft"]},
    ],
    "kami": [
        {"kanji": "神", "meaning_en": "god, deity", "description": "Divine spirit. Represents sacred power.", "tags": ["strong", "mysterious"]},
        {"kanji": "上", "meaning_en": "above, superior", "description": "Above and upper. Symbolizes excellence.", "tags": ["strong", "cool"]},
    ],
    "kan": [
        {"kanji": "寛", "meaning_en": "generous, tolerant", "description": "Generosity and tolerance. Represents magnanimity.", "tags": ["kind", "calm"]},
        {"kanji": "環", "meaning_en": "ring, circle", "description": "Ring and circle. Symbolizes completeness.", "tags": ["soft", "elegant"]},
        {"kanji": "歓", "meaning_en": "joy, delight", "description": "Joy and delight. Represents happiness.", "tags": ["joyful", "kind"]},
        {"kanji": "漢", "meaning_en": "man, China", "description": "Man or Han Chinese. Represents strength.", "tags": ["strong", "cool"]},
        {"kanji": "館", "meaning_en": "mansion, hall", "description": "Grand mansion. Symbolizes nobility.", "tags": ["elegant", "strong"]},
    ],
    "kata": [
        {"kanji": "方", "meaning_en": "direction, person", "description": "Direction or respectful person. Represents approach.", "tags": ["cool", "smart"]},
        {"kanji": "片", "meaning_en": "one-sided,片", "description": "One side or fragment. Symbolizes uniqueness.", "tags": ["cool"]},
    ],
    "kats": [
        {"kanji": "勝", "meaning_en": "victory, win", "description": "Victory and triumph. Represents winning spirit.", "tags": ["strong", "brave"]},
        {"kanji": "活", "meaning_en": "lively, active", "description": "Lively activity. Symbolizes vitality.", "tags": ["energetic", "joyful"]},
    ],
    "katsu": [
        {"kanji": "勝", "meaning_en": "victory", "description": "Victory and success. Represents triumph.", "tags": ["strong", "brave", "energetic"]},
        {"kanji": "克", "meaning_en": "overcome, conquer", "description": "To overcome obstacles. Symbolizes perseverance.", "tags": ["strong", "brave"]},
    ],
    "kawa": [
        {"kanji": "川", "meaning_en": "river, stream", "description": "Flowing river. Represents natural flow and journey.", "tags": ["natural", "calm"]},
        {"kanji": "河", "meaning_en": "river", "description": "Large river. Symbolizes major waterway.", "tags": ["natural", "strong"]},
    ],
    "kaze": [
        {"kanji": "風", "meaning_en": "wind", "description": "Wind and breeze. Represents freedom and change.", "tags": ["natural", "energetic"]},
    ],
    "kiku": [
        {"kanji": "菊", "meaning_en": "chrysanthemum", "description": "Chrysanthemum flower. Imperial symbol of Japan.", "tags": ["elegant", "soft", "natural"]},
    ],
    "kin": [
        {"kanji": "金", "meaning_en": "gold, metal", "description": "Gold metal. Represents wealth and value.", "tags": ["strong", "elegant"]},
        {"kanji": "欽", "meaning_en": "respect, admire", "description": "Respect and admiration. Symbolizes reverence.", "tags": ["kind", "elegant"]},
    ],
    "kiyo": [
        {"kanji": "清", "meaning_en": "pure, clean", "description": "Purity and cleanliness. Represents clarity.", "tags": ["calm", "soft", "kind"]},
    ],
    "koku": [
        {"kanji": "国", "meaning_en": "country, nation", "description": "Country and nation. Represents homeland.", "tags": ["strong", "cool"]},
        {"kanji": "刻", "meaning_en": "engrave, time", "description": "To engrave or time. Symbolizes permanence.", "tags": ["strong", "smart"]},
    ],
    "koma": [
        {"kanji": "駒", "meaning_en": "pony, chess piece", "description": "Small horse or chess piece. Represents agility.", "tags": ["cute", "energetic"]},
    ],
    "koto": [
        {"kanji": "琴", "meaning_en": "koto instrument", "description": "Traditional Japanese harp. Symbolizes musical elegance.", "tags": ["artistic", "elegant", "soft"]},
        {"kanji": "言", "meaning_en": "say, word", "description": "Words and speech. Represents communication.", "tags": ["smart", "cool"]},
    ],
    "kuni": [
        {"kanji": "国", "meaning_en": "country", "description": "Nation and country. Represents homeland pride.", "tags": ["strong", "cool"]},
        {"kanji": "邦", "meaning_en": "country, Japan", "description": "Country or homeland. Symbolizes national identity.", "tags": ["strong", "elegant"]},
    ],
    "kura": [
        {"kanji": "蔵", "meaning_en": "storehouse, hide", "description": "Storehouse and treasury. Represents preservation.", "tags": ["cool", "strong"]},
        {"kanji": "倉", "meaning_en": "warehouse", "description": "Warehouse and storage. Symbolizes abundance.", "tags": ["strong", "cool"]},
    ],
    "kuro": [
        {"kanji": "黒", "meaning_en": "black", "description": "Black color. Represents mystery and depth.", "tags": ["mysterious", "cool"]},
        {"kanji": "玖", "meaning_en": "black jewel", "description": "Beautiful black gemstone. Symbolizes rare beauty.", "tags": ["mysterious", "elegant"]},
    ],
    "man": [
        {"kanji": "万", "meaning_en": "ten thousand", "description": "Ten thousand or countless. Represents vast quantity.", "tags": ["strong", "cool"]},
        {"kanji": "満", "meaning_en": "full,満足", "description": "Fullness and satisfaction. Symbolizes completeness.", "tags": ["joyful", "kind"]},
    ],
    "mare": [
        {"kanji": "稀", "meaning_en": "rare, precious", "description": "Rare and precious. Represents uniqueness.", "tags": ["elegant", "soft"]},
    ],
    "masa": [
        {"kanji": "将", "meaning_en": "general, leader", "description": "Military general. Symbolizes leadership.", "tags": ["strong", "brave"]},
        {"kanji": "匡", "meaning_en": "correct, reform", "description": "To correct and reform. Represents righteousness.", "tags": ["strong", "smart"]},
    ],
    "masu": [
        {"kanji": "益", "meaning_en": "benefit, profit", "description": "Benefit and advantage. Represents gain.", "tags": ["smart", "kind"]},
        {"kanji": "増", "meaning_en": "increase, grow", "description": "To increase and grow. Symbolizes expansion.", "tags": ["strong", "energetic"]},
    ],
    "matsu": [
        {"kanji": "松", "meaning_en": "pine tree", "description": "Pine tree. Symbolizes longevity and steadfastness.", "tags": ["natural", "strong", "calm"]},
        {"kanji": "末", "meaning_en": "end, youngest", "description": "End or youngest child. Represents conclusion.", "tags": ["cool"]},
    ],
    "michi": [
        {"kanji": "通", "meaning_en": "pass through, expert", "description": "To pass through or be expert. Represents mastery.", "tags": ["smart", "cool"]},
    ],
    "midori": [
        {"kanji": "緑", "meaning_en": "green", "description": "Green color. Represents nature and freshness.", "tags": ["natural", "calm", "soft"]},
        {"kanji": "翠", "meaning_en": "jade green", "description": "Jade green color. Symbolizes precious nature.", "tags": ["elegant", "natural", "soft"]},
    ],
    "mika": [
        {"kanji": "美", "meaning_en": "beauty", "description": "Beautiful perfection. Symbolizes aesthetic excellence.", "tags": ["cute", "soft", "elegant"]},
    ],
    "mine": [
        {"kanji": "峰", "meaning_en": "peak, summit", "description": "Mountain peak. Represents reaching the top.", "tags": ["strong", "cool", "brave"]},
    ],
    "minoru": [
        {"kanji": "実", "meaning_en": "fruit, reality", "description": "Fruit and truth. Represents genuine results.", "tags": ["kind", "smart"]},
        {"kanji": "稔", "meaning_en": "harvest, ripen", "description": "Harvest and ripening. Symbolizes fruition.", "tags": ["natural", "kind"]},
    ],
    "misa": [
        {"kanji": "美", "meaning_en": "beauty", "description": "Beautiful grace. Represents loveliness.", "tags": ["cute", "soft", "elegant"]},
    ],
    "mitsu": [
        {"kanji": "光", "meaning_en": "light", "description": "Radiant light. Symbolizes brilliance.", "tags": ["energetic", "strong"]},
        {"kanji": "満", "meaning_en": "full", "description": "Fullness. Represents abundance.", "tags": ["joyful", "kind"]},
        {"kanji": "密", "meaning_en": "dense, secret", "description": "Dense or secret. Symbolizes intimacy.", "tags": ["mysterious", "cool"]},
    ],
    "miya": [
        {"kanji": "宮", "meaning_en": "palace, shrine", "description": "Palace or shrine. Represents sacred nobility.", "tags": ["elegant", "mysterious"]},
    ],
    "mizu": [
        {"kanji": "水", "meaning_en": "water", "description": "Water element. Represents flow and adaptability.", "tags": ["natural", "calm", "soft"]},
    ],
    "mori": [
        {"kanji": "森", "meaning_en": "forest", "description": "Dense forest. Symbolizes nature and abundance.", "tags": ["natural", "strong", "calm"]},
        {"kanji": "守", "meaning_en": "protect, guard", "description": "To protect and guard. Represents守護 spirit.", "tags": ["strong", "brave", "kind"]},
    ],
    "nagi": [
        {"kanji": "凪", "meaning_en": "calm sea", "description": "Calm ocean waters. Represents tranquility.", "tags": ["calm", "soft", "natural"]},
    ],
    "nami": [
        {"kanji": "波", "meaning_en": "wave", "description": "Ocean waves. Symbolizes rhythm and flow.", "tags": ["natural", "soft", "energetic"]},
        {"kanji": "並", "meaning_en": "row, line up", "description": "To line up. Represents order.", "tags": ["cool"]},
    ],
    "nobu": [
        {"kanji": "信", "meaning_en": "faith, trust", "description": "Faith and trust. Symbolizes reliability.", "tags": ["strong", "kind"]},
        {"kanji": "伸", "meaning_en": "stretch, extend", "description": "To stretch and grow. Represents expansion.", "tags": ["energetic", "strong"]},
        {"kanji": "延", "meaning_en": "prolong, extend", "description": "To prolong. Symbolizes continuation.", "tags": ["cool", "smart"]},
    ],
    "nozomu": [
        {"kanji": "望", "meaning_en": "hope, desire", "description": "Hope and望. Represents aspiration.", "tags": ["strong", "energetic"]},
        {"kanji": "希", "meaning_en": "hope, rare", "description": "Hope and rarity. Symbolizes precious wishes.", "tags": ["soft", "kind"]},
    ],
    "oka": [
        {"kanji": "岡", "meaning_en": "hill, ridge", "description": "Hill or ridge. Represents elevated land.", "tags": ["natural", "strong"]},
    ],
    "oki": [
        {"kanji": "沖", "meaning_en": "open sea, offshore", "description": "Open ocean. Symbolizes vastness.", "tags": ["natural", "cool"]},
    ],
    "oshi": [
        {"kanji": "押", "meaning_en": "push, press", "description": "To push forward. Represents assertiveness.", "tags": ["strong", "energetic"]},
    ],
    "oto": [
        {"kanji": "音", "meaning_en": "sound", "description": "Sound and music. Represents harmony.", "tags": ["artistic", "soft", "cute"]},
        {"kanji": "乙", "meaning_en": "second, strange", "description": "Second or unique. Symbolizes distinction.", "tags": ["cool", "mysterious"]},
    ],
    "ran": [
        {"kanji": "乱", "meaning_en": "disorder, rebellion", "description": "Disorder or rebellion. Represents chaos and change.", "tags": ["strong", "energetic"]},
    ],
    "riku": [
        {"kanji": "律", "meaning_en": "rhythm, law", "description": "Rhythm and law. Represents order and律.", "tags": ["smart", "cool"]},
        {"kanji": "立", "meaning_en": "stand, establish", "description": "To stand up. Symbolizes independence.", "tags": ["strong", "brave"]},
    ],
    "ringo": [
        {"kanji": "林", "meaning_en": "forest", "description": "Forest and woods. Represents nature.", "tags": ["natural", "calm"]},
    ],
    "ritsu": [
        {"kanji": "律", "meaning_en": "law, rhythm", "description": "Law and rhythm. Symbolizes order.", "tags": ["smart", "cool"]},
        {"kanji": "立", "meaning_en": "stand", "description": "To stand. Represents establishment.", "tags": ["strong", "brave"]},
    ],
    "roku": [
        {"kanji": "六", "meaning_en": "six", "description": "The number six. Represents harmony.", "tags": ["cool"]},
        {"kanji": "緑", "meaning_en": "green", "description": "Green color. Symbolizes nature.", "tags": ["natural", "calm"]},
    ],
    "rui": [
        {"kanji": "類", "meaning_en": "kind,類", "description": "Kind or類. Represents category.", "tags": ["smart", "cool"]},
        {"kanji": "涙", "meaning_en": "tears", "description": "Tears. Symbolizes emotion and sensitivity.", "tags": ["soft", "kind"]},
        {"kanji": "塁", "meaning_en": "base, fortress", "description": "Military base. Represents defense.", "tags": ["strong", "brave"]},
    ],
    "sachi": [
        {"kanji": "幸", "meaning_en": "happiness", "description": "Happiness and fortune. Represents joy.", "tags": ["joyful", "kind", "cute"]},
    ],
    "sae": [
        {"kanji": "冴", "meaning_en": "clear, sharp", "description": "Clarity and sharpness. Symbolizes brilliance.", "tags": ["smart", "cool"]},
        {"kanji": "紗", "meaning_en": "gauze", "description": "Delicate silk gauze. Represents refinement.", "tags": ["soft", "elegant", "cute"]},
    ],
    "saga": [
        {"kanji": "嵯", "meaning_en": "steep, craggy", "description": "Steep mountain. Represents ruggedness.", "tags": ["strong", "natural"]},
    ],
    "sake": [
        {"kanji": "栄", "meaning_en": "prosperity", "description": "Prosperity and glory. Represents flourishing.", "tags": ["strong", "joyful"]},
    ],
    "saku": [
        {"kanji": "咲", "meaning_en": "bloom", "description": "Flowers blooming. Represents flourishing.", "tags": ["cute", "soft", "joyful"]},
        {"kanji": "作", "meaning_en": "make, create", "description": "To create. Symbolizes craftsmanship.", "tags": ["artistic", "smart"]},
        {"kanji": "朔", "meaning_en": "new moon, north", "description": "New moon. Represents new beginnings.", "tags": ["mysterious", "cool"]},
    ],
    "sara": [
        {"kanji": "沙", "meaning_en": "sand", "description": "Fine sand. Symbolizes natural beauty.", "tags": ["soft", "natural"]},
        {"kanji": "皿", "meaning_en": "plate, dish", "description": "Plate or dish. Represents container.", "tags": ["cool"]},
    ],
    "sei": [
        {"kanji": "聖", "meaning_en": "holy, saint", "description": "Holy and sacred. Represents divinity.", "tags": ["elegant", "mysterious", "strong"]},
        {"kanji": "清", "meaning_en": "pure, clean", "description": "Purity and cleanliness. Symbolizes clarity.", "tags": ["calm", "kind", "soft"]},
        {"kanji": "晴", "meaning_en": "clear weather", "description": "Clear sunny skies. Represents optimism.", "tags": ["joyful", "energetic"]},
        {"kanji": "星", "meaning_en": "star", "description": "Stars in the sky. Symbolizes dreams and guidance.", "tags": ["mysterious", "cute", "cool"]},
        {"kanji": "誠", "meaning_en": "sincerity", "description": "Sincerity and truth. Represents honesty.", "tags": ["strong", "kind"]},
        {"kanji": "生", "meaning_en": "life, birth", "description": "Life and生. Symbolizes vitality.", "tags": ["energetic", "natural"]},
    ],
    "sen": [
        {"kanji": "千", "meaning_en": "thousand", "description": "One thousand. Represents vastness.", "tags": ["cool"]},
        {"kanji": "泉", "meaning_en": "spring, fountain", "description": "Water spring. Symbolizes source and purity.", "tags": ["natural", "calm", "soft"]},
        {"kanji": "仙", "meaning_en": "hermit, immortal", "description": "Taoist immortal. Represents mysticism.", "tags": ["mysterious", "smart", "cool"]},
        {"kanji": "先", "meaning_en": "before, previous", "description": "Before or先. Symbolizes leadership.", "tags": ["strong", "smart"]},
    ],
    "shige": [
        {"kanji": "茂", "meaning_en": "luxuriant, flourish", "description": "Luxuriant growth. Represents prosperity.", "tags": ["strong", "natural"]},
        {"kanji": "重", "meaning_en": "heavy, important", "description": "Heavy or important. Symbolizes significance.", "tags": ["strong", "cool"]},
    ],
    "shiki": [
        {"kanji": "識", "meaning_en": "consciousness, knowledge", "description": "Knowledge and識. Represents awareness.", "tags": ["smart", "cool"]},
        {"kanji": "四", "meaning_en": "four", "description": "The number four. Represents stability.", "tags": ["cool"]},
    ],
    "shino": [
        {"kanji": "篠", "meaning_en": "bamboo grass", "description": "Bamboo grass. Symbolizes flexibility.", "tags": ["natural", "soft", "elegant"]},
    ],
    "shio": [
        {"kanji": "潮", "meaning_en": "tide, salt water", "description": "Ocean tide. Represents natural rhythm.", "tags": ["natural", "energetic"]},
        {"kanji": "汐", "meaning_en": "evening tide", "description": "Evening tide. Symbolizes peaceful flow.", "tags": ["calm", "natural", "soft"]},
    ],
    "shiro": [
        {"kanji": "白", "meaning_en": "white", "description": "White color. Represents purity and simplicity.", "tags": ["calm", "soft", "kind"]},
        {"kanji": "城", "meaning_en": "castle", "description": "Castle fortress. Symbolizes strength.", "tags": ["strong", "elegant", "brave"]},
    ],
    "shizu": [
        {"kanji": "静", "meaning_en": "quiet, calm", "description": "Quietness and静. Represents tranquility.", "tags": ["calm", "soft", "kind"]},
        {"kanji": "雫", "meaning_en": "drop, droplet", "description": "Water droplet. Symbolizes purity.", "tags": ["soft", "natural", "cute"]},
    ],
    "sho": [
        {"kanji": "将", "meaning_en": "general, leader", "description": "Military general. Represents leadership.", "tags": ["strong", "brave", "cool"]},
        {"kanji": "照", "meaning_en": "shine, illuminate", "description": "To shine and illuminate. Symbolizes radiance.", "tags": ["energetic", "kind"]},
        {"kanji": "祥", "meaning_en": "auspicious, good omen", "description": "Auspicious signs. Represents good fortune.", "tags": ["joyful", "kind"]},
        {"kanji": "省", "meaning_en": "reflect,省", "description": "To reflect or省. Symbolizes introspection.", "tags": ["smart", "calm"]},
    ],
    "sui": [
        {"kanji": "水", "meaning_en": "water", "description": "Water element. Represents flow and life.", "tags": ["natural", "calm", "soft"]},
        {"kanji": "翠", "meaning_en": "jade green", "description": "Beautiful jade green. Symbolizes precious nature.", "tags": ["elegant", "natural"]},
        {"kanji": "粋", "meaning_en": "essence, chic", "description": "Essence and elegance. Represents refined taste.", "tags": ["elegant", "cool"]},
    ],
    "suke": [
        {"kanji": "助", "meaning_en": "help, assist", "description": "To help and assist. Represents support.", "tags": ["kind", "strong"]},
        {"kanji": "祐", "meaning_en": "divine help", "description": "Divine assistance. Symbolizes blessing.", "tags": ["kind", "soft"]},
        {"kanji": "介", "meaning_en": "mediate, help", "description": "To介 or assist. Represents facilitation.", "tags": ["kind", "smart"]},
    ],
    "sumi": [
        {"kanji": "澄", "meaning_en": "clear, pure", "description": "Clear water. Symbolizes purity.", "tags": ["calm", "soft", "kind"]},
        {"kanji": "墨", "meaning_en": "ink, black", "description": "Black ink. Represents artistic expression.", "tags": ["artistic", "mysterious"]},
    ],
    "suzu": [
        {"kanji": "鈴", "meaning_en": "bell", "description": "Small bell. Symbolizes clarity and joy.", "tags": ["cute", "soft", "joyful"]},
        {"kanji": "涼", "meaning_en": "cool, refreshing", "description": "Cool breeze. Represents refreshment.", "tags": ["calm", "soft", "natural"]},
    ],
    "tai": [
        {"kanji": "大", "meaning_en": "big, great", "description": "Great and large. Represents magnitude.", "tags": ["strong", "cool"]},
        {"kanji": "太", "meaning_en": "thick, big", "description": "Thick and substantial. Symbolizes strength.", "tags": ["strong", "cool"]},
        {"kanji": "泰", "meaning_en": "peaceful, great", "description": "Peaceful greatness. Represents calm strength.", "tags": ["strong", "calm"]},
        {"kanji": "体", "meaning_en": "body, form", "description": "Body and form. Symbolizes physical being.", "tags": ["strong", "natural"]},
    ],
    "taka": [
        {"kanji": "鷹", "meaning_en": "hawk, falcon", "description": "Hawk bird. Symbolizes keen vision and strength.", "tags": ["strong", "brave", "cool"]},
    ],
    "take": [
        {"kanji": "武", "meaning_en": "martial, military", "description": "Martial arts. Represents warrior spirit.", "tags": ["strong", "brave"]},
        {"kanji": "竹", "meaning_en": "bamboo", "description": "Bamboo plant. Symbolizes flexibility and strength.", "tags": ["natural", "strong", "elegant"]},
        {"kanji": "岳", "meaning_en": "mountain peak", "description": "Mountain peak. Represents lofty heights.", "tags": ["strong", "natural", "brave"]},
        {"kanji": "猛", "meaning_en": "fierce, violent", "description": "Fierce strength. Symbolizes intensity.", "tags": ["strong", "brave", "energetic"]},
    ],
    "tama": [
        {"kanji": "玉", "meaning_en": "jewel, ball", "description": "Precious jewel. Represents beauty and value.", "tags": ["elegant", "cute", "soft"]},
        {"kanji": "魂", "meaning_en": "soul, spirit", "description": "Soul and spirit. Symbolizes essence.", "tags": ["mysterious", "strong"]},
    ],
    "tami": [
        {"kanji": "民", "meaning_en": "people, citizens", "description": "The people. Represents community.", "tags": ["kind", "cool"]},
    ],
    "tana": [
        {"kanji": "棚", "meaning_en": "shelf, rack", "description": "Shelf or rack. Represents organization.", "tags": ["cool"]},
    ],
    "tane": [
        {"kanji": "種", "meaning_en": "seed, species", "description": "Seed of plant. Symbolizes potential.", "tags": ["natural", "soft"]},
    ],
    "tate": [
        {"kanji": "館", "meaning_en": "mansion, hall", "description": "Grand館. Represents nobility.", "tags": ["elegant", "strong"]},
    ],
    "tatsu": [
        {"kanji": "龍", "meaning_en": "dragon", "description": "Mighty dragon. Ultimate symbol of power.", "tags": ["strong", "brave", "mysterious"]},
        {"kanji": "達", "meaning_en": "accomplish,達", "description": "To accomplish. Represents mastery.", "tags": ["strong", "smart"]},
        {"kanji": "建", "meaning_en": "build, establish", "description": "To build. Symbolizes creation.", "tags": ["strong", "smart"]},
    ],
    "teru": [
        {"kanji": "照", "meaning_en": "shine, illuminate", "description": "To shine. Represents radiance.", "tags": ["energetic", "joyful"]},
        {"kanji": "輝", "meaning_en": "radiance", "description": "Brilliant radiance. Symbolizes glory.", "tags": ["strong", "energetic"]},
    ],
    "toki": [
        {"kanji": "時", "meaning_en": "time, hour", "description": "Time and hour. Represents temporal flow.", "tags": ["smart", "cool"]},
        {"kanji": "朱", "meaning_en": "vermillion", "description": "Vermillion red. Symbolizes vibrant energy.", "tags": ["energetic", "cute"]},
    ],
    "tora": [
        {"kanji": "虎", "meaning_en": "tiger", "description": "Tiger animal. Represents courage and power.", "tags": ["strong", "brave", "energetic"]},
    ],
    "toshi": [
        {"kanji": "俊", "meaning_en": "genius, excellence", "description": "Genius and excellence. Represents outstanding ability.", "tags": ["smart", "cool", "strong"]},
        {"kanji": "敏", "meaning_en": "quick, clever", "description": "Quick cleverness. Symbolizes agility.", "tags": ["smart", "energetic"]},
        {"kanji": "利", "meaning_en": "profit, sharp", "description": "Sharp and利. Represents advantage.", "tags": ["smart", "strong"]},
    ],
    "tsuki": [
        {"kanji": "月", "meaning_en": "moon", "description": "Beautiful moon. Symbolizes mystery and cycles.", "tags": ["mysterious", "soft", "calm"]},
        {"kanji": "築", "meaning_en": "build,築", "description": "To build and築. Represents construction.", "tags": ["strong", "smart"]},
    ],
    "tsuru": [
        {"kanji": "鶴", "meaning_en": "crane bird", "description": "Crane bird. Symbolizes longevity and grace.", "tags": ["elegant", "soft", "kind"]},
    ],
    "uta": [
        {"kanji": "歌", "meaning_en": "song, poem", "description": "Song and poetry. Represents artistic expression.", "tags": ["artistic", "cute", "soft"]},
    ],
    "waka": [
        {"kanji": "若", "meaning_en": "young, fresh", "description": "Youth and freshness. Represents vitality.", "tags": ["energetic", "joyful", "soft"]},
    ],
    "yama": [
        {"kanji": "山", "meaning_en": "mountain", "description": "Mountain. Represents strength and stability.", "tags": ["natural", "strong", "calm"]},
    ],
    "yasu": [
        {"kanji": "安", "meaning_en": "peace,安", "description": "Peace and安. Represents tranquility.", "tags": ["calm", "kind", "soft"]},
        {"kanji": "康", "meaning_en": "healthy, peaceful", "description": "Health and peace. Symbolizes well-being.", "tags": ["kind", "calm"]},
        {"kanji": "泰", "meaning_en": "peaceful", "description": "Great peace. Represents calm strength.", "tags": ["strong", "calm"]},
    ],
    "yoshi": [
        {"kanji": "良", "meaning_en": "good, fine", "description": "Good and excellent. Represents quality.", "tags": ["kind", "cool"]},
        {"kanji": "吉", "meaning_en": "good luck", "description": "Good fortune. Symbolizes auspiciousness.", "tags": ["joyful", "kind"]},
        {"kanji": "芳", "meaning_en": "fragrant, virtuous", "description": "Fragrant virtue. Represents good reputation.", "tags": ["elegant", "kind", "soft"]},
        {"kanji": "義", "meaning_en": "justice, righteousness", "description": "Justice and righteousness. Represents moral integrity.", "tags": ["strong", "brave"]},
        {"kanji": "喜", "meaning_en": "joy, rejoice", "description": "Joy and happiness. Symbolizes delight.", "tags": ["joyful", "kind", "cute"]},
    ],
    "yoshi": [
        {"kanji": "佳", "meaning_en": "excellent, beautiful", "description": "Excellence and beauty. Represents grace.", "tags": ["soft", "kind", "elegant"]},
    ],
    "yuko": [
        {"kanji": "優", "meaning_en": "gentle, superior", "description": "Gentle excellence. Represents graceful superiority.", "tags": ["kind", "soft", "elegant"]},
    ],
    "yuri": [
        {"kanji": "百", "meaning_en": "lily flower", "description": "Lily flower. Symbolizes purity and elegance.", "tags": ["elegant", "soft", "cute"]},
        {"kanji": "友", "meaning_en": "friend", "description": "Friendship. Represents companionship.", "tags": ["kind", "soft"]},
    ],
    "yuuki": [
        {"kanji": "勇", "meaning_en": "courage, brave", "description": "Courage and bravery. Represents fearlessness.", "tags": ["strong", "brave", "energetic"]},
        {"kanji": "優", "meaning_en": "gentle, superior", "description": "Gentle excellence. Symbolizes grace.", "tags": ["kind", "soft", "elegant"]},
    ],
} 


import random


def simple_split_romaji(text: str):
    """ローマ字を音節に分割（改良版）"""
    text = text.lower().strip()
    chunks = []
    i = 0
    
    # 3文字の組み合わせを優先的にチェック
    three_char_patterns = ["cha", "chi", "chu", "cho", "sha", "shi", "shu", "sho", 
                          "kya", "kyu", "kyo", "gya", "gyu", "gyo", "nya", "nyu", "nyo",
                          "hya", "hyu", "hyo", "bya", "byu", "byo", "pya", "pyu", "pyo",
                          "mya", "myu", "myo", "rya", "ryu", "ryo"]
    
    while i < len(text):
        if not text[i].isalpha():
            i += 1
            continue
        
        # 3文字先読み
        if i + 2 < len(text):
            three_char = text[i:i+3]
            if three_char in three_char_patterns or three_char in KANJI_DB:
                chunks.append(three_char)
                i += 3
                continue
        
        # 2文字先読み
        if i + 1 < len(text):
            two_char = text[i:i+2]
            if two_char in KANJI_DB:
                chunks.append(two_char)
                i += 2
                continue
        
        # 1文字
        one_char = text[i]
        if one_char in KANJI_DB:
            chunks.append(one_char)
        i += 1
    
    return chunks


def choose_kanji_for_chunk(chunk, style_tag):
    """指定されたチャンクとスタイルに合う漢字を選択"""
    candidates = KANJI_DB.get(chunk, [])
    if style_tag:
        filtered = [c for c in candidates if style_tag in c["tags"]]
        if filtered:
            candidates = filtered
    if not candidates:
        return None
    return random.choice(candidates)


def generate_name_ideas(pron_romaji: str, style_tag: str, num_patterns: int = 5):
    """名前の漢字候補を生成"""
    chunks = simple_split_romaji(pron_romaji)
    
    if not chunks:
        return []
    
    results = []
    attempts = 0
    max_attempts = num_patterns * 3
    
    while len(results) < num_patterns and attempts < max_attempts:
        attempts += 1
        kanji_list = []
        meaning_list = []
        description_list = []
        
        for ch in chunks:
            info = choose_kanji_for_chunk(ch, style_tag)
            if info is None:
                break
            kanji_list.append(info["kanji"])
            meaning_list.append(info["meaning_en"])
            description_list.append(info["description"])
        
        if len(kanji_list) != len(chunks):
            continue
        
        name_kanji = "".join(kanji_list)
        meaning_en = " + ".join(meaning_list)
        
        # 全体的な説明を生成
        full_description = " ".join(description_list)
        
        # 重複チェック
        if not any(r["kanji"] == name_kanji for r in results):
            results.append({
                "kanji": name_kanji,
                "meaning_en": meaning_en,
                "description": full_description,
            })
    
    return results