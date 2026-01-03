#!/usr/bin/python3
"""
Task 2: Consuming and processing data from an API using Python
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints the status code
    and the titles of the posts.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves specific fields
    (id, title, body) into a CSV file named posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        
        # Structure the data into a list of dictionaries
        posts_data = []
        for post in posts:
            post_dict = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            posts_data.append(post_dict)

        # Write data to CSV
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(posts_data)
