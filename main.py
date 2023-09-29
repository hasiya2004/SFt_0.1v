import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Loading dataset or creating a new one
try:
    df = pd.read_csv("qa_dataset.csv")
except FileNotFoundError:
    data = {
        'Question': [
            "how are you",
            "weather",
            "joke",
            "photosynthesis",
            "world series in 2020",
            "how does orbital navigation work",
            "tell me about the apollo 11 mission",
            "how do neurons transmit signals",
            "what is the role of synapses",
            "explain the theory of relativity",
            "who was the first human to travel to space",
            "describe the function of the hippocampus"
        ],
        'Answer': [
            "I'm just a computer program, so I don't have feelings, but I'm operating normally.",
            "Sorry, I don't have real-time weather information right now.",
            "Why did the chicken cross the road? To get to the other side.",
            "Photosynthesis is the process used by plants, algae, and some bacteria to convert sunlight into energy.",
            "The Los Angeles Dodgers won the World Series in 2020.",
            "Orbital navigation involves understanding and controlling the trajectory of a spacecraft to ensure it remains on the desired orbital path.",
            "Apollo 11 was the first manned mission to land on the Moon in 1969, with astronauts Neil Armstrong, Buzz Aldrin, and Michael Collins.",
            "Neurons transmit signals using a combination of electrical impulses (action potentials) and chemical signals (neurotransmitters).",
            "Synapses are the junctions where neurons communicate. They transmit signals using neurotransmitters.",
            "The theory of relativity, proposed by Albert Einstein, revolutionized the way we understand time, space, and the universe's structure.",
            "Yuri Gagarin was the first human to travel to space aboard Vostok 1 in 1961.",
            "The hippocampus is a region in the brain primarily associated with memory and spatial navigation."
        ]
    }
    # Adding questions related to Brownian Motion
    brownian_questions = [
        "What is Brownian motion?",
        "Who discovered Brownian motion?",
        "How is Brownian motion related to diffusion?",
        "Is Brownian motion a result of random particle movement?",
        # ... [Add up to 100 questions]
    ]

    brownian_answers = [
        "Brownian motion describes the random movement of particles suspended in a fluid (liquid or gas) resulting from their collision with fast atoms or molecules in the gas or liquid.",
        "Brownian motion was discovered by the botanist Robert Brown in 1827.",
        "Brownian motion is a physical phenomenon underlying the mathematical theory of diffusion and heat conduction.",
        "Yes, Brownian motion is due to the random movement of particles.",
        # ... [Add corresponding answers for the above questions]
    ]

    # Appending to the existing dataset
    data['Question'].extend(brownian_questions)
    data['Answer'].extend(brownian_answers)

    df = pd.DataFrame(data)

# Using TF-IDF to transform questions for similarity search
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df['Question'])

def get_closest_match_from_df(question):
    # Transforming the user's question with the vectorizer
    tfidf_question = tfidf_vectorizer.transform([question])

    # Calculating cosine similarities
    cosine_similarities = linear_kernel(tfidf_question, tfidf_matrix).flatten()

    # Getting the index of the most similar question
    closest_match_idx = cosine_similarities.argsort()[-1]

    if cosine_similarities[closest_match_idx] == 0:
        return None

    return df.iloc[closest_match_idx]['Answer']

# Interactive loop
while True:
    user_input = input("\nAsk me a question (or type 'exit' to quit, 'add' to add a Q&A pair): ")
    if user_input.lower() == 'exit':
        df.to_csv("qa_dataset.csv", index=False)
        break
    elif user_input.lower() == 'add':
        question = input("Enter the question: ")
        answer = input("Enter the answer: ")
        df = df.append({"Question": question, "Answer": answer}, ignore_index=True)
        # Re-transforming the tfidf matrix after adding new data
        tfidf_matrix = tfidf_vectorizer.fit_transform(df['Question'])
        print("Q&A pair added!")
    else:
        response = get_closest_match_from_df(user_input)
        if response:
            print(response)
        else:
            print("Sorry, I don't know the answer to that.")
