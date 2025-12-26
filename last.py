
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataAnalysisProject:

    def __init__(self):
        self.data = None
        self.last_plot = None

    def load_dataset(self):
        path = input("Enter CSV file path: ")
        try:
            self.data = pd.read_csv(path)
            print("Dataset loaded successfully!")
        except Exception as e:
            print(" Error:", e)

    def explore_dataset(self):
        if self.data is None:
            print("Load dataset first!")
            return

        print("\n1. First 5 rows")
        print("2. Last 5 rows")
        print("3. Column names")
        print("4. Data types")
        print("5. Dataset info")

        ch = int(input("Enter choice: "))

        if ch == 1:
            print(self.data.head())
        elif ch == 2:
            print(self.data.tail())
        elif ch == 3:
            print(self.data.columns)
        elif ch == 4:
            print(self.data.dtypes)
        elif ch == 5:
            print(self.data.info())

    def show_shape(self):
        print("Rows:", self.data.shape[0])
        print("Columns:", self.data.shape[1])

    def unique_values(self):
        col = input("Enter column name: ")
        print(self.data[col].unique())

    def rename_column(self):
        old = input("Old column name: ")
        new = input("New column name: ")
        self.data.rename(columns={old: new}, inplace=True)
        print(" Column renamed")

    def delete_column(self):
        col = input("Column name to delete: ")
        self.data.drop(columns=[col], inplace=True)
        print("Column deleted")

    def handle_missing_values(self):
        print("\n1. Show missing values")
        print("2. Fill with mean")
        print("3. Drop rows")
        print("4. Replace with value")

        ch = int(input("Enter choice: "))

        if ch == 1:
            print(self.data.isnull().sum())
        elif ch == 2:
            self.data.fillna(self.data.mean(numeric_only=True), inplace=True)
            print("Filled with mean")
        elif ch == 3:
            self.data.dropna(inplace=True)
            print("Rows dropped")
        elif ch == 4:
            val = input("Enter value: ")
            self.data.fillna(val, inplace=True)
            print(" Values replaced")

  
    def descriptive_stats(self):
        print(self.data.describe())

    def dataframe_operations(self):
        print("\n1. Search")
        print("2. Sort")
        print("3. Filter")
        print("4. Aggregate")

        ch = int(input("Enter choice: "))

        if ch == 1:
            c = input("Column: ")
            v = input("Value: ")
            print(self.data[self.data[c].astype(str) == v])

        elif ch == 2:
            c = input("Sort column: ")
            print(self.data.sort_values(by=c))

        elif ch == 3:
            c = input("Column: ")
            v = input("Value: ")
            print(self.data[self.data[c].astype(str) == v])

        elif ch == 4:
            c = input("Numeric column: ")
            print("Sum:", self.data[c].sum())
            print("Mean:", self.data[c].mean())
            print("Count:", self.data[c].count())

    def group_by_analysis(self):
        g = input("Group by column: ")
        n = input("Numeric column: ")
        print(self.data.groupby(g)[n].mean())

    def visualize_data(self):
        print("\n1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Heatmap")
        print("7. Box Plot")

        ch = int(input("Enter choice: "))

        if ch == 1:
            x = input("X column: ")
            y = input("Y column: ")
            self.data.plot(kind='bar', x=x, y=y)
            self.last_plot = plt
            plt.show()

        elif ch == 2:
            x = input("X column: ")
            y = input("Y column: ")
            self.data.plot(kind='line', x=x, y=y)
            self.last_plot = plt
            plt.show()

        elif ch == 3:
            x = input("X column: ")
            y = input("Y column: ")
            plt.scatter(self.data[x], self.data[y])
            self.last_plot = plt
            plt.show()

        elif ch == 4:
            c = input("Column: ")
            self.data[c].value_counts().plot(kind='pie', autopct='%1.1f%%')
            self.last_plot = plt
            plt.show()

        elif ch == 5:
            c = input("Numeric column: ")
            plt.hist(self.data[c])
            self.last_plot = plt
            plt.show()

        elif ch == 6:
            sns.heatmap(self.data.corr(numeric_only=True), annot=True)
            self.last_plot = plt
            plt.show()

        elif ch == 7:
            c = input("Numeric column: ")
            sns.boxplot(y=self.data[c])
            self.last_plot = plt
            plt.show()

    def save_graph(self):
        name = input("Enter file name (plot.png): ")
        self.last_plot.savefig(name)
        print("Graph saved")

    def export_csv(self):
        name = input("Enter file name (cleaned.csv): ")
        self.data.to_csv(name, index=False)
        print("Dataset exported")

def main():
    p = DataAnalysisProject()

    while True:
        print("\n========= DATA ANALYSIS PROJECT =========")
        print("1. Load Dataset")
        print("2. Explore Dataset")
        print("3. Dataset Shape")
        print("4. Unique Values")
        print("5. Rename Column")
        print("6. Delete Column")
        print("7. Handle Missing Values")
        print("8. Descriptive Statistics")
        print("9. DataFrame Operations")
        print("10. Group By Analysis")
        print("11. Data Visualization")
        print("12. Save Visualization")
        print("13. Export CSV")
        print("14. Exit")

        ch = int(input("Enter choice: "))

        if ch == 1:
            p.load_dataset()
        elif ch == 2:
            p.explore_dataset()
        elif ch == 3:
            p.show_shape()
        elif ch == 4:
            p.unique_values()
        elif ch == 5:
            p.rename_column()
        elif ch == 6:
            p.delete_column()
        elif ch == 7:
            p.handle_missing_values()
        elif ch == 8:
            p.descriptive_stats()
        elif ch == 9:
            p.dataframe_operations()
        elif ch == 10:
            p.group_by_analysis()
        elif ch == 11:
            p.visualize_data()
        elif ch == 12:
            p.save_graph()
        elif ch == 13:
            p.export_csv()
        elif ch == 14:
            print("Program Ended")
            break
        else:
            print(" Invalid choice")

main()