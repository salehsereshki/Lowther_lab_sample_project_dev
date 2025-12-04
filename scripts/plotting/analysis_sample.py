import matplotlib.pyplot as plt

def distribution_plot(data_dict, title, xlabel, ylabel, output_file):
    plt.figure(figsize=(10, 6))
    plt.boxplot(data_dict.values(), labels=data_dict.keys())
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(output_file)
    plt.close()
