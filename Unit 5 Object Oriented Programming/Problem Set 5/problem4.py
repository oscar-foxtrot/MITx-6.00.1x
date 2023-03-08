def decrypt_story():
    """
    Decrypts the story
    
    Returns: str: the joke in decrypted text
    """
    story = CiphertextMessage(get_story_string())
    return story.decrypt_message()
