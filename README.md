# Robotics

## Setup

### Prerequisites
Tested on Ubuntu 22.04 and Python 3.10.

### Install
```
python -m venv django-env
source django-env/bin/activate
python -m pip install Django django-publications
```

### Download and execute
```
git clone https://github.com/OpenSourceDatabase/Robotics.git
cd Robotics/publication-server
python manage.py runserver
```

## Docker
Tested on Docker version 27.5.0, build a187fa5.
```
docker run --rm -it -p 8000:8000 ghcr.io/opensourcedatabase/robotics:main
```

## Browse
* [Complete list of publications](http://localhost:8000/publications/)
* Publications by year:
  * [2024](http://localhost:8000/publications/year/2024/), [2023](http://localhost:8000/publications/year/2023/), [2022](http://localhost:8000/publications/year/2022/), [2021](http://localhost:8000/publications/year/2021/),  [2020](http://localhost:8000/publications/year/2020/), [2019](http://localhost:8000/publications/year/2019/), [2018](http://localhost:8000/publications/year/2018/), [2017](http://localhost:8000/publications/year/2017/), [2016](http://localhost:8000/publications/year/2016/), [2013](http://localhost:8000/publications/year/2013/)

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

### Execute
```
python process_CSV_files.py
cd publication-server
sqlite3 db.sqlite3 < import_csv_files.sql
```
