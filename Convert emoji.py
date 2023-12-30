import demoji

# Downloading emojis (if required, although not necessary in newer version
# Text with emojis
text_with_emojis = "I love 😉 coding! 🚀"

# Extracting emojis and their descriptions
emojis_dict = demoji.findall(text_with_emojis)
print(emojis_dict)  # Output: {'😊': 'smiling_face_with_smiling_eyes', '🚀': 'rocket'}

# Removing emojis from text
text_without_emojis = demoji.replace(text_with_emojis, "")
print(text_without_emojis)  # Output: 'I love  coding! '

