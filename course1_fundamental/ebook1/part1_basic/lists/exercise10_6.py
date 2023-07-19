def is_anagram(string1, string2):
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False
    
print(is_anagram("post", "tsop"))
print(is_anagram("post", "tgop"))