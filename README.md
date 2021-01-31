# Obesity Prediction API

So in this project I have downloaded data from Kaggle, [click here](https://www.kaggle.com/ankurbajaj9/obesity-levels)

After getting the data, Now have to encode the features i.e we have to change from categorical into numerical, there so many techniques lke
*One Hot code encoding
*Custom Encoding
*Weight of Evidence encoding

but I used Leave one out encoding why?

``` 
To overcome such challenge,Leave-One-Out Encoding produces the mean value of the target over all rows for the same categorical level, excluding the row itself. 
It leaves the target value of the row itself out — thus the name Leave-One-Out. This avoids direct target leakage.
```

I have read about different types of encoding techniques and went with LOO.

Now normalizing the data, this is done to ensure that none of the variables have biased weights, Normalization is done..

****

## Step 2 Fature Extraction

So there are somany variables given in the dataset, so inorder to remove the non significant variables we will be doing feature extraction.. so in here there are so many techniques 
I have tested so many techniques at last I have used Pearson Correlation because I think it justified common sense 

This is the image 
![Image of Pearson correlation ](https://github.com/amahavishnua/MlprojectFlask/blob/master/Pearson%20Correlation.png)


From this we can see strongly corelated features for the 0 column which is the target variable i.e ** Obesity TYpe** Now I have taken top 7 into consideration
I started to build the model

****

## Step 3 Building a Model

Now I went Polynomial Regression, I have used poly to transofrm the variables and then I feeded them to Logistic Regression model.
As the training and testing data are very less I have got very less accuracy of 71% Which is not bad when given so many features and such less data..

****

## Step 4 Deploying Model

After creating the model I exported the model and using Flask I created an API which takes the features from the index.html and throwout the type of possible **Obesity Type**
I tried deploying on AWS instances but some small error with encodings keep popping on AWS instance(I installed all the libraries I used in AWS) cant figure out..

****

Thankyou 
mra503

