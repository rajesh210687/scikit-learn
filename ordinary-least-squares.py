from sklearn import linear_model
req = linear_model.LinearRegression()
req.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
print(req.coef_)
print(req.intercept_)
