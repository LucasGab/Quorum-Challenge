# Answers

### 1. Discuss your solution’s time complexity. What tradeoffs did you make?

I decided to use a consolidated data analysis library (Pandas) so I could make the filter and analysis faster and performatic.

Using pandas we have the following tradeoffs:

Pros:

- Best performance and fine tunning vector algorithms if compared with algorithms like python built-in filter
- Library suitable for incremental complexity on new analysis
- Better reading of the filters and logic code

Cons:

- Maybe over complexity for the requested analysis
- Add a learning curve into the code for maintenance
- For larger datasets (10M+) can be memory heavy, so is recommend parallel and faster libs like polar and numpy

### 2. How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?

If is just add new column information, it's not needed a lot of changes, just change into models files.

### 3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?

Change almost nothing if the data structer remains the same.

### 4. How long did you spend working on the assignment?

3 hours
