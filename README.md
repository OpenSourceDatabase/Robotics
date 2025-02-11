# Robotics

## Setup

### Prerequisites
```
python -m pip install Django django-publications
```
### Download and execute
```
git clone https://github.com/OpenSourceDatabase/Robotics.git
cd Robotics/publication-server
python manage.py runserver
```
### Browse
* [Complete list of publications](http://localhost:8000/publications/)
* [Publications in 2024](http://localhost:8000/publications/year/2024/)

## Raw data

Raw data has been obtained from [IEEE Xplore](https://ieeexplore.ieee.org/Xplore/home.jsp) using [advanced search](https://ieeexplore.ieee.org/search/advanced) with the "github" keyword in all metadata and either the conference name in the publication title or the journal ISSN, for the following conferences and journals:
* International Conference on Robotics and Automation (ICRA)
* International Conference on Intelligent Robots and Systems (IROS)
* International Conference on Automation Science and Engineering (CASE)
* Robotics and Automation Letters
* Robotics & Automation Magazine
* Transactions on Automation Science and Engineering
* Transactions on Robotics

## Data cleaning

The Github code repository is obtained from the abstract. 

If the URL contains "github.io" the linked page is retrieved and searched for a Github code repository.
