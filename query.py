"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# It returns a query object that you call methods on, such as .all(),
# .one() or .first()
# having no data, it returns the the ordered query ready to be run and grab the
# thing in quesiton that was querried.
# The query "Brand.query.filter_by(name='Ford')" translates to
# "select * from brands where name='ford'""


# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# An assocation table maps multiple tables to each other by referencing the
# primary keys of each data table. In affect, the association table itself
# contains forign keys, each in a many to one relationship. One being the
# assocation table and many to relational data tables.
# That said, assocation tables manage many to many relationships.

# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the ``id`` of "ram."
q1 = Brand.query.filter_by(brand_id='ram').first()

# Get all models with the name "Corvette" and the brand_id "che."
q2 = Model.query.filter(Model.name == 'Corvette', Model.brand_id == 'che').all()

# Get all models that are older than 1960. ????????
q3 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor."
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued. ???
q6 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.discontinued !=None) | (Brand.founded < 1950)).all()

# Get any model whose brand_id is not "for."
q8 = Model.query.filter(Model.brand_id != 'for').all()


# -------------------------------------------------------------------
# Part 4: Write Functions
def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    #get all models from given year.

    # models = Model.query.filter_by(year=year).all()
    models_for_year = db.session.query(Model).filter(Model.year == year).all()

    # print each model info
    for model in models_for_year:
        print model.name, '\t', model.brand.name, '\t', model.brand.headquarters


def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""

    records_list = db.session.query(Brand.name, Model.name, Model.year).join(Model).order_by(Model.brand_id).all()
    for record in records_list:
        print record[0], '\t\t', record[1], '\t\t', record[2]


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    partial_brand = '%%%s%%' % mystr

    return Brand.query.filter(Brand.name.like(partial_brand)).all()


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    return Model.query.filter(Model.year >= start_year, Model.year < end_year).all()
