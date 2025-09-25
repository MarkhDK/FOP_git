def display_feed(posts):
    pass


def create_post(posts, text):
    id = len(posts)
    hashtags = get_hashtags(text)

    posts[id] = {"text": text, "hashtags": hashtags}


def get_hashtags(text):
    words = split_words(text)
    hashtags = extract_hashtags(words)
    unique_hashtags = get_unique_hashtags(hashtags)


def split_words(text):
    word = ""
    words = []
    for i in range(len(text) - 1):
        if text[i] != " ":
            word = word + text[i]

        if text[i] == " " or i == len(text) - 1:
            if text[i] != "":
                words.append(word)
                word = ""
    return words


def extract_hashtags(words):
    hashtags = []
    for i in range(len(words) - 1):
        if words[i][0] == "#":
            hashtags.append(words[i])
    return hashtags


def get_unique_hashtags(hashtags):
    unique_hashtags = []
    for i in range(len(hashtags)):
        match_found = False
        for j in range(len(unique_hashtags)):
            if hashtags[i] == unique_hashtags[j]:
                match_found = True
        if match_found != True:
            unique_hashtags.append(hashtags[i])


def main():
    user_input = ""
    posts = {}
    while user_input != "exit":
        display_feed(posts)
        user_input = input("Write a new tweet!\n")
        if user_input != "exit":
            posts = create_post(posts, user_input)


if __name__ == "__main__":
    main()
