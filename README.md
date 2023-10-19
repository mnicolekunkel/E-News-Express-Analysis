# E-News-Express-Analysis
The central question is: should E-News deploy a new landing page?
The company is interested in enhancing user engagement, as they have determined that their decrease in monthly subscribers is due to their current webpage design.
A/B testing with random sampling used to test a new design: 50 users were exposed to new landing page and another 50 users were exposed to the current landing page. In both cases, users were allowed to select the language in which they wanted the page shown to them.

## Subquestions to solve this business question:
 - Do the users spend more time on the new landing page than on the existing landing page?
 - Is the conversion rate (the proportion of users who visit the landing page and get converted) for the new page greater than the conversion rate for the old page?
 - Is the time spent on the new page the same for the different language users?
 - Does the converted status depend on the preferred language?


## Data Dictionary:
- user_id - Unique user ID of the person visiting the website
- group - Whether the user belongs to the first group (control) or the second group (treatment)
- landing_page - Whether the landing page is new or old
- time_spent_on_the_page - Time (in minutes) spent by the user on the landing page
- converted - Whether the user gets converted to a subscriber of the news portal or not
- language_preferred - Language chosen by the user to view the landing page
