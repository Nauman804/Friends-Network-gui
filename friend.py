import tkinter as tk
from tkinter import messagebox
from collections import deque


class FriendsNetwork:
    def __init__(self):
        self.network = {}

    def add_person(self, name):
        if name not in self.network:
            self.network[name] = set()
            return f"{name} added to the network."
        return f"{name} already exists."

    def remove_person(self, name):
        if name in self.network:
            for friends in self.network.values():
                friends.discard(name)
            del self.network[name]
            return f"{name} removed from the network."
        return f"{name} not found."

    def add_friendship(self, p1, p2):
        if p1 in self.network and p2 in self.network:
            self.network[p1].add(p2)
            self.network[p2].add(p1)
            return f"{p1} and {p2} are now friends."
        return "Both persons must exist in the network."

    def remove_friendship(self, p1, p2):
        if p1 in self.network and p2 in self.network:
            self.network[p1].discard(p2)
            self.network[p2].discard(p1)
            return f"{p1} and {p2} are no longer friends."
        return "Both persons must exist in the network."

    def mutual_friends(self, p1, p2):
        if p1 in self.network and p2 in self.network:
            mutual = self.network[p1].intersection(self.network[p2])
            if mutual:
                return f"Mutual friends of {p1} and {p2}: {', '.join(mutual)}"
            return f"No mutual friends between {p1} and {p2}."
        return "Both persons must exist in the network."

    def shortest_path(self, start, end):
        if start not in self.network or end not in self.network:
            return "Both persons must exist in the network."

        queue = deque([(start, [start])])
        visited = set()

        while queue:
            current, path = queue.popleft()
            if current == end:
                return f"Shortest path between {start} and {end}: {' -> '.join(path)}"
            visited.add(current)
            for friend in self.network[current]:
                if friend not in visited:
                    queue.append((friend, path + [friend]))

        return f"No connection found between {start} and {end}."

    def display_network(self):
        if not self.network:
            return "Network is empty."
        result = "🌐 Friends Network:\n"
        for person, friends in self.network.items():
            result += f"{person} → {', '.join(friends) if friends else 'No friends'}\n"
        return result



class FriendsNetworkApp:
    def __init__(self, root):
        self.network = FriendsNetwork()
        self.root = root
        self.root.title("Friends Network System")
        self.root.geometry("650x500")
        self.root.resizable(False, False)
        self.root.config(bg="#E8F0FE")

        tk.Label(root, text="Friends Network System", font=("Arial", 20, "bold"), bg="#E8F0FE").pack(pady=10)

        # Input fields
        frame = tk.Frame(root, bg="#E8F0FE")
        frame.pack(pady=5)

        tk.Label(frame, text="Person 1:", bg="#E8F0FE").grid(row=0, column=0, padx=5)
        self.entry1 = tk.Entry(frame, width=20)
        self.entry1.grid(row=0, column=1, padx=5)

        tk.Label(frame, text="Person 2:", bg="#E8F0FE").grid(row=0, column=2, padx=5)
        self.entry2 = tk.Entry(frame, width=20)
        self.entry2.grid(row=0, column=3, padx=5)

        # Buttons
        btn_frame = tk.Frame(root, bg="#E8F0FE")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Person", command=self.add_person, width=15, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Remove Person", command=self.remove_person, width=15, bg="#f44336", fg="white").grid(row=0, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Add Friendship", command=self.add_friendship, width=15, bg="#2196F3", fg="white").grid(row=1, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Remove Friendship", command=self.remove_friendship, width=15, bg="#FF9800", fg="white").grid(row=1, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Mutual Friends", command=self.mutual_friends, width=15, bg="#9C27B0", fg="white").grid(row=2, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Shortest Path", command=self.shortest_path, width=15, bg="#795548", fg="white").grid(row=2, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Show Network", command=self.display_network, width=33, bg="#607D8B", fg="white").grid(row=3, column=0, columnspan=2, pady=10)


        self.output = tk.Text(root, width=75, height=12, bg="white", fg="black", wrap="word")
        self.output.pack(pady=10)
        self.output.insert(tk.END, "Welcome to the Friends Network System!\n")

    def get_entries(self):
        return self.entry1.get().strip(), self.entry2.get().strip()

    def add_person(self):
        p1, _ = self.get_entries()
        if p1:
            msg = self.network.add_person(p1)
            self.show_output(msg)
        else:
            messagebox.showwarning("Input Error", "Enter a name in 'Person 1' field.")

    def remove_person(self):
        p1, _ = self.get_entries()
        if p1:
            msg = self.network.remove_person(p1)
            self.show_output(msg)
        else:
            messagebox.showwarning("Input Error", "Enter a name in 'Person 1' field.")

    def add_friendship(self):
        p1, p2 = self.get_entries()
        msg = self.network.add_friendship(p1, p2)
        self.show_output(msg)

    def remove_friendship(self):
        p1, p2 = self.get_entries()
        msg = self.network.remove_friendship(p1, p2)
        self.show_output(msg)

    def mutual_friends(self):
        p1, p2 = self.get_entries()
        msg = self.network.mutual_friends(p1, p2)
        self.show_output(msg)

    def shortest_path(self):
        p1, p2 = self.get_entries()
        msg = self.network.shortest_path(p1, p2)
        self.show_output(msg)

    def display_network(self):
        msg = self.network.display_network()
        self.show_output(msg)

    def show_output(self, msg):
        self.output.insert(tk.END, msg + "\n")
        self.output.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = FriendsNetworkApp(root)
    root.mainloop()
