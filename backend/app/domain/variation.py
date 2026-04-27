import re

SWAP_DICT = {
    "Rahul": "Riya",
    "Riya": "Rahul",
    "male": "female",
    "female": "male",
    "he": "she",
    "she": "he",
    "his": "her",
    "her": "his",
    "man": "woman",
    "woman": "man"
}

def create_variation(prompt: str) -> str:
    """Create a variation by swapping sensitive attributes deterministically."""
    applied_swaps = set()
    
    def replace_func(match):
        w = match.group(0)
        lw = w.lower()
        for k, v in SWAP_DICT.items():
            if lw == k.lower():
                # Prevent symmetrical un-swapping
                if v.lower() in applied_swaps:
                    return w
                applied_swaps.add(k.lower())
                
                if w.istitle():
                    return v.capitalize()
                elif w.isupper():
                    return v.upper()
                else:
                    return v
        return w
        
    return re.sub(r'\b[a-zA-Z]+\b', replace_func, prompt)
