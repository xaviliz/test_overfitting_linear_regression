def linear_regression(x, y, degree, draw):
	if len(x)!=len(y):
		print "x and y have to have the same lenght!"
		return 0
	if degree>0:
		X = np.array(np.ones(len(x)))
		for i in range(1, degree):
			x_over = pow(x,i)
			X = np.vstack((X,x_over))
		# transpose X
		X = np.stack(X,axis=1)
		theta = ((np.linalg.pinv(X.T.dot(X))).dot(X.T)).dot(y)
	if draw:
		# Display y
		#plt.figure(figsize=(20,5))
		fig, ax = plt.subplots()
		ax.plot(y, 'ro', label ='y')
		ax.plot(X.dot(theta), 'bs', label = 'Ax')
		plt.axis([-1, x.size+1, -.5, 1.5])
		plt.title("y vs X*theta with degree= " + str(degree))
		plt.ylabel("samples")
		plt.xlabel("y[n]")
		legend = ax.legend(loc='upper right', shadow=True)
		#plt.legend(handles=[xtheta], loc=1)
		plt.grid()
		plt.show()
		error = sum(pow(abs(X.dot(theta) - y),2))
		return theta, error

y = np.random.rand(10)
for i in range(2,20):
	degree = i
	theta, error = linear_regression(np.arange(0.0,1.0,0.1),y, degree, True)
	print "linear regression with degree: " + str(degree) + " quadratic error: " + str(error)
