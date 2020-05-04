import matplotlib
import numpy as np
from matplotlib import pyplot as plt
import cycler

# n = 3
# color = plt.cm.viridis(np.linspace(0, 1, n))
# matplotlib.rcParams['axes.prop_cycle'] = cycler.cycler('color', color)

# plt.rcParams["axes.prop_cycle"] = plt.cycler("color", plt.cm.tab20c.colors)
# plt.rcParams["axes.prop_cycle"] = plt.cycler("color","viridis")
def quantile_plot(q):
    error=np.arange(-1,1,0.01)
    
    quantile_loss = error*(q-(error<0))
    quantile_loss2 = np.maximum(q * error, (q - 1) * error)
    # print(quantile_loss)
    plt.figure(1)
    plt.plot(error,quantile_loss, label=rf'$\tau$={q}')
    plt.legend()



if __name__ == "__main__":
    for q in [0.25, 0.5, 0.75, 0.9]:
        quantile_plot(q=q)
    plt.title('Quantile loss')
    plt.xlabel('Residual')
    plt.ylabel('Loss')
    plt.xticks(np.arange(-1, 1.5, step=0.5))
    plt.show()
    
