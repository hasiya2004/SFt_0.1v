import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Loading dataset or creating a new one
try:
    df = pd.read_csv("qa_dataset_sinhala.csv")
except FileNotFoundError:
    data = {
        'Question': [
            "ඔයාට කොහොමද",
            "කාලගුණය කොහොමද",
            "විහිළුවක් කීයක් කියන්න",
            # ... [Add more questions in Sinhala]
        ],
        'Answer': [
            "මම කොම්පියුටර් වැඩසටහනක් පමණි, සැබෑ හැඟීම් නැත.",
            "සමාවන්න, මම විද්‍යුත් කාලගුණ තොරතුරු දැනට ලබා නොගත්තා.",
            "මහත්වරයා මාගේ සරල ප්‍රශ්නයට උත්තර දෙන්නේ කුහක්ද?",
            # ... [Add corresponding answers in Sinhala]
        ]
    }

    df = pd.DataFrame(data)

# Using TF-IDF to transform questions for similarity search
tfidf_vectorizer = TfidfVectorizer(stop_words=None)  # Sinhala doesn't have a predefined stop word list in scikit-learn
tfidf_matrix = tfidf_vectorizer.fit_transform(df['Question'])

def get_closest_match_from_df(question):
    tfidf_question = tfidf_vectorizer.transform([question])
    cosine_similarities = linear_kernel(tfidf_question, tfidf_matrix).flatten()
    closest_match_idx = cosine_similarities.argsort()[-1]

    if cosine_similarities[closest_match_idx] == 0:
        return None

    return df.iloc[closest_match_idx]['Answer']

# Interactive loop
while True:
    user_input = input("\nකරුණාකර මට ප්‍රශ්නයක් අසන්න (වෙනස් කිරීමට 'exit' ලියන්න, ප්‍රශ්න-පිළිතුරු දෙමින් එක් කිරීමට 'add' ලියන්න): ")
    if user_input.lower() == 'exit':
        df.to_csv("qa_dataset_sinhala.csv", index=False)
        break
    elif user_input.lower() == 'add':
        question = input("ප්‍රශ්නය ඇතුලත් කරන්න: ")
        answer = input("පිළිතුර ඇතුලත් කරන්න: ")
        df = df.append({"Question": question, "Answer": answer}, ignore_index=True)
        tfidf_matrix = tfidf_vectorizer.fit_transform(df['Question'])
        print("ප්‍රශ්න-පිළිතුරු දෙමින් එක් කර ඇත!")
    else:
        response = get_closest_match_from_df(user_input)
        if response:
            print(response)
        else:
            print("සමාවන්න, මම එයට උත්තරයක් නොදන්නා.")

