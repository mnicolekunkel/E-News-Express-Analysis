# make the mean time and SE spent explicit:
grouped_data = data.groupby('language_preferred')['time_spent_on_the_page'].agg(['mean', 'sem']).reset_index()

plt.figure(figsize=(7, 6)) # set figure size
plt.bar(grouped_data['language_preferred'], grouped_data['mean'], yerr=grouped_data['sem'], # plots mean + SE by group
        capsize=2, # changes width of SE bar "caps"
        color='skyblue') # color for the bar plots

# labels:
plt.ylabel('Minutes')
plt.ylim(0, 7)
plt.title('Average Time Users Spent on Landing Page Across Preferred Languages with Standard Errors')
plt.tick_params(axis='x', which='both', bottom=False) # removes x axis ticks under bars while preserving labels

# cleaning up the plot
ax = plt.gca() # for making customizations to our axes
ax.spines['top'].set_visible(False) # remove the top border
ax.spines['right'].set_visible(False) # remove the right border
ax.spines['bottom'].set_visible(False) # remove the bottom border

plt.show()
