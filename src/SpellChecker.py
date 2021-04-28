from ContextIdentifier import ContextIdentifier
from LevenshteinDistance import LevenshteinDistance

class SpellChecker:
    sim_min = 0.75 # Minimum similarity, inclusive

    def __init__(self):
        self.keyword = ContextIdentifier().getKeyword()
        self.distance_counter = LevenshteinDistance()
        
    def getWordSuggestion(self, text):
        word_suggestion = set()
        suggested_word_candidate_set = set(self.keyword)
        word_set = {word.lower() for word in text.split(" ") if word != ""}
        for word in word_set:
            current_suggestion = suggested_word_candidate_set - word_suggestion
            for suggested_word_candidate in current_suggestion:
                distance = self.distance_counter.getDistance(word, suggested_word_candidate)
                value = 1 - distance/max(len(word), len(suggested_word_candidate))
                if value > self.sim_min:
                    word_suggestion.add(suggested_word_candidate)
                    suggested_word_candidate_set.remove(suggested_word_candidate)
                    
        return list(word_suggestion)
        