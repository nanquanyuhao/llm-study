import json

def prepare_data(path, size):
    with open(path, 'r', encoding='utf-8') as f:
        batch_docs = []
        for line in f:
            batch_docs.append(json.loads(line.strip()))
            if len(batch_docs) == size:
                yield batch_docs[:]
                batch_docs.clear()

        if batch_docs:
            yield batch_docs