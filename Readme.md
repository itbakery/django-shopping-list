Django Shopping List
====================

To view the app, go to fierce-beach-8243.herokuapp.com.  You will have to
create an account.  When you create an account you must choose a unique
username.  The email and confirm password fields are ignored for the time being.

If you are not logged in upon signing up, then the username you chose may have
already been taken. (The app currently issues no warning or message of any kind
when this occurs - still a first draft.) Try again with a more unique username.

Upon logging in successfully you will be taken to a page with an empty shopping 
list in the middle.  You can add items using the control that is provided.  Once an item has
been added, you can scroll over with your mouse and buttons will appear that
will allow you to check off the item or delete it.

If you are using a mobile phone the buttons will appear upon touching the row
with your finger (only tested on an iPhone so far).

The app makes use of Twitter Bootstrap, which is a responsive UI framework, for
front-end UI elements and should be functional on a mobile device.

Adding, deleting, and checking off items all use Ajax so that the page does
not have to reload as the shopping list is updated.

If you log out and then log back in you should find that the state of your 
shopping list has been preserved.

You cannot add duplicate items to the shopping list.  You can, however, rearrange
the order of the items if you are using an interface with a mouse (i.e., not a mobile
device).  In order to re-arrange the order, move the mouse over the name of 
the item. The mouse should change into a shape with 4 arrows, indicating that the 
item can be dragged.  You can then drag it to a new position in the list. 
Unfortunately there is no guarantee that the items will remain in that order the
next time you log in (a project for the second draft).

Multiple users can create accounts and maintain shopping lists without interfering with each other.

If you use the app from multiple devices then you will have to refresh the shopping
list page in order to see the updates made from another device.

The source code can be viewed at https://github.com/jononomo/django-shopping-list

