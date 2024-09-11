

class dataClass:
    def __init__(self, refresh_rate, storeTime, ax):
        self.refresh_rate = refresh_rate
        self.storeTime = storeTime
        # number of data points
        n = (1.0 / self.refresh_rate) * storeTime
        self.x_data = [0.0] * int(n)
        for i in range(len(self.x_data)):
            self.x_data[i] = -i * self.refresh_rate
        self.x_data.reverse()
        self.y_data = [0.0] * int(n)
        self.ax = ax
        self.line, = self.ax.plot(self.x_data, self.y_data, '-')

    def addData(self, x, y):
            self.x_data.append(x)
            self.y_data.append(y)
            self.x_data.pop(0)
            self.y_data.pop(0)
            self.line.set_data(self.x_data, self.y_data)
            self.ax.relim()
            self.ax.autoscale_view()
            #self.ax.figure.canvas.draw()  # Force a redraw of the figure