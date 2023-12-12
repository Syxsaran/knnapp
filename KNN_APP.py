import tkinter as tk
from sklearn.neighbors import KNeighborsClassifier
from PIL import Image, ImageTk

class KnnApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Knn App")
        self.root.geometry("1080x720")
        
        self.widgets()

    

    def widgets(self):
        greeting = tk.Label(self.root, text="KNN APP", fg="black", font=("Arial", 16))
        greeting.place(x=10, y=10)

        frame1 = tk.Frame(self.root, width=500, height=500, bg="#001466")
        frame1.place(x=30, y=50)

        frame2 = tk.Frame(self.root, width=370, height=500, bg="#612180")
        frame2.place(x=700, y=10)

        frame2_text = tk.Label(frame2, text="INPUT", fg="white", font=("Arial", 20), bg="#612180")
        frame2_text.place(x=260, y=10)

        input_labels = ["SEX", "AGE", "WEIGHT", "HEIGHT"]
        self.input_entries = []

        for i, label_text in enumerate(input_labels):
            label = tk.Label(frame2, text=label_text, fg="white", font=("Arial", 14), bg="#612180")
            label.place(x=20, y=70 + i * 40)

            var = tk.StringVar()
            entry = tk.Entry(frame2, textvariable=var, font=("Arial", 14), bg="white")
            entry.place(x=120, y=70 + i * 40)

            self.input_entries.append(entry)

        frame3 = tk.Frame(self.root, width=1065, height=220, bg="#50E943")
        frame3.place(x=5, y=510)

        frame4 = tk.Frame(self.root, width=970, height=180, bg="#FFFFFF")
        frame4.place(x=55, y=560)

        predict_button = tk.Button(frame4, text="Predict", command=self.predict, font=("Arial", 22), bg="#A577BB", fg="black")
        predict_button.grid(row=0, column=0, pady=60, padx=250)

        self.predict_label = tk.Label(frame4, text="Predict: unknown", font=("Arial", 22), bg="#FFFFFF", fg="black")
        self.predict_label.grid(row=0, column=1, pady=60, padx=60)

        self.data = [
            ["SEX", "AGE", "WEIGHT", "HEIGHT", "BODY"],
            [1, 27, 60, 170, "slim"],
            [1, 18, 70, 180, "fat"],
            [0, 19, 64, 174, "slim"],
            [0, 25, 80, 167, "fat"],
            [1, 40, 56, 172, "slim"],
            [0, 32, 45, 156, "thin"],
            [1, 24, 52, 170, "thin"],
            [1, 28, 70, 180, "slim"],
            [0, 19, 45, 165, "thin"],
            [1, 20, 120, 165, "fat"],
        ]

        for i, row in enumerate(self.data):
            for j, value in enumerate(row):
                label = tk.Label(frame1, width=10, height=1, text=str(value), bg="#FFFFFF", fg="black")
                label.grid(row=i, column=j, padx=10, pady=10)
                if i == 0:
                    label.configure(bg="#F1D3FF")



    def predict(self):
        user_input = [float(entry.get()) for entry in self.input_entries]

        knn_model = KNeighborsClassifier(n_neighbors=3)
        X_train = [row[:-1] for row in self.data[1:]] 
        y_train = [row[-1] for row in self.data[1:]]
        knn_model.fit(X_train, y_train)
        prediction = knn_model.predict([user_input])

        self.predict_label.configure(text=f"Predict: {prediction[0]}")



        if prediction[0] == "slim":
            self.open_new_window_slim("slim.png")

    def open_new_window_slim(self, image_path):
        new_window = tk.Toplevel(self.root)
        new_window.title("Image Window")

        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(new_window, image=photo)
        label.image = photo
        label.pack()



def main():
    root = tk.Tk()
    app = KnnApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
