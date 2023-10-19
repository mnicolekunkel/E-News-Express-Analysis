# define colors for each conversion category
color_mapping = {
    "yes": 'skyblue',
    "no": '#9a8c98'
}

df = old_conversion # starting with the old landing page

# initialize a variable to keep track of the left position
# (stacking towards the right)
left = 0

# set the figure size
plt.figure(figsize=(7, 3))  # longer and not too tall

# create a stacked bar chart by interatively aggregating % ratings in a  single bar
for i, row in df.iterrows():
    category = row['conversion'] # defining our categories
    count = row['count'] # defining the numerical values
    percentage = count / df['count'].sum() * 100  # calculate the percentage of customers converted and not converted
    color = color_mapping.get(category, 'gray')  # default to gray if color not defined
    plt.barh(0, count, left=left, color=color) # horizontal bar of percentage with predefined parameters

    # Add text labels for rating and percentage without a background
    plt.text(left + count / 2, 0, f'{category}\n{count} total\n{percentage:.0f}%',
            # x position centered based on the size of the ar/the total counts
            #                 y position centered at 0
             ha='center', va='center', color='white', fontsize=10)

    left += count

    # prettying up the plot:
    plt.title('Conversion: Old Landing Page') # give title
    #plt.legend() # to include legend
    plt.yticks([])# remove y-axis ticks and labels, since we have a legend
    plt.xlabel('Number of Converted Customers')

    # remove the top and right spines (borders)
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.show()
