import csv
import re
OUTPUT_FILE = "linguistic_report.csv"
from collections import Counter


ITALIAN_STOPWORDS = {
    "il", "lo", "la", "i", "gli", "le", "un", "una", "uno",
    "di", "a", "da", "in", "con", "su", "per", "tra", "fra",
    "e", "o", "che", "è", "sono", "questo", "questa", "nei",
    "dati", "spesso"
}

ENGLISH_STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "in", "on",
    "with", "for", "is", "are", "this", "that", "can", "often"
}


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zàèéìòù\s']", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize(text):
    cleaned = clean_text(text)
    return cleaned.split()


ddef detect_language(text):
    text_lower = text.lower()

    italian_markers = ["è", "questa", "questo", "dati", "linguistici", "intelligenza"]
    english_markers = ["this", "language", "data", "artificial", "intelligence", "project"]

    italian_score = sum(1 for marker in italian_markers if marker in text_lower)
    english_score = sum(1 for marker in english_markers if marker in text_lower)

    total = italian_score + english_score

    if total == 0:
        return "Unknown"

    ratio = italian_score / total

    if 0.4 <= ratio <= 0.6:
        return "Mixed (balanced)"
    elif ratio > 0.6:
        if english_score > 0:
            return "Italian (dominant)"
        return "Italian"
    else:
        if italian_score > 0:
            return "English (dominant)"
        return "English"

def lexical_diversity(tokens):
    if not tokens:
        return 0
    return round(len(set(tokens)) / len(tokens), 2)


def remove_stopwords(tokens, language):
    if language.startswith("Italian"):
        return [t for t in tokens if t not in ITALIAN_STOPWORDS]

    if language.startswith("English"):
        return [t for t in tokens if t not in ENGLISH_STOPWORDS]

    if language.startswith("Mixed"):
        combined_stopwords = ITALIAN_STOPWORDS.union(ENGLISH_STOPWORDS)
        return [t for t in tokens if t not in combined_stopwords]

    return tokens


def analyze_text(text):
    language = detect_language(text)
    tokens = tokenize(text)
    content_tokens = remove_stopwords(tokens, language)

    return {
        "language": language,
        "word_count": len(tokens),
        "unique_words": len(set(tokens)),
        "lexical_diversity": lexical_diversity(tokens),
        "top_words": Counter(content_tokens).most_common(5)
    }


def load_texts(filepath):
    rows = []

    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    return rows


def main():
    texts = load_texts("data/sample_texts.csv")

    total_texts = 0
    language_counts = {"Italian": 0, "English": 0, "Unknown": 0}
    all_tokens = []
    lexical_scores = []
    language_word_counts = {"Italian": [], "English": [], "Unknown": []}
    language_lexical_scores = {"Italian": [], "English": [], "Unknown": []}
    report_rows = []

    for row in texts:
        analysis = analyze_text(row["text"])
        report_rows.append({
            "id": row["id"],
            "language": analysis["language"],
            "word_count": analysis["word_count"],
            "unique_words": analysis["unique_words"],
            "lexical_diversity": analysis["lexical_diversity"],
            "top_words": analysis["top_words"]
        })

        total_texts += 1
        language_counts[analysis["language"]] += 1
        lexical_scores.append(analysis["lexical_diversity"])

        tokens = tokenize(row["text"])
        content_tokens = remove_stopwords(tokens, analysis["language"])
        all_tokens.extend(content_tokens)

        print(f"\nID: {row['id']}")
        print(f"Text: {row['text']}")
        print(f"Language: {analysis['language']}")
        print(f"Word count: {analysis['word_count']}")
        print(f"Unique words: {analysis['unique_words']}")
        print(f"Lexical diversity: {analysis['lexical_diversity']}")
        language_word_counts[analysis["language"]].append(analysis["word_count"])
        language_lexical_scores[analysis["language"]].append(analysis["lexical_diversity"])
        print(f"Top words: {analysis['top_words']}")
        
        

    print("\n--- DATASET SUMMARY ---")
    print(f"Total texts: {total_texts}")
    print(f"Italian texts: {language_counts['Italian']}")
    print(f"English texts: {language_counts['English']}")

    avg_lexical = round(sum(lexical_scores) / len(lexical_scores), 2)
    print(f"Average lexical diversity: {avg_lexical}")

    top_words = Counter(all_tokens).most_common(10)
    print(f"Top words overall: {top_words}")
    print("\n--- LANGUAGE COMPARISON ---")

    for language in ["English", "Italian"]:
       word_counts = language_word_counts[language]
       lexical_values = language_lexical_scores[language]

       avg_words = round(sum(word_counts) / len(word_counts), 2) if word_counts else 0
       avg_lexical = round(sum(lexical_values) / len(lexical_values), 2) if lexical_values else 0

       print(f"{language}:")
       print(f"  Texts: {language_counts[language]}")
       print(f"  Average word count: {avg_words}")
       print(f"  Average lexical diversity: {avg_lexical}")
       with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as file:
           fieldnames = ["id", "language", "word_count", "unique_words", "lexical_diversity", "top_words"]
           writer = csv.DictWriter(file, fieldnames=fieldnames)
           writer.writeheader()
           writer.writerows(report_rows)
       print(f"\nReport exported to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()