from datastructure.Utility import countBST


def main():
    number = int(input("Enter the number:-"))

    tree_ways = countBST(number)

    print("Count of BST with", number, "nodes is", tree_ways)


if __name__ == '__main__':
    main()
