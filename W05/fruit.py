def main():
    try:
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")
        
        fruit_list.reverse()
        print(f"Reversed: {fruit_list}")
        
        fruit_list.append('orange')
        print(f"Append Orange: {fruit_list}")
        
        index = fruit_list.index('apple')
        fruit_list.insert(index, 'cherry')
        print(f"Inserted cherry: {fruit_list}")
        
        fruit_list.remove('banana')
        print(f"Remove 'banana': {fruit_list}")
        
        popped = fruit_list.pop()
        print(f"Popped: {popped}")
        
        fruit_list.sort()
        print(f"Sort: {fruit_list}")
        
        fruit_list.clear()
        print(f"Cleared: {fruit_list}")
    except IndexError as index_err:
        print(index_err)
    
if __name__ == "__main__":
    main()