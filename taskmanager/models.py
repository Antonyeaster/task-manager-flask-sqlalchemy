from taskmanager import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    # allows a string of 25 characters - unique=True making sure its a new entry
    # nullable=False making sure its not left empty or blank,
    # meaning it's required
    tasks = db.relationship(
        "Task", backref="category", cascade="all, delete", lazy=True)
    # will not be visable on the database like using column, 
    # just to reference the one or many relationships
    # backref means it reverses and becomes many-to-one
    # cascade will find all related tasks and delete them
    # lazy means when we query the database we can simultaneously identify 
    # any tasks linked to the categorys

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Task(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    # allows a string of 50 characters - unique=True making sure its a new 
    # entry nullable=False making sure its not left empty or blank, 
    # meaning it's required
    task_description = db.Column(db.Text, nullable=False)
    # using text instead of string means its a larger entry of text
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(
        "category.id", ondelete="CASCADE"), nullable=False)
    # uses the category class with foreignkey, ondelete cascade means anything
    # linked with that id will be deleted to avoid unwanted errors

    def __repr__(self):
        # __repr__ to represent the class objects as a string
        return f"#{self.id} - Task:{self.task_name} | Urgent:{self.is_urgent}"
