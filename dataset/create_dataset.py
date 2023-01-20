import datasets

domains = ["blogs", "comics", "court", "eu_docs", "gov_docs", "government_gazzette", "law_eu", "law_mt", "legal", "nonfiction", "parliament", "press_eu", "press_mt", "speeches", "theses", "umlib_oar", "web_general", "wiki"]

entire_string = ""

for domain in domains:
    dataset = datasets.load_dataset("MLRS/korpus_malti", domain)

    for document in dataset['train']:
        entire_string += " ".join(document['text'])

    with open("dataset/dataset.txt", "w") as f:
        f.write(entire_string)
