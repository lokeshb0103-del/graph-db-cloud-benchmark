import csv

nodes = set()
relationships = []

with open("datasets/wiki-Vote.txt", "r") as file:

    for line in file:

        if line.startswith("#"):
            continue

        source, target = line.strip().split()

        nodes.add(source)
        nodes.add(target)

        relationships.append([source, target])

with open("datasets/nodes.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["id"])

    for node in sorted(nodes):
        writer.writerow([node])

with open("datasets/relationships.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["source", "target"])

    writer.writerows(relationships)

print("Dataset converted successfully!")