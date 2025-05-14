        search_btn = Button(Search_frame, text="Search", width=12,
                            font=("times new roman", 12, "bold"),
                            bg="blue", fg="white",
                            command=self.search_data)
        search_btn.grid(row=0, column=3, padx=4)

        # Show All button
        showAll_btn = Button(Search_frame, text="Show All", width=12,
                            font=("times new roman", 12, "bold"),
                            bg="blue", fg="white",
                            command=self.fetch_data)
        showAll_btn.grid(row=0, column=4, padx=4)