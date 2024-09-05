"""
Question 1. Product Review Analysis
Task 1: Keyword Highlighter

Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.
    reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."

Task 2: Sentiment Tally

Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
Task 3: Review Summary

Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

Example: "This product is really good. I'm...",
"""

reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."]

keywords = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing", "average", "bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

results = []
for review in reviews:
    for keyword in keywords:
        if review.find(keyword)!= -1:
            results.append((review, keyword))

for result in results:
    print("Review: " + result[0])
    print("Keyword: " + result[1].upper())
    print()


reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
ordinary_words = ["average", "standard", "median", "normal", "typical", "regular"]
def review_counter(reviews):
    positive_count = 0
    negative_count = 0
    for count, r in enumerate(reviews):
        for word in positive_words:
            if word in r:
                positive_count += 1
        for word in negative_words:
            if word in r:
                negative_count += 1
    
    print(f"There were found {positive_count} positive and {negative_count} negative reviews out of {count} reviews total!\nWith a {(positive_count / count) * 100:.2f}% positive feedback on this product.\n")
    return positive_count, negative_count

review_counter(reviews)

search = input("Do you want to search for a keyword? (yes/no): ")

while search.lower() == "yes":
    keyword = input("Enter a keyword to search for: ")
    found_reviews = [review for review in reviews if keyword in review]
    if found_reviews:
        for review in found_reviews:
            print("Found a review that mentions:", keyword)
            print(review)
    else:
        print("No reviews found that mention:", keyword)
    
    search = input("Do you want to search for another keyword? (yes/no): ")

print("Thank you for your time!")


def create_summary(review):
    if len(review) <= 30:
        return review
    else:
        summary = review[:30]
        last_space = summary.rfind(' ')
        if last_space!= -1:
            summary = summary[:last_space]
        return summary + "…"


def add_review(reviews):
    while True:
        add_review = input("Do you want to add a review? (yes/no): ")
        if add_review.lower() == "yes":
            review = input("Enter your review: ")
            reviews.append(review)
            print("Your review has been added.")
        elif add_review.lower() == "no":
            print("Thank you for your time!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

add_review(reviews)

for review in reviews:
    print("Summary:", create_summary(review))
    print()