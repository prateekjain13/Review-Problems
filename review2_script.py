def find_second_largest(lst):
    """
    Finds the second largest element in a list, or returns a message if not found.

    Args:
    lst (list): List of integers or floats.

    Returns:
    int or float: Second largest element or message if not found.
    """
    largest=-10**31
    second=-10**30
    for num in lst:
        if num>largest:
            second=largest
            largest=num
        elif num>second and num<largest:
            second=num
    return second or "No second largest element"

def main():
    try:
        lst=[]
        n=int(input("Enter number of elements: "))
        if n<2:
            raise ValueError("At least two elements are required.")
        for i in range(n):
            lst.append(int(input("Enter number: ")))
        print(f"Second largest element in list: {find_second_largest(lst)}")
    except ValueError as e:
        print("Error:", e)

if __name__=="__main__":
    main()
