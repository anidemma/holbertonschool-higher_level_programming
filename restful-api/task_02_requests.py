import requests
import csv

def fetch_and_print_posts():
    request = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = request.json()

    print("Status Code: {}".format(request.status_code))    
    if request.status_code == 200:
        for post in posts:
            print(post["title"])
        print(request.status_code)

def fetch_and_save_posts():
    request = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = request.json()

    print("Status Code: {}".format(request.status_code))
    if request.status_code == 200:
        with open('posts.csv', 'w', newline='') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow({'id': post['id'], 'title': post['title'], 'body': post['body']})
        print(request.status_code)
