import customtkinter


class PieChartFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create a canvas widget
        self.canvas = customtkinter.CTkCanvas(self, width=100, height=100)
        self.canvas.grid(row = 1, column = 0)

        # Create a list of colors for the segments
        #self.colors = ["red", "green", "blue", "yellow", "red", "green", "blue", "yellow"]

        self.data = []
        
        # Initialize the chart
        self.update_chart()  

    

    def update_chart(self):
        # Clear the canvas
        self.canvas.delete("pie")
        
        # Add your data here, for example:
        
        
        # Calculate the total value of the data
        total = sum(self.data)
        
        # Calculate the starting angle for each segment
        start_angle = 0
        for i, value in enumerate(self.data):
            if total != 0:
                # Calculate the extent angle for this segment
                extent_angle = (value/total) * 360
                
                # Draw the segment on the canvas
                self.canvas.create_arc(10, 10, 90, 90, start=start_angle, extent=extent_angle, fill=self.colors[i], tags="pie")
                
                # Update the starting angle for the next segment
                start_angle += extent_angle
