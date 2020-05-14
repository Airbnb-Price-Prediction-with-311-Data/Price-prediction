# Effect of 311 service complaints on Airbnb Prices 

The aim of this project is to predict Airbnb prices in NYC. We try to analyse the effect of 311 service complaints in a given zipcode on the Airbnb prices. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

What things you need to install the software and how to install them

```

```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Data Cleaning 

* Navigate to the data-cleaning directory to find the scripts that were used for preprocessing the respective datasets. 
* Under 311-dataset-cleaning, the scripts clean.py and count_per_complaint_type.py directly perform actions on the original dataset which can be found on https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9 , it hasn't been added to this repository due to it's size ( greater than 7GB)
* The get_one_hot.py script, takes the count_by_incident_zip_complaint_type_2010.csv which contains relevant columns from the 311 dataset that were used for the project. 
* The pre-processed datasets for both Airbnb and 311 service complaints dataset (Airbnb_processed2.csv and complaint_type2.csv) can be found in the dataset directory.

## Data Integration

* Navigate to the data-integration directory to find the script used for integration. 
* The two datasets, Airbnb and 311 service complaints are merged using zipcode. 
* This dataset can be found in the dataset directory labelled as Airbnb_Service_complaints_merged.csv

## Feature Selection

* Navigate to the feature-selection/ directory, several methods of feature-selection were used. 
* The different methods are as follows:
    - Recursive feature elimination
    - Handpicking
    - Correlation
    - Forward- selection
    
* The results for these can be found in the results directory containing csv files after performing the various feature selection techniques.

## Data Modeling 

* Several data modeling techniques such as:
    - Linear Regresssion
    - Ensemble Boost
    - XgBoost
    - Random Forest
    - K-Nearest Neighbors

* Results for the K-Nearest Neighbors have not been included due to the large amount of time taken to run it. 
* The run_models.py script uses all the modeling techniques on all the feature selection methods that were tried in the previous section. 

## Results Analysis
Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
