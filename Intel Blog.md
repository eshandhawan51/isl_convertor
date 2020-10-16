Our main goal is to recognize the hand detection of Deaf and Mute whether they literate or not. We aim at promoting Indian sign language and to train sign linguistic and other related areas. We aim at focusing on the foster development of Deaf identity to help them communicate efficiently. 
### Project Status: Under Development

### Overview / Usage

Verbal Communication is the only way using which people have interacted with each other over the years but the case stands different for the disabled. The barrier created between the impaired and the normal people is one of the setbacks of the society. For impaired people (deaf & mute), sign language is the only way to communicate. In order to help the deaf and mute communicate efficiently with normal people, an effective solution has been devised. Our aim is to design a system that analyses and recognizes various alphabets from a database of sign images. In order to accomplish this, the application uses various techniques of Image Processing such as segmentation & feature extraction. We investigate different machine learning techniques like SVM, KNN, CNN for the detection of sign language. We are utilizing datasets available online, each alphabet has almost 60,000 datasets. Given the large availability of the dataset, we can produce a fully generalizable translator for all Indian Standard Language (ISL). This system will help to eradicate the barrier between the deaf-mute & normal people. This system will standardize the Indian Sign Language in India. It will also improve the quality of teaching and learning in deaf and mute institutes. Just as Hindi is recognized as the standard language for conversation throughout India, ISL will be recognized as the standard sign language throughout India. The main aim of this work is serving mankind that is achieved by providing better teaching and better learning.
Methodology / Approach

### Image Acquisition

The development of a vision-based static hand gesture recognition system uses a web-camera in real-time applications. The dataset to train our software will be gained from an online repository or designed by ourselves. Since the dataset available online is not properly organized, we will involve our friends and collect data from different hand sizes and shapes to avoid over-fitting. During this process, Image Augmentation will also be used for improving efficiency.

### Image Pre-Processing

Digital image processing is the use of computer algorithms to perform image processing on digital images. It allows a much wider range of algorithms to be applied to the input data — the aim of digital image processing is to improve the image data (features) by suppressing unwanted distortions and/or enhancement of some important image features so that our AI-Computer Vision** **models can benefit from this improved data to work on.

The Image Pre-Processing is done using techniques such as Gaussian Mixture Model.

### Gaussian Mixture Model (GMM) For Background Subtraction:

In this we cancel out the image distortion by using GMM in a step by step process, A GMM is known as parametric probability density function which is signified as a weighted sum of a Mixture of Gaussians (MOG) parameters, and 𝑀 component Gaussian densities function is defined as follows

* Initially construct the initial background model by using selective averaging method is as follows  
𝐵𝑀𝑁 (𝑥, 𝑦) = ∑ 𝑁 𝑚= 𝐼𝑚 (𝑥, 𝑦)

* After that image distortion is canceled out by,  
𝑝(𝑥|𝜆) = ∑ 𝑤𝑖𝑔 (𝑋|𝜇𝑖, Σ𝑖)

* Later pixel probability value is defined as,  
𝑃(𝑧) = ∑ 𝑤𝑖𝑁 (𝜇𝑡Σ𝑡, 𝑍)

### Segmentation

There are several algorithms used for segmentation but one of the best methods used for detection of disease is k- means clustering. k-means clustering is a method of vector quantization, originally from signal processing, that is popular for cluster analysis in data mining. k-means clustering aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean, serving as a prototype of the cluster. This results in a partitioning of the data space into Voronoi cells-means clustering tends to find clusters of comparable spatial extent, while the expectation-maximization mechanism allows clusters to have different shapes. The algorithm has a loose relationship to the k-nearest neighbor classifier, a popular machine learning technique for classification that is often confused with k-means because of the k in the name. One can apply the 1-nearest neighbor classifier on the cluster centers obtained by k-means to classify new data into the existing clusters. Classify the colors a*b* color space using k-means clustering. Since the image has 3 colors, we create three clusters. Measure the distance Euclidean Distance Metric. Label every pixel in that image using results from K means. Given a set of observations (x1, x2, ..., xn), where each observation is a d-dimensional real vector, k-means clustering aims to partition the n observations into k (≤ n) sets S = {S1, S2, ..., Sk} so as to minimize the within-cluster sum of squares (WCSS) (sum of distance functions of each point in the cluster to the K center).

In other words, its objective is to find:

Cluster analysis or clustering is the task of grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar (in some sense or another) to each other than to those in other groups (clusters). In cluster analysis, the k-means algorithm can be used to partition the input data set into k partitions. Label every pixel in the image using results from K means. Then a blank cell array is created to store the results of clustering. Followed by creating RGB label using pixel labels. The selection of appropriate clusters is another important aspect. The cluster which displays the maximum disease affected part is to be selected. In the next step of feature extraction, the features of the selected cluster are extracted.

### Feature Extraction

The features of the selected cluster are extracted. The selected image is converted to

grayscale since the image is in RGB format. At the next step the Gray Level Co-occurrence

Matrices (GLCM). The required statistics are derived from Gray level concurrence Matrices

(GLCM). The following 13 features that are extracted and evaluated: Contrast, Correlation, Energy, Homogeneity, Mean, Standard Deviation, Entropy, RMS. Variance, Smoothness, Kurtosis, Skewness. The thirteen features are stored in an array.

### Classification

In machine learning and statistics, classification is a supervised learning approach in which the computer program learns from the data input given to it and then uses this learning to classify new observations. This data set may simply be bi-class (like identifying whether the person is male or female or that the mail is spam or non-spam) or it may be multi-class too. Some examples of classification problems are speech recognition, handwriting recognition, biometric identification, document classification, etc.

Here we have the types of classification algorithms in Machine Learning:

* Linear Classifiers: Naive Bayes Classifier

* Nearest Neighbour

* Support Vector Machines

* Decision Trees

* Boosted Trees

* Random Forest

* Neural Networks

Out of all the classification techniques listed above, SVM gives the best output and has the highest accuracy among all. So, we are using SVM as a classification algorithm in our system.

### Support Vector Machine:

A Support Vector Machine (SVM) is a discriminative classifier formally defined by a separating hyperplane. In other words, given labeled training data (supervised learning), the algorithm outputs an optimal hyperplane which categorizes new examples. In two dimensional space, this hyperplane is a line dividing a plane into two parts wherein each class lay on either side.

### Conversion of Text to Speech

For converting into speech, few words are trained and stored in a database. Using grammar-translation, the signs recognized are framed into words, and the web-text is used to display speech or text. There are several APIs available lately to convert text to speech. APIs such as Google Text to Speech API, etc. will be used here to convert the obtained text to speech.

​
## Technologies Used

### Languages Used

Python 3.6 is a multi-paradigm programming language. Object-oriented programming and structured programming are fully supported and many of its features support functional programming and aspect-oriented programming. Many other paradigms are supported via extensions, including design by contract and logic programming. Python uses dynamic typing and a combination of reference counting and a cycle-detecting garbage collector for memory management. It also features dynamic name resolution, which binds methods and variable names during program execution.

### List of Python supported library

1. Keras

Keras is a library used to train images and get various types of efficient formulas with low complexity inside code. Keras uses Tensorflow as a backend and generally imports MNIST datasets with Keras.

Syntax: ```$ pip install keras tensorflow numpy mnist```

2. Tensorflow

Tensorflow was created and developed by Google and released under the Apache 2.0 open source license. The API is nominally for the Python programming language, although there is access to the underlying C++ API. It is an open-source library.

Syntax: ```$ pip install tensorflow```

3. Numpy

Numpy is a general-purpose array-processing package. It provides a high-performance multidimensional array object and tools for working with these arrays. It is the fundamental package for scientific computing with Python. Besides its obvious scientific uses, Numpy can also be used as an efficient multi-dimensional container of generic data. Arrays in Numpy can be created in multiple ways, with various numbers of Ranks, defining the size of the Array.

Syntax: ``` $ import numpy as np```

4. Pandas

Pandas is a python package providing fast, flexible, and expressive data structures designed to make working with labeled and relational data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real-world data analysis in Python. Used for data alignment, missing data, inserting, deletion, and various other problems in programming code.

Syntax: ```$ import pandas as pd```

5. Matplotlib

Matplotlib is a 2-D plotting library that helps in visualizing figures. Matplotlib emulates Matlab like graphs and visualizations. Matlab is not free, is difficult to scale, and as a programming language is tedious. So, matplotlib in Python is used as it is a robust, free, and easy library for data visualization.

Syntax: ```$ import matplotlib.pyplot as plt```

6. Scikit learn

Scikit learn is a library used to perform machine learning in Python. Scikit learn is an open-source library that is licensed under BSD and is reusable in various contexts, encouraging academic and commercial use. It provides a range of supervised and unsupervised learning algorithms in Python. Scikit learns consists of popular algorithms and libraries.

Syntax: ```$ pip install scipy```

7. Google Text to Speech

Google Text to Speech is an API that is widely used to convert text to speech in python. It is also known as gTTS API. gTTS is a tool that can be very easily used to convert the entered text to audio which can be saved as an mp3 file. The gTTS API supports several languages including English, Hindi, Tamil, and many more of which Hindi will be useful to us. The speech can be delivered fast or slow as per the designer’s preference. However, changing the voice of the generated audio is not possible.

Syntax: ```pip install gTTS```

8. CGI

CGI as the name suggests, CGI means "Common" gateway interface for everything. CGI is one of the essential parts of HTTP. It is a set of standards that define a standard way of passing information or web-user request to an application program & to get data back to forward it to users. This is the exchange of information between a web-server and a custom script. When the users requested the web-page, the server sends the requested web-page. The web server usually passes the information to all application programs that process data and sends back an acknowledged message this technique of passing data back-and-forth between server and application is the Common Gateway Interface.

Syntax: ```>>import cgitb >>cgitb.enable ()```

### Tools

1. Anaconda python

Anaconda Python is a free and open-source distribution of the Python and R programming languages for data science, machine learning applications, large-scale data processing, predictive analytics, etc. like scientific computing techniques, which aims to simplify package management and deployment. Package versions are managed by the package management system conda and can be navigated using anaconda navigator console. The Anaconda distribution is used by over 15 million users and includes more than 1500 popular data-science packages suitable for Windows, Linux, and macOS. Anaconda contains various types of in-built functions defined for the user and is open source available to anyone like Spyder, Jupyter notebook, Qtconsole, Orange, Rstudio, Glueviz, Visual studio code.

2. Jupyter Notebook

Jupyter Notebook is a web-based interactive computational environment for creating Jupyter notebook documents. The "notebook" term can make reference to many different entities, mainly the Jupyter web application, Python web server, or document format depending on the context. A Jupyter Notebook document is a JSON document, following a versioned schema, and containing an ordered list of input/output cells which can contain code, markdown, mathematics, plots, and rich media, usually ending with the .ipynb extension. A Jupyter notebook can be converted into various output formats like HTML, slides, markdown and etc.

3. GCP

Google Cloud Platform (GCP), offered by Google, is a suite of cloud computing services that runs on the same infrastructure that Google uses internally for its end-user products, such as Google search and YouTube. Alongside a set of management tools, it provides a series of modular cloud services including computing, data storage, data analytics, and machine learning. Registration requires a credit card or bank account details. Google cloud platform provides infrastructure as a service, platform as a service, and serverless computing environments. GCP offers over 90 types of cloud products and free of cost or a small amount of penny to access cloud services over the internet on their platform.

4. Google Colab

Google Colab is a free and well-maintained online environment. It is a Jupyter notebook environment that runs entirely on cloud and therefore requires no setup. If a machine learning model is to be developed but the person has no system that can take the load then Google Colab is the place to be.

### Connectivity

1. SQL

SQL stands for Structured Query Language. SQL is a programming language designed especially for managing data in Relational Database Management System. MySQL is an open-source DBMS which is developed and distributed by Oracle Corporation. It is supported by most of the popular operating systems, such as Windows, Linux, etc. It can be used to develop different types of applications but it is mainly used for developing web applications. MySQL uses GNU General Public License so that anyone can download and install it for developing those applications which will be published or distributed freely. But if a user wants to develop any commercial application using MySQL then he/she will need to buy the commercial version of MySQL.

```Connection-Object= mysql.connector.connect (host = , user = , passwd = )```

Syntax: ```import MySQL. Connector```

2. Firebase

The Firebase Real-Time Database is a cloud-hosted database. Data is stored as JSON and synchronized in real-time to every connected client. It is used to build cross-platform apps with iOS, Android, and JavaScript SDKs, all clients share one Realtime Database instance and automatically receive updates with the newest data. Firebase allows a NoSQL cloud database where data is synced when the user is offline. Firebase also supports various types of a setup like IOS, Android, REST API, C++, Unity, Admin which allows application development to user inefficient and easy manner.
