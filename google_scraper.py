try:
    # import requests
    from googlesearch import search
except ImportError:
    print("No import named 'google' found")
with open("company name.txt", "r") as name:

        for line in name:
            query = line
            for j in search(query, tld="com", lang='en', num=1, stop=1, pause=10):
                with open("link_collection.txt", "a") as linked:
                    linked.write(j + "\n")
                # print(j)
