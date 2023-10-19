# make the mean time and SE spent explicit:
grouped_data = data.groupby('landing_page')['time_spent_on_the_page'].agg(['mean', 'sem']).reset_index()

plt.figure(figsize=(7, 6)) # set figure size
plt.bar(grouped_data['landing_page'], grouped_data['mean'], yerr=grouped_data['sem'], # plots mean + SE by group
        capsize=2, # changes width of SE bar "caps"
        color='skyblue') # color for the bar plots

# labels:
plt.xlabel('Landing Page Shown')
plt.ylabel('Minutes')
plt.ylim(0, 8)
plt.title('Average Time Users Spent Across Landing Pages with Standard Errors')

# cleaning up the plot
ax = plt.gca() # for making customizations to our axes
ax.spines['top'].set_visible(False) # remove the top border
ax.spines['right'].set_visible(False) # remove the right border
ax.spines['bottom'].set_visible(False) # remove the bottom border
ax.set_xticks([]) # remove x-axis ticks
label_positions = [0, 1]  # positioning: 0 is the left box, and 1 is the right box, since these are categorical
label_texts = ['New', 'Old']  # set the labels for the left and right boxes
for i in range(len(label_positions)):
    plt.text(label_positions[i], -0.52, label_texts[i], ha='center', va='center', fontsize=10)

plt.show()
