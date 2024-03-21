import matplotlib.pyplot as plt
import numpy as np

# Define the function to plot
def iv_curve(order, voltage):
    return (voltage ** order) / (1 + voltage ** order)

# Create the voltage range
voltage = np.linspace(0.8, 1.2, 100)

# Plotting the IV curves for different orders
# Adjusting line styles and colors to match the uploaded figure
# Adjusting the plot to add markers to the lines

# Adjusting the plot to have non-solid (hollow) markers with 'none' fillstyle

plt.clf()

# Define line styles and hollow markers for each order to match the uploaded figure
line_styles = {
    10: ('k', '-', 'o', 'none'),   # Solid line with hollow circle markers
    20: ('r', '--', 's', 'none'),  # Dashed line with hollow square markers
    40: ('b', ':', '^', 'none'),   # Dotted line with hollow triangle_up markers
    100: ('g', '-.', 'D', 'none')  # Dash-dot line with hollow diamond markers
}

# Plot each curve with the specified line style and hollow marker
for order, (color, style, marker, fill_style) in line_styles.items():
    current = iv_curve(order, voltage)
    plt.plot(voltage, current, linestyle=style, color=color, marker=marker, fillstyle=fill_style, markevery=10, label=f'Order {order}',linewidth=5, markersize=15, markeredgewidth=3)

# Customizing the plot to match the given style
plt.xlabel('Voltage (mV)')
plt.ylabel('Current (μA)')
plt.title('The science + ieee styles for IEEE papers:')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
