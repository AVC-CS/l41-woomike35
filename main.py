def main():
    N = int(input("Enter the number N:10"))

    result = [2 ** i for i in range(N + 1)]

    print(*result)

    return result

if __name__ == '__main__':
    result = main()
