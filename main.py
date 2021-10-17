import matplotlib.pyplot as plt
from numpy import *


def main():
    plt.figure(figsize=(13, 7))
    x = arange(-10.0, 10.0, 0.0003)

    plt.fill('#c79fef')
    plt.subplot(231)
    y = sin(x) / x
    plt.axis([-10,10,-10,10])
    plt.plot(x, y, '#c79fef')
    plt.title(r'1)$\frac{\sin{\left(x \right)}}{x}$')
    plt.grid(True)

    plt.subplot(232)
    y = ((x ** 3) - (6 * x ** 2) + (3 * x)) / abs(x)
    plt.axis([-10,10,-10,10])
    plt.plot(x, y, '#c79fef')
    plt.title(r'2)$f {\left(x \right)} = \frac{\left(x^{3} - 6 x^{2} + 3 x \right)}{\left|{x}\right|}$')
    plt.grid(True)

    plt.subplot(233)
    y1 = 2 ** sin(x)
    y2 = 2 ** x
    plt.axis([-10,10,-10,10])
    plt.plot(x, y1, '#7e1e9c', x, y2, '#c79fef')
    plt.title(r'3)$2^{\sin{\left(x \right)}} 2^{x}$')
    plt.grid(True)

    plt.subplot(234)
    y = x ** 2 - 2 * x - 4 - abs(x ** 2 + x - 2)
    plt.axis([-10,10,-10,10])
    plt.plot(x, y, '#c79fef')
    plt.title(r'4)$f {\left(x \right)} = x^{2} - 2x - 4 - |x^{2} + x - 2|$')
    plt.grid(True)

    plt.subplot(235)
    y = (1 / (x - 2)) + 1
    plt.axis([-10,10,-10,10])
    plt.plot(x, y, '#c79fef')
    plt.title(r'5)$f{\left(x \right)} = \frac{1}{x - 2} + 1$')
    plt.grid(True)

    plt.subplot(236)
    x = arange(-50.0, 50.0, 0.0013)
    y = sqrt(x) * sqrt(1 - x)
    plt.plot(x, y, '#c79fef')
    plt.title(r'6)${y} = \sqrt{x} \sqrt{1 - x}$')
    plt.grid(True)

    plt.show()

if __name__ == '__main__':
    main()