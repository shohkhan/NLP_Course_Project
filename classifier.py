def creat_FPC():
    import numpy as np
    from sklearn import svm, metrics
    f = open("test4_1")
    #f.readline()  # skip the header

    data = np.loadtxt(f)

    svm_x_train = data[:, 0:11]  # select columns 1 through 11
    svm_y_train  = data[:, 12]   # select column 0, the stock price

    f = open("test4_2")
    #f.readline()  # skip the header
    Test = np.loadtxt(f)
    svm_x_test = Test[:, 0:11]  # select columns 1 through 11
    svm_y_test  = Test[:, 12]   # select column 0, the stock price

    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    clf.fit(svm_x_train, svm_y_train)
    expected = svm_y_test
    predicted = clf.predict(svm_x_test)
    print("Classification report for classifier %s:\n%s\n"
      % (clf , metrics.classification_report(expected, predicted)))
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

'''
    from sklearn.ensemble import RandomForestClassifier
    #create the classifier and tune the parameters (more on the documentations)
    rf = RandomForestClassifier(n_estimators= 10000, max_depth= None,max_features = 0.9,random_state= 11 )
    #fit the data
    rf.fit(svm_x_train, svm_y_train)
    #make the prediction on the unseen data
    expected = svm_y_test
    predicted =rf.predict(svm_x_test)
    print("Classification report for classifier %s:\n%s\n"
      % (rf , metrics.classification_report(expected, predicted)))
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
'''

def classNN():
    import numpy as np
    from sklearn.neural_network import MLPClassifier
    from sklearn import metrics
    f = open("test4_1")
    #f.readline()  # skip the header
    train = np.loadtxt(f)

    x_train = train[:, 0:11]  # select columns 1 through 11
    y_train  = train[:, 12]   # select column 0, the stock price
    #X = [[0., 0.], [1., 1.]]
    #y = [0, 1]

    f = open("test4_2")
    #f.readline()  # skip the header
    test = np.loadtxt(f)
    x_test = test[:, 0:11]  # select columns 1 through 11
    y_test  = test[:, 12]   # select column 0, the stock price

    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100,100), random_state=1)
    clf.fit(x_train, y_train)


    expected = y_test
    predicted = clf.predict(x_test)
    print("Classification report for classifier %s:\n%s\n"
      % (clf , metrics.classification_report(expected, predicted)))
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

classNN()
creat_FPC()