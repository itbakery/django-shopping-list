Django Shopping List
====================

The assignment:

Create a Django-based web shopping list application designed for use by a single user.  The application should use Django's ORM to persist the shopping list items to the data store.  Each item should be stored as a single row in the data store.  The class to represent an item should be named ListItem.

The application should allow the user to add and delete items from their shopping list.  Adding and removing items from the user's shopping list requires the user be authenticated.  Use Django's built-in authentication system and function decorators to handle the user authentication.

Your solution should define a User class that represents the single user of the application, and should provide methods to get the total number of items on the user's shopping list and a list of the ListItem objects belonging to the user.

