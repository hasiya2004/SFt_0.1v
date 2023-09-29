# Q&A Retrieval System

## Overview

Developed by Hasindu Senarathne, this code provides a simple Q&A retrieval system using the Term Frequency-Inverse Document Frequency (TF-IDF) technique. The system can find the closest match to a user's question from a given dataset and return the associated answer. It also provides an interactive loop for the user to ask questions and add new Q&A pairs to the dataset.

## Features

- Load an existing Q&A dataset or create a new one.
- Search for the closest matching question using TF-IDF and cosine similarity.
- Interactively ask questions.
- Add new Q&A pairs to the dataset.
- Save the updated dataset.

## Prerequisites

- Python
- pandas: `pip install pandas`
- scikit-learn: `pip install scikit-learn`

## How To Use

1. Run the script.
2. Type in your question when prompted.
3. If the system recognizes a similar question from the dataset, it will return the associated answer.
4. Type 'add' to add a new Q&A pair to the dataset.
5. Type 'exit' to save the dataset and quit the program.

## Structure

- **Loading Dataset**: The system first tries to load an existing `qa_dataset.csv`. If not found, it creates a new dataset with some predefined questions and answers.
- **TF-IDF Transformation**: The system transforms the questions using TF-IDF for similarity search.
- **Retrieving Answers**: Based on cosine similarity, the system finds the closest matching question from the dataset and returns its answer.
- **Interactive Loop**: The user can interact with the system to ask questions or add new Q&A pairs. The updated dataset is saved when exiting.

## Example Questions in the Dataset

- "how are you"
- "weather"
- "joke"
- "photosynthesis"
- ... and many more.

## Contributions

If you wish to contribute to this project or have any suggestions, feel free to reach out to Hasindu Senarathne.

