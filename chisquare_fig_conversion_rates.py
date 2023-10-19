# creating a normalized crosstab:
ct = pd.crosstab(data['language_preferred'], data['converted'], normalize=True) # normalize puts things into proportions

# define colors for each conversion category
color_mapping = {
    "yes": 'skyblue',
    "no": '#9a8c98'
}

ax = pd.crosstab(data.language_preferred, data.converted, normalize=True).plot(kind='bar',
                                                                          stacked=True,
                                                                          color=[color_mapping[col] for col in ct.columns]);

# customizing the legend
handles, labels = ax.get_legend_handles_labels();
ax.legend(handles=handles, labels=['no', 'yes'], title='Conversion Status', # edit text
          bbox_to_anchor=(1, 1), loc='upper left'); # move the legend to the right so it doesn't overlap with the bars

plt.title('Preferred Language and Conversion') # plot title
ax.set_ylabel('Proportion of Total Sample') # y axis label
ax.set_xlabel('') # remove the x axis label
ax.tick_params(axis='x', rotation=45) # the rotation default is 90 degrees

# removing unnecessary lines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# add percentage labels to each bar, denoting the percent of the total sample contained in each bar
for i, container in enumerate(ax.containers):
    for j, v in enumerate(container):
        total = sum(ct.iloc[j])
        percentage = f'{v.get_height() * 100:.0f}%'
        ax.annotate(percentage, (v.get_x() + v.get_width() / 2, v.get_y() + v.get_height() / 2),
                    ha='center', va='center', color='white')
