import matplotlib.pyplot as plt

def fibonacci_sequence(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

# Plotting deret Fibonacci
n = 10
fib_seq = fibonacci_sequence(n)
plt.plot(range(n), fib_seq, marker='o')
plt.title('Deret Fibonacci')
plt.xlabel('n')
plt.ylabel('Fibonacci ke-n')
plt.grid(True)
plt.show()
