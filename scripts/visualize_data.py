import matplotlib.pyplot as plt

def plot_data(df, column):
    print(f"📊 Plotting '{column}' distribution...")
    df[column].value_counts().plot(kind='bar', color='skyblue')
    plt.title(f"{column.capitalize()} Distribution")
    plt.xlabel(column.capitalize())
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("data/plot.png")
    plt.show()
    print("✅ Plot saved as data/plot.png")
