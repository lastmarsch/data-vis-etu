# Multidimensional data visualization. Introduction to Matplotlib.

## Source data 
[Data of rotary machine defects](https://www.kaggle.com/datasets/kazakovyurii/data-of-rotary-machine-defects)


## Tasks
### Implement data analysis: 
  - Identify data set type and attribute types
	- Identify data set cardinality 
   	- How many items in data set
    - What is cardinality of each attribute ()
      - Range for qualitative data
      - Number of values for nominal data
    - Consider whether to transform the data.

*Recommendations:*
  1. At this point is it is recommended to apply statistical analysis of the data, for each qualitative parameter calculate mean, variance, for nominal parameters – moda.
  2. Calculate correlation between parameters to see if any relationships exist
  3. Think of any transformation of the data set. For example, it is possible to join all data sets in one with adding a new nominal attribute – label, that encodes the result of the experiment. Try to one-hot or dummy encoding to see if there is a correlation between label and source attributes. 
  4. Think of deriving new attributes, for example, calculate difference between parameters from “normal” data set and “abnormal” data set.
  5. Keep in mind your ultimate goal explain the signs of rotary defects. 


### Visualize your data:
  - Use simple plots: line charts, hist, bars (with errors). 
  - Consider the range of the attributes
  - Organize your views in a manner that support comparison (i.e. the goal of the task) 
  - Think of giving overview on all data set.

*Recommendations:*
  1. Use multiple subplots to arrange plots.
  2. Use annotations (or text ) function to mark interesting things.
  3. Do not experiment with colors.
  4. Check that attributes visualizing on one plot have same range.
  5. Consider filtering a subset of attributes if needed. 

### Describe and explain your choices.