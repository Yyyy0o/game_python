import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

if __name__ == '__main__':
    font_set = FontProperties(fname=r"c:windows\fonts\simsun.ttc", size=14)

    squares = [1, 4, 9, 16, 25]

    fig, ax = plt.subplots()
    ax.plot(squares, linewidth=3)

    ax.set_title(u"平方数", fontproperties=font_set)
    ax.set_xlabel(u"值", fontproperties=font_set)
    ax.set_ylabel(u"值的平方", fontproperties=font_set)

    ax.tick_params(axis='both', labelsize=14)

    plt.show()
